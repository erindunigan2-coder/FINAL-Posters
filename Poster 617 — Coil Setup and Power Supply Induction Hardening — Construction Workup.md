---
Project: Plating Posters Inc
Poster Number: 617
Title: "Coil Setup & Power Supply -- Induction Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7, Section 7.5)"
Technical Source: Induction hardening coil (inductor) design and power supply selection. Covers coil geometry, coupling gap, flux concentrators, and power supply types (IGBT, MOSFET, vacuum tube, dual-frequency). Custom coil design is the single most critical factor in induction hardening -- the coil IS the process.
Process Scope: Induction hardening -- coil setup and power supply
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - InductionHardening
  - CoilSetup
  - PowerSupply
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #617 -- Construction Workup
## Coil Setup & Power Supply -- Induction Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The coil poster is the technical heart of the induction hardening cluster. If the Process Flow poster (#613) is the map and Part Prep (#615) is the foundation, this is where the magic actually happens. The inductor coil is a custom-engineered tool -- not a commodity item -- and its geometry, combined with the frequency and power density from the supply, determines everything about the hardened pattern. Think of the coil as a mold for heat: shape the coil, shape the case.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Power supply comparison table (Block B -- HERO):** Four-column comparison of IGBT, MOSFET, vacuum tube, and dual-frequency systems.
2. **Coil geometry gallery (Block D):** Six coil types with diagram placeholders and application notes.
3. **Flux concentrator callout (Block E):** What they do, when to use them, materials.
4. **Frequency selection guide (Block F):** Frequency vs. case depth quick-reference strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- POWER SUPPLY TYPES / HERO (4.2"--14.5" / ~10.3")
  Block B: Four power supply comparison panels
  Block C: "Frequency = Case Depth" key principle callout
ZONE 4 -- COIL GEOMETRY GALLERY (14.5"--22.0" / ~7.5")
  Block D: Six coil types with diagrams and applications
ZONE 5 -- FLUX CONCENTRATORS + FREQUENCY GUIDE (22.0"--32.5" / ~10.5")
  Block E: Flux concentrator panel
  Block F: Frequency selection quick-reference
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `COIL SETUP & POWER SUPPLY` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Induction Hardening -- Stage 5 of 9` -- 36 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `The coil is a custom tool, not a commodity. Its geometry and the power supply behind it determine the entire hardened pattern.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Part fixtured and rotating  -->  After: Coil positioned, power supply configured, recipe loaded`

---

### ZONE 3 -- Power Supply Types (HERO)

**Section label:** `POWER SUPPLY TYPES -- MATCHING SOURCE TO APPLICATION` -- Y: 4.4".

**BLOCK B -- Four Power Supply Panels**

Y: 5.0" to 12.5". Four panels side by side.

Each panel: Rounded rect W: 5.5", H: 7.0", fill `#1E2435`, radius 8, top accent 4 pt.

| Panel | X | Type | Accent | Freq Range | Power Range | Application |
|---|---|---|---|---|---|---|
| 1 | 0.5" | SOLID-STATE (IGBT) | `#27AE60` | 1--50 kHz | 25--3000 kW | Most common; versatile; medium-to-deep case; shafts, gears, large parts |
| 2 | 6.25" | SOLID-STATE (MOSFET) | `#2EC4B6` | 50--400 kHz | 5--500 kW | High-frequency; thin case; small parts, gear teeth, valve seats |
| 3 | 12.0" | VACUUM TUBE (LEGACY) | `#E8A020` | 200--500 kHz | 10--200 kW | Older installations; being replaced by solid-state; high maintenance |
| 4 | 17.75" | DUAL-FREQUENCY | `#E8A020` | Combination | Variable | Gear tooth contour hardening; simultaneous MF + HF for root and tip |

Panel interior:
- Type name: Barlow SemiBold 18 pt, accent color
- Frequency: JetBrains Mono Regular 14 pt `#E8A020`
- Power: JetBrains Mono Regular 14 pt `#F0EDE8`
- Application: Inter Regular 13 pt `#F0EDE8` line height 155%
- Diagram placeholder: Rounded rect 4.5" x 2.0", fill `#252B3D`, border 1 pt accent color. Center text: `[Power supply diagram]` Inter Regular 11 pt `#F0EDE8` at 40%

**BLOCK C -- Key Principle Callout**

Y: 12.8" to 14.3". Full-width callout.
- Rounded rect W: 23.0", H: 1.3", fill `#1E2435`, left accent 0.06" `#27AE60`
- Text: `FREQUENCY = CASE DEPTH. Higher frequency concentrates current closer to the surface (skin effect). Lower frequency heats deeper. The power supply frequency is your primary depth control -- power and time are secondary.` -- Inter Medium 14 pt `#F0EDE8`

---

### ZONE 4 -- Coil Geometry Gallery

**Section label:** `COIL TYPES -- THE TOOL THAT SHAPES THE HEAT` -- Y: 14.7".

**BLOCK D -- Six Coil Types**

Y: 15.3" to 21.8". Two rows of three cards.

Each card: Rounded rect W: 7.33", H: 3.0", fill `#1E2435`, radius 6, left accent 0.06" `#2EC4B6`.

| Pos | Coil Type | Application | Key Detail |
|---|---|---|---|
| R1C1 | ENCIRCLING (SOLENOID) | Shafts, pins, axles -- entire circumference | Most common; surrounds the part; uniform circumferential heating |
| R1C2 | PANCAKE (FLAT) | Flat surfaces, bearing races, ways | Single-sided heating; part does not need to be encircled |
| R1C3 | HAIRPIN | Internal bores, ID hardening | U-shaped; fits inside bore; limited to larger IDs |
| R2C1 | CHANNEL (U-SHAPE) | Rail heads, gear teeth (progressive) | Wraps partially around the profile; used in scanning |
| R2C2 | TOOTH-BY-TOOTH (CONTOUR) | Individual gear teeth | Shaped to match tooth profile; indexes between teeth |
| R2C3 | SPLIT (CLAMSHELL) | Parts that cannot be loaded through a coil | Opens to load part; closes for heating; more complex mechanically |

Grid positions:
- Row 1: Y: 15.3". X: 0.5" / 8.17" / 15.83"
- Row 2: Y: 18.6". X: 0.5" / 8.17" / 15.83"

Card interior:
- Coil name: Barlow SemiBold 16 pt `#F0EDE8`
- Application: Inter Regular 12 pt `#F0EDE8` at 80%
- Key detail: Inter Medium 12 pt `#2EC4B6`

---

### ZONE 5 -- Flux Concentrators + Frequency Guide

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Flux Concentrators (X: 0.5", W: 11.0"):**

Section label: `FLUX CONCENTRATORS` Barlow Condensed ExtraBold 24 pt.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
WHAT THEY DO:
Magnetic laminations or ferrite inserts placed
behind or around the coil to concentrate the
magnetic field toward the workpiece.

WHEN TO USE:
- Heating only one side of a part
- Reducing stray heating of adjacent areas
- Improving efficiency on complex geometries
- Gear tooth contour hardening (critical)

MATERIALS:
- Fluxtrol (iron powder composite) -- most common
- Ferrotron (ferrite-based)
- Silicon steel laminations (legacy)

EFFECT ON EFFICIENCY:
20--40% improvement in heating efficiency
in targeted zone. Reduces power requirement.
```

Data values: JetBrains Mono Regular 13 pt `#E8A020`. Body: Inter Regular 13 pt `#F0EDE8`.

**Right -- Frequency Selection Guide (X: 12.0", W: 11.5"):**

Section label: `FREQUENCY VS. CASE DEPTH -- QUICK REFERENCE` Barlow Condensed ExtraBold 24 pt.

Table (Y: 23.0" to 30.0"):

| Frequency | Case Depth | Typical Application |
|---|---|---|
| 1--3 kHz (low) | 0.120--0.300 in (3.0--7.6 mm) | Large shafts, heavy sections |
| 3--10 kHz (medium) | 0.060--0.150 in (1.5--3.8 mm) | Axle shafts, spindles |
| 10--50 kHz (medium-high) | 0.030--0.080 in (0.76--2.0 mm) | Gears, cams, smaller shafts |
| 100--500 kHz (high) | 0.010--0.040 in (0.25--1.0 mm) | Small parts, gear teeth, valve seats |

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.9".
Data: JetBrains Mono Regular 12 pt `#F0EDE8`.

Bottom note: `Skin depth (delta) = 503 x sqrt(rho / (mu x f)). In practice: doubling the frequency halves the reference depth. Choose frequency FIRST, then adjust power and time.` Inter Medium 13 pt `#E8A020`

---

### ZONE 6 -- Footer

Standard footer. Title: `Coil Setup & Power Supply -- Induction Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Coil design is application-specific and requires engineering expertise. Parameters shown are typical industry ranges. Consult your equipment manufacturer and coil designer for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 4; AMS 2759/12.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Coil Setup Power Supply Induction Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is the technical centerpiece of the induction cluster. The power supply comparison gives supervisors the vocabulary to discuss equipment specifications. The coil gallery shows operators that coil design is not one-size-fits-all -- every part geometry demands a custom approach. The flux concentrator section is insider knowledge that separates good induction shops from great ones. The frequency vs. case depth table is the single most-referenced quick-reference on the shop floor.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #617 -- Construction Workup v1.0*
*2026-04-26*
