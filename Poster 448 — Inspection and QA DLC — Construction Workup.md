---
Project: Plating Posters Inc
Poster Number: 448
Title: "Inspection & QA -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Sections 5.3, 5.8)"
Process Scope: Post-coating inspection, testing, and quality assurance for DLC coatings
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #448 -- Construction Workup
## Inspection & QA -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the DLC cluster. This is where coating quality is verified -- hardness, adhesion, thickness, friction, and sp3 content. DLC inspection uses a mix of standard mechanical tests (Rockwell indent, scratch test, nanoindentation) and specialized analytical tools (Raman spectroscopy, ball-on-disc tribometry). The adhesion classification (VDI 3198 HF1-HF6) is the hero visual -- it is the universal language of DLC adhesion quality. The Raman spectrum interpretation panel is the intellectual backbone.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Adhesion classification hero (Block B):** VDI 3198 HF1 through HF6 scale with descriptions and accept/reject criteria. Built as a horizontal scale with color-coded zones.
2. **Test methods reference table (Block D):** All QA test methods in one table.
3. **Raman spectroscopy interpretation (Block E):** D and G peak positions and what they mean.
4. **Accept/reject decision tree (Block F):** Go/no-go flowchart.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- VDI 3198 ADHESION HERO (2.9"--14.5" / ~11.6")
  Block B: HF1--HF6 adhesion classification scale
ZONE 3 -- TEST METHODS REFERENCE (14.5"--20.5" / ~6.0")
  Block D: Complete QA test method table
ZONE 4 -- RAMAN SPECTROSCOPY (20.5"--26.5" / ~6.0")
  Block E: D/G peak interpretation guide
ZONE 5 -- ACCEPT/REJECT DECISION (26.5"--32.5" / ~6.0")
  Block F: Go/no-go criteria
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`.
**Subheading:** `Diamond-Like Carbon -- Verifying Coating Quality` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `You cannot see sp3 content with your eyes. You cannot feel 2,000 HV with your fingers. Testing is not optional -- it is the only way to know what you deposited.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- VDI 3198 Adhesion Classification Hero

**Section label:** `ADHESION -- THE VDI 3198 ROCKWELL INDENTATION TEST` -- Y: 3.1".

**BLOCK B -- HF Scale**

Y: 3.8" to 14.3".

**Introduction text (Y: 3.8" to 4.8"):**
- Inter Regular, 14 pt, `#F0EDE8`
- Text: `A Rockwell C indent (150 kgf, diamond cone) is made on the coated surface. The crack pattern around the indent is compared to the HF (Haftfestigkeitsklasse / adhesion class) reference images. HF1 = excellent adhesion. HF6 = complete failure. For most DLC applications, HF1 through HF4 are acceptable.`

**Six HF classification cards (Y: 5.2" to 14.0"):**

Two rows of three cards.

| Position | Class | Accent | Description | Verdict |
|---|---|---|---|---|
| R1C1 | HF1 | `#27AE60` | No delamination. Only radial cracks from indent. Coating intact around entire indentation. | EXCELLENT |
| R1C2 | HF2 | `#27AE60` | Minor radial cracks. Slight spalling directly adjacent to indent edge. < 10% of indent circumference affected. | GOOD |
| R1C3 | HF3 | `#2EC4B6` | Moderate spalling at indent edge. Radial cracks with some lateral delamination. 10--30% circumference. | ACCEPTABLE |
| R2C1 | HF4 | `#E8A020` | Significant spalling around indent. Delamination extends beyond radial cracks. 30--50% circumference. | MARGINAL |
| R2C2 | HF5 | `#E05C5C` | Extensive delamination. Coating lifted in large flakes around indent. > 50% circumference. | REJECT |
| R2C3 | HF6 | `#E05C5C` | Complete delamination around indent. Coating fully separated from substrate in indent zone. | REJECT |

Each card: Rounded rect, W: 7.33", H: 4.0", fill `#1E2435`, left accent 0.06".
- Class badge: Rounded rect, 1.5" x 0.5", fill accent color. Text: `HF1` etc., Barlow Condensed ExtraBold, 18 pt, `#1A1F2E`.
- Description: Inter Regular, 13 pt, `#F0EDE8`, line height 160%.
- Verdict: Barlow SemiBold, 16 pt, accent color. Right-aligned at bottom of card.

**Acceptance note (below cards, Y: 13.5"):**
- `Industry standard: HF1--HF2 preferred. HF3--HF4 acceptable for many applications. HF5--HF6 always rejected. For high-stress applications (cutting tools, piston rings), specify HF1--HF2 only.` -- Inter Medium, 13 pt, `#E8A020`.

---

### ZONE 3 -- Test Methods Reference

**Section label:** `COMPLETE QA TEST REFERENCE` -- Y: 14.7".

**BLOCK D -- Test Methods Table**

Y: 15.3" to 20.3".

| Test | Standard | What It Measures | Equipment | Typical Values (Good DLC) |
|---|---|---|---|---|
| Rockwell adhesion | VDI 3198 | Adhesion class (HF1--HF6) | Rockwell hardness tester + optical microscope | HF1--HF4 |
| Nanoindentation | ISO 14577 | Hardness (GPa) and elastic modulus | Nanoindenter (Berkovich tip) | a-C:H: 10--20 GPa / ta-C: 40--80 GPa |
| Scratch test | ASTM C1624 | Critical load Lc1 (cohesive) and Lc2 (adhesive) | Scratch tester with Rockwell diamond stylus | Lc2 > 10--30 N |
| Calotest | ISO 26423 | Coating thickness (um) | Ball cratering device + optical measurement | 0.5--5 um per specification |
| Ball-on-disc | ASTM G99 | Friction coefficient and wear rate | Pin-on-disc tribometer | CoF: 0.05--0.15 (dry) |
| Raman spectroscopy | -- | sp3/sp2 content; D and G peak analysis | Raman spectrometer (514 or 532 nm laser) | See Zone 4 |
| Visual inspection | -- | Color, uniformity, defects | Naked eye + 10x magnification | Uniform dark coating, no flaking |
| Profilometry | ISO 4287 | Surface roughness (Ra) | Stylus profilometer or optical | Ra < 0.05 um (bearing applications) |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Inter Regular 12 pt `#F0EDE8`. Values: JetBrains Mono 11 pt `#2EC4B6`.

---

### ZONE 4 -- Raman Spectroscopy Interpretation

**Section label:** `RAMAN SPECTROSCOPY -- READING THE SPECTRUM` -- Y: 20.7".

**BLOCK E -- D/G Peak Guide**

Y: 21.3" to 26.3".

**Left -- Spectrum description (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6`

Title: `THE D AND G PEAKS` -- Barlow SemiBold, 18 pt, `#2EC4B6`.

Content (Inter Regular, 14 pt, `#F0EDE8`):

```
Every DLC film produces two broad peaks in
its Raman spectrum:

G PEAK (~1580 cm-1): "Graphite" peak.
  All sp2 carbon. Always present.

D PEAK (~1350 cm-1): "Disorder" peak.
  Activated by sp3 disorder in sp2 clusters.

The ratio ID/IG, the G peak position, and the
G peak width together characterize the DLC type
and quality.
```

**Right -- Interpretation table (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`

Title: `WHAT THE SPECTRUM TELLS YOU` -- Barlow SemiBold, 18 pt, `#E8A020`.

| Observation | Meaning |
|---|---|
| G peak shifts UP (toward 1600 cm-1) | More sp2 clustering; film is more graphitic |
| G peak shifts DOWN (toward 1540 cm-1) | More sp3; film is more diamond-like |
| Broad G peak (FWHM > 150 cm-1) | Highly disordered; typical of good a-C:H |
| Narrow G peak (FWHM < 100 cm-1) | Ordered graphite; film has low sp3 |
| High ID/IG ratio | More disorder; can indicate higher sp3 for a-C:H |
| Photoluminescence background (slope) | High hydrogen content; strong in a-C:H |
| No D peak visible | Very high sp3 content; ta-C signature |

Data: Inter Regular, 12 pt, `#F0EDE8`. Observation: JetBrains Mono 11 pt `#E8A020`.

---

### ZONE 5 -- Accept/Reject Decision

**Section label:** `GO / NO-GO -- ACCEPT OR REJECT THE BATCH` -- Y: 26.7".

**BLOCK F -- Decision Criteria Cards**

Y: 27.3" to 32.3". Five cards in a row.

| Card | X | W | Test | Accept | Reject |
|---|---|---|---|---|---|
| 1 | 0.5" | 4.4" | ADHESION | HF1--HF4 (HF1--HF2 for critical apps) | HF5 or HF6 |
| 2 | 5.1" | 4.4" | HARDNESS | Within spec range (+/- 15%) | Below minimum; > 20% deviation |
| 3 | 9.7" | 4.4" | THICKNESS | Within tolerance (+/- 10% of target) | Outside tolerance; visible thin spots |
| 4 | 14.3" | 4.4" | FRICTION | CoF < 0.15 (dry) per spec | CoF > 0.20; inconsistent values |
| 5 | 18.9" | 4.6" | VISUAL | Uniform dark color; no flaking, blistering, or haze | Flaking, delamination, color variation, haze |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6.
- Test: Barlow SemiBold, 16 pt, `#F0EDE8`, top center.
- Accept: Inter Medium, 13 pt, `#27AE60`. Label: `ACCEPT` Barlow SemiBold 12 pt `#27AE60`.
- Reject: Inter Medium, 13 pt, `#E05C5C`. Label: `REJECT` Barlow SemiBold 12 pt `#E05C5C`.
- Divider line between accept and reject: 1 pt `#3A4055`.

---

### ZONE 6 -- Footer

Standard. Title: `Inspection & QA -- DLC`. Version `v1.0 -- 2026`.

Footer disclaimer text:

> This poster is an educational reference tool. Process parameters shown are typical industry values for Diamond-Like Carbon coating inspection. Adhesion classification per VDI 3198. Specific acceptance criteria vary by customer specification and application. Consult your process supplier and quality requirements for application-specific acceptance limits. Source: General industry knowledge; VDI 3198; VDI 2840; ISO 14577; ASTM C1624; ASTM G99.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection and QA DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the DLC cluster with the quality gate. The VDI 3198 scale is the most important visual -- every DLC coating engineer in the world uses this classification system. The Raman interpretation panel is what separates this poster from a generic "inspection checklist" -- it gives real analytical depth. The accept/reject cards in Zone 5 provide the operational bottom line. Together, the 10 DLC posters (439--448) form a complete reference library for Diamond-Like Carbon coating from incoming inspection to final QA.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #448 -- Construction Workup v1.0*
*2026-04-26*
