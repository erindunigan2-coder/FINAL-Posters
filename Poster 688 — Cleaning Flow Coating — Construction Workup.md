---
Project: Plating Posters Inc
Poster Number: 688
Title: "Cleaning -- Flow Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 5: Flow Coating, Section 5.3)"
Process Scope: Cleaning for flow coating -- Stage 2 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FlowCoating
  - Cleaning
  - ConstructionWorkup
  - PaintingCoating
  - ClusterFC
---

# Poster #688 -- Construction Workup
## Cleaning -- Flow Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 7. Cleaning for flow coating is straightforward but non-negotiable -- solvent wipe or alkaline wash, verified by the water break test. Flow coating is a thin-film system with recirculation, so any residual oil that gets into the coating reservoir contaminates every part that follows. Clean once, coat thousands -- or contaminate once, ruin thousands.

Hero visual: water break test comparison -- clean surface (unbroken sheet of water) vs. contaminated surface (water beading/breaking).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Water break test hero (Block B):** Two side-by-side panels showing water behavior on clean vs. dirty surfaces. Built with rounded rectangles, gradient fills, and droplet shapes.
2. **Cleaning methods table (Block D):** 4-row comparison table (solvent wipe, alkaline wash, spray washer, vapor degrease).
3. **Contamination consequence callout (Block E):** Large warning panel showing how oil in the recirculation system amplifies contamination.
4. **Defect strip (Block F):** 4 common cleaning failures.

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
  Stage 2 highlighted (Teal)
ZONE 3 -- WATER BREAK TEST HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING METHODS TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- RECIRCULATION CONTAMINATION WARNING (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON CLEANING FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flow Coating -- Stage 2 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `One drop of oil in the recirculation tank contaminates every part on the line. Clean it right or coat it wrong.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Seven mini-boxes representing the 7-stage process. Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. All others dimmed: fill `#252B3D`, text `#F0EDE8` at 40%.

Below: `Before: Blasted / prepped surface with oils, soils, grinding dust  -->  After: Water-break-free surface ready for rinse and pretreatment`

Inter Regular, 13 pt, `#F0EDE8` at 70%.

---

### ZONE 3 -- Water Break Test Hero

**Section label:** `THE WATER BREAK TEST -- YOUR GO / NO-GO CHECK` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Water Break Test Comparison**

Y: 5.0" to 14.0". Two large panels side by side.

**Left panel -- CLEAN (X: 0.5", W: 11.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Badge: `PASS` -- rounded rect 1.4" x 0.4", fill `#27AE60`, text `#1A1F2E` Barlow Condensed ExtraBold 14 pt
- Title: `Water-Break-Free Surface` -- Barlow SemiBold, 20 pt, `#27AE60`
- Visual description: Large rounded rect representing metal surface (`#3A4055`), with a smooth continuous water film overlay (`#2EC4B6` at 15%) covering the entire surface uniformly
- Label: `Unbroken sheet of water -- no beading, no breaks` -- Inter Medium, 14 pt, `#F0EDE8`
- Standard ref: `ASTM F22 -- Water Break Test` -- JetBrains Mono Regular, 12 pt, `#2EC4B6`
- Explanation: `Surface tension of clean metal holds a continuous water film. Any contamination disrupts the surface energy and causes the film to break.` -- Inter Regular, 13 pt, `#F0EDE8` at 70%

**Right panel -- CONTAMINATED (X: 12.0", W: 11.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E05C5C`
- Badge: `FAIL` -- rounded rect 1.4" x 0.4", fill `#E05C5C`, text `#F0EDE8` Barlow Condensed ExtraBold 14 pt
- Title: `Water Breaks on Surface` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Visual description: Same metal surface rect, but water shown as scattered irregular droplets/spots (`#2EC4B6` at 20%) with gaps between them
- Label: `Water beads and pulls away -- oil or contamination present` -- Inter Medium, 14 pt, `#F0EDE8`
- Warning: `DO NOT PROCEED -- re-clean and retest` -- Inter Medium, 13 pt, `#E05C5C`
- Explanation: `Even fingerprint-level oil contamination (< 1 mg/ft2) causes water breaks. In a flow coat system, this oil transfers to the recirculation tank.` -- Inter Regular, 13 pt, `#F0EDE8` at 70%

---

### ZONE 4 -- Cleaning Methods Table

**Section label:** `CLEANING METHODS FOR FLOW COATING` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- 4-Row Comparison Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Method (4.0") | Chemistry (5.0") | Temperature (3.0") | Time (2.5") | Best For (4.5") | Verification (4.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".

| Method | Chemistry | Temp | Time | Best For | Verification |
|---|---|---|---|---|---|
| Solvent Wipe | Acetone, MEK, IPA | Ambient | 2-rag method | Job shop / small batch | Water break test |
| Alkaline Wash | pH 10-12, 2-5% conc. | 130-160 F | 2-5 min | Batch immersion | Water break test |
| Multi-Stage Spray Washer | Alkaline spray + rinse | 120-150 F | 60-120 sec/stage | Continuous flow coat lines | Conductivity < 200 uS/cm |
| Vapor Degrease | TCE or nPB vapor | Boiling point | Until condensation stops | Heavy oil loads | Visual + water break |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Method names: Inter Medium, 13 pt.

Footnote below table:
- `Two-rag method: wet rag dissolves contamination, dry rag removes it before solvent evaporates and redeposits the contamination.` -- Inter Regular, 12 pt, `#E8A020`

---

### ZONE 5 -- Recirculation Contamination Warning

**Section label:** `WHY CLEANING MATTERS MORE FOR FLOW COATING` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Contamination Amplification Panel**

Y: 21.3" to 26.3".

**Large callout box (X: 0.5", W: 23.0", H: 4.8"):**
- Fill `#1E2435`, left accent 0.06" `#E05C5C`
- Title: `THE RECIRCULATION PROBLEM` -- Barlow SemiBold, 22 pt, `#E05C5C`

**Three-step contamination chain (horizontal, evenly spaced within the box):**

Step 1 (X: 1.0", W: 6.5"):
- Mini rounded rect, fill `#252B3D`, H: 2.8"
- Badge: `1` circle, fill `#E05C5C`, 0.4" diameter
- Title: `Oil on One Part` -- Barlow SemiBold, 14 pt, `#F0EDE8`
- Body: `Residual oil from incomplete cleaning -- as little as 1 mg/ft2` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

Arrow: 3 pt `#3A4055`, right-pointing, between steps.

Step 2 (X: 8.5", W: 6.5"):
- Same style
- Badge: `2`
- Title: `Oil Enters Reservoir` -- Barlow SemiBold, 14 pt, `#F0EDE8`
- Body: `Excess coating drains back carrying dissolved oil. Oil accumulates with every contaminated part.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

Arrow: right-pointing.

Step 3 (X: 16.0", W: 6.5"):
- Same style
- Badge: `3`
- Title: `Every Part Contaminated` -- Barlow SemiBold, 14 pt, `#E05C5C`
- Body: `Recirculated coating now carries oil to every subsequent part. Fish-eyes, adhesion loss, and cratering across the entire run.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

**Bottom insight strip:**
- Rounded rect, W: 22.0", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `In spray painting, one dirty part affects one part. In flow coating, one dirty part contaminates the entire reservoir.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 6 -- Common Cleaning Failures

**Section label:** `WHAT GOES WRONG -- 4 CLEANING FAILURES` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | FISH-EYES IN COATING | Silicone or oil contamination | Strain reservoir; re-clean all parts; check compressed air for oil |
| 2 | 6.33" | ADHESION LOSS (FIELD) | Incomplete oil removal before prime | Water break test every batch; switch to alkaline wash |
| 3 | 12.16" | COATING REJECTION | Solvent residue from single-rag wipe | Use two-rag method; wet then dry |
| 4 | 18.0" | SILICATE RESIDUE | High-silicate alkaline cleaner | Use silicate-free formulation for flow coat lines |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

**Key insight callout (Y: 30.6" to 32.3"):**
- Full-width rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Text: `The water break test (ASTM F22) is the single most important in-process check for flow coating cleaning. If water breaks on the surface, the part is not clean -- period. No exceptions, no shortcuts.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Flow Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Flow Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Cleaning is the most underrated step on a flow coat line. The recirculation system is both the greatest efficiency advantage and the greatest contamination risk. The hero visual makes this viscerally clear: pass or fail, there is no middle ground. The contamination chain in Zone 5 is the money shot -- it shows why flow coating amplifies cleaning failures in a way that spray painting does not.

---

*Alaina -- Poster #688 -- Construction Workup v1.0 -- 2026-04-26*
