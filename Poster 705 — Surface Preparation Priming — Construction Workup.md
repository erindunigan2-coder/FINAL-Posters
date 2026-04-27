---
Project: Plating Posters Inc
Poster Number: 705
Title: "Surface Preparation -- Priming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Surface preparation requirements for industrial primers. Covers SSPC blast standards, profile requirements, soluble salt limits, and substrate-specific prep for steel, aluminum (aerospace), and maintenance coatings.
Process Scope: Surface preparation for industrial priming -- Stage 2 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IndustrialPriming
  - SurfacePreparation
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #705 -- Construction Workup
## Surface Preparation -- Priming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 8. Surface preparation is the single most critical factor for zinc-rich primer performance. The zinc particles must be in direct metallic contact with the steel for galvanic protection to work. This poster is about blast standards, profile requirements, and why "good enough" surface prep is never good enough for IOZ.

Hero visual: a cross-section showing blast profile peaks and valleys with zinc particles seated in the profile, making metallic contact with the steel substrate.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Blast profile cross-section hero (Block B):** A stylized cross-section showing steel substrate with a blast profile (peaks and valleys) and zinc primer particles sitting in the valleys making galvanic contact. Built with layered rectangles and zigzag line shapes.
2. **SSPC standards matrix (Block D):** Table comparing SP5, SP6, SP7, SP10, SP11 with descriptions and which primer types require each.
3. **Profile specification panel (Block E):** ASTM D4417 methods and target ranges.
4. **Soluble salt limits callout (Block F):** Critical contamination thresholds.
5. **Aerospace prep sidebar (Block G):** Aluminum-specific preparation.
6. **Defect grid (Block H):** 6 common surface prep failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- BLAST PROFILE HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- SSPC STANDARDS MATRIX + PROFILE SPECS (14.0"--20.5" / ~6.5")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- SOLUBLE SALTS + AEROSPACE PREP (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SURFACE PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Industrial Priming -- Stage 2 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Skip the prep. Ruin the primer. The zinc must touch the steel -- no exceptions, no shortcuts.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Mill scale, rust, oil, contaminants  -->  After: Clean, profiled steel ready for zinc-rich primer`

---

### ZONE 3 -- Blast Profile Hero

**Section label:** `WHY SURFACE PREP MATTERS -- THE GALVANIC CIRCUIT` -- Y: 4.4".

**BLOCK B -- Profile Cross-Section Diagram**

Y: 5.0" to 13.5".

**Steel substrate base:**
- Rectangle, X: 1.5", Y: 10.0", W: 21.0", H: 2.5", fill `#3A4055`, border 2 pt `#C8D0D8`
- Label below: `STEEL SUBSTRATE` Barlow SemiBold 16 pt `#C8D0D8`

**Blast profile (zigzag surface on top of steel):**
- Irregular zigzag line across top of steel rectangle representing peaks and valleys
- Stroke: 3 pt `#C8D0D8`
- Profile depth labels: `1.5--3.0 mils` JetBrains Mono 14 pt `#E8A020`

**Zinc primer layer (above profile):**
- Irregular fill above the zigzag, ~1.0" thick, fill `#27AE60` at 30%
- Small circles representing zinc dust particles scattered throughout: fill `#C8D0D8`, 0.15" diameter
- Label: `ZINC PARTICLES (75--85% by weight in IOZ)` Barlow SemiBold 14 pt `#27AE60`

**Galvanic contact callout arrows:**
- Arrows from zinc particles down to steel surface at valley bottoms
- Stroke: 2 pt `#E8A020`, dashed
- Label: `Metallic contact = galvanic circuit` Inter Medium 13 pt `#E8A020`

**Right-side annotation panel (X: 15.0", Y: 5.5", W: 8.0", H: 4.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `WHY THIS MATTERS` Barlow SemiBold 16 pt `#E05C5C`
- Body bullets:
  - `Mill scale = electrical insulator = NO galvanic protection`
  - `Rust = weak mechanical bond = adhesion failure`
  - `Oil film = total barrier to zinc-steel contact`
  - `Soluble salts = osmotic blistering under the primer`
- Inter Regular 13 pt `#F0EDE8`, line height 155%

---

### ZONE 4 -- SSPC Standards Matrix + Profile Specs

**Section label:** `BLAST STANDARDS -- KNOW YOUR SPEC` -- Y: 14.2".

**BLOCK D -- SSPC Standards Table (Y: 14.8" to 18.5")**

| Standard | ISO Equiv | Description | Remaining Contaminant | Required For |
|---|---|---|---|---|
| SSPC-SP5 | Sa 3 | White Metal Blast | 0% mill scale/rust | IOZ (high-perf), immersion |
| SSPC-SP10 | Sa 2.5 | Near-White Blast | < 5% staining | IOZ (standard), OZ |
| SSPC-SP6 | Sa 2 | Commercial Blast | < 33% staining | Epoxy primer (new steel) |
| SSPC-SP7 | Sa 1 | Brush-Off Blast | Removes loose only | Sweep blast for recoat prep |
| SSPC-SP3 | -- | Power Tool Cleaning | Loose material removed | Epoxy (maintenance/repair) |
| SSPC-SP11 | -- | Power Tool to Bare Metal | Bare metal achieved | Spot repair to bare steel |

Header: `#3A4055`. Alternating rows `#1E2435` / `#252B3D`. Data: JetBrains Mono 12 pt.

**BLOCK E -- Profile Requirements (Y: 18.8" to 20.3")**

Two side-by-side callouts:

Left -- Profile Measurement:
- `ASTM D4417` Barlow SemiBold 16 pt `#2EC4B6`
- `Method A: Stylus profilometer (lab)`
- `Method B: Depth micrometer (field)`
- `Method C: Replica tape (most common field method)`
- Inter Regular 13 pt `#F0EDE8`

Right -- Target Ranges:
- `IOZ Primers: 1.5--3.0 mils (38--76 um)` JetBrains Mono 14 pt `#27AE60`
- `Epoxy Primers: 1.5--2.5 mils (38--64 um)` JetBrains Mono 14 pt `#E8A020`
- `High-build protective: 2.0--4.0 mils (51--102 um)` JetBrains Mono 14 pt `#2EC4B6`

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 SURFACE PREP FAILURES` -- Y: 20.7".

**BLOCK H -- 3x2 Grid (Y: 21.3" to 26.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | FLASH RUST | `#E05C5C` | Blast-to-prime delay in humid air | Prime within 4 hr; dehumidify if needed |
| R1C2 | ADHESION FAILURE | `#E05C5C` | Residual mill scale or oil film | Re-blast to spec; solvent clean first |
| R1C3 | OSMOTIC BLISTERING | `#E8A020` | Soluble salts (chloride/sulfate) on steel | Test per SSPC Guide 15; water wash before blast |
| R2C1 | INSUFFICIENT PROFILE | `#2EC4B6` | Wrong media or worn nozzle | Use angular media; check nozzle orifice |
| R2C2 | OVER-PROFILE | `#E8A020` | Media too aggressive for DFT | Switch to finer grit; fill with extra primer coat |
| R2C3 | EMBEDDED CONTAMINANT | `#E05C5C` | Contaminated blast media or oily air | Test media; blotter test compressed air |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- Soluble Salts + Aerospace Prep

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Soluble Salt Limits (X: 0.5", W: 11.0"):**

Section label: `SOLUBLE SALT CONTAMINATION` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| Contaminant | Max Limit | Test Method |
|---|---|---|
| Chloride (Cl-) | < 3 ug/cm2 | SSPC Guide 15 / ISO 8502-6 (Bresle patch) |
| Sulfate (SO4 2-) | < 10 ug/cm2 | SSPC Guide 15 / ISO 8502-6 |
| Total conductivity | < 7 ug/cm2 NaCl equiv | Conductometric per ISO 8502-9 |

Warning callout: `Coastal and marine environments: ALWAYS test for soluble salts. Invisible chloride contamination is the #1 cause of premature coating failure on offshore steel.` Inter Medium 13 pt `#E05C5C`.

**Right -- Aerospace Substrate Prep (X: 12.0", W: 11.5"):**

Section label: `AEROSPACE PRIMERS -- SUBSTRATE PREP` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

| Substrate | Pretreatment | Spec |
|---|---|---|
| Aluminum | Chromate conversion (Type I or II) | MIL-DTL-5541 |
| Aluminum | Chromic acid or thin sulfuric anodize | MIL-PRF-8625 Type I/IIB |
| Steel (aero) | Zn-Ni plate + chromate conversion | Per OEM spec |
| Non-chrome alt | Ti/Zr sol-gel or TCP | MIL-DTL-5541 Type II |

Note: `Aerospace surface prep is specification-driven -- always verify current revision of the governing spec before starting.` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 7 -- Footer

Standard. Title: `Surface Preparation -- Priming`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; SSPC standards; ASTM test methods; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Surface Preparation Priming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most important single poster in the Industrial Priming cluster. Surface preparation is to primers what a foundation is to a skyscraper -- everything above it depends on getting it right. The blast profile cross-section hero visual should make the galvanic contact concept viscerally clear: zinc particles must physically touch the steel. The soluble salt panel addresses the invisible enemy that causes more field failures than any other single factor.

---

*Alaina -- Poster #705 -- Construction Workup v1.0 -- 2026-04-26*
