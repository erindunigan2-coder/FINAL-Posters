---
Project: Plating Posters Inc
Poster Number: 691
Title: "Flow Application -- Flow Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 5: Flow Coating, Section 5.6)"
Process Scope: Flow application stage for flow coating -- Stage 5 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FlowCoating
  - Application
  - ConstructionWorkup
  - PaintingCoating
  - ClusterFC
---

# Poster #691 -- Construction Workup
## Flow Application -- Flow Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 7. This is the main event -- liquid coating pumped over the part, gravity pulling it down, excess collected and recirculated. No spray gun, no compressed air, no booth. Just a pump, nozzles, and gravity. The simplicity is the advantage and the limitation: you cannot place coating precisely, but you can coat huge parts with 90-95% transfer efficiency.

Hero visual: schematic of a flow coating system showing the nozzle manifold, part, drain pan, and recirculation tank with flow arrows.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Flow coating system schematic hero (Block B):** A simplified side-view diagram showing the nozzle bank, a suspended part, drain pan below, and recirculation loop (pump, filter, reservoir). Built with rectangles, arrows, and labeled components.
2. **Application methods comparison table (Block D):** Curtain flow vs. flood/flow vs. dip-drain hybrid.
3. **Viscosity and recirculation control panel (Block E):** The dominant operational challenge.
4. **Defect strip (Block F):** 4 common application failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- FLOW COATING SYSTEM SCHEMATIC HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- APPLICATION METHODS TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- VISCOSITY AND RECIRCULATION CONTROL (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON APPLICATION FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FLOW APPLICATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flow Coating -- Stage 5 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Pump it over the part. Let gravity do the work. Collect the excess and use it again. 90-95% transfer efficiency with nothing but a pump and a pan.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Pretreated, dry surface ready for coating  -->  After: Wet-coated part draining excess coating back to reservoir`

---

### ZONE 3 -- Flow Coating System Schematic Hero

**Section label:** `THE FLOW COATING SYSTEM -- HOW IT WORKS` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- System Schematic Diagram**

Y: 5.0" to 14.0". Full-width diagram panel (X: 0.5", W: 23.0", H: 8.5"), fill `#1E2435`, radius 8.

**Component layout (side-view schematic, left to right):**

**Recirculation Tank (bottom-left, X: 1.5", Y: 10.5", W: 5.0", H: 2.5"):**
- Rounded rect, fill `#252B3D`, border 2 pt `#C8D0D8`
- Label: `RESERVOIR` -- Barlow SemiBold, 14 pt, `#F0EDE8`
- Sublabel: `50-500 gal` -- JetBrains Mono, 11 pt, `#E8A020`
- Interior: Partial fill rect `#E8A020` at 20% (representing coating level)
- Filter icon (small rect with cross-hatch): Label `FILTER (60-100 mesh)` -- Inter Medium, 11 pt, `#2EC4B6`

**Pump (center-bottom, X: 7.5", Y: 11.0"):**
- Small circle with directional arrow, fill `#3A4055`, border `#C8D0D8`
- Label: `PUMP` -- Barlow SemiBold, 12 pt, `#F0EDE8`

**Supply pipe (from pump upward to nozzle manifold):**
- Vertical line, stroke 3 pt `#E8A020`, with upward arrow

**Nozzle Manifold (top-center, X: 9.0", Y: 5.5", W: 8.0", H: 0.8"):**
- Horizontal rect, fill `#3A4055`, border `#C8D0D8`
- Label: `NOZZLE MANIFOLD` -- Barlow SemiBold, 13 pt, `#F0EDE8`
- 4-5 downward-pointing triangles below (nozzles)
- Label below nozzles: `1-5 gal/min per nozzle` -- JetBrains Mono, 11 pt, `#E8A020`

**Coating curtain (from nozzles downward):**
- Vertical wavy lines from each nozzle downward, stroke 2 pt `#E8A020` at 40%
- Label: `COATING FLOW` -- Inter Medium, 12 pt, `#E8A020`

**Part (center, suspended, X: 10.0", Y: 6.8", W: 4.0", H: 4.5"):**
- Irregular shape (rectangle with notch to suggest a real part), fill `#3A4055`, border 2 pt `#C8D0D8`
- Label: `PART` -- Barlow SemiBold, 16 pt, `#F0EDE8`
- Coating film on surface: thin `#E8A020` at 30% overlay on the left and top faces

**Drain Pan (below part, X: 8.0", Y: 12.0", W: 8.0", H: 0.8"):**
- Shallow rounded rect, fill `#252B3D`, border `#C8D0D8`
- Label: `DRAIN PAN` -- Barlow SemiBold, 12 pt, `#F0EDE8`

**Return line (from drain pan back to reservoir):**
- Curved line from drain pan back to reservoir, stroke 3 pt `#2EC4B6`, with arrow
- Label: `RETURN / RECIRCULATE` -- Inter Medium, 11 pt, `#2EC4B6`

**Key parameter callouts (right side of diagram):**

Callout 1 (X: 18.0", Y: 5.5"):
- Small rounded rect, fill `#252B3D`, W: 5.0", H: 1.2"
- `Viscosity: 15-40 sec (Zahn #2)` -- JetBrains Mono, 12 pt, `#E8A020`
- `Check hourly -- solvent evaporation drifts viscosity up` -- Inter Regular, 11 pt, `#F0EDE8` at 70%

Callout 2 (X: 18.0", Y: 7.2"):
- Same style
- `DFT: 0.5-3.0 mils` -- JetBrains Mono, 12 pt, `#E8A020`
- `Controlled by viscosity, flow rate, and drain time` -- Inter Regular, 11 pt, `#F0EDE8` at 70%

Callout 3 (X: 18.0", Y: 8.9"):
- Same style
- `Transfer efficiency: 90-95%` -- JetBrains Mono, 12 pt, `#27AE60`
- `Excess coating recirculated -- nearly zero waste` -- Inter Regular, 11 pt, `#F0EDE8` at 70%

---

### ZONE 4 -- Application Methods Table

**Section label:** `FLOW COATING METHODS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Methods Comparison Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Method (4.0") | Description (6.5") | DFT Range (3.0") | Best For (5.0") | Uniformity (4.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 1.2".

| Method | Description | DFT | Best For | Uniformity |
|---|---|---|---|---|
| Curtain Flow | Coating poured from a weir or slot die in a continuous curtain; part passes through on conveyor | 0.5-2.0 mils | Flat panels, sheet products, coil-like applications | +/- 20-30% (best for flow coat) |
| Flood / Flow | Nozzles flood coating over the part from above; gravity pulls coating down | 0.5-3.0 mils | Large 3D parts: tanks, enclosures, frames, structural steel | +/- 30-50% (moderate) |
| Dip-Drain (Hybrid) | Part immersed briefly, withdrawn, excess drains | 1.0-3.0 mils | Small-to-medium parts; overlap with dip coating | +/- 20-40% |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Method names: Inter Medium, 13 pt.

Footnote:
- `Flood/flow is the most common flow coating method for industrial steel fabrication. Curtain flow is used for flat stock. Dip-drain is the hybrid between flow coating and dip coating (Cluster 4).` -- Inter Regular, 12 pt, `#E8A020`

---

### ZONE 5 -- Viscosity and Recirculation Control

**Section label:** `VISCOSITY CONTROL -- THE #1 DAY-TO-DAY CHALLENGE` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Control Panel**

Y: 21.3" to 26.3".

**Left -- Viscosity Management (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `VISCOSITY DRIFT` -- Barlow SemiBold, 18 pt, `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
Problem: Solvent evaporates from the recirculation
tank during operation. Viscosity climbs.

Rate: 1-3 sec/hr Zahn #2 drift (typical open tank)

Measurement: Zahn #2 cup per ASTM D4212
  - Target: 15-40 sec (coating dependent)
  - Check: Every hour minimum
  - Correct: Add solvent per coating TDS

Rule: Never add reducer by "feel" -- always
measure viscosity before and after adjustment.
```

JetBrains Mono for parameter values; Inter Regular for explanatory text.

**Right -- Recirculation Best Practices (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `RECIRCULATION SYSTEM CARE` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Filter continuously: 60-100 mesh screen minimum`
- `Strain for cured skin and debris at every shift change`
- `Keep tank covered when not in use -- reduces solvent loss by 50%+`
- `Agitate or recirculate slowly during downtime to prevent skinning`
- `2K coatings: pot life applies to the ENTIRE reservoir volume -- plan batch size carefully`
- `Temperature: ambient preferred -- heat accelerates solvent loss and shortens pot life`

---

### ZONE 6 -- Common Application Failures

**Section label:** `WHAT GOES WRONG -- 4 APPLICATION FAILURES` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | THIN FILM / POOR COVERAGE | Viscosity too low or flow rate insufficient | Check Zahn cup; increase viscosity; increase nozzle flow |
| 2 | 6.33" | EXCESSIVE FILM / RUNS | Viscosity too high or drain time too short | Reduce viscosity; extend drain time; reposition part angle |
| 3 | 12.16" | HOLIDAYS (MISSED AREAS) | Shielded surfaces not reached by gravity flow | Reposition part; add nozzles; manual touch-up spray |
| 4 | 18.0" | CONTAMINATION IN FILM | Debris from unfiltered recirculation system | Clean filter; strain reservoir; check for cured skin |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

**Key insight callout (Y: 30.6" to 32.3"):**
- Full-width rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Text: `Viscosity is to flow coating what current density is to electroplating -- it is the single variable that controls film build, coverage, and appearance. Check it hourly. Adjust it carefully. Log it always.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Flow Application -- Flow Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Application Flow Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The system schematic is the hero -- it must communicate the entire flow coating concept in one image. Pump, nozzles, part, drain, return. The recirculation loop is what makes flow coating unique and what drives 90-95% transfer efficiency. The viscosity control panel is the practical takeaway -- this is what operators deal with every day. The analogy to current density in electroplating bridges back to the plating poster series for shop audiences who know both worlds.

---

*Alaina -- Poster #691 -- Construction Workup v1.0 -- 2026-04-26*
