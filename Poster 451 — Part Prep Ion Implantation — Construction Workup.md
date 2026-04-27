---
Project: Plating Posters Inc
Poster Number: 451
Title: "Part Prep -- Ion Implantation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Sections 6.1, 6.3)"
Process Scope: Substrate inspection and preparation for ion implantation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IonImplantation
  - PartPrep
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #451 -- Construction Workup
## Part Prep -- Ion Implantation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Part prep for ion implantation is different from every coating process in the poster library. No adhesion interlayer is needed -- there is nothing to adhere. Instead, the concern is channeling (ions traveling too deep along crystal planes), masking accuracy (the mask must stop ions at the implant energy), and surface condition verification. For semiconductor, this means photoresist patterning and screen oxide growth. For industrial, it means clean surfaces and metal masks. The hero visual is a cross-section showing how ions interact with an unmasked vs. masked surface, with channeling illustrated.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Ion-surface interaction hero (Block B):** Cross-section diagram showing ions entering unmasked substrate, being stopped by mask, and channeling effect. Built with layered rectangles and arrows.
2. **Semiconductor vs. Industrial prep comparison (Block D):** Side-by-side prep requirements.
3. **Masking requirements table (Block E):** Mask materials, thickness, and ion stopping range.
4. **Channeling prevention (Block F):** Tilt angle, screen oxide, and pre-amorphization.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.0" / 20.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ION-SURFACE INTERACTION HERO (2.9"--14.0" / ~11.1")
  Block B: Cross-section of implantation with masking and channeling
ZONE 3 -- SEMICONDUCTOR vs. INDUSTRIAL PREP (14.0"--20.0" / ~6.0")
  Block D: Side-by-side prep requirements
ZONE 4 -- MASKING REQUIREMENTS (20.0"--26.5" / ~6.5")
  Block E: Mask materials, thickness, stopping range
ZONE 5 -- CHANNELING PREVENTION (26.5"--32.5" / ~6.0")
  Block F: How to prevent anomalous ion depth
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREP` -- 88 pt `#F0EDE8`.
**Subheading:** `Ion Implantation -- Substrate Inspection, Masking & Surface Preparation` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `No interlayer. No adhesion concern. The prep challenge here is controlling WHERE ions go and how DEEP they penetrate.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Ion-Surface Interaction Hero

**Section label:** `HOW IONS INTERACT WITH YOUR SURFACE` -- Y: 3.1".

**BLOCK B -- Cross-Section Diagram**

Y: 3.8" to 13.8".

**Full-width schematic (X: 1.0", W: 22.0"):**

Rounded rect container, H: 9.5", fill `#1E2435`.

Three side-by-side cross-section panels:

**Panel 1 -- Normal Implantation (X: 1.5", W: 6.5"):**
- Substrate rect: fill `#3A4055`, H: 4.0"
- Label: `SUBSTRATE` Barlow SemiBold 12 pt `#C8D0D8`
- Downward arrows (5) representing ion beam: stroke 2 pt `#27AE60`
- Label above arrows: `N+ BEAM (50 keV)` JetBrains Mono 12 pt `#27AE60`
- Implanted zone: Horizontal band within substrate, 0.5" below surface, fill `#27AE60` at 20%, dashed border 1 pt `#27AE60`
- Label: `Modified zone (Rp = 50--500 nm)` JetBrains Mono 10 pt `#27AE60`
- Annotation: `Ions stop within near-surface region` Inter Regular 11 pt `#F0EDE8` at 60%
- Title: `NORMAL IMPLANT` Barlow SemiBold 14 pt `#27AE60`

**Panel 2 -- Masked Implantation (X: 8.5", W: 6.5"):**
- Substrate rect: fill `#3A4055`, H: 4.0"
- Mask rect on top (partial coverage): fill `#E8A020` at 40%, H: 0.8"
- Label: `MASK (resist or metal)` JetBrains Mono 10 pt `#E8A020`
- Downward arrows: 3 arrows hit mask (blocked -- shown as X), 2 arrows pass through opening to substrate
- Implanted zone only under opening: fill `#27AE60` at 20%
- Label: `Implanted only in unmasked area` Inter Regular 11 pt `#27AE60`
- Title: `MASKED IMPLANT` Barlow SemiBold 14 pt `#E8A020`

**Panel 3 -- Channeling (X: 15.5", W: 6.5"):**
- Substrate rect: fill `#3A4055`, H: 4.0", with faint vertical lines representing crystal lattice planes
- Downward arrows: aligned with lattice planes
- Deep penetration zone: fill `#E05C5C` at 20%, extending much deeper than normal
- Label: `Ions travel along crystal planes -- 5x--10x deeper than expected` JetBrains Mono 10 pt `#E05C5C`
- Title: `CHANNELING (PROBLEM)` Barlow SemiBold 14 pt `#E05C5C`

**Bottom annotation (Y: 12.5" to 13.5"):**
- `The projected range (Rp) is the average depth where implanted ions come to rest. It depends on ion species, energy, and substrate material. Example: B at 50 keV in Si has Rp of ~170 nm. P at 100 keV in Si has Rp of ~130 nm. As at 100 keV in Si has Rp of ~50 nm (heavier ions stop sooner).` -- Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 3 -- Semiconductor vs. Industrial Prep

**Section label:** `TWO PREP WORLDS` -- Y: 14.2".

**BLOCK D -- Side-by-Side Comparison**

Y: 14.8" to 19.8". Two-column layout.

**Left -- Semiconductor (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `SEMICONDUCTOR WAFER PREP` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Step | Detail |
|---|---|
| Starting material | Single-crystal Si wafer (100, 111, or 110 orientation) |
| Cleaning | RCA clean (SC-1: NH4OH/H2O2; SC-2: HCl/H2O2) or equivalent |
| Screen oxide | Grow 10--20 nm thermal SiO2 to prevent channeling |
| Photoresist mask | Spin-coat 0.5--5 um resist; pattern via photolithography |
| Mask verification | Optical inspection; CD-SEM for critical dimension verification |
| Alignment | Wafer flat or notch aligned to crystal orientation |

**Right -- Industrial (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `INDUSTRIAL PART PREP` -- Barlow SemiBold, 18 pt, `#E8A020`

| Step | Detail |
|---|---|
| Starting material | Steel, Ti alloy, WC-Co, ceramics, or polymers |
| Cleaning | Ultrasonic alkaline wash + rinse + dry |
| Surface finish | Ra < 0.4 um preferred; implantation does not change finish |
| Metal masks | Stainless steel or Mo sheet; laser-cut to define implant area |
| Mask attachment | Clamped or fixtured over non-implant regions |
| Dimensional verification | Calipers/CMM; implantation adds zero measurable thickness |

Data: Inter Regular, 13 pt, `#F0EDE8`. Detail: JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 4 -- Masking Requirements

**Section label:** `MASKING -- THE MASK MUST STOP THE IONS` -- Y: 20.2".

**BLOCK E -- Masking Table**

Y: 20.8" to 26.3".

| Mask Material | Typical Thickness | Max Energy Stopped | Application | Notes |
|---|---|---|---|---|
| Photoresist | 0.5--5 um | 200 keV (B); 100 keV (As) | Semiconductor -- patterned by lithography | Must exceed Rp at implant energy; higher density materials stop ions faster |
| SiO2 (thermal oxide) | 0.1--2 um | Proportional to thickness | Semiconductor -- hard mask | More durable than resist for high-dose implants |
| Si3N4 | 0.05--1 um | Similar to SiO2 | Semiconductor -- hard mask | Often used as a dual stack with oxide |
| Stainless steel | 0.5--3 mm | Up to 500 keV (N+) | Industrial -- reusable masks | Heavy; clamped to part; laser-cut openings |
| Molybdenum | 0.3--2 mm | Up to 500 keV (N+) | Industrial -- high-energy implants | Higher density = better stopping; reusable |
| Tungsten | 0.2--1 mm | Up to MeV range | Research; extreme energy implants | Highest density common mask material |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Inter Regular 12 pt `#F0EDE8`. Thickness: JetBrains Mono 12 pt `#E8A020`.

**Key rule callout (Y: 25.5"):**
- `RULE: Mask thickness must exceed the projected range (Rp) of the ion at the implant energy. If Rp in the mask material is 0.5 um, the mask must be > 0.5 um thick -- with safety margin. Use SRIM/TRIM simulation to verify.` -- Inter Medium, 14 pt, `#E8A020`.

---

### ZONE 5 -- Channeling Prevention

**Section label:** `PREVENTING CHANNELING` -- Y: 26.7".

**BLOCK F -- Three Prevention Methods**

Y: 27.3" to 32.3". Three cards in a row.

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | TILT THE WAFER | `#2EC4B6` | Tilt the substrate 7 degrees off the major crystal axis. This misaligns the beam from the lattice channels. Standard practice for all semiconductor implants. Industrial parts (polycrystalline) are less susceptible but tilt is still good practice. |
| 2 | 8.16" | 7.33" | SCREEN OXIDE | `#E8A020` | Grow a thin amorphous SiO2 layer (10--20 nm) on the Si wafer surface before implant. The amorphous oxide scatters ions entering the crystal, randomizing their direction and preventing channeling. |
| 3 | 15.83" | 7.33" | PRE-AMORPHIZATION | `#27AE60` | Implant a heavy species (Si+ or Ge+) at high dose first to amorphize the substrate surface layer. Then implant the desired dopant into the amorphous region. No crystal channels = no channeling. Used for ultra-shallow junctions. |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold, 18 pt, accent color.
Content: Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard. Title: `Part Prep -- Ion Implantation`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Prep Ion Implantation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The cross-section hero (Zone 2) must visually sell the difference between normal implantation, masked implantation, and the channeling problem. These three panels tell the entire story of ion implantation prep in one glance. The channeling panel is intentionally alarming (Coral red, deeper-than-expected penetration) because channeling is the most common unintended outcome in semiconductor implantation. The masking table (Zone 4) serves both semiconductor and industrial audiences with specific materials for each.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #451 -- Construction Workup v1.0*
*2026-04-26*
