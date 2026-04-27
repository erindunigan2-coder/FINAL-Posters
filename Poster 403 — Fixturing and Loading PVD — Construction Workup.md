---
Project: Plating Posters Inc
Poster Number: 403
Title: "Fixturing & Loading -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Section 1.2)"
Technical Source: PVD fixturing covering planetary rotation, line-of-sight requirements, part spacing, fixture materials, and loading best practices.
Process Scope: PVD fixturing and loading (Stage 3 of 10)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PVD
  - Fixturing
  - Loading
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #403 -- Construction Workup
## Fixturing & Loading -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 10. PVD is a line-of-sight process -- if a surface cannot "see" the target, it will not be coated. Fixturing determines coating uniformity, and loading density determines batch economics. This poster covers planetary rotation, part spacing, fixture materials, and the critical handling rules between cleaning and chamber closure.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Planetary rotation diagram (Block B -- HERO):** Top-down schematic of a PVD chamber showing planetary rotation fixture with target positions, part positions, and rotation axes.
2. **Line-of-sight callout (Block C):** Visual showing coated vs. shadowed surfaces.
3. **Fixture material table (Block D):** Materials, temperature limits, reuse considerations.
4. **Loading rules checklist (Block E):** Best practices for loading parts.
5. **Common fixturing failures (Block F):** Problem/cause/fix cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 16.0" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Teal -- loading)
ZONE 3 -- PLANETARY ROTATION DIAGRAM / HERO (4.2"--16.0" / ~11.8")
ZONE 4 -- FIXTURE MATERIALS + LINE-OF-SIGHT (16.0"--21.5" / ~5.5")
ZONE 5 -- LOADING RULES (21.5"--27.0" / ~5.5")
ZONE 6 -- COMMON FIXTURING FAILURES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FIXTURING & LOADING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PVD -- Stage 3 of 10 -- Rotation, Spacing, and Line-of-Sight` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `PVD coats what it can see. Planetary rotation, proper spacing, and smart fixturing make the difference between a uniform coating and an expensive reject.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, dry parts (Stage 2) --> After: Parts fixtured in chamber, ready for pump-down`

---

### ZONE 3 -- Planetary Rotation Diagram (HERO)

**Section label:** `PLANETARY ROTATION -- THE KEY TO UNIFORM PVD COATINGS` -- Y: 4.4".

**BLOCK B -- Chamber Top-Down Schematic (Y: 5.0" to 13.5")**

Top-down view of cylindrical PVD chamber:
- Outer circle: Chamber wall, stroke 3 pt `#C8D0D8`, fill `#252B3D`
- Diameter representation: ~18" wide on poster, centered

**Targets (on chamber walls):**
- 2-4 rectangles positioned on the inner wall of the circle
- Fill: `#E8A020`, W: 1.5", H: 3.0"
- Label: `TARGET` Barlow SemiBold 12 pt `#E8A020`
- Sub-label: `(Ti, TiAl, Cr)` JetBrains Mono 11 pt `#F0EDE8` at 60%

**Turntable (center):**
- Large circle, fill `#1E2435`, border 2 pt `#3A4055`
- Label: `TURNTABLE` Inter Medium 12 pt `#F0EDE8` at 60%
- Central axis indicator: small circle `#C8D0D8`
- Rotation arrow: curved arrow `#2EC4B6`, label `1-20 rpm`

**Satellite spindles (on turntable):**
- 4-6 smaller circles on turntable, each with own rotation arrow
- Fill: `#1E2435`, border 1 pt `#2EC4B6`
- Label: `SPINDLE` Inter Regular 11 pt `#2EC4B6`
- Each spindle has part indicators (small rectangles) representing tooling

**Rotation labels:**
- `PRIMARY ROTATION: turntable 1-20 rpm` JetBrains Mono 13 pt `#2EC4B6`
- `SECONDARY ROTATION: spindles (planetary)` JetBrains Mono 13 pt `#E8A020`
- `TRIPLE ROTATION: individual fixtures (optional)` JetBrains Mono 12 pt `#F0EDE8` at 60%

**Key parameters (right side callout):**
- Rounded rect, X: 17.0", Y: 6.0", W: 6.5", H: 4.0", fill `#1E2435`, left accent `#E8A020`
- Title: `ROTATION SPECS` Barlow SemiBold 16 pt `#E8A020`
- `Speed: 1-20 rpm` JetBrains Mono 14 pt `#F0EDE8`
- `Direction: alternating preferred`
- `Part-to-target distance: varies by chamber`
- `Uniformity target: +/- 10% thickness`

**BLOCK C -- Line-of-Sight Callout (Y: 13.8" to 15.8")**

Full-width callout, H: 1.8", fill `#1E2435`, left accent `#E05C5C`.

Two side-by-side diagrams (simplified cross-section of a part):
- Left: Part facing target -- coating shown on exposed surface (`#27AE60`), shadow on back (`#3A4055`)
- Right: Part on rotating fixture -- coating shown on all surfaces due to rotation

Labels:
- Left: `NO ROTATION: coating on one side only` Inter Medium 14 pt `#E05C5C`
- Right: `WITH ROTATION: uniform coating all around` Inter Medium 14 pt `#27AE60`

Center callout: `PVD is line-of-sight. Without rotation, you get a coating on the front and nothing on the back.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Fixture Materials + Details

**Section label:** `FIXTURE MATERIALS AND HANDLING` -- Y: 16.2".

**BLOCK D -- Two-Column Layout (Y: 16.8" to 21.3")**

**Left -- Fixture Material Table (X: 0.5", W: 11.0"):**

| Material | Max Temp | Pros | Cons |
|---|---|---|---|
| Stainless steel (304/316) | 800 C | Durable, reusable, standard | Heavy; builds up coating over time |
| Titanium | 1000 C | Light, low outgassing | Expensive; less common |
| Molybdenum | 2000 C | Very high temp; low vapor pressure | Brittle; specialty use |
| Graphite | 2500 C | Ultra-high temp; light | Friable; particulate risk |

Header: Barlow SemiBold 13 pt, fill `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Fixture Maintenance (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.3", fill `#1E2435`, left accent `#2EC4B6`
- Title: `FIXTURE MAINTENANCE` Barlow SemiBold 18 pt `#2EC4B6`

Items (Inter Regular 14 pt `#F0EDE8`):
- `Bead blast fixtures after 5-10 runs to remove coating buildup`
- `Coating buildup changes thermal mass and can flake onto parts`
- `Inspect fixture pins and threads for wear -- loose parts shift during rotation`
- `Clean fixtures with same protocol as parts (ultrasonic + solvent)`
- `Track fixture run count in logbook`

---

### ZONE 5 -- Loading Rules

**Section label:** `LOADING BEST PRACTICES` -- Y: 21.7".

**BLOCK E -- Rule Cards (Y: 22.2" to 26.8")**

Two columns of 4 rules each. Each rule: Rounded rect W: 11.0", H: 1.1", fill `#1E2435`, left accent `#27AE60`.

| Column | Rule |
|---|---|
| Left 1 | Nitrile gloves at all times -- never touch cleaned parts with bare hands |
| Left 2 | Space parts to prevent shadowing -- minimum 5 mm gap between adjacent parts |
| Left 3 | Orient critical surfaces toward targets -- the surface that matters most faces the source |
| Left 4 | Do not overload -- reduced spacing = non-uniform coating and longer cycle |
| Right 1 | Verify rotation before closing chamber -- spin turntable by hand to check clearance |
| Right 2 | Secure all parts -- loose parts during rotation become projectiles in vacuum |
| Right 3 | Load within 2-4 hours of cleaning -- surface recontamination increases with time |
| Right 4 | Document load map -- which parts are where, for traceability and troubleshooting |

Rule text: Inter Medium 13 pt `#F0EDE8`.

---

### ZONE 6 -- Common Fixturing Failures

**Section label:** `FIXTURING FAILURES -- WHAT GOES WRONG` -- Y: 27.2".

**BLOCK F -- Four Failure Cards (Y: 27.8" to 32.3")**

| Card | X | W | Failure | Cause | Fix |
|---|---|---|---|---|---|
| 1 | 0.5" | 5.5" | NON-UNIFORM THICKNESS | Parts too close together; shadowing | Increase spacing; check fixture layout |
| 2 | 6.33" | 5.5" | BARE SPOTS | No rotation or rotation failure mid-cycle | Verify drive before cycle; monitor during |
| 3 | 12.16" | 5.5" | FLAKING FROM FIXTURES | Coating buildup on fixture flakes onto parts | Bead blast fixtures per schedule |
| 4 | 18.0" | 5.5" | PARTS SHIFTED / LOOSE | Fixture worn or not secured | Inspect pins/clips; replace worn fixtures |

Standard failure card format: Barlow SemiBold 15 pt `#E05C5C` / Inter Regular 12 pt / Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Fixturing & Loading -- PVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Fixturing Loading PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The planetary rotation diagram is the hero because it communicates the single most important concept in PVD fixturing: parts must rotate to achieve uniform coating. The top-down chamber view is intuitive for operators who see this geometry every day. The line-of-sight callout reinforces why rotation matters. Fixture maintenance is chronically neglected in real shops -- including it here is deliberate.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #403 -- Construction Workup v1.0*
*2026-04-26*
