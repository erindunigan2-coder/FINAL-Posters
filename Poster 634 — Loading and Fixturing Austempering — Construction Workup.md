---
Project: Plating Posters Inc
Poster Number: 634
Title: "Loading & Fixturing -- Austempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 9: Austempering, Section 9.4)"
Process Scope: Loading, fixturing, drainage orientation, and transfer mechanisms for austempering salt bath operations
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Austempering
  - Loading
  - Fixturing
  - ConstructionWorkup
  - ClusterHT09
---

# Poster #634 -- Construction Workup
## Loading & Fixturing -- Austempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Loading for austempering is defined by two imperatives: (1) parts must be oriented for rapid, complete immersion in the salt bath -- no air pockets, no cupped geometries trapping salt -- and (2) the transfer mechanism from austenitizing furnace to salt bath must deliver the load in under 15 seconds. Miss that window and the pearlite nose eats your parts. This poster covers fixture materials, drainage orientation, transfer speed requirements, and thermocouple placement.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Drainage orientation hero (Block B):** Visual showing correct vs. incorrect part orientation for salt bath immersion -- cupped vs. drained geometry.
2. **Fixture materials table (Block C):** Material options with temperature ratings and salt compatibility.
3. **Transfer speed callout (Block D):** Critical 15-second window with TTT reference.
4. **Load planning checklist (Block E):** Practical checklist for load configuration.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Teal)
ZONE 3 -- DRAINAGE ORIENTATION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- FIXTURE MATERIALS TABLE (14.5"--21.0" / ~6.5")
ZONE 5 -- TRANSFER SPEED CRITICAL (21.0"--27.5" / ~6.5")
ZONE 6 -- LOAD PLANNING CHECKLIST (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING & FIXTURING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Austempering -- Salt Bath Immersion & Transfer` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Drain it, space it, move it fast. Fifteen seconds from furnace to salt -- or the pearlite nose wins.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 of 9 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, verified parts on fixtures --> After: Loaded, oriented for rapid salt bath immersion`

---

### ZONE 3 -- Drainage Orientation Hero

**Section label:** `PART ORIENTATION FOR SALT BATH IMMERSION` -- Y: 4.4".

**BLOCK B -- Correct vs. Incorrect Orientation**

Y: 5.0" to 14.0". Two-column layout showing schematic part cross-sections.

**Left column -- CORRECT (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`, radius 6.

Title: `CORRECT ORIENTATION` -- Barlow SemiBold, 20 pt, `#27AE60`

Four orientation rules with schematic descriptions:

| Rule | Description |
|---|---|
| Bore vertical | Cylindrical parts hung or fixtured with bore vertical -- salt drains freely on extraction |
| No cupping | Open side faces DOWN during immersion -- prevents trapped air pockets that block salt contact |
| Tilt flat parts | Flat stampings tilted 10-15 deg on fixture -- prevents salt pooling on top surface during removal |
| Space for flow | Minimum 0.25" (6 mm) between parts -- salt must circulate on all surfaces |

Each rule: Barlow SemiBold 14 pt (rule name in `#27AE60`), Inter Regular 13 pt (description in `#F0EDE8`).

Bottom note: `Proper drainage reduces salt carryover by 50-70% and eliminates trapped-air soft spots` -- Inter Medium, 13 pt, `#27AE60`

**Right column -- INCORRECT (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`, radius 6.

Title: `COMMON MISTAKES` -- Barlow SemiBold, 20 pt, `#E05C5C`

| Mistake | Consequence |
|---|---|
| Cupped parts facing up | Trapped air pocket = no salt contact = soft spot (pearlite) |
| Parts nested/touching | Contact point blocks quench = non-uniform transformation |
| Flat parts horizontal | Salt pools on extraction = excessive carryover = waste + drip hazard |
| No drainage clearance | Salt trapped in fixture = poor extraction + burn risk |

Each: Barlow SemiBold 14 pt (mistake in `#E05C5C`), Inter Regular 13 pt (consequence in `#F0EDE8`).

**Center warning banner (Y: 13.5"):**
- Rounded rect, full width, H: 0.5", fill `#E05C5C` at 20%, border 2 pt `#E05C5C`
- Text: `TRAPPED AIR = SOFT SPOTS. If salt cannot reach the surface, bainite cannot form there.` -- Barlow SemiBold, 15 pt, `#E05C5C`, Center

---

### ZONE 4 -- Fixture Materials Table

**Section label:** `FIXTURE MATERIALS FOR SALT BATH SERVICE` -- Y: 14.7".

**BLOCK C -- Materials Table**

Y: 15.3" to 20.8". Column widths (23.0" total):
- Material (5.0") | Max Temp (3.5") | Salt Compatible (3.0") | Pros (6.0") | Cons (5.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Material | Max Temp | Salt OK? | Pros | Cons |
|---|---|---|---|---|
| Alloy steel baskets (RA 330) | 2100 F | Yes | Strong, weldable, good creep resistance | Expensive; eventually degrades in salt |
| Inconel 601 | 2200 F | Yes | Best salt resistance; longest life | Highest cost |
| Low-alloy steel hooks | 1200 F | Austempering only | Cheap, simple, replaceable | Limited to lower salt temps; corrodes |
| Carbon steel wire baskets | 1000 F | Limited | Lowest cost for disposable use | Short life; scale forms; salt attack |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Material names: Inter Medium, 13 pt.

**Note below table:**
- `Fixture weight counts against load capacity. Salt bath volume must accommodate total immersed volume (parts + fixtures) without overflow.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 5 -- Transfer Speed Critical

**Section label:** `THE 15-SECOND RULE -- TRANSFER FROM FURNACE TO SALT` -- Y: 21.2".

**BLOCK D -- Transfer Window**

Y: 21.8" to 27.3". Two-panel layout.

**Left -- The Rule (X: 0.5", W: 14.0"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`, radius 6.

Title: `MAXIMUM 15 SECONDS` -- Barlow Condensed ExtraBold, 28 pt, `#E05C5C`

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
From the moment the furnace door opens to the moment the last
part is submerged in salt -- 15 seconds maximum.

WHY: The pearlite nose on the TTT diagram for most austempering
steels occurs between 1000-1100 F. If any part of the cross-
section cools into this range and lingers, pearlite forms
irreversibly. Pearlite = scrap.

TRANSFER METHODS:
  Overhead crane     -- 8-12 sec typical
  Automated conveyor -- 5-8 sec typical
  Robot arm          -- 3-6 sec (fastest, most consistent)
```

Parameters: JetBrains Mono Regular, 13 pt.

**Right -- What Happens If You Miss (X: 15.0", W: 8.5"):**

Three stacked callout boxes:

| Delay | Outcome |
|---|---|
| < 15 sec | Full bainite -- GOOD |
| 15-30 sec | Mixed bainite + pearlite -- may or may not meet spec |
| > 30 sec | Significant pearlite -- likely scrap |

Box fills: first `#27AE60` at 12%, second `#E8A020` at 12%, third `#E05C5C` at 12%. Border 1 pt matching accent.

Data: JetBrains Mono Regular 14 pt. Outcome labels: Inter Medium 14 pt in accent color.

---

### ZONE 6 -- Load Planning Checklist

**Section label:** `LOAD PLANNING CHECKLIST` -- Y: 27.7".

**BLOCK E -- Checklist**

Y: 28.3" to 32.3". Rounded rect, full width, H: 3.8", fill `#1E2435`, left accent `#2EC4B6`, radius 8.

Checklist items (Inter Medium 15 pt `#F0EDE8`):

```
[ ] Verify all parts are clean, dry, and free of organic contamination
[ ] Orient parts for drainage -- open ends DOWN, bores VERTICAL
[ ] Minimum 0.25" spacing between all parts -- no nesting or contact
[ ] Confirm fixture material rated for austenitizing temperature (1500+ F)
[ ] Pre-heat fixtures to 250+ F before immersion in molten salt
[ ] Verify transfer path is clear -- no obstacles between furnace and salt bath
[ ] Confirm salt bath level can accommodate full load volume without overflow
[ ] Test transfer time with empty fixture -- must achieve < 15 sec consistently
```

Each checkbox: 0.25" x 0.25" rounded rect, border 1 pt `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Loading & Fixturing -- Austempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; ASTM A897. Specific fixture selections and transfer configurations vary by equipment.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading Fixturing Austempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The drainage orientation hero is the visual hook -- side-by-side correct vs. incorrect makes the point instantly. The 15-second rule is the process-critical message that must hit hard. Color-coded outcome boxes (green/amber/coral) for transfer delay create an at-a-glance risk ladder. The checklist in Zone 6 is the actionable takeaway -- this lives on the wall next to the loading station.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #634 -- Construction Workup v1.0*
*2026-04-26*
