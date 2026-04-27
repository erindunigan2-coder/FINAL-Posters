---
Project: Plating Posters Inc
Poster Number: 445
Title: "Parameter Setup -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Sections 5.3, 5.5)"
Process Scope: Interlayer architecture and deposition parameter setup for DLC coating
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - ParameterSetup
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #445 -- Construction Workup
## Parameter Setup -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the most technically dense poster in the DLC cluster. It covers the interlayer architecture (the secret to adhesion), the relationship between substrate bias and sp3 content, gas flow and pressure settings, and the recipe differences between a-C:H (PECVD) and ta-C (filtered arc). The interlayer gradient (Cr -> CrC -> DLC or Si -> SiC -> DLC) is the hero concept.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Interlayer architecture hero (Block B):** A cross-section stack diagram showing substrate -> metal interlayer -> gradient -> DLC. Built with horizontal stacked rectangles and gradient-fill transitions.
2. **Bias vs. sp3 relationship (Block D):** Conceptual graph placeholder or data callout.
3. **a-C:H recipe table (Block E):** Full PECVD recipe.
4. **ta-C recipe table (Block F):** Full filtered arc recipe.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- INTERLAYER ARCHITECTURE HERO (2.9"--14.5" / ~11.6")
  Block B: Cross-section stack + interlayer options
ZONE 3 -- BIAS & sp3 RELATIONSHIP (14.5"--20.0" / ~5.5")
  Block D: Ion energy -> sp3 content -> hardness chain
ZONE 4 -- RECIPE TABLES (20.0"--26.5" / ~6.5")
  Block E: a-C:H (PECVD) recipe
  Block F: ta-C (filtered arc) recipe
ZONE 5 -- PARAMETER TROUBLESHOOTING (26.5"--32.5" / ~6.0")
  Block G: If you see X, adjust Y
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `Diamond-Like Carbon -- Interlayer Architecture & Deposition Recipe` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `The interlayer is the foundation. Without it, DLC is just expensive carbon sitting on top of your part waiting to peel off.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Interlayer Architecture Hero

**Section label:** `THE INTERLAYER -- YOUR ADHESION INSURANCE` -- Y: 3.1".

**BLOCK B -- Cross-Section Stack Diagram**

Y: 3.8" to 11.5".

**Stack diagram (X: 2.0", W: 20.0"):**

Five horizontal stacked layers, building bottom to top:

| Layer | Fill | Height | Label | Thickness | Color Accent |
|---|---|---|---|---|---|
| Substrate (bottom) | `#3A4055` | 2.0" | `SUBSTRATE (STEEL, Ti, Al, CARBIDE)` | Bulk material | `#C8D0D8` |
| Metal interlayer | `#C8D0D8` at 50% | 0.8" | `METAL INTERLAYER (Cr or Si)` | 100--300 nm | `#C8D0D8` |
| Gradient transition | Gradient from `#C8D0D8` to `#1A1F2E` | 1.0" | `GRADIENT (CrC or SiC)` | 100--500 nm | `#E8A020` |
| DLC coating | `#1A1F2E` with subtle highlight | 1.2" | `DLC (a-C:H or ta-C)` | 0.5--5 um | `#27AE60` |
| Surface (top) | -- | -- | `Ultra-low friction surface` | -- | `#27AE60` |

Each layer label: Barlow SemiBold, 16 pt, layer accent color.
Thickness: JetBrains Mono 14 pt, `#E8A020`.

Annotations (right side):
- Arrow spanning metal + gradient: `Adhesion zone -- bonds metal to carbon` Inter Medium 14 pt `#E8A020`
- Arrow at substrate: `Surface activated by Ar+ ion etch` Inter Regular 12 pt `#F0EDE8` at 60%
- Arrow at DLC: `Hardness: 1,000--8,000 HV depending on type` JetBrains Mono 13 pt `#27AE60`

**Interlayer Options Panel (Y: 12.0" to 14.3"):**

Four small cards in a row:

| Card | X | W | System | Stack |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | Cr/CrC/DLC | Most common for steel substrates |
| 2 | 6.33" | 5.5" | Si/SiC/DLC | Common for PECVD systems |
| 3 | 12.16" | 5.5" | Ti/TiN/DLC | Higher temperature applications |
| 4 | 18.0" | 5.5" | WC/WC:C/DLC | W-containing DLC systems |

Each: Rounded rect, H: 2.0", fill `#1E2435`, left accent `#E8A020`.

---

### ZONE 3 -- Bias & sp3 Relationship

**Section label:** `ION ENERGY CONTROLS HARDNESS` -- Y: 14.7".

**BLOCK D -- Bias -> sp3 -> Hardness Chain**

Y: 15.3" to 19.8". Full width.

**Three linked callout cards:**

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | SUBSTRATE BIAS | `#E8A020` | Bias voltage controls ion energy. Higher bias = higher energy ions striking the growing film. PECVD: -200 to -400 V. Arc: -50 to -2000 V. |
| 2 | 8.16" | 7.33" | sp3 CONTENT | `#2EC4B6` | Ion energy determines sp3/sp2 carbon bonding ratio. Sweet spot: 50--200 eV per ion. Too low = graphitic (sp2). Too high = implantation damage. |
| 3 | 15.83" | 7.33" | HARDNESS | `#27AE60` | More sp3 = harder coating. a-C:H (30--50% sp3) = 1,000--2,000 HV. ta-C (60--85% sp3) = 4,000--8,000 HV. |

Arrows between cards: `->` 3 pt `#3A4055`.

**Bottom note:** `This is why bias voltage is the single most critical deposition parameter in DLC. Get it wrong, and you deposit graphite instead of diamond.` -- Inter Medium, 14 pt, `#E05C5C`.

---

### ZONE 4 -- Recipe Tables

**Section label:** `DEPOSITION RECIPES -- TWO SYSTEMS` -- Y: 20.2".

**Two-column layout:**

**Left -- BLOCK E: a-C:H by PECVD (X: 0.5", W: 11.0"):**
- Rounded rect, H: 6.0", fill `#1E2435`, left accent `#2EC4B6`
- Title: `a-C:H (PECVD) RECIPE` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Parameter | Value |
|---|---|
| Precursor | C2H2 (preferred) or CH4 |
| Carrier gas | Ar |
| Working pressure | 100--300 mTorr |
| RF power | 200--800 W at 13.56 MHz |
| Substrate bias | -200 to -400 V |
| Ion energy | 50--200 eV |
| Substrate temp | 80--150 C |
| Interlayer | Cr or Si, 100--300 nm |
| Gradient | CrC or SiC, 100--500 nm |
| DLC thickness | 1--3 um |
| Deposition rate | 1--3 um/hr |
| Total cycle | 2--6 hours |

**Right -- BLOCK F: ta-C by Filtered Arc (X: 12.0", W: 11.5"):**
- Rounded rect, H: 6.0", fill `#1E2435`, left accent `#E8A020`
- Title: `ta-C (FILTERED ARC) RECIPE` -- Barlow SemiBold, 18 pt, `#E8A020`

| Parameter | Value |
|---|---|
| Source | Solid graphite cathode |
| Process gas | None |
| Working pressure | < 1 mTorr |
| Arc current | 40--100 A |
| Filter coil | 5--20 A |
| Substrate bias | -50 to -2000 V |
| Ion energy | 20--100 eV (optimum ~50 eV for ta-C) |
| Substrate temp | RT--150 C |
| Interlayer | Cr or Si (from secondary source) |
| DLC thickness | 0.5--2 um |
| Deposition rate | 0.1--1 um/hr |
| Total cycle | 3--8 hours |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

---

### ZONE 5 -- Parameter Troubleshooting

**Section label:** `IF YOU SEE THIS -- ADJUST THAT` -- Y: 26.7".

**BLOCK G -- 6 Diagnostic Cards (3x2 grid)**

Y: 27.3" to 32.3".

| Position | Symptom | Accent | Likely Cause | Adjustment |
|---|---|---|---|---|
| R1C1 | Soft coating (low hardness) | `#E8A020` | Bias too low; excessive hydrogen | Increase bias; reduce pressure; check gas ratio |
| R1C2 | High stress / delamination | `#E05C5C` | Bias too high; film too thick | Reduce bias; use metal-doped DLC; limit thickness |
| R1C3 | Non-uniform color | `#E8A020` | Thickness variation; poor rotation | Check rotation speed; verify fixture uniformity |
| R2C1 | Pinholes / defects | `#E05C5C` | Particles; substrate defects | Improve cleaning; inspect substrate pre-load |
| R2C2 | Macroparticles (arc only) | `#E8A020` | Filter inefficient; high arc current | Check filter magnetic field; reduce arc current |
| R2C3 | Poor adhesion at edges | `#E05C5C` | Stress concentration; thin interlayer | Round edges before coating; increase interlayer |

Each card: Rounded rect, W: 7.33", H: 2.3", fill `#1E2435`, left accent 0.06".

---

### ZONE 6 -- Footer

Standard. Title: `Parameter Setup -- DLC`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The interlayer cross-section (Zone 2) is the most important visual in the entire DLC cluster. It explains WHY DLC sticks (or doesn't). The bias-to-hardness chain (Zone 3) is the conceptual backbone -- it explains WHY different DLC types have different hardness. These two concepts, combined, give the reader a complete mental model of DLC coating design. This is the poster that a coating engineer will spend the most time studying.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #445 -- Construction Workup v1.0*
*2026-04-26*
