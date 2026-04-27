---
Project: Plating Posters Inc
Poster Number: 369
Title: "Passivation -- Acid Pickling (Stainless Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-4.6)"
Technical Source: Industry-standard passivation of stainless steel per ASTM A967 / AMS 2700. Covers nitric acid passivation (Methods 1--4), citric acid passivation (Method 5), and passivation verification testing. This is the secondary treatment step that restores the protective chromium oxide film after pickling.
Process Scope: Passivation of stainless steel -- restoring the Cr2O3 passive film after acid pickle
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - StainlessSteel
  - Passivation
  - ChromiumOxide
  - ASTMA967
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT04
---

# Poster #369 -- Construction Workup
## Passivation -- Acid Pickling (Stainless Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 6 of 7 in the CT-04 cluster. This is the poster that answers the question every fabricator asks after pickling: "How do I get the corrosion resistance back?" Pickling strips the passive Cr2O3 film. Passivation rebuilds it. The hero concept is a side-by-side comparison of nitric acid passivation (the traditional standard) vs. citric acid passivation (the environmentally preferred alternative). ASTM A967 governs both. The verification tests -- copper sulfate, high-humidity, and salt spray -- prove the passive film is intact.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Passivation mechanism diagram (Block B -- HERO):** How HNO3 or citric acid selectively dissolves free iron from the surface while promoting chromium oxide formation.
2. **ASTM A967 method comparison table (Block D):** Five methods side by side.
3. **Verification testing (Block E):** Three tests with pass/fail criteria.
4. **Common failures (Block F).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 6 of 7 highlighted (Emerald -- treatment/restoration)
ZONE 3 -- PASSIVATION MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ASTM A967 METHOD COMPARISON (14.5"--21.0" / ~6.5")
ZONE 5 -- VERIFICATION TESTING (21.0"--27.0" / ~6.0")
ZONE 6 -- COMMON FAILURES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PASSIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Stainless Steel -- Restoring the Chromium Oxide Shield` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Pickling stripped the passive film. Passivation rebuilds it. Without this step, your stainless steel is just expensive carbon steel waiting to rust.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly pickled stainless with exposed iron and chromium  -->  After: Restored Cr2O3 passive film -- corrosion-resistant`

---

### ZONE 3 -- Passivation Mechanism Hero

**Section label:** `HOW PASSIVATION WORKS -- IRON OUT, CHROMIUM UP` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**Two-column hero (Y: 5.0" to 14.0"):**

**Left -- Nitric Acid Passivation (X: 0.5", W: 11.0"):**

Rounded rect H: 8.5", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `NITRIC ACID PASSIVATION` Barlow Condensed ExtraBold 24 pt `#E8A020`.
Subtitle: `The Traditional Standard -- ASTM A967 Methods 1--4` Barlow SemiBold 14 pt `#F0EDE8` at 60%.

**Mechanism (Inter Regular 13 pt `#F0EDE8`, line height 155%):**
```
1. HNO3 is a strong OXIDIZER
2. It selectively dissolves free iron (Fe)
   from the stainless surface
3. It PROMOTES Cr2O3 formation:
   -- Chromium is oxidized to Cr(III) oxide
   -- The oxide film forms spontaneously
      in the oxidizing environment
4. Result: chromium-enriched surface
   with a dense, protective Cr2O3 film
```

**Key parameters box:**
- `HNO3: 20--50% by volume` JetBrains Mono 14 pt `#E8A020`
- `Temperature: 70--140 F (21--60 C)` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 20--30 minutes` JetBrains Mono 13 pt `#F0EDE8`

**Right -- Citric Acid Passivation (X: 12.0", W: 11.5"):**

Rounded rect H: 8.5", fill `#1E2435`, left accent 0.06" `#27AE60`.

Title: `CITRIC ACID PASSIVATION` Barlow Condensed ExtraBold 24 pt `#27AE60`.
Subtitle: `The Environmental Alternative -- ASTM A967 Method 5` Barlow SemiBold 14 pt `#F0EDE8` at 60%.

**Mechanism:**
```
1. Citric acid chelates free iron (Fe)
   from the stainless surface
2. Chelation is SELECTIVE -- citric acid
   binds iron preferentially over chromium
3. Iron is removed as a soluble citrate complex
4. Chromium remains on the surface and
   oxidizes naturally in air to form Cr2O3
5. Result: same chromium-enriched surface
   and protective passive film
```

**Key parameters box:**
- `Citric acid: 4--10% by weight` JetBrains Mono 14 pt `#27AE60`
- `Temperature: 70--160 F (21--71 C)` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 4--20 minutes` JetBrains Mono 13 pt `#F0EDE8`

**Bottom callout spanning both columns (Y: 14.0"):**
- Rounded rect W: 23.0", H: 0.4", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- `Both methods achieve the same result: a chromium-enriched, iron-depleted surface with a stable Cr2O3 passive film. The choice is environmental, not metallurgical.` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- ASTM A967 Method Comparison

**Section label:** `ASTM A967 -- FIVE PASSIVATION METHODS` -- Y: 14.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK D -- Five-Method Table (Y: 15.3" to 20.8")**

Column widths (23.0" total):
- Method (3.5") | Chemistry (5.0") | Temperature (3.5") | Time (3.0") | Notes (8.0")

Header row: fill `#3A4055`, H: 0.5".

| Method | Chemistry | Temperature | Time | Notes |
|---|---|---|---|---|
| Method 1 -- Nitric (high conc.) | 20--25% HNO3 | 120--140 F (49--60 C) | 20--30 min | Standard; most common |
| Method 2 -- Nitric (med. conc.) | 30--40% HNO3 | 70--120 F (21--49 C) | 20--30 min | Room temperature operation |
| Method 3 -- Nitric (high conc., RT) | 40--50% HNO3 | 70--90 F (21--32 C) | 20--30 min | Highest concentration, lowest temp |
| Method 4 -- Nitric + dichromate | 20--50% HNO3 + 2--6 oz/gal Na2Cr2O7 | 120--140 F (49--60 C) | 20--30 min | Maximum passivation; contains Cr(VI) -- legacy |
| Method 5 -- Citric acid | 4--10% citric by weight | 70--160 F (21--71 C) | 4--20 min | ENVIRONMENTALLY PREFERRED; increasing adoption |

Data: JetBrains Mono 11 pt. Method names: Inter Medium 12 pt.
Method 4 "contains Cr(VI)" in `#E05C5C`.
Method 5 "ENVIRONMENTALLY PREFERRED" in `#27AE60`.

Below: `Method 5 (citric acid) is the fastest-growing passivation method. Shorter time, lower hazard, no NOx fumes, easier waste treatment. Verify customer spec acceptance before switching.` Inter Medium 12 pt `#27AE60`

---

### ZONE 5 -- Verification Testing

**Section label:** `PASSIVATION VERIFICATION -- PROVE THE FILM EXISTS` -- Y: 21.2". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK E -- Three Test Cards (Y: 21.8" to 26.8")**

| Card | X | W | Test | Standard | Method | Pass Criteria |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | COPPER SULFATE TEST | ASTM A967 Practice E | Apply CuSO4 solution to surface; observe for 6 seconds | No copper deposit (pink/copper color) = PASS. Copper deposit = free iron present = FAIL |
| 2 | 8.0" | 7.33" | HIGH-HUMIDITY TEST | ASTM A967 Practice C | Expose to >97% RH at 100--115 F for 24 hours | No rust or staining = PASS. Any rust = FAIL |
| 3 | 15.5" | 8.0" | SALT SPRAY TEST | ASTM A967 Practice B / ASTM B117 | 5% NaCl fog per B117 for 2--24 hours | No rust = PASS. Any rust = FAIL |

Each card: Rounded rect H: 4.5", fill `#1E2435`, radius 6, left accent 0.06" `#2EC4B6`.
Test name: Barlow SemiBold 16 pt `#2EC4B6`.
Standard: JetBrains Mono 11 pt `#F0EDE8` at 60%.
Method: Inter Regular 12 pt `#F0EDE8`.
Pass: Inter Medium 12 pt `#27AE60`. Fail: Inter Medium 12 pt `#E05C5C`.

Below cards: `The copper sulfate test is the fastest field check -- results in 6 seconds. If copper deposits on the surface, free iron is present and the passive film is incomplete. Re-passivate.` Inter Medium 13 pt `#E8A020`

---

### ZONE 6 -- Common Failures

**Section label:** `WHAT GOES WRONG -- 5 PASSIVATION FAILURES` -- Y: 27.2".

**BLOCK F -- Failure Table (Y: 27.8" to 32.3")**

| Failure | Cause | Fix |
|---|---|---|
| Copper sulfate test fails (copper deposits) | Free iron still present; passivation incomplete | Re-passivate with longer time or higher concentration; verify pickle removed all scale first |
| Rust spots within 24 hours | Iron contamination from carbon steel tooling or handling | Eliminate carbon steel contact; use stainless-only tooling; re-pickle and re-passivate |
| Tea staining in service | Embedded iron from fabrication; incomplete passivation | Verify with copper sulfate test; mechanical cleaning to remove embedded iron; re-passivate |
| Orange peel after passivation | Over-pickling prior to passivation (grain boundary attack) | Metallurgical issue from upstream -- reduce pickle time; passivation cannot repair grain boundary damage |
| Passivation tank ineffective | Acid depleted; dissolved iron too high | Check free acid; replace if dissolved metals exceed capacity; filter |

Each row: Rounded rect H: 0.8", alternating fills.
Failure: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Passivation -- Acid Pickling (Stainless Steel)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM A967 (Standard Specification for Chemical Passivation Treatments); AMS 2700 (Passivation of Corrosion Resistant Steels); ASTM A380; general industry knowledge. Specific passivation methods and verification requirements are dictated by customer specification. Citric acid methods are gaining acceptance but verify customer approval before substitution.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Passivation Stainless Steel -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Passivation is the "happy ending" of the stainless steel pickle cluster. After five posters of acid hazards, HF warnings, and safety protocols, this poster shows the payoff: a restored, corrosion-resistant surface. The dual-column hero (nitric vs. citric) is the visual anchor -- same result, different chemistry, different environmental footprint. The ASTM A967 method table is the definitive reference; shops receiving customer purchase orders that specify "passivation per ASTM A967" can look at this poster and know exactly what is required. The verification testing section (Zone 5) closes the quality loop: do not ship parts without proving the passive film exists. The copper sulfate test is 6 seconds -- there is no excuse for skipping it.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #369 -- Construction Workup v1.0*
*2026-04-26*
