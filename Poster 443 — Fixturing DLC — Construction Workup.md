---
Project: Plating Posters Inc
Poster Number: 443
Title: "Fixturing -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Sections 5.2, 5.4)"
Process Scope: Fixturing and loading for DLC vacuum coating chambers
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - Fixturing
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #443 -- Construction Workup
## Fixturing -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

DLC coating is a vacuum line-of-sight process (for sputtering) and semi-line-of-sight (for PECVD). Fixturing and rotation are critical for uniform thickness. This poster covers planetary rotation systems, contact point management, loading density, and the relationship between fixture design and coating uniformity. Contact points will have no coating -- their placement must be in non-functional areas.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Rotation concept hero (Block B):** A top-down schematic of a planetary rotation system -- central spindle, satellite spindles, part positions. Built with circles, lines, and labels.
2. **Contact point management (Block D):** Where to place contacts, witness marks.
3. **Loading density guidelines (Block E):** Part spacing and shadowing rules.
4. **Fixture material reference (Block F):** What materials are used for DLC fixtures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ROTATION CONCEPT HERO (2.9"--14.5" / ~11.6")
  Block B: Planetary rotation schematic + uniformity callout
ZONE 3 -- CONTACT POINT MANAGEMENT (14.5"--20.5" / ~6.0")
  Block D: Rules for contact placement
ZONE 4 -- LOADING DENSITY (20.5"--26.5" / ~6.0")
  Block E: Spacing, shadowing, and batch optimization
ZONE 5 -- FIXTURE MATERIALS (26.5"--32.5" / ~6.0")
  Block F: Material compatibility table
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `FIXTURING` -- 88 pt `#F0EDE8`.
**Subheading:** `Diamond-Like Carbon -- Chamber Loading & Rotation` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Rotation is uniformity. Contact points are coating voids. Load smart -- every part sees the plasma equally.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Rotation Concept Hero

**Section label:** `PLANETARY ROTATION -- THE KEY TO UNIFORM DLC` -- Y: 3.1".

**BLOCK B -- Rotation Schematic**

Y: 3.8" to 12.5".

**Central concept diagram (X: 2.0", Y: 4.5", W: 20.0", H: 7.5"):**

Rounded rect container, fill `#1E2435`.

- Central spindle: Circle, center (12.0", 8.5"), radius 0.4", fill `#3A4055`, border 2 pt `#E8A020`
- Label: `MAIN AXIS` Barlow SemiBold 12 pt `#E8A020`
- Curved arrow around spindle indicating rotation direction

- Satellite spindles (3 shown): Circles at 120-degree spacing, radius 0.3", offset ~3.5" from center, fill `#3A4055`, border 2 pt `#2EC4B6`
- Label each: `SATELLITE` JetBrains Mono 10 pt `#2EC4B6`
- Curved arrows around each satellite

- Part positions on each satellite: 3--4 small squares (0.3" x 0.3") around each satellite, fill `#27AE60` at 40%
- Label: `PARTS` Inter Medium 10 pt `#27AE60`

- Annotation arrows pointing to key features:
  - `Main rotation: 1--5 rpm` JetBrains Mono 12 pt `#E8A020`
  - `Satellite rotation: 5--20 rpm` JetBrains Mono 12 pt `#2EC4B6`
  - `Dual rotation = all surfaces exposed` Inter Medium 13 pt `#F0EDE8`

**Key principle callout (Y: 12.8" to 14.3"):**
- Rounded rect, full width, fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Single-axis rotation: acceptable for simple cylindrical parts. Planetary (dual-axis): required for complex geometry. Without rotation, thickness varies by 10x or more between source-facing and shadowed surfaces.` -- Inter Medium, 14 pt, `#F0EDE8`

---

### ZONE 3 -- Contact Point Management

**Section label:** `CONTACT POINTS -- WHERE COATING WON'T BE` -- Y: 14.7".

**BLOCK D -- Contact Rules**

Y: 15.3" to 20.3". Three equal-width cards in a row.

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | PLACEMENT | `#E8A020` | Contact points must be in non-functional, non-visible areas. Discuss with customer BEFORE loading. Mark contact locations on part drawing. |
| 2 | 8.16" | 7.33" | WITNESS MARKS | `#E05C5C` | Every contact point leaves an uncoated witness mark. Typical mark: 1--3 mm diameter. Cannot be eliminated -- only hidden. |
| 3 | 15.83" | 7.33" | MINIMIZE CONTACTS | `#27AE60` | Use minimum contacts for secure fixturing. 2--3 points per part typical. More contacts = more uncoated areas. Spring-loaded contacts reduce mark size. |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold, 18 pt, accent color.
Content: Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 4 -- Loading Density

**Section label:** `LOADING DENSITY & SHADOWING` -- Y: 20.7".

**BLOCK E -- Spacing Rules**

Y: 21.3" to 26.3". Table + callout.

| Rule | Value | Why |
|---|---|---|
| Minimum part spacing | 10--20 mm between parts | Prevents shadowing between adjacent parts |
| Source-to-part distance | 50--150 mm (varies by system) | Affects deposition rate and uniformity |
| Batch loading | 100--10,000 parts per run typical | Depends on chamber size and part geometry |
| Shadowing check | Verify no part blocks line-of-sight to source for adjacent part | Shadowed areas receive thin or no coating |
| Height limit | Parts must not extend beyond fixture envelope | Interference with chamber or electrodes |

Header: Barlow SemiBold, 14 pt, `#F0EDE8`. Fill `#3A4055`.
Values: JetBrains Mono Regular, 13 pt, `#E8A020`.
Why: Inter Regular, 12 pt, `#F0EDE8`.

**Shadowing warning (Y: 25.5"):**
- `SHADOWING = THIN DLC = PREMATURE FAILURE. If a part cannot "see" the plasma source, it will not be coated properly.` -- Inter Medium, 14 pt, `#E05C5C`.

---

### ZONE 5 -- Fixture Materials

**Section label:** `FIXTURE MATERIAL REFERENCE` -- Y: 26.7".

**BLOCK F -- Material Table**

Y: 27.3" to 32.3".

| Material | Used For | Pros | Cons |
|---|---|---|---|
| Stainless steel (304, 316) | General fixturing | Durable, reusable, machinable | Accumulates DLC buildup -- needs periodic stripping |
| Titanium | High-end fixturing | Light, strong, compatible | Expensive; also accumulates buildup |
| Graphite | Masking, spacers | Easy to machine, conducts | Fragile; particulate risk |
| Ceramic (Al2O3) | Electrical isolation | Non-conductive, no buildup | Brittle; limited shapes |

Note: `All fixtures accumulate DLC coating over multiple runs. Schedule periodic stripping (bead blasting or chemical) to maintain dimensional accuracy and prevent flaking contamination.` Inter Regular, 13 pt, `#E8A020`.

---

### ZONE 6 -- Footer

Standard. Title: `Fixturing -- DLC`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Fixturing DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The rotation schematic is the visual anchor. Most people outside the vacuum coating industry have never seen a planetary rotation system -- this poster makes it intuitive. The contact point discussion is commercially important: customers need to know WHERE their parts will have no coating, and that decision must be made before loading, not discovered after.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #443 -- Construction Workup v1.0*
*2026-04-26*
