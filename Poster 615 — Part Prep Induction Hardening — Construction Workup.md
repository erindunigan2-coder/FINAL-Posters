---
Project: Plating Posters Inc
Poster Number: 615
Title: "Part Prep -- Induction Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7, Section 7.7)"
Technical Source: Part preparation for induction hardening. Surface cleanliness, prior microstructure requirements, and the critical distinction that no stop-off coating is needed (unlike carburizing). Steel grade selection tied to carbon content requirements.
Process Scope: Induction hardening -- part preparation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - InductionHardening
  - PartPrep
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #615 -- Construction Workup
## Part Prep -- Induction Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Part preparation for induction hardening is simpler than for diffusion processes (no masking, no stop-off plating), but the requirements that DO exist are non-negotiable. Prior microstructure is the hidden variable -- a coarse pearlite structure will not respond the same as a fine Q&T structure, and the rapid heating of induction makes this more critical than in furnace hardening.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Prior microstructure comparison (Block B -- HERO):** Side-by-side panels showing ideal vs. problematic starting microstructures and their effect on induction response.
2. **Steel grade selection table (Block D):** Comprehensive table of suitable steels with carbon content and expected hardness.
3. **Surface condition checklist (Block E):** Go/no-go checklist for surface readiness.
4. **Decarburization warning (Block F):** Critical callout on decarburized surfaces.

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
  Stage 1 highlighted (Teal)
ZONE 3 -- PRIOR MICROSTRUCTURE / HERO (4.2"--14.5" / ~10.3")
  Block B: Microstructure comparison panels
  Block C: "Why Prior Micro Matters" callout
ZONE 4 -- STEEL GRADE TABLE (14.5"--22.0" / ~7.5")
  Block D: Suitable steel grades with expected hardness
ZONE 5 -- SURFACE CONDITION CHECKLIST + DECARB WARNING (22.0"--32.5" / ~10.5")
  Block E: Go/no-go surface checklist
  Block F: Decarburization warning panel
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Induction Hardening -- Stage 1 of 7` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `No stop-off. No masking. But the steel must be right -- carbon content and prior microstructure determine everything.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw or machined part  -->  After: Clean, verified, ready for fixturing`

---

### ZONE 3 -- Prior Microstructure (HERO)

**Section label:** `PRIOR MICROSTRUCTURE -- THE HIDDEN VARIABLE` -- Y: 4.4".

**BLOCK B -- Microstructure Comparison**

Y: 5.0" to 12.5". Four side-by-side panels showing starting structures:

Each panel: Rounded rect W: 5.5", H: 7.0", fill `#1E2435`, radius 8.

| Panel | X | Structure | Accent | Rating | Description |
|---|---|---|---|---|---|
| 1 | 0.5" | FINE Q&T (Tempered Martensite) | `#27AE60` | IDEAL | Fine, uniform structure. Austenitizes rapidly and uniformly under induction. Produces the most consistent case depth and hardness. |
| 2 | 6.25" | FINE PEARLITE (Normalized) | `#27AE60` | GOOD | Fine lamellar pearlite. Austenitizes well but slightly slower than Q&T. Acceptable for most applications. |
| 3 | 12.0" | COARSE PEARLITE (Annealed) | `#E8A020` | CAUTION | Coarse lamellar structure. Requires higher temperature or longer heating to fully austenitize. Risk of incomplete transformation and mixed hardness. |
| 4 | 17.75" | BANDED / SEGREGATED | `#E05C5C` | PROBLEM | Chemical segregation from hot working. Creates non-uniform carbon distribution. Induction heating amplifies the non-uniformity -- hard and soft bands in the case. |

Panel interior:
- Structure name: Barlow SemiBold 18 pt, accent color
- Rating badge: Rounded rect 1.4" x 0.35", fill = accent color. Text: Barlow Condensed ExtraBold 12 pt `#1A1F2E`
- Description: Inter Regular 13 pt `#F0EDE8` line height 155%
- Microstructure placeholder: Rounded rect 4.5" x 2.5", fill `#252B3D`, border 1 pt accent color. Center text: `[Metallographic image placeholder]` Inter Regular 11 pt `#F0EDE8` at 40%

**BLOCK C -- Why Prior Micro Matters**

Y: 12.8" to 14.3". Full-width callout.
- Rounded rect W: 23.0", H: 1.3", fill `#1E2435`, left accent 0.06" `#E8A020`
- Text: `Induction heating is FAST (100--1000 F/sec). There is no time for slow diffusion processes to homogenize the structure. What you start with is what you get -- magnified. A furnace process has minutes to hours for the structure to equilibrate. Induction has seconds.` -- Inter Medium 14 pt `#F0EDE8`

---

### ZONE 4 -- Steel Grade Table

**Section label:** `SUITABLE STEEL GRADES FOR INDUCTION HARDENING` -- Y: 14.7".

**BLOCK D -- Grade Table**

Y: 15.3" to 21.8". Column widths (23.0" total):
- Category (4.0") | Grades (5.5") | Carbon % (3.0") | Surface HRC (3.0") | Notes (7.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Category | Grades | Carbon % | Surface HRC | Notes |
|---|---|---|---|---|
| Medium carbon (workhorse) | 1045, 1050, 1055 | 0.43--0.55 | 58--62 | THE standard induction steels |
| Alloy (medium C) | 4140, 4150, 4340, 4145H | 0.38--0.53 | 58--62 | Higher hardenability for deeper case or less severe quench |
| High carbon | 1060, 1070, 1095, 52100 | 0.55--1.00 | 60--65 | Bearing races, springs |
| Microalloy | 1541, 15B41, 10V45 | 0.40--0.50 | 55--60 | Automotive forgings |
| Cast iron | Gray 40+, Ductile 80-55-06 | 3.0--3.8 (total) | 45--55 | Camshafts, cylinder liners, brake drums |
| NOT SUITABLE | 1018, 1020, 8620 | < 0.30 | -- | Too low carbon; will not form useful martensite unless previously carburized |

Data: JetBrains Mono Regular 12 pt `#F0EDE8`. "NOT SUITABLE" row: `#E05C5C` text.

Bottom note: `Rule of thumb: 0.35% C minimum for useful induction hardness. Below 0.30% C = do not attempt unless surface has been carburized first.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Surface Condition + Decarb Warning

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Surface Condition Checklist (X: 0.5", W: 11.0"):**

Section label: `SURFACE CONDITION -- GO / NO-GO` Barlow Condensed ExtraBold 24 pt.

Checklist items (Y: 23.0" to 30.0"):

| Item | Status | Detail |
|---|---|---|
| Scale-free surface | GO | Light oxide scale interferes with electromagnetic coupling -- reduces heating efficiency and creates soft spots |
| Rust-free | GO | Same as scale -- barrier to coupling |
| Oil/grease-free | GO | Burns off during heating but creates smoke and uneven heating |
| No copper stop-off needed | NOTE | Unlike carburizing, induction heats only where the coil is -- no masking required. The coil IS the mask. |
| Proper prior microstructure | GO | Fine pearlite or Q&T preferred; verify on first-article |
| Dimensional check | GO | Parts must be within tolerance BEFORE hardening -- distortion will move dimensions |
| Deburr sharp edges | GO | Sharp edges overheat first due to current concentration -- can crack |

Each row: Rounded rect H: 0.9", fill alternating `#1E2435` / `#252B3D`.
Status badge: GO = `#27AE60`, NOTE = `#E8A020`.
Item: Inter Medium 13 pt. Detail: Inter Regular 12 pt `#F0EDE8` at 75%.

**Right -- Decarburization Warning (X: 12.0", W: 11.5"):**

Section label: `DECARBURIZATION -- THE SILENT KILLER` Barlow Condensed ExtraBold 24 pt `#E05C5C`.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E05C5C`
- Warning text (Inter Regular 14 pt `#F0EDE8`, line height 160%):

```
A decarburized surface CANNOT be induction
hardened to specification.

Decarburization = carbon loss from the surface
layer during prior heat treatment or hot working.

If the surface carbon is below ~0.35%, no amount
of induction power will produce 58+ HRC martensite.

HOW TO CHECK:
- Microhardness traverse on cross-section
- Nital etch (3--5%) -- decarb layer appears lighter
- Carbon analysis by OES or GDOES

COMMON SOURCES OF DECARB:
- Prior normalizing without protective atmosphere
- Hot forging without scale protection
- Prolonged storage of hot-rolled bar stock

IF DECARB IS FOUND:
- Machine off the decarburized layer (if tolerance allows)
- Or reject the lot for induction hardening
- Carburize first to restore surface carbon (rare, expensive)
```

Bottom highlight: `Decarb is invisible to the naked eye. Always verify surface carbon on first articles from new material lots.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Footer

Standard footer. Title: `Part Prep -- Induction Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; AMS 2745.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Prep Induction Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Prior microstructure is the concept that separates a knowledgeable induction operator from a button-pusher. Most induction training focuses on power, frequency, and time -- but the starting structure of the steel is equally important and rarely discussed on the shop floor. This poster makes it visual and unavoidable. The decarburization warning is the single most important "gotcha" for parts coming from forging or prior heat treatment.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #615 -- Construction Workup v1.0*
*2026-04-26*
