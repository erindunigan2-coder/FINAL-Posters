---
Project: Plating Posters Inc
Poster Number: 672
Title: "Application -- E-Coat"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 3, Section 3.6)"
Technical Source: Cathodic electrodeposition tank chemistry and mechanism. Covers the self-limiting deposition process, bath parameters, anode management, and cathodic vs. anodic comparison.
Process Scope: E-coat tank application (cathodic electrodeposition) -- Stage 6 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ECoating
  - Application
  - Electrodeposition
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC03
---

# Poster #672 -- Construction Workup
## Application -- E-Coat

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 9. This is the heart of e-coat -- the electrodeposition tank. DC voltage drives cationic resin micelles toward the cathodic body, where local pH rise from water electrolysis causes the resin to precipitate as a dense, insulating film. The self-limiting mechanism is the genius of the process: once the film insulates a surface, current stops flowing there and deposition moves to the next uncoated area. That is why e-coat reaches every cavity a spray gun cannot.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Electrodeposition mechanism diagram (Block B -- HERO):** Cross-section view of body in tank showing cathode (body), anodes in anode boxes, electric field lines, micelle migration, and OH- generation at cathode surface. Simplified but technically accurate.
2. **Bath parameter table (Block C):** Cathodic vs. anodic side-by-side parameter comparison.
3. **Anode management panel (Block D):** Callout explaining anode boxes, dialysis membranes, and anolyte bleed.
4. **Self-limiting mechanism callout (Block E):** Step-by-step explanation of the deposition and self-limiting process.
5. **Defect grid (Block F):** 6 application defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Amber)
ZONE 3 -- ELECTRODEPOSITION MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH PARAMETERS + CATHODIC VS. ANODIC (14.5"--21.0" / ~6.5")
ZONE 5 -- ANODE MANAGEMENT + SELF-LIMITING (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT DIAGNOSIS GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `APPLICATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `E-Coat Tank -- Cathodic Electrodeposition -- Stage 6 of 9` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `200--400 volts DC. 120--180 seconds. Every cavity, every weld seam, every box section -- coated. The self-limiting film that spray cannot match.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Zinc-phosphated body, wet from DI rinse  -->  After: Uniform 0.6--1.2 mil electrodeposited primer on every surface`

---

### ZONE 3 -- Electrodeposition Mechanism Hero

**Section label:** `HOW CATHODIC ELECTRODEPOSITION WORKS` -- Y: 4.4".

**BLOCK B -- Mechanism Diagram**

Y: 5.0" to 14.0". Full width within margins.

Large cross-section schematic of an e-coat tank. This is a conceptual layout description for the generation prompt:

**Tank outline:** Large rounded rect, X: 1.0", Y: 5.5", W: 22.0", H: 7.5", fill `#252B3D`, stroke 2 pt `#3A4055`.

**Body (Cathode) -- center of tank:**
- Simplified car body profile (rectangular with roof profile), centered in tank.
- Label: `BODY (CATHODE -)` Barlow SemiBold 18 pt `#E8A020`
- Connected to DC power supply (negative terminal).

**Anodes -- along tank walls:**
- Two vertical rectangles on left and right walls of tank.
- Label: `ANODE (+)` on each.
- Color fill: `#3A4055` with `#E8A020` stroke.
- Sub-label: `316 SS in anode boxes` Inter Regular 12 pt `#F0EDE8` at 60%.

**Electric field arrows:** Dashed lines from anodes toward body, showing field direction.

**Micelle migration arrows:**
- Solid amber arrows from bath toward body surface.
- Label: `Cationic resin micelles migrate to cathode` Inter Medium 13 pt `#E8A020`.

**At cathode surface (zoomed callout box, X: 14.0", Y: 5.5", W: 9.0", H: 4.5"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `AT THE CATHODE SURFACE` Barlow SemiBold 16 pt `#E8A020`
- Step-by-step (JetBrains Mono 12 pt `#F0EDE8`):
```
1. Water electrolysis:
   2H2O + 2e- -> H2 + 2OH-

2. Local pH rises at surface

3. Cationic resin (amine groups)
   neutralizes -- becomes insoluble

4. Resin + pigment deposits as
   dense, adherent film

5. Film insulates surface --
   current stops -- deposition
   moves to uncoated areas
```

**Bath contents label (in tank area):**
- `18--22% solids` / `pH 5.8--6.2` / `85--95 F` / `1,000--1,800 uS/cm`
- JetBrains Mono 14 pt `#F0EDE8` at 70%.

**DC Power Supply indicator (top center):**
- Small box: `200--400 V DC` Barlow SemiBold 16 pt `#E8A020`
- Lines connecting to cathode (-) and anode (+).

---

### ZONE 4 -- Bath Parameters + Cathodic vs. Anodic

**Section label:** `BATH PARAMETERS -- CATHODIC VS. ANODIC` -- Y: 14.7".

**BLOCK C -- Comparison Table (Y: 15.3" to 20.8")**

Column widths (23.0" total):
- Parameter (5.0") | Cathodic Epoxy (9.0") | Anodic Acrylic (9.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

Column headers: `PARAMETER` | `CATHODIC EPOXY E-COAT` (color `#E8A020`) | `ANODIC ACRYLIC E-COAT` (color `#2EC4B6`)

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.45".

| Parameter | Cathodic Epoxy | Anodic Acrylic |
|---|---|---|
| Part polarity | Cathode (no metal dissolution) | Anode (metal dissolves) |
| Solids content | 18--22% by weight | 8--14% |
| pH | 5.8--6.2 | 7.5--8.5 |
| Conductivity | 1,000--1,800 uS/cm | 800--1,500 uS/cm |
| Temperature | 85--95 F (29--35 C) | 80--90 F (27--32 C) |
| Voltage | 200--400 V DC | 50--250 V DC |
| Immersion time | 120--180 sec | 90--120 sec |
| DFT (cured) | 0.6--1.2 mils (15--30 um) | 0.4--0.8 mils |
| P/B ratio | 0.15--0.25 | 0.10--0.20 |
| MEQ (acid/100g solids) | 30--45 | N/A (base-neutralized) |
| Throwing power | Excellent (8--12" into cavities) | Moderate |
| Corrosion (B117) | 500--1,000+ hr (primer alone) | Lower |
| Anode material | 316 stainless steel | Carbon/graphite |
| Market share | >95% automotive worldwide | Small appliances, general |

Data: JetBrains Mono Regular 11 pt `#F0EDE8`. Parameter labels: Inter Medium 12 pt.

---

### ZONE 5 -- Anode Management + Self-Limiting

**Two-column layout (Y: 21.2" to 26.3"):**

**Left -- Anode Management (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `ANODE MANAGEMENT` Barlow SemiBold 20 pt `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
Anodes are enclosed in ANODE BOXES --
dialysis membranes that allow organic acid
anions to pass out of the bath.

Anode box effluent (anolyte) is bled off
and replaced with DI water to control
bath pH and conductivity.

Anode material:
  Cathodic: 316 stainless steel
  Anodic: Carbon/graphite (SS dissolves
          in anodic bath)

Anode boxes prevent acid buildup in the
bath -- essential for pH stability.
```

Key highlight:
- `Without anode boxes, organic acids accumulate and crash bath pH.` Inter Medium 13 pt `#E05C5C`

**Right -- Self-Limiting Mechanism (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `THE SELF-LIMITING MECHANISM` Barlow SemiBold 20 pt `#27AE60`

Content:
```
1. Voltage drives resin to cathode surface
2. Film deposits and grows thicker
3. Deposited film is electrically insulating
4. Once film reaches critical thickness,
   current cannot flow through that area
5. Deposition STOPS at coated areas
6. Current redirects to remaining bare
   metal -- including deep cavities
7. Process continues until all accessible
   surfaces reach uniform thickness

This is why e-coat reaches every weld
seam, box section, and interior cavity.
Spray painting cannot do this.
```

Key highlight:
- `Self-limiting = uniform thickness = unmatched throwing power. The physics does the work.` Inter Medium 13 pt `#27AE60`

---

### ZONE 6 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 E-COAT TANK DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid**

Y: 27.3" to 32.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | THIN FILM IN CAVITIES | `#E05C5C` | Voltage too low or bath conductivity off | Increase voltage; verify conductivity 1,000--1,800 uS/cm |
| R1C2 | CRATERS / PINHOLES | `#E05C5C` | Phosphate porosity, bath contamination, or gas bubbles | Improve seal rinse; filter bath; check H2 evolution |
| R1C3 | ORANGE PEEL / ROUGHNESS | `#E8A020` | Bath solids too high or P/B ratio drift | Check solids 18--22%; verify P/B 0.15--0.25 |
| R2C1 | HIGH FILM BUILD (WASTE) | `#E8A020` | Voltage too high or immersion time excessive | Reduce voltage; optimize dwell time |
| R2C2 | pH DRIFT | `#2EC4B6` | Anode box membrane failure or anolyte bleed rate off | Inspect anode box membranes; adjust bleed rate |
| R2C3 | BATH FOAMING | `#E05C5C` | Contamination (oil, cleaning surfactant carry-over) | Identify contamination source; activate defoamer |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Application -- E-Coat`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; automotive cathodic e-coat specifications. Bath parameters are typical for cathodic epoxy systems. Specific values vary by supplier formulation.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Application E-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the flagship poster of the E-Coating cluster -- the mechanism diagram is the most technically ambitious visual in the series. The self-limiting mechanism is the single most important concept: it explains why e-coat exists, why it beats spray, and why it is the universal automotive primer. The cathode surface callout with the electrolysis equation grounds the process in real chemistry. The cathodic vs. anodic table answers the inevitable "why not anodic?" question with data, not opinion.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #672 -- Construction Workup v1.0*
*2026-04-26*
