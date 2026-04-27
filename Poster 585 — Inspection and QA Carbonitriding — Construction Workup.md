---
Project: Plating Posters Inc
Poster Number: 585
Title: "Inspection & QA -- Carbonitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 3: Carbonitriding, Sections 3.7, 3.9 / Process 1 Sections 1.9, 1.10)"
Technical Source: Quality testing and inspection for carbonitrided parts. Microhardness traverse, surface hardness, retained austenite, nitrogen measurement, microstructure evaluation, and applicable standards.
Process Scope: Carbonitriding inspection, quality assurance, and applicable standards
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Carbonitriding
  - Inspection
  - QualityAssurance
  - HeatTreatment
  - ConstructionWorkup
---

# Poster #585 -- Construction Workup
## Inspection & QA -- Carbonitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the carbonitriding cluster. Everything comes down to this: did the case meet spec? This poster covers all the tests a metallurgist uses to verify a carbonitrided part -- microhardness traverse for effective case depth, surface and core hardness, retained austenite measurement, nitrogen content verification, and microstructure evaluation. It also lists the applicable industry standards.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Test method grid (Block B -- HERO):** 3x2 grid of test method cards -- each card describes one QA test.
2. **Acceptance criteria table (Block D):** Master table of typical accept/reject values.
3. **Applicable standards panel (Block E):** Standards list with coverage descriptions.
4. **Common failures strip (Block F):** 4 inspection findings and their root causes.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- TEST METHOD GRID / HERO (2.9"--15.5" / ~12.6")
  Block B: 3x2 QA test cards
ZONE 3 -- ACCEPTANCE CRITERIA TABLE (15.5"--21.5" / ~6.0")
  Block D: Accept/reject master table
ZONE 4 -- APPLICABLE STANDARDS (21.5"--27.0" / ~5.5")
  Block E: Standards list
ZONE 5 -- COMMON INSPECTION FINDINGS (27.0"--32.5" / ~5.5")
  Block F: 4 finding cards
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Carbonitriding -- Every Test That Proves the Case Met Spec` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The furnace says it ran to recipe. The tests say whether the parts actually hardened. Trust the tests.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Test Method Grid (HERO)

**Section label:** `SIX QUALITY TESTS FOR CARBONITRIDED PARTS` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- 3x2 Test Grid**

Y: 3.8" to 15.3". Cards in 3 columns x 2 rows.

Each card: Rounded rect, W: 7.33", H: 5.3", fill `#1E2435`, radius 6. Gap: 0.33".

Row 1 (Y: 3.8"):

| Position | Test | Accent | Method | Accept | Key Note |
|---|---|---|---|---|---|
| R1C1 (X: 0.5") | EFFECTIVE CASE DEPTH (ECD) | `#27AE60` | `Microhardness traverse per ASTM E384` / `Knoop or Vickers, 300--500 gf` | `Depth to 50 HRC (~513 HV)` | `THE primary measurement for carbonitriding` |
| R1C2 (X: 8.17") | SURFACE HARDNESS | `#E8A020` | `Rockwell C per ASTM E18` / `Or Vickers microhardness at surface` | `58--63 HRC typical` | `Per drawing specification` |
| R1C3 (X: 15.83") | CORE HARDNESS | `#2EC4B6` | `Rockwell C per ASTM E18` / `Measured at mid-section` | `25--45 HRC (grade dependent)` | `Depends on steel alloy and section size` |

Row 2 (Y: 9.4"):

| Position | Test | Accent | Method | Accept | Key Note |
|---|---|---|---|---|---|
| R2C1 (X: 0.5") | RETAINED AUSTENITE | `#E05C5C` | `Visual estimate at 500--1000x` / `Or XRD per ASTM E975` | `Max 15--20% (per spec)` | `HIGHER RISK in CN vs. carburizing -- nitrogen stabilizes RA` |
| R2C2 (X: 8.17") | NITROGEN CONTENT | `#2EC4B6` | `GDOES or combustion analysis` | `0.2--0.4 wt% N at surface` | `Verifies nitrogen actually entered the case` |
| R2C3 (X: 15.83") | MICROSTRUCTURE | `#E8A020` | `Metallographic section, 2% nital etch` / `100--500x magnification` | `Tempered martensite; no porosity; no massive carbides` | `Check for surface microporosity from excess NH3` |

Interior per card:
- Test name: Barlow SemiBold, 18 pt, accent color
- Left accent: 0.06", accent color
- Method: Inter Regular, 13 pt, `#F0EDE8`, line height 150%
- Accept: JetBrains Mono Regular, 13 pt, `#27AE60`
- Key note: Inter Medium, 12 pt, `#F0EDE8` at 70%

---

### ZONE 3 -- Acceptance Criteria Table

**Section label:** `ACCEPTANCE CRITERIA -- QUICK REFERENCE` -- Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Master Table**

Y: 16.3" to 21.3". Columns: Parameter (5.5") | Typical Range (5.0") | Spec Reference (5.0") | Action if Fail (7.5")

Header row: fill `#3A4055`. Barlow SemiBold, 14 pt.
Data rows: alternating fills, H: 0.8".

| Parameter | Typical Range | Spec Reference | Action if Fail |
|---|---|---|---|
| ECD (at 50 HRC) | 0.005--0.030 in | Drawing + AMS 2759 | Scrap or rework (re-process if under) |
| Surface hardness | 58--63 HRC | Drawing | If low: check quench severity, Cp, NH3 |
| Core hardness | 25--45 HRC | Drawing | Grade/section dependent |
| Retained austenite | < 15--20% | Spec dependent | Sub-zero treat at -100 to -120 F |
| Surface nitrogen | 0.2--0.4 wt% N | Process validation | If low: check NH3 flow; if high: reduce NH3 |
| Microstructure | Tempered martensite, no porosity | AMS 2759 | Porosity = excess NH3; adjust process |

Data: JetBrains Mono Regular, 12 pt. Action if Fail in `#E05C5C` for scrap, `#E8A020` for rework.

---

### ZONE 4 -- Applicable Standards

**Section label:** `APPLICABLE STANDARDS` -- Y: 21.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Standards List**

Y: 22.3" to 26.8". Columns: Standard (4.5") | Coverage (18.5")

Header row: fill `#3A4055`. Barlow SemiBold, 14 pt.
Data rows: alternating fills, H: 0.8".

| Standard | Coverage |
|---|---|
| AMS 2759 | General heat treatment of steel parts (baseline) |
| AMS 2759/7 | Carburizing and heat treatment of carburizing grade steel parts -- covers carbonitriding |
| ASTM E384 | Microhardness testing (Knoop and Vickers) |
| ASTM E18 | Rockwell hardness testing |
| ASTM E975 | Retained austenite measurement by XRD |
| CQI-9 | AIAG special process audit for heat treatment (automotive) |

Data: JetBrains Mono Regular, 13 pt for standard codes. Coverage: Inter Regular 13 pt.

---

### ZONE 5 -- Common Inspection Findings

**Section label:** `COMMON FINDINGS AND ROOT CAUSES` -- Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- 4 Finding Cards**

Y: 27.8" to 32.3". Four cards in a row.

| Card | X | Finding | Root Cause | Corrective Action |
|---|---|---|---|---|
| 1 | 0.5" | SHALLOW CASE | Low temp, short time, or excess NH3 blocking C | Increase time/temp; optimize NH3 % |
| 2 | 6.33" | HIGH RETAINED AUSTENITE | Excess ammonia; surface N too high | Reduce NH3; sub-zero treatment |
| 3 | 12.16" | SURFACE MICROPOROSITY | Excess ammonia; nitrogen gas entrapment | Reduce NH3 addition rate; avoid spikes |
| 4 | 18.0" | LOW SURFACE HARDNESS | Quench too slow; steel grade wrong; decarb | Verify quench; check material cert; check Cp |

Card format: same as all troubleshooting strips.

---

### ZONE 6 -- Footer

Standard footer. Title: `Inspection & QA -- Carbonitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA Carbonitriding -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The test method grid is the hero -- each card is a self-contained reference for one QA test. The nitrogen content card (R2C2) is unique to carbonitriding and does not appear on carburizing QA posters. The retained austenite card (R2C1) gets a Coral accent because high RA is the single most common carbonitriding quality issue.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #585 -- Construction Workup v1.0*
*2026-04-26*
