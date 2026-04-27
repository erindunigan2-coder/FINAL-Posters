---
Project: Plating Posters Inc
Poster Number: 689
Title: "Rinse / Dry -- Flow Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 5: Flow Coating, Section 5.4)"
Process Scope: Rinse and dry for flow coating -- Stage 3 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FlowCoating
  - Rinse
  - ConstructionWorkup
  - PaintingCoating
  - ClusterFC
---

# Poster #689 -- Construction Workup
## Rinse / Dry -- Flow Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 7. Rinse removes cleaner residue; drying eliminates every trace of moisture. Trapped water in a recess is a time bomb -- it blisters under the coating during cure, and on a flow coat line those blisters show up on part after part because the recirculated coating carries the contamination forward. Complete drying is not optional.

Hero visual: cross-section diagram showing trapped moisture in a part recess blisterng under a cured coating film.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Blister cross-section hero (Block B):** Stylized cross-section showing a part recess with trapped water vapor pushing up through the coating, forming a blister dome. Built with layered rectangles, arc shapes, and labeled callouts.
2. **Rinse quality table (Block D):** Parameters for DI rinse, city water rinse, and conductivity targets.
3. **Drying methods comparison (Block E):** Side-by-side comparison of forced air, oven dry, and air knife methods.
4. **Defect strip (Block F):** 4 common rinse/dry failures.

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
  Stage 3 highlighted (Teal)
ZONE 3 -- BLISTER CROSS-SECTION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE QUALITY TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- DRYING METHODS COMPARISON (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON RINSE/DRY FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE / DRY` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flow Coating -- Stage 3 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Trapped water in a recess is a blister waiting to happen. Dry it completely or pay for it in rework.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned surface with cleaner residue and standing water  -->  After: Residue-free, bone-dry surface ready for pretreatment`

---

### ZONE 3 -- Blister Cross-Section Hero

**Section label:** `WHAT HAPPENS WHEN MOISTURE IS TRAPPED` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Blister Formation Cross-Section**

Y: 5.0" to 14.0".

**Full-width diagram panel (X: 0.5", W: 23.0", H: 8.5"):**
- Fill: `#1E2435`, radius 8

**Left half -- BEFORE CURE (X: 1.0", W: 10.5"):**
- Title: `BEFORE CURE` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Substrate: Large rect (`#3A4055`) representing metal with an L-shaped recess cut into it
- Water droplet: Small ellipse in the recess, fill `#2EC4B6` at 40%
- Label: `Trapped moisture in recess` -- Inter Medium, 12 pt, `#2EC4B6`
- Coating layer: Thin strip above substrate, fill `#E8A020` at 30%
- Label: `Wet flow coat film` -- Inter Medium, 12 pt, `#E8A020`

**Arrow between halves:** 3 pt `#3A4055`, right-pointing, label `CURE OVEN` Barlow SemiBold 12 pt `#E05C5C`

**Right half -- AFTER CURE (X: 12.5", W: 10.5"):**
- Title: `AFTER CURE` -- Barlow SemiBold, 18 pt, `#E05C5C`
- Same substrate with recess
- Blister dome: Arc shape rising above the coating surface, fill `#E05C5C` at 20%, stroke 2 pt `#E05C5C`
- Steam arrows: Small upward arrows from the recess, `#2EC4B6` at 60%
- Label: `Water vaporizes -- pushes coating up` -- Inter Medium, 12 pt, `#E05C5C`
- Label: `Blister / delamination` -- Inter Medium, 13 pt, `#E05C5C`

**Callout boxes flanking the diagram:**

Left callout (X: 1.0", Y: 12.0", W: 10.5", H: 1.8"):
- Fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `WHY FLOW COAT IS WORSE` -- Barlow SemiBold, 14 pt, `#E05C5C`
- Body: `Flow coating fills recesses by design -- coating flows into channels and pockets. But so does rinse water. Any area the coating reaches, water reached first.` -- Inter Regular, 13 pt, `#F0EDE8`

Right callout (X: 12.5", Y: 12.0", W: 10.5", H: 1.8"):
- Fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `PREVENTION` -- Barlow SemiBold, 14 pt, `#27AE60`
- Body: `Forced-air blow-off + oven dry. Check recesses by hand. If you can feel moisture, the part is not ready. Tilt parts to drain standing water from channels.` -- Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 4 -- Rinse Quality Table

**Section label:** `RINSE QUALITY PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Rinse Parameters Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Rinse Stage (4.5") | Water Source (4.0") | Conductivity Target (4.5") | Temperature (3.0") | Purpose (7.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.8".

| Rinse Stage | Water Source | Conductivity | Temp | Purpose |
|---|---|---|---|---|
| Post-Clean Rinse | City water | < 500 uS/cm | Ambient | Remove bulk cleaner residue |
| Post-Clean Rinse (if pretreatment follows) | DI preferred | < 200 uS/cm | Ambient | Prevent cleaner drag-in to pretreatment |
| Final Rinse (before dry) | DI water | < 50 uS/cm | Ambient | Eliminate salt deposits that cause osmotic blistering |
| Counterflow Design | Fresh water enters last stage | Per stage target | Ambient | Conserve water; progressive quality improvement |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

Footnote:
- `Conductivity over target? Dump and recharge -- do not dilute. High TDS rinse water deposits invisible salts that cause blistering under the coating.` -- Inter Regular, 12 pt, `#E8A020`

---

### ZONE 5 -- Drying Methods Comparison

**Section label:** `DRYING METHODS -- GET IT BONE DRY` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Three-Column Comparison**

Y: 21.3" to 26.3". Three callout boxes side by side.

**Column 1 -- Forced Air Blow-Off (X: 0.5", W: 7.33", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `FORCED AIR` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Properties (Inter Regular 13 pt `#F0EDE8`, line height 155%):
  - Method: `Compressed air nozzles or blowers`
  - Temperature: `Ambient`
  - Time: `Until no visible water`
  - Best For: `Removing standing water from recesses`
  - Limitation: `Cannot remove absorbed moisture`
  - Key Check: `Air supply must be oil-free (ASTM D4285 blotter test)`

**Column 2 -- Oven Dry (X: 8.33", W: 7.33", H: 4.8"):**
- Same style, left accent `#E8A020`
- Title: `OVEN DRY` -- Barlow SemiBold, 18 pt, `#E8A020`
- Properties:
  - Method: `Convection or IR oven`
  - Temperature: `200-250 F (93-121 C)`
  - Time: `10-15 min at metal temp`
  - Best For: `Complete moisture elimination`
  - Limitation: `Energy cost; heavy parts need longer soak`
  - Key Check: `Part must cool before coating (hot parts = uneven film)`

**Column 3 -- Air Knife (X: 16.16", W: 7.33", H: 4.8"):**
- Same style, left accent `#27AE60`
- Title: `AIR KNIFE` -- Barlow SemiBold, 18 pt, `#27AE60`
- Properties:
  - Method: `High-velocity laminar air curtain`
  - Temperature: `Ambient or heated (120-160 F)`
  - Time: `Continuous at line speed`
  - Best For: `In-line continuous flow coat lines`
  - Limitation: `May not reach deep recesses`
  - Key Check: `Combine with forced air for complex parts`

Labels: Inter Medium 12 pt `#F0EDE8` at 60%. Values: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Common Rinse/Dry Failures

**Section label:** `WHAT GOES WRONG -- 4 RINSE / DRY FAILURES` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | BLISTERING IN RECESSES | Trapped moisture vaporizing under coating during cure | Forced air + oven dry; tilt parts to drain |
| 2 | 6.33" | SALT DEPOSITS / WHITE SPOTS | High-TDS rinse water evaporating on surface | Use DI water for final rinse; target < 50 uS/cm |
| 3 | 12.16" | OSMOTIC BLISTERING (FIELD) | Soluble salts from rinse water trapped under coating | Monitor rinse conductivity; counterflow design |
| 4 | 18.0" | CLEANER RESIDUE | Insufficient rinse volume or contact time | Add rinse stage; increase spray pressure; verify water break |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

**Key insight callout (Y: 30.6" to 32.3"):**
- Full-width rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Text: `The most dangerous moisture is the moisture you cannot see. Standing water is obvious -- but absorbed moisture in porous substrates or trapped water in blind holes only reveals itself as blisters after curing. When in doubt, oven dry.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse / Dry -- Flow Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Flow Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The blister cross-section hero tells a story in two frames: before and after the oven. It should make the viewer instinctively check their parts for moisture. The rinse quality table gives inspectors something concrete to measure (conductivity numbers), and the drying methods comparison helps shops pick the right approach for their setup. The recirculation angle from Poster #688 carries forward -- flow coating amplifies every upstream failure.

---

*Alaina -- Poster #689 -- Construction Workup v1.0 -- 2026-04-26*
