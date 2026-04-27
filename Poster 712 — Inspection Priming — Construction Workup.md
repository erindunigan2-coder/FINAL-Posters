---
Project: Plating Posters Inc
Poster Number: 712
Title: "Inspection -- Priming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Inspection and handling requirements for industrial primers. DFT measurement (ASTM D7091), SSPC-PA 2 acceptance, adhesion testing (ASTM D4541), zinc loading verification, salt spray performance expectations, and key standards governing this cluster.
Process Scope: Inspection and handling for industrial priming -- Stage 8 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - IndustrialPriming
  - Inspection
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #712 -- Construction Workup
## Inspection -- Priming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 8. The final poster in the Industrial Priming cluster. This covers everything that happens after cure and before topcoating: DFT measurement, adhesion verification, visual inspection, and the salt spray performance benchmarks that justify why zinc-rich primers are specified for the most demanding applications. The hero is a salt spray performance comparison showing IOZ alone, OZ alone, and the full IOZ + epoxy + urethane system.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Salt spray performance hero (Block B):** Horizontal bar chart comparing B117 hours for different primer and system configurations. Built with rectangles and labels.
2. **DFT measurement panel (Block D):** ASTM D7091 and SSPC-PA 2 procedures and acceptance.
3. **Adhesion testing panel (Block E):** ASTM D4541 pull-off and requirements.
4. **Key standards reference (Block F):** Complete list of governing standards for the cluster.
5. **Zinc loading verification sidebar (Block G):** COA and XRF.

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
  Stage 8 highlighted (Bright Silver)
ZONE 3 -- SALT SPRAY PERFORMANCE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DFT MEASUREMENT + SSPC-PA 2 (14.5"--21.0" / ~6.5")
ZONE 5 -- ADHESION + ZINC LOADING VERIFICATION (21.0"--27.0" / ~6.0")
ZONE 6 -- KEY STANDARDS REFERENCE (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Industrial Priming -- Stage 8 of 8` -- 32 pt `#C8D0D8` (Bright Silver). Y: 1.4".
**Tagline:** `Measure the DFT. Test the adhesion. Verify the cure. The primer you cannot see failing is the one that will.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#C8D0D8`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cured primer on substrate  -->  After: Verified, documented, ready for topcoat or service`

---

### ZONE 3 -- Salt Spray Performance Hero

**Section label:** `SALT SPRAY PERFORMANCE -- WHY ZINC-RICH PRIMERS ARE SPECIFIED` -- Y: 4.4".

**BLOCK B -- Performance Bar Chart (Y: 5.0" to 14.0")**

Horizontal bar chart showing ASTM B117 salt spray hours:

Seven bars, each a rounded rectangle of variable width, sorted by performance:

| System | B117 Hours | Bar Color | Bar Width (relative) |
|---|---|---|---|
| IOZ + epoxy intermediate + PU topcoat (6--10 mils total) | 5,000--10,000+ | `#27AE60` | Full width |
| IOZ primer alone (3 mil DFT) | 1,500--3,000+ | `#27AE60` at 70% | ~30% |
| Epoxy primer alone (3 mil DFT) | 500--1,500 | `#2EC4B6` | ~15% |
| OZ primer alone (3 mil DFT) | 500--1,500 | `#E8A020` | ~15% |

Bar chart layout:
- Y: 5.5" to 13.5". Left labels at X: 0.5" (system name). Bars start at X: 8.0", maximum width to X: 23.5".
- Each bar: rounded rect, H: 1.5", radius 4. Gap between bars: 0.5".
- System name: Inter Medium 14 pt `#F0EDE8` (left-aligned, vertically centered with bar)
- Hours label: JetBrains Mono 16 pt, `#F0EDE8`, positioned at end of bar

Scale bar at bottom (X: 8.0" to 23.5"):
- Tick marks at 0, 2,000, 4,000, 6,000, 8,000, 10,000 hours
- JetBrains Mono 11 pt `#F0EDE8` at 50%
- Label: `ASTM B117 -- 5% NaCl Fog at 95 deg F` Inter Medium 12 pt `#F0EDE8` at 60%

Context callout (bottom of zone):
- Rounded rect, W: 23.0", H: 0.8", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `A properly applied IOZ + epoxy + urethane system on bridges and offshore steel routinely provides 20--30+ years of service life.` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- DFT Measurement + SSPC-PA 2

**Section label:** `DFT MEASUREMENT -- GETTING IT RIGHT` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.8"):**

**Left -- DFT Measurement (X: 0.5", W: 11.0"):**

Callout, fill `#1E2435`, left accent `#2EC4B6`:
- Title: `ASTM D7091 -- MAGNETIC GAUGE` Barlow SemiBold 18 pt `#2EC4B6`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
- `Magnetic gauge (steel) or eddy current gauge (aluminum)`
- `IOZ on steel: use gauge calibrated for rough surfaces`
- `Some gauges read HIGH on rough IOZ -- verify with calibration shims`
- `Minimum 5 spot readings per area`
- `Record readings in coating inspection report`

DFT targets summary:
| Primer | Target DFT | Min | Max |
|---|---|---|---|
| IOZ | 2.5--4.0 mils | 2.0 mils | 5.0 mils (mud cracking above this) |
| OZ | 2.0--3.5 mils | 1.5 mils | 4.0 mils |
| Epoxy | 1.0--3.0 mils | 0.8 mils | Per TDS |

Data: JetBrains Mono 12 pt.

**Right -- SSPC-PA 2 Acceptance (X: 12.0", W: 11.5"):**

Callout, fill `#1E2435`, left accent `#E8A020`:
- Title: `SSPC-PA 2 -- ACCEPTANCE CRITERIA` Barlow SemiBold 18 pt `#E8A020`

Content:
- `SSPC-PA 2 defines how to evaluate DFT conformance for protective coatings`
- `Spot measurement: Average of 3--5 gauge readings within a 1.5" diameter circle`
- `Area measurement: Average of spot measurements across a defined area`
- `Acceptance: No individual spot reading below 80% of specified minimum DFT`
- `No area average below the specified minimum DFT`
- Inter Regular 13 pt `#F0EDE8`

Key rule: `DFT is not a single number -- it is a statistical distribution. SSPC-PA 2 ensures the distribution meets the specification.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 5 -- Adhesion + Zinc Loading Verification

**Two-column layout (Y: 21.2" to 26.8"):**

**Left -- Adhesion Testing (X: 0.5", W: 11.0"):**

Section label: `ADHESION TESTING` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

| Test | Method | Equipment | Pass Criterion |
|---|---|---|---|
| Pull-off (primary) | ASTM D4541 | Elcometer / Positest AT | > 200 psi (or cohesive failure in primer) |
| X-cut tape | ASTM D3359 Method A | Razor + tape | No delamination from scribe |

Callout, fill `#1E2435`, left accent `#2EC4B6`:
- `For IOZ primers: adhesion failure often occurs in the IOZ film itself (cohesive failure) rather than at the steel interface`
- `Cohesive failure in the primer at > 200 psi is acceptable -- it means the steel bond is STRONGER than the primer`
- `Adhesive failure at the primer-steel interface at ANY psi = surface prep problem`
- Inter Regular 13 pt `#F0EDE8`

**Right -- Zinc Loading Verification (X: 12.0", W: 11.5"):**

Section label: `ZINC LOADING -- IS IT REALLY ZINC-RICH?` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Callout, fill `#1E2435`, left accent `#E8A020`:
- Title: `VERIFICATION METHODS` Barlow SemiBold 16 pt `#E8A020`
- `Manufacturer COA (Certificate of Analysis):`
- `  -- Confirms zinc content in the supplied product`
- `  -- IOZ: 75--85% zinc by weight in dry film`
- `  -- OZ: 65--80% zinc by weight in dry film`
- `  -- Per SSPC-Paint 20 and SSPC-PS 12.01`
- Inter Regular 13 pt `#F0EDE8`

Secondary method:
- `XRF analysis (rare -- laboratory method):`
- `  -- Portable XRF can verify zinc presence in the applied film`
- `  -- Used for forensic analysis of coating failures`
- `  -- Not routine QC`
- Inter Regular 12 pt `#F0EDE8` at 70%

Zinc dust spec: `ASTM D520 (Zinc Dust) Type I = irregular, Type II = spherical. ASTM D521 = Chemical Analysis of Zinc Dust (Metallic Zinc Content).` JetBrains Mono 11 pt `#F0EDE8` at 50%.

---

### ZONE 6 -- Key Standards Reference

**Section label:** `KEY STANDARDS -- INDUSTRIAL PRIMING CLUSTER` -- Y: 27.2".

**BLOCK F -- Standards Table (Y: 27.8" to 32.3")**

| Standard | Description | Use |
|---|---|---|
| SSPC-PS 12.01 | Guide for Selecting Zinc-Rich Primers | IOZ vs. OZ selection |
| SSPC-Paint 20 | Zinc-Rich Primers (Type I inorganic, Type II organic) | Primer specification |
| ASTM D520 | Specification for Zinc Dust | Zinc dust quality |
| ASTM D521 | Chemical Analysis of Zinc Dust | Metallic zinc content |
| ASTM D7091 | DFT by Magnetic/Eddy Current Gauge | Film thickness measurement |
| SSPC-PA 2 | DFT Conformance Procedure | Acceptance criteria |
| ASTM D4541 | Pull-Off Adhesion | Adhesion verification |
| ASTM B117 | Salt Spray (Neutral Fog) | Corrosion testing |
| ASTM D1654 | Evaluation After Salt Spray | Creepage from scribe |
| ISO 12944 | Corrosion Protection by Paint Systems | System design (C1--C5, CX) |
| MIL-PRF-23377 | Chromated Epoxy Primer | Aerospace |
| MIL-PRF-85582 | Non-Chromate Epoxy Primer | Aerospace |

Header: `#3A4055`. Alternating rows `#1E2435` / `#252B3D`. Standard codes: JetBrains Mono 12 pt `#2EC4B6`. Descriptions: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection -- Priming`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; SSPC standards; ASTM test methods; Watson Research Brief. This poster concludes Cluster 7: Industrial Priming Systems (Posters #704--#712).`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Priming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the Industrial Priming cluster with the data that justifies everything that came before. The salt spray bar chart is the hero because it answers the question every specifier asks: "How long will this system last?" An IOZ + epoxy + urethane system at 5,000--10,000+ hours B117 is the gold standard for bridges, offshore, and marine steel. The DFT and adhesion panels give the inspector the tools and criteria. The standards reference serves as a one-page lookup for the entire cluster -- hang this poster next to the others and you have a complete wall reference for industrial priming.

---

*Alaina -- Poster #712 -- Construction Workup v1.0 -- 2026-04-26*
