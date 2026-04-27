---
Project: Plating Posters Inc
Poster Number: 458
Title: "Inspection & QA -- Ion Implantation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Sections 6.1, 6.5, 6.8)"
Process Scope: Post-implantation characterization, quality assurance, and acceptance testing
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IonImplantation
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #458 -- Construction Workup
## Inspection & QA -- Ion Implantation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the Ion Implantation cluster. Inspection for ion implantation relies on analytical techniques that are distinct from any other process in the poster library. You cannot measure implant quality with a micrometer, a coating thickness gauge, or a visual inspection. SIMS (Secondary Ion Mass Spectrometry) is the gold standard -- it provides a depth profile of the implanted species with nanometer resolution. For semiconductor, 4-point probe sheet resistance is the fast inline check. For industrial, nanoindentation and pin-on-disc wear testing measure the actual property improvements. The hero visual is a SIMS depth profile annotated with key features.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **SIMS depth profile hero (Block B):** Annotated SIMS profile showing concentration vs. depth.
2. **Characterization methods table (Block D):** All QA methods for both semiconductor and industrial.
3. **Semiconductor inline QC (Block E):** 4-point probe and sheet resistance mapping.
4. **Common issues and accept/reject (Block F):** Go/no-go decision criteria.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SIMS DEPTH PROFILE HERO (2.9"--14.5" / ~11.6")
  Block B: Annotated SIMS profile with key features
ZONE 3 -- CHARACTERIZATION METHODS (14.5"--20.5" / ~6.0")
  Block D: Complete test method reference table
ZONE 4 -- SEMICONDUCTOR INLINE QC (20.5"--26.5" / ~6.0")
  Block E: 4-point probe, sheet resistance, and dose verification
ZONE 5 -- ACCEPT/REJECT CRITERIA (26.5"--32.5" / ~6.0")
  Block F: Go/no-go decisions for both applications
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`.
**Subheading:** `Ion Implantation -- Verifying What You Cannot See` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `The implanted layer is 50--500 nm deep and invisible to the naked eye. Your coating thickness gauge is useless here. The only way to verify implant quality is analytical instrumentation.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- SIMS Depth Profile Hero

**Section label:** `SIMS -- THE GOLD STANDARD FOR IMPLANT VERIFICATION` -- Y: 3.1".

**BLOCK B -- Annotated SIMS Profile**

Y: 3.8" to 14.3".

**Left -- Profile Visualization (X: 0.5", W: 14.0"):**
- Rounded rect container, H: 10.0", fill `#1E2435`
- Title: `SIMS DEPTH PROFILE -- N+ IN STEEL` Barlow SemiBold 18 pt `#27AE60`. Y: 4.2".

Profile diagram (Y: 5.0" to 12.5"):
- Axes:
  - X-axis: `DEPTH (nm)` JetBrains Mono 12 pt `#F0EDE8`. Marks at 0, 100, 200, 300, 400, 500.
  - Y-axis: `CONCENTRATION (atoms/cm3)` JetBrains Mono 12 pt `#F0EDE8`. Log scale: 10^18 to 10^22.
- Profile curve: Approximate Gaussian shape
  - Rising from surface (0 nm) to peak at Rp
  - Peak at ~100 nm (for 100 keV N+ in steel)
  - Falling off at greater depth
  - Built with a series of short line segments, stroke 3 pt `#27AE60`

Annotations on profile:
- Arrow at surface: `Surface concentration` Inter Regular 11 pt `#F0EDE8`
- Arrow at peak: `Rp (projected range) -- peak concentration` JetBrains Mono 11 pt `#E8A020`
- Arrow at peak width: `Delta Rp (straggle) -- profile width` JetBrains Mono 11 pt `#2EC4B6`
- Arrow at deep tail: `Channeling tail (if present)` Inter Regular 11 pt `#E05C5C`
- Dashed horizontal line at target concentration: `TARGET PEAK CONC.` JetBrains Mono 10 pt `#E8A020`

**Right -- Profile Interpretation Guide (X: 15.0", W: 8.5"):**
- Rounded rect, H: 10.0", fill `#1E2435`, left accent `#E8A020`
- Title: `READING THE PROFILE` Barlow SemiBold 18 pt `#E8A020`. Y: 4.2".

| Feature | What It Tells You |
|---|---|
| Peak position (Rp) | Confirms implant energy was correct. Rp scales with energy. |
| Peak concentration | Confirms dose was delivered. Higher dose = higher peak. |
| Profile width (Delta Rp) | Natural straggle; increases with energy. Wider = more distributed. |
| Channeling tail | Deep extension beyond Gaussian profile. Indicates ions traveled along crystal channels. Should be minimal if tilt/screen oxide used. |
| Surface peak | May indicate surface contamination stopping ions early, or sputtering redepositing material. |
| Shoulder or double peak | May indicate molecular contamination in beam (e.g., BF2+ partially dissociating to B+ at different energy). |

Data: Inter Regular, 12 pt, `#F0EDE8`. Feature: JetBrains Mono 12 pt `#E8A020`.

---

### ZONE 3 -- Characterization Methods

**Section label:** `COMPLETE CHARACTERIZATION REFERENCE` -- Y: 14.7".

**BLOCK D -- Methods Table**

Y: 15.3" to 20.3".

| Method | Standard | What It Measures | Equipment | Application |
|---|---|---|---|---|
| SIMS | ASTM E1438 | Depth profile of implanted species (concentration vs. depth) | Secondary ion mass spectrometer | Gold standard for dose and depth verification; destructive |
| 4-point probe | ASTM F84 | Sheet resistance (ohms/square) after anneal | Four-point probe station | Semiconductor inline QC; fast, non-destructive |
| Spreading resistance (SRP) | ASTM F525 | Carrier concentration vs. depth | Spreading resistance profiler | Detailed electrical profile; destructive |
| Nanoindentation | ISO 14577 | Surface hardness and elastic modulus | Nanoindenter (Berkovich tip) | Industrial -- verifies hardness improvement |
| Pin-on-disc wear test | ASTM G99 | Friction coefficient and wear rate | Tribometer | Industrial -- verifies wear improvement |
| Rutherford Backscattering (RBS) | -- | Composition and dose (non-destructive) | MeV ion beam + detector | Research; quantitative without standards |
| Cross-section TEM | -- | Lattice damage, amorphous zones, precipitates | Transmission electron microscope | Research -- direct observation of implant damage |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Inter Regular 12 pt `#F0EDE8`. Application: JetBrains Mono 11 pt `#2EC4B6`.

---

### ZONE 4 -- Semiconductor Inline QC

**Section label:** `SEMICONDUCTOR -- FAST INLINE VERIFICATION` -- Y: 20.7".

**BLOCK E -- 4-Point Probe and Sheet Resistance**

Y: 21.3" to 26.3". Two panels.

**Left -- How It Works (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `THE 4-POINT PROBE` Barlow SemiBold 18 pt `#2EC4B6`.

Content (Inter Regular, 14 pt, `#F0EDE8`):

```
Four equally-spaced probes touch the wafer surface.
Current flows through the outer two probes.
Voltage is measured across the inner two probes.

Sheet resistance Rs = (pi / ln2) x (V / I)
                    = 4.532 x (V / I)

Units: ohms/square (ohms/sq)

Lower Rs = higher dose and/or better activation.
Measurement time: < 5 seconds per site.
Typical: 9-point or 49-point wafer map.
```

JetBrains Mono 12 pt `#F0EDE8`. Formula: `#E8A020`.

**Right -- What Good Looks Like (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `ACCEPTANCE CRITERIA` Barlow SemiBold 18 pt `#E8A020`.

| Metric | Specification | Typical Requirement |
|---|---|---|
| Rs mean | Within +/- 3--5% of target | Process control; tight spec |
| Rs uniformity (1 sigma) | < 1--2% across wafer | Indicates uniform dose and anneal |
| Wafer-to-wafer Rs | < 1--3% variation | Indicates stable implanter and anneal |
| Lot-to-lot Rs | < 2--5% variation | Long-term process stability |

Data: JetBrains Mono 12 pt `#F0EDE8`. Specification: Inter Medium 12 pt `#27AE60`.

---

### ZONE 5 -- Accept/Reject Criteria

**Section label:** `GO / NO-GO -- ACCEPT OR REJECT` -- Y: 26.7".

**BLOCK F -- Decision Cards**

Y: 27.3" to 32.3". Two panels (semiconductor and industrial).

**Left -- Semiconductor (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `SEMICONDUCTOR ACCEPT/REJECT` Barlow SemiBold 16 pt `#2EC4B6`.

| Test | Accept | Reject |
|---|---|---|
| Sheet resistance (Rs) | Within +/- 5% of target; uniformity < 2% | Outside spec; non-uniform map |
| SIMS profile (if measured) | Rp within +/- 5% of target; dose within +/- 3% | Peak shifted; dose deviation > 5%; channeling tail |
| Visual | Clean, no particles, no resist residue | Particles, staining, resist residue |
| Wafer warpage | Within spec for downstream processing | Exceeds bow/warp limit |

Accept: Inter Medium, 12 pt, `#27AE60`.
Reject: Inter Medium, 12 pt, `#E05C5C`.

**Right -- Industrial (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `INDUSTRIAL ACCEPT/REJECT` Barlow SemiBold 16 pt `#E8A020`.

| Test | Accept | Reject |
|---|---|---|
| Nanoindentation hardness | Within spec range; improvement > 30% over baseline | Below minimum hardness; no measurable improvement |
| Wear test (if specified) | Wear rate reduction > 2x vs. untreated baseline | No improvement; inconsistent results |
| SIMS (if specified) | Dose and depth within tolerance | Dose deviation > 10%; depth shifted |
| Visual | Uniform color (discoloration normal at high dose); no defects | Uneven treatment; mask alignment errors |
| Dimensional check | Zero measurable change | Should never fail -- if it does, process is wrong |

Accept: Inter Medium, 12 pt, `#27AE60`.
Reject: Inter Medium, 12 pt, `#E05C5C`.

---

### ZONE 6 -- Footer

Standard. Title: `Inspection & QA -- Ion Implantation`. Version `v1.0 -- 2026`.

Footer disclaimer:

> This poster is an educational reference tool. Characterization methods shown are industry-standard techniques for ion implantation verification. Specific acceptance criteria vary by device specification, customer requirements, and application. SIMS depth profiling, sheet resistance measurement, and nanoindentation follow published ASTM and ISO standards. Source: General industry knowledge; ASM Handbook Vol. 5; semiconductor process literature; ASTM E1438; ASTM F84; ISO 14577.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection and QA Ion Implantation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The SIMS depth profile hero (Zone 2) is the signature visual of the entire Ion Implantation cluster. SIMS is not a household name -- most people in metal finishing have never heard of it. But it is the analytical backbone of implantation QA. The annotated profile teaches the reader how to read the most important graph in implantation science. The 4-point probe section (Zone 4) is the fast, practical semiconductor tool -- it is the equivalent of a plating thickness gauge, just measuring sheet resistance instead of thickness. The dual accept/reject panels (Zone 5) close the cluster by giving both semiconductor and industrial audiences their specific go/no-go criteria. Together, the 10 Ion Implantation posters (449--458) form a complete reference library for this unique surface modification process.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #458 -- Construction Workup v1.0*
*2026-04-26*
