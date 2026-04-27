---
Project: Plating Posters Inc
Poster Number: 235
Title: "Rinse -- EN (High Phos) -- Pre-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 3: EN High-P)"
Technical Source: Pre-plate rinse between activation and EN High-P bath. Stage 4 of 8. The most critical rinse in the EN process line. No brand names.
Process Scope: Pre-plate rinse stage for electroless nickel high-phosphorus process
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - HighPhosphorus
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ClusterEN03
---

# Poster #235 -- Construction Workup
## Rinse -- EN (High Phos) -- Pre-Plate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. This is the most critical rinse in the entire EN process line. What goes into the EN bath stays in the EN bath -- there is no easy way to remove contaminants from a hot, acidic autocatalytic solution. Chloride drag-in from HCl activation causes pitting. Chromate traces from plastic etch poison the bath. Zinc residue from zincate is tolerable in small amounts but excessive drag-in raises zinc contamination. This rinse is the last line of defense before the main tank.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero (Block B):** Similar to Poster #233 but with emphasis on DI water quality and tighter conductivity targets.
2. **Contamination threat matrix (Block D):** Specific contaminants that damage the EN bath, with consequences.
3. **Zincated aluminum special handling (Block E):** Time-critical transfer to prevent zinc oxidation.
4. **Conductivity and quality targets (Block F):** Tighter specifications than pre-activation rinse.

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
  Stage 4 highlighted (Teal)
ZONE 3 -- RINSE SYSTEM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINATION THREAT MATRIX (14.5"--20.5" / ~6.0")
ZONE 5 -- ALUMINUM TRANSFER TIMING (20.5"--26.5" / ~6.0")
ZONE 6 -- QUALITY TARGETS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN (High Phos) -- Pre-Plate -- Stage 4 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The last line of defense before the main tank. What you drag in, the EN bath absorbs -- permanently.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Acid/zincate residue on surface  -->  After: Neutral, ultra-clean surface ready for EN deposition`

---

### ZONE 3 -- Rinse System Hero

**Section label:** `THE MOST CRITICAL RINSE IN THE EN LINE` -- Y: 4.4".

**BLOCK B -- Rinse System Diagram**

Y: 5.0" to 14.0".

Same counterflow rinse diagram structure as Poster #233, with these key differences:

**Parameter labels (Y: 7.0"):**
- `Water: DI REQUIRED (not optional)` JetBrains Mono 14 pt `#E05C5C`
- `Temp: Ambient (18--30 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Time: 30--60 sec` JetBrains Mono 14 pt `#F0EDE8`
- `Target: <20 uS/cm for critical work` JetBrains Mono 14 pt `#27AE60`
- `Single or double counterflow` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Hero callout (large, centered, Y: 11.0"):**
- Rounded rect, W: 18.0", H: 1.5", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Text: `THE EN BATH HAS NO ANODE. NO RECTIFIER. NO WAY TO PURIFY ITSELF.` Barlow Condensed ExtraBold 22 pt `#E05C5C`
- Subtext: `Contaminants that enter the EN bath accumulate until the bath fails. This rinse prevents that.` Inter Medium 14 pt `#F0EDE8`

**Bottom callout (Y: 13.5"):**
- `DI water is essential here -- municipal water introduces chlorides, calcium, and silicates that contaminate the EN bath.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Contamination Threat Matrix

**Section label:** `WHAT THREATENS YOUR EN BATH -- AND WHERE IT COMES FROM` -- Y: 14.7".

**BLOCK D -- Threat Table (Y: 15.3" to 20.3")**

Column widths: Contaminant (4.0") | Source (5.0") | Effect on EN Bath (7.0") | Severity (3.0") | Prevention (4.0")

Header row: fill `#3A4055`. Barlow SemiBold, 14 pt.

| Contaminant | Source | Effect on EN Bath | Severity | Prevention |
|---|---|---|---|---|
| Chloride (Cl-) | HCl activation drag-in | Pitting; accelerates bath aging; attacks stabilizer | HIGH | DI rinse; extended rinse time |
| Chromate (Cr6+) | Plastic etch drag-in | Stabilizer poisoning at ppm levels; bath goes inert | CRITICAL | Dedicated rinse line; never cross-contaminate |
| Zinc (Zn) | Zincate drag-in (Al parts) | Slight amounts OK; excess raises Zn contamination | LOW-MED | Brief but thorough rinse |
| Sulfate (SO4) | H2SO4 activation | Minor; bath already sulfate-based | LOW | Standard rinse sufficient |

Data: JetBrains Mono Regular, 12 pt. Severity column color-coded: CRITICAL = `#E05C5C`, HIGH = `#E8A020`, LOW-MED = `#2EC4B6`, LOW = `#27AE60`.

---

### ZONE 5 -- Aluminum Transfer Timing

**Section label:** `ZINCATED ALUMINUM -- THE 30-SECOND RULE` -- Y: 20.7".

**BLOCK E -- Transfer Timing Visual (Y: 21.3" to 26.3")**

**Central timeline graphic:**
- Horizontal bar representing time from zincate completion to EN bath entry
- 0 sec (zincate complete) to 60 sec
- Green zone: 0-30 sec -- `SAFE: Zinc layer intact and active`
- Yellow zone: 30-45 sec -- `RISK: Zinc layer beginning to oxidize`
- Red zone: 45-60+ sec -- `DANGER: Oxidized zinc = poor adhesion`

**Callout boxes:**

Left (X: 0.5", W: 11.0"):
- `WHY THE RUSH?` Barlow SemiBold 18 pt `#E8A020`
- `The zincate process deposits a sub-micron zinc film on aluminum. This zinc is catalytic for EN deposition and dissolves as the first nickel layers deposit -- creating intimate metallurgical bonding. But zinc oxidizes rapidly in air and rinse water. An oxidized zinc layer will not bond properly to nickel.` Inter Regular 13 pt `#F0EDE8`

Right (X: 12.0", W: 11.5"):
- `WHAT TO DO` Barlow SemiBold 18 pt `#27AE60`
- `1. Minimize rinse time -- quick dip, not prolonged soak`
- `2. Transfer to EN bath within 30 seconds of leaving rinse`
- `3. Do not allow parts to air-dry at any point`
- `4. If delay occurs: re-zincate (strip in HNO3, re-apply zincate)`
- `5. Consider rack design that allows rapid transfer`

---

### ZONE 6 -- Quality Targets

**Section label:** `RINSE QUALITY SPECIFICATIONS` -- Y: 26.7".

**BLOCK F -- Specification Comparison (Y: 27.3" to 32.3")**

**Two-column comparison:**

Left -- Standard Work (X: 0.5", W: 11.0"):
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `STANDARD APPLICATIONS` Barlow SemiBold 18 pt `#2EC4B6`
- `Conductivity: <50 uS/cm` JetBrains Mono 16 pt `#27AE60`
- `Water: DI or RO`
- `Stages: Single or double counterflow`
- `Time: 30-60 sec`
- `Acceptable for most steel and copper substrates`

Right -- Critical Work (X: 12.0", W: 11.5"):
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `CRITICAL APPLICATIONS` Barlow SemiBold 18 pt `#E8A020`
- `Conductivity: <20 uS/cm` JetBrains Mono 16 pt `#27AE60`
- `Water: DI only (18 MOhm preferred)`
- `Stages: Double or triple counterflow`
- `Time: 30-60 sec per stage`
- `Required for: oil/gas downhole, aerospace, semiconductor, non-magnetic verification parts`

**Bottom callout (full-width, Y: 31.5"):**
- `A $5 conductivity meter saves thousands in EN bath chemistry. Measure. Every. Time.` Inter Medium 14 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- EN (High Phos) -- Pre-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse parameters shown are typical industry values for pre-plate rinsing in electroless nickel processes. Consult your process supplier for application-specific guidance.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse EN High-P Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This rinse poster has more technical weight than the pre-activation rinse (#233) because the consequences of failure are more severe and more expensive. The "30-second rule" for zincated aluminum is a memorable, actionable takeaway. The contamination threat matrix connects specific drag-in chemicals to specific bath failures -- this is the kind of cause-and-effect teaching that makes a poster useful at 3 AM when the bath is pitting and the operator needs to think backward through the process.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #235 -- Construction Workup v1.0*
*2026-04-26*
