---
Project: Plating Posters Inc
Poster Number: 451
Title: "Part Prep -- Ion Implantation"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 451 — Part Prep Ion Implantation — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - IonImplantation
  - IonImplantation
  - PartPrep
  - ThinFilm
  - ClusterTF06
  - v1
---

# Claude Chat Generation Prompt -- Poster #451
## Part Prep -- Ion Implantation
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `PART PREP` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Ion Implantation -- Substrate Inspection, Masking & Surface Preparation` -- `32` pt `#2EC4B6`. Y: **1.4"**.
### Step 3 -- `No interlayer. No adhesion concern. The prep challenge here is controlling WHERE ions go and how DEEP they penetrate.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 3 of 10 highlighted.

---

## Phase 4 -- Semiconductor vs. Industrial Prep

Y: 14.8" to 19.8".

| Step | Detail |
|---|---|
| Starting material | Single-crystal Si wafer (100, 111, or 110 orientation) |
| Cleaning | RCA clean (SC-1: NH4OH/H2O2; SC-2: HCl/H2O2) or equivalent |
| Screen oxide | Grow 10--20 nm thermal SiO2 to prevent channeling |
| Photoresist mask | Spin-coat 0.5--5 um resist; pattern via photolithography |
| Mask verification | Optical inspection; CD-SEM for critical dimension verification |
| Alignment | Wafer flat or notch aligned to crystal orientation |

| Step | Detail |
|---|---|
| Starting material | Steel, Ti alloy, WC-Co, ceramics, or polymers |
| Cleaning | Ultrasonic alkaline wash + rinse + dry |
| Surface finish | Ra < 0.4 um preferred; implantation does not change finish |
| Metal masks | Stainless steel or Mo sheet; laser-cut to define implant area |
| Mask attachment | Clamped or fixtured over non-implant regions |
| Dimensional verification | Calipers/CMM; implantation adds zero measurable thickness |

---

## Phase 5 -- Masking Requirements

Y: 20.8" to 26.3".
Section: `0.5 um thick -- with safety margin. Use SRIM/TRIM simulation to verify.` -- Inter Medium, 14 pt, `#E8A020`.`.

| Mask Material | Typical Thickness | Max Energy Stopped | Application | Notes |
|---|---|---|---|---|
| Photoresist | 0.5--5 um | 200 keV (B); 100 keV (As) | Semiconductor -- patterned by lithography | Must exceed Rp at implant energy; higher density materials stop ions faster |
| SiO2 (thermal oxide) | 0.1--2 um | Proportional to thickness | Semiconductor -- hard mask | More durable than resist for high-dose implants |
| Si3N4 | 0.05--1 um | Similar to SiO2 | Semiconductor -- hard mask | Often used as a dual stack with oxide |
| Stainless steel | 0.5--3 mm | Up to 500 keV (N+) | Industrial -- reusable masks | Heavy; clamped to part; laser-cut openings |
| Molybdenum | 0.3--2 mm | Up to 500 keV (N+) | Industrial -- high-energy implants | Higher density = better stopping; reusable |
| Tungsten | 0.2--1 mm | Up to MeV range | Research; extreme energy implants | Highest density common mask material |

---

## Phase 6 -- Channeling Prevention

Y: 27.3" to 32.3".

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | TILT THE WAFER | `#2EC4B6` | Tilt the substrate 7 degrees off the major crystal axis. This misaligns the beam from the lattice channels. Standard practice for all semiconductor implants. Industrial parts (polycrystalline) are less susceptible but tilt is still good practice. |
| 2 | 8.16" | 7.33" | SCREEN OXIDE | `#E8A020` | Grow a thin amorphous SiO2 layer (10--20 nm) on the Si wafer surface before implant. The amorphous oxide scatters ions entering the crystal, randomizing their direction and preventing channeling. |
| 3 | 15.83" | 7.33" | PRE-AMORPHIZATION | `#27AE60` | Implant a heavy species (Si+ or Ge+) at high dose first to amorphize the substrate surface layer. Then implant the desired dopant into the amorphous region. No crystal channels = no channeling. Used for ultra-shallow junctions. |

---

## Phase 7 -- Footer

Standard. Title: `Part Prep -- Ion Implantation`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 8 -- Review

- [ ] Headline `PART PREP` 88pt
- [ ] Orientation strip with poster 3 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Part Prep Ion Implantation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
