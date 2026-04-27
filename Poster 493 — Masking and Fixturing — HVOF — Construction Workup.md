---
Project: Plating Posters Inc
Poster Number: 493
Title: "Masking & Fixturing -- HVOF"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 5)"
Technical Source: HVOF masking materials and fixturing. HVOF generates more localized heat than APS -- masking materials see higher thermal loading. Metal masks preferred for production. Lathe-type fixtures for cylindrical parts (landing gear, hydraulic rods). Typical surface speeds 0.5-2.0 m/s.
Process Scope: HVOF thermal spray -- masking materials and part fixturing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - Masking
  - Fixturing
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #493 -- Construction Workup
## Masking & Fixturing -- HVOF

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of the HVOF process. HVOF generates more localized heat than APS and higher particle velocities, which means masking materials take more punishment. Metal masks are the production standard. The fixturing section focuses on cylindrical parts (landing gear, hydraulic rods, pump shafts) since these dominate HVOF work.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Masking materials table (Block B):** 5-row comparison with HVOF-specific temperature and velocity ratings.
2. **Fixturing design rules (Block C):** 6 rules for cylindrical part fixturing.
3. **Landing gear fixture callout (Block D):** HVOF's signature application -- how to fixture large cylindrical parts.
4. **Common mistakes grid (Block E):** 4 cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- MASKING MATERIALS HERO (4.2"--14.5" / ~10.3")
  Block B: Masking materials comparison table
  Block C: Fixturing design rules
ZONE 4 -- CYLINDRICAL PART FIXTURING (14.5"--20.5" / ~6.0")
  Block D: Landing gear / hydraulic rod fixture setup
ZONE 5 -- COMMON MISTAKES (20.5"--26.5" / ~6.0")
  Block E: 4 mistake cards
ZONE 6 -- PRE-SPRAY CHECKLIST (26.5"--32.5" / ~6.0")
  Block F: Pre-spray fixture verification checklist
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `MASKING & FIXTURING` -- 80 pt `#F0EDE8`.
**Subheading:** `HVOF -- Protect, Position, Rotate -- Stage 3 of 10` -- 32 pt `#E8A020`. Y: 1.4".
**Tagline:** `HVOF hits harder and hotter than APS. Your masking and fixturing must survive supersonic particle impact and concentrated thermal loading.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted (Amber). Others dimmed.

---

### ZONE 3 -- Masking Materials + Fixturing (HERO)

**Section label:** `MASKING MATERIALS FOR HVOF` -- Y: 4.4".

**BLOCK B -- Masking Materials Table (left, W: 13.0")**

Y: 5.0" to 10.5".

| Material | Temp Rating | HVOF Suitability | Best For | Limitations |
|---|---|---|---|---|
| Metal masks (SS, Cu) | > 500 degC | EXCELLENT -- production standard | High-volume production; repeatable geometry | Requires machining; upfront cost |
| Silicone tape (hi-temp) | 260 degC (500 degF) | ACCEPTABLE -- non-critical areas only | Quick masking of flat surfaces, edges | Higher thermal load in HVOF can degrade faster |
| Silicone plugs & caps | 260 degC (500 degF) | GOOD | Holes, bores, threaded features | Check for deformation after each use |
| Ceramic fiber tape | > 1000 degC | GOOD -- extreme zones | Areas near direct combustion jet impingement | Fragile; limited adhesion; single use |
| Liquid maskant (peelable) | 200-300 degC | LIMITED | Complex shapes; backup masking | May not survive concentrated HVOF heat |

Header: fill `#3A4055`, Barlow SemiBold 13 pt. Data: Inter Regular 12 pt. Suitability column color-coded: EXCELLENT `#27AE60`, GOOD `#2EC4B6`, ACCEPTABLE `#E8A020`, LIMITED `#E05C5C`.

**BLOCK C -- Fixturing Design Rules (right, W: 9.5")**

Y: 5.0" to 10.5". Six numbered rule cards stacked vertically.

| Rule | Text |
|---|---|
| 1 | Surface speed at coating surface: 0.5-2.0 m/s (lathe-type rotation) |
| 2 | Compressed air cooling jets (dry, oil-free) directed at substrate backside |
| 3 | Programmable rotation + gun traverse for cylindrical parts |
| 4 | Fixture must not shadow spray pattern -- 360-degree access for round parts |
| 5 | Ground fixture to workpiece for electrostatic discharge prevention |
| 6 | Sacrificial test tabs on same fixture for in-process QC |

Each rule: Rounded rect, H: 0.85", fill `#1E2435`, left accent `#2EC4B6`.
Rule number: Barlow Condensed ExtraBold 16 pt `#2EC4B6`. Text: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 4 -- Cylindrical Part Fixturing

**Section label:** `FIXTURING CYLINDRICAL PARTS -- THE HVOF WORKHORSE` -- Y: 14.7".

**BLOCK D -- Landing Gear / Hydraulic Rod Fixture**

Y: 15.3" to 20.3". Full width.

Two-column layout:

**Left -- Setup Description (W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `LATHE-TYPE FIXTURE FOR CYLINDRICAL HVOF` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
HVOF dominates cylindrical part coating:
- Landing gear (chrome replacement)
- Hydraulic cylinder rods
- Pump shafts and valve stems
- Paper mill rolls

Fixture requirements:
- Centers or chucks supporting full part weight
- Variable speed drive: surface speed 0.5-2.0 m/s
- Gun mounted on robot or linear traverse
- Traverse synchronized with rotation
- Compressed air cooling from backside or co-axial
```

**Right -- Key Parameters (W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `CRITICAL FIXTURE PARAMETERS` Barlow SemiBold 18 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Surface speed | 0.5-2.0 m/s at coating surface |
| Traverse speed | 300-1000 mm/s (gun movement) |
| Step increment | 3-6 mm overlap between passes |
| Cooling | Compressed air: dry, oil-free, directed at backside |
| Max substrate temp | 150 degC (monitor with IR pyrometer) |
| Runout tolerance | < 0.05 mm TIR for precision parts |

Labels: Inter Medium 12 pt `#F0EDE8` at 60%. Values: JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 5 -- Common Mistakes

**Section label:** `4 MASKING & FIXTURING MISTAKES` -- Y: 20.7".

Four cards in a row:

| Problem | Cause | Fix |
|---|---|---|
| COATING UNDER MASK | Tape not sealed; gap at edge; HVOF velocity drives particles under loose masks | Use metal masks with tight edge fit |
| MASK BURNTHROUGH | Silicone tape in direct spray path; HVOF heat overwhelms tape rating | Switch to metal mask or ceramic fiber for high-heat zones |
| TAPER ON CYLINDER | Inconsistent traverse speed at ends of stroke | Program robot decel/accel at turnaround; verify overlap |
| PART OVERHEATING | Insufficient cooling; slow rotation | Increase surface speed; add cooling air; reduce pass dwell |

Each card: Rounded rect, W: 5.5", H: 5.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

---

### ZONE 6 -- Pre-Spray Checklist

**Section label:** `PRE-SPRAY FIXTURE VERIFICATION` -- Y: 26.7".

**BLOCK F -- Checklist (10 items)**

Two columns of 5 items. Each: checkbox + text.

| Item |
|---|
| Part securely fixtured -- no wobble or runout |
| Masking complete and inspected -- metal masks seated |
| No masking tape in direct spray path |
| Cooling air nozzles positioned and tested |
| Fixture does not shadow any coated area |
| Sacrificial test tabs installed on fixture |
| Rotation speed verified at correct surface speed |
| Part grounded to fixture |
| All non-coated features masked (holes, threads, journals) |
| Standoff distance verified at all angular positions |

Checkbox squares: 0.25" x 0.25", border 2 pt `#27AE60`, no fill.
Item text: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Masking & Fixturing -- HVOF`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Masking Fixturing HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

HVOF is overwhelmingly a cylindrical-part process -- landing gear, hydraulic rods, pump shafts. The fixturing section reflects this reality. Metal masks are the production standard because silicone tape struggles with HVOF's concentrated heat. The "mask burnthrough" mistake card is HVOF-specific and critical: operators moving from APS may not realize how much more aggressive HVOF is on masking materials.

---

*Alaina -- Poster #493 -- Construction Workup v1.0 -- 2026-04-26*
