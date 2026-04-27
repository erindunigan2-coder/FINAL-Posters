---
Project: Plating Posters Inc
Poster Number: 645
Title: "Heat Cycle -- Martempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 10, Section 10.6)"
Technical Source: Martempering heat cycle -- austenitizing parameters (1475--1600 F), transfer timing (< 15 sec), salt/oil hold for equalization (5--15 min at just above Ms), and air cool through martensite transformation. The cycle is defined by two critical temperatures: the austenitizing temperature and the Ms temperature of the specific steel.
Process Scope: Martempering -- heat cycle
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Martempering
  - HeatCycle
  - ConstructionWorkup
  - ClusterHT10
---

# Poster #645 -- Construction Workup
## Heat Cycle -- Martempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The martempering heat cycle is a four-beat rhythm: austenitize, transfer, equalize, air cool. Every beat has a hard number attached to it. The austenitizing temperature comes from the steel's phase diagram. The transfer time comes from the TTT curve (miss the pearlite nose or you lose). The equalization hold temperature comes from the Ms of that specific steel -- set the salt bath just above it. And the air cool is where martensite actually forms, uniformly, because the surface and core are at the same temperature when it starts. This poster quantifies each beat.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Four-beat cycle diagram (Block B -- HERO):** Visual timeline showing the four cycle phases with temperature and time for each.
2. **Ms temperature reference table (Block C):** Common steels and their Ms temperatures -- the number that sets the salt bath.
3. **TTT curve concept (Block D):** Simplified schematic showing the pearlite nose and why transfer speed matters.
4. **Cycle parameter summary table (Block E):** Complete cycle parameters in one table.

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
  Stage 6 highlighted (Amber)
ZONE 3 -- FOUR-BEAT CYCLE / HERO (4.2"--14.5" / ~10.3")
  Block B: Four-phase cycle diagram
  Block C: Ms temperature reference
ZONE 4 -- TTT CURVE CONCEPT (14.5"--22.0" / ~7.5")
  Block D: Simplified TTT schematic
ZONE 5 -- CYCLE PARAMETER TABLE (22.0"--28.5" / ~6.5")
  Block E: Complete parameter summary
ZONE 6 -- FOOTER BAND (28.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `HEAT CYCLE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Martempering -- Stage 6 of 9` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Austenitize. Transfer fast. Equalize at Ms. Air cool to martensite. Four beats. Every temperature matters.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts loaded and fixtured  -->  After: Austenitized, equalized, and cooled -- martensite formed uniformly`

---

### ZONE 3 -- Four-Beat Cycle (HERO)

**Section label:** `THE FOUR-BEAT CYCLE` -- Y: 4.4".

**BLOCK B -- Four-Phase Cycle Diagram**

Y: 5.0" to 10.5". Four side-by-side phase panels connected by arrows.

Each panel: Rounded rect W: 5.3", H: 5.0", fill `#1E2435`, radius 8, top accent 4 pt.

| Phase | X | Accent | Title | Temperature | Time | What Happens |
|---|---|---|---|---|---|---|
| 1 | 0.5" | `#E8A020` | AUSTENITIZE | 1475--1600 F (802--871 C) | 30--90 min | Full transformation to FCC austenite. Temperature depends on steel grade. Hold until core reaches austenitizing temp. |
| 2 | 6.3" | `#E05C5C` | TRANSFER | Dropping | < 15 sec | Rapid transfer from furnace to salt/oil bath. CRITICAL: Must beat the pearlite nose on the TTT curve. |
| 3 | 12.1" | `#27AE60` | EQUALIZE | Just above Ms (350--600 F) | 5--15 min | Surface and core temperatures equalize. NO transformation occurs. This is the key to low distortion. |
| 4 | 17.9" | `#2EC4B6` | AIR COOL | Ms to RT | 15--60 min | Remove from bath. Still air cool. Martensite forms uniformly because surface and core start at the same temperature. |

Panel interior:
- Phase badge: Rounded rect 0.8" x 0.35", fill accent color, text `PHASE [N]` Barlow Condensed ExtraBold 13 pt `#1A1F2E`
- Title: Barlow Condensed ExtraBold, 20 pt, accent color
- Temperature: JetBrains Mono Regular, 14 pt, `#F0EDE8`
- Time: JetBrains Mono Regular, 13 pt, `#F0EDE8` at 70%
- What happens: Inter Regular, 12 pt, `#F0EDE8`, line height 150%

Arrows between panels: 3 pt `#3A4055`, filled arrowhead right.

**BLOCK C -- Ms Temperature Reference Table**

Y: 11.0" to 14.3".

Section label: `Ms TEMPERATURE -- SET YOUR SALT BATH JUST ABOVE THIS` Barlow SemiBold 16 pt `#F0EDE8`.

| Steel Grade | Ms (F) | Ms (C) | Suggested Salt Bath (F) | Application |
|---|---|---|---|---|
| 1045 | 640 | 338 | 660--680 | Gears, shafts |
| 4140 | 600 | 316 | 620--640 | General purpose |
| 4340 | 530 | 277 | 550--570 | Aircraft, high-strength |
| 52100 | 420 | 216 | 440--460 | Bearings |
| H13 | 610 | 321 | 630--650 | Die casting dies |
| M2 (HSS) | 400 | 204 | 420--440 | Cutting tools |
| D2 | 370 | 188 | 390--410 | Blanking dies |

Header: fill `#3A4055`, H: 0.45". Data rows: alternating `#1E2435` / `#252B3D`, H: 0.4".
Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Grade: Inter Medium 13 pt. Application: Inter Regular 12 pt `#F0EDE8` at 60%.

Note: `Ms values are approximate and vary with exact chemistry. Always verify against the steel supplier's data sheet or published TTT/CCT curves.` Inter Regular 11 pt `#F0EDE8` at 50%.

---

### ZONE 4 -- TTT Curve Concept

**Section label:** `WHY TRANSFER SPEED MATTERS -- THE TTT CURVE` -- Y: 14.7".

**BLOCK D -- Simplified TTT Schematic**

Y: 15.3" to 21.8". Full-width panel.

- Rounded rect W: 23.0", H: 6.0", fill `#1E2435`, radius 8

Two-column layout:

**Left -- TTT Description (X: 1.0", W: 10.5"):**

Title: `TIME-TEMPERATURE-TRANSFORMATION` -- Barlow SemiBold, 18 pt, `#F0EDE8`

Content (Inter Regular, 13 pt, `#F0EDE8`, line height 165%):
```
The TTT (Time-Temperature-Transformation)
diagram maps what microstructure forms at each
temperature and time combination.

KEY FEATURES:
- PEARLITE NOSE: The fastest transformation
  region (typically 1000--1200 F / 540--650 C)
- The cooling path must PASS the nose before
  transformation starts
- Transfer time < 15 seconds ensures the part
  reaches the salt bath before pearlite nucleates

IF YOU'RE TOO SLOW:
  Pearlite forms = soft spots = REJECT
```

Key terms in `#E8A020` (Pearlite nose), `#E05C5C` (too slow / reject).

**Right -- Simplified Diagram (X: 12.5", W: 10.0"):**

Conceptual TTT layout built with rectangles and labels:

Vertical axis label: `TEMPERATURE` -- Barlow SemiBold 14 pt `#F0EDE8`, rotated 90 degrees
Horizontal axis label: `LOG TIME` -- Barlow SemiBold 14 pt `#F0EDE8`

Zone labels positioned within the diagram area:
- Top: `AUSTENITE` -- Inter Medium 16 pt `#E8A020`
- Upper-middle (nose area): `PEARLITE NOSE` -- Inter Medium 14 pt `#E05C5C`, surrounded by rounded rect fill `#E05C5C` at 15%
- Lower-middle: `BAINITE` -- Inter Medium 14 pt `#F0EDE8` at 50%
- Bottom: `Ms LINE` -- JetBrains Mono Regular 14 pt `#27AE60`, horizontal dashed line 2 pt `#27AE60`
- Below Ms: `MARTENSITE` -- Inter Medium 16 pt `#27AE60`

Cooling path arrow: curved/stepped line from top-left to bottom (representing rapid cool past pearlite nose to salt bath, hold at Ms, then air cool), stroke 3 pt `#2EC4B6`, dashed.

Label on path: `MARTEMPERING PATH` -- Inter Medium 12 pt `#2EC4B6`

---

### ZONE 5 -- Cycle Parameter Table

**Section label:** `COMPLETE CYCLE PARAMETERS` -- Y: 22.2".

**BLOCK E -- Parameter Summary Table**

Y: 22.9" to 28.3". Column widths (23.0" total):
- Phase (3.5") | Temperature (5.0") | Time (3.5") | Key Control (11.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Phase | Temperature | Time | Key Control |
|---|---|---|---|
| Austenitize | 1475--1600 F (802--871 C) | 30--90 min | Full transformation; verify with load thermocouple; AMS 2750 Class 3 or 4 |
| Transfer | Dropping (no hold) | < 15 sec | Beat the pearlite nose; automated transfer preferred |
| Salt/oil hold | Just above Ms (350--600 F) | 5--15 min | EQUALIZATION ONLY -- if bainite starts forming, salt temp is too high or hold too long |
| Air cool | Ms to room temperature | 15--60 min | Still air; martensite forms uniformly; do not force-cool |
| Temper | Per grade (300--1100 F) | 1--4 hr | Follow immediately; mandatory for martensite |

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.85".
Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Phase: Inter Medium 13 pt.

Highlight "Transfer" row with left accent `#E05C5C`. Highlight "Salt/oil hold" row with left accent `#27AE60`.

---

### ZONE 6 -- Footer

Standard footer. Title: `Heat Cycle -- Martempering`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Ms temperatures are approximate and vary with exact steel chemistry. Austenitizing temperatures vary by grade. Consult steel supplier data sheets and TTT/CCT curves for grade-specific parameters. Source: General industry knowledge; ASM Handbook Vol. 4; AMS 2759 series.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Heat Cycle Martempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The Ms temperature table is the most actionable content on this poster -- it directly tells the operator what temperature to set the salt bath. The simplified TTT diagram translates abstract metallurgy into a spatial concept: the cooling path must dodge the pearlite nose. Building this as a labeled zone diagram (not a true curve) works within our design constraints and is arguably more readable at wall distance than a proper TTT curve would be. The four-beat rhythm (austenitize / transfer / equalize / air cool) gives the entire cycle a memorable structure.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #645 -- Construction Workup v1.0*
*2026-04-26*
