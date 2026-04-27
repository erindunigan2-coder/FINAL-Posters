---
Project: Plating Posters Inc
Poster Number: 698
Title: "Pretreatment -- Coil Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating, Section 6.5)"
Process Scope: Pretreatment (conversion coating) for coil coating -- Stage 4 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - Pretreatment
  - ConversionCoating
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #698 -- Construction Workup
## Pretreatment -- Coil Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 9. The conversion coating that bonds primer to metal. The coil coating industry is in the middle of a generational shift -- from hexavalent chromate (the legacy king of adhesion and corrosion performance) to chrome-free Ti/Zr nanoceramic (the REACH-compliant replacement that is now the standard for new lines). This poster maps both legacy and current chemistries, their application methods, and the coating weights that determine performance.

Hero visual: side-by-side comparison of four conversion coating types (chromate, Ti/Zr, dry-in-place, phosphate) with coating weight ranges and application methods.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Four conversion coating comparison (Block B):** Four panels showing each chemistry with coating weight, method, and status (legacy/current/emerging).
2. **Application method detail (Block D):** Roll-apply vs. spray for conversion coatings at line speed.
3. **Chrome-to-chrome-free transition panel (Block E):** Regulatory drivers and performance comparison.
4. **Defect strip (Block F):** 4 pretreatment-related defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber)
ZONE 3 -- CONVERSION COATING TYPES HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- APPLICATION METHODS (14.5"--20.5" / ~6.0")
ZONE 5 -- CHROME-FREE TRANSITION (20.5"--26.5" / ~6.0")
ZONE 6 -- PRETREATMENT DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PRETREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Coil Coating -- Stage 4 of 9` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The invisible layer that holds everything together. 5-30 mg/ft2 of conversion coating is the difference between a 30-year warranty and a peeling roof panel.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, dry strip at 100-120 F  -->  After: Conversion-coated surface bonded to metal, ready for prime coat`

---

### ZONE 3 -- Conversion Coating Types Hero

**Section label:** `FOUR CONVERSION COATING CHEMISTRIES` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Four Chemistry Panels (Y: 5.0" to 14.0")**

Four equal panels. Each: Rounded rect, W: 5.5", H: 8.5", fill `#1E2435`, top accent 4 pt.

**Panel 1 -- Chromate Rinse (X: 0.5", accent `#E05C5C`):**
- Badge: `LEGACY` fill `#E05C5C`, text `#F0EDE8`
- Title: `Hexavalent Chromate (CrVI)` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Chemistry: `Chromic acid + silica sol` JetBrains Mono 11 pt `#F0EDE8`
- Application: `Roll apply or spray`
- Coating weight: `10-30 mg/ft2 Cr`
- Performance: `Best adhesion and corrosion resistance`
- Status: `Declining -- restricted by RoHS/REACH` Inter Medium 12 pt `#E05C5C`
- Note: `Still running on legacy lines where regulations permit` Inter Regular 11 pt `#F0EDE8` at 60%

**Panel 2 -- Chrome-Free Ti/Zr (X: 6.33", accent `#27AE60`):**
- Badge: `CURRENT STANDARD` fill `#27AE60`, text `#1A1F2E`
- Title: `Chrome-Free Ti/Zr` -- Barlow SemiBold, 16 pt, `#27AE60`
- Chemistry: `Fluorotitanic / fluorozirconic acid` JetBrains Mono 11 pt
- Application: `Roll apply or spray`
- Coating weight: `5-15 mg/ft2`
- Performance: `Comparable to chromate for most applications`
- Status: `REACH compliant -- new industry standard` Inter Medium 12 pt `#27AE60`
- Note: `Effective on multi-metal lines (steel + aluminum)` Inter Regular 11 pt at 60%

**Panel 3 -- Dry-in-Place (X: 12.16", accent `#2EC4B6`):**
- Badge: `EMERGING` fill `#2EC4B6`, text `#1A1F2E`
- Title: `Dry-in-Place (No Rinse)` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Chemistry: `Proprietary chrome-free polymers` JetBrains Mono 11 pt
- Application: `Roll apply only`
- Coating weight: `Very thin (< 5 mg/ft2 metal)`
- Performance: `Adequate for interior and light-duty exterior`
- Status: `Simplest process -- no rinse water waste` Inter Medium 12 pt `#2EC4B6`
- Note: `Eliminates post-treatment rinse stage entirely` Inter Regular 11 pt at 60%

**Panel 4 -- Phosphate (X: 18.0", accent `#E8A020`):**
- Badge: `NICHE` fill `#E8A020`, text `#1A1F2E`
- Title: `Iron or Zinc Phosphate` -- Barlow SemiBold, 16 pt, `#E8A020`
- Chemistry: `Phosphoric acid based (spray)` JetBrains Mono 11 pt
- Application: `Spray`
- Coating weight: `25-75 mg/ft2 (iron phos)`
- Performance: `Good; more common for heavy-gauge applications`
- Status: `Less common for high-speed coil lines` Inter Medium 12 pt `#E8A020`
- Note: `Requires more stages and sludge management` Inter Regular 11 pt at 60%

---

### ZONE 4 -- Application Methods

**Section label:** `HOW CONVERSION COATINGS ARE APPLIED AT LINE SPEED` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Two-Column Method Comparison**

Y: 15.3" to 20.3".

**Left -- Roll Apply (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `ROLL APPLY` -- Barlow SemiBold, 18 pt, `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
  - `Conversion coating solution applied by rubber roll directly to moving strip`
  - `Precise, uniform coverage -- roll coater meters the exact volume`
  - `Preferred for Ti/Zr and dry-in-place chemistries`
  - `No overspray waste; minimal solution consumption`
  - `Roll condition and nip pressure determine uniformity`

**Right -- Spray Apply (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `SPRAY APPLY` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Body:
  - `Solution sprayed onto moving strip through nozzle headers`
  - `Excess drains and recirculates`
  - `Traditional method for chromate and phosphate chemistries`
  - `Easier to maintain (no roll changes) but less precise`
  - `Requires post-treatment rinse to remove excess`

Comparison callout (Y: 19.5"):
- Pill, fill `#252B3D`, W: 23.0", H: 0.6"
- Text: `Roll apply is gaining ground because it eliminates the rinse step after conversion coating, reducing water consumption and line footprint.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Chrome-Free Transition

**Section label:** `THE CHROME-FREE TRANSITION` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Full-Width Panel**

Y: 21.3" to 26.3". Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".

**Three-column layout:**

**Column 1 -- Regulatory Drivers (X: 1.0", W: 7.0"):**
- Title: `WHY THE SHIFT` Barlow SemiBold 16 pt `#27AE60`
- `EU REACH Regulation (EC 1907/2006)` -- `Restricts hexavalent chromium`
- `RoHS Directive (2011/65/EU)` -- `Bans Cr6+ in electrical/electronic equipment`
- `Customer specifications` -- `Many OEMs now require chrome-free`
- `Worker safety` -- `CrVI is a known carcinogen (IARC Group 1)`
- Inter Regular 12 pt `#F0EDE8`

**Column 2 -- Performance Comparison (X: 8.5", W: 7.0"):**
- Title: `PERFORMANCE` Barlow SemiBold 16 pt `#E8A020`

| Property | Chromate | Ti/Zr Chrome-Free |
|---|---|---|
| Adhesion (dry) | Excellent | Excellent |
| Adhesion (wet/humid) | Excellent | Very good |
| Salt spray (with coating system) | 1,000-3,000 hr | 750-2,500 hr |
| Multi-metal compatibility | Good | Excellent |
| Environmental compliance | Restricted | Fully compliant |

JetBrains Mono 11 pt `#F0EDE8`.

**Column 3 -- Key Takeaway (X: 16.0", W: 7.0"):**
- Title: `BOTTOM LINE` Barlow SemiBold 16 pt `#2EC4B6`
- Body: `Chrome-free Ti/Zr conversion coatings meet or approach chromate performance for the vast majority of coil coating applications. The transition is driven by regulation, not by performance failure. New lines install chrome-free. Legacy lines convert as permit conditions require.` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 6 -- Pretreatment Defects

**Section label:** `WHAT GOES WRONG -- 4 PRETREATMENT DEFECTS` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | LOW COATING WEIGHT | Depleted chemistry or low concentration | Titrate and adjust; check roll apply uniformity |
| 2 | 6.33" | UNEVEN TREATMENT (STREAKING) | Water droplets on strip or uneven roll contact | Verify dryer; check roll condition and pressure |
| 3 | 12.16" | ADHESION FAILURE AFTER FORMING | Conversion coating missing or too thin on one side | Check both sides of strip; verify roll apply covers top and bottom |
| 4 | 18.0" | CHEMISTRY CONTAMINATION | Oil carryover from inadequate cleaning | Improve upstream cleaning; check oil removal < 5 mg/m2 |

**Key insight callout (Y: 30.6" to 32.3"):**
- Text: `Conversion coating weight on coil is measured in single-digit mg/ft2 -- invisible to the eye. The only way to verify it is by measurement (XRF, coating weight strips, or supplier test methods). Trust measurement, not appearance.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Pretreatment -- Coil Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Pretreatment Coil Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chrome-to-chrome-free transition is the story of this poster. Every coil coater either has made this switch, is making it, or is watching the regulatory clock count down. The four-panel hero makes the landscape visible: legacy chromate, current Ti/Zr, emerging dry-in-place, and niche phosphate. The performance comparison table in Zone 5 is the data the decision-maker needs: chrome-free is not worse, it is different and compliant. The regulatory drivers column answers why.

---

*Alaina -- Poster #698 -- Construction Workup v1.0 -- 2026-04-26*
