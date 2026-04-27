---
Project: Plating Posters Inc
Poster Number: 699
Title: "Application -- Coil Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating, Section 6.6)"
Process Scope: Application (reverse roll coater) for coil coating -- Stages 6 and 8 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - Application
  - RollCoater
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #699 -- Construction Workup
## Application -- Coil Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stages 6 and 8 of 9 -- prime coat and finish coat, both applied by the same method: the reverse roll coater. This is the heart of a coil coating line. A pickup roll lifts coating from a reservoir, transfers it to an applicator roll, and the applicator roll presses it onto the moving strip -- rotating in the opposite direction to strip travel. That reverse action produces the smoothest, most uniform film in all of industrial painting. Primer at 0.15-0.30 mil. Topcoat at 0.60-1.0 mil. Applied at 200-700 ft/min. The coating chemistry families (polyester, SMP, PVDF, polyurethane) each serve a different durability tier, from 15-year economy to 40-year premium.

Hero visual: reverse roll coater mechanical diagram showing pickup roll, applicator roll, and strip with rotation arrows indicating the reverse relationship, plus a coating chemistry comparison table.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Reverse roll coater diagram (Block B):** Cross-section showing three rolls (pickup, applicator, backup) and the strip, with rotation arrows and labeled film transfer.
2. **Roll coater parameters table (Block D):** Primer vs. finish coat specifications.
3. **Coating chemistry comparison (Block E):** Six chemistry families with DFT, flexibility, and weathering performance.
4. **Defect strip (Block F):** 4 application defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stages 6 + 8 highlighted (Amber)
ZONE 3 -- REVERSE ROLL COATER HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ROLL COATER PARAMETERS (14.5"--21.0" / ~6.5")
ZONE 5 -- COATING CHEMISTRY FAMILIES (21.0"--27.5" / ~6.5")
ZONE 6 -- APPLICATION DEFECTS (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `APPLICATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Coil Coating -- Stages 6 + 8: Prime Coat & Finish Coat` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The reverse roll coater. Pickup, transfer, apply -- all while the strip flies past at 400 ft/min. The roll speed ratio and nip pressure determine whether you get a smooth film or a warranty claim.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 6 and 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed. Two badges illuminated on the flow strip.
Below: `Before: Pretreated strip, dry and warm  -->  After: Primed and topcoated strip entering cure ovens`

---

### ZONE 3 -- Reverse Roll Coater Hero

**Section label:** `THE REVERSE ROLL COATER -- HOW IT WORKS` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Mechanical Diagram (Y: 5.0" to 14.0")**

Full-width rounded rect, W: 23.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#E8A020`.

Cross-section diagram (centered, Y: 5.5" to 12.5"):

Three circles representing rolls in a vertical stack:

**Top -- Backup Roll (Y: 5.8"):**
- Circle, diameter ~2.0", fill `#3A4055`, border `#C8D0D8`
- Label: `BACKUP ROLL` Barlow SemiBold 13 pt `#F0EDE8`
- Rotation arrow: clockwise (same as strip direction)
- Note: `Controls nip pressure against applicator`

**Middle -- Applicator Roll (Y: 8.0"):**
- Circle, diameter ~2.5", fill `#E8A020` at 30%, border `#E8A020`
- Label: `APPLICATOR ROLL` Barlow SemiBold 14 pt `#E8A020`
- Rotation arrow: COUNTER-CLOCKWISE (REVERSE to strip travel)
- Big highlight: `REVERSE ROTATION` JetBrains Mono 12 pt `#E8A020`
- Note: `Rotates OPPOSITE to strip travel`

**Bottom -- Pickup Roll (Y: 10.5"):**
- Circle, diameter ~2.0", fill `#2EC4B6` at 30%, border `#2EC4B6`
- Label: `PICKUP ROLL` Barlow SemiBold 13 pt `#2EC4B6`
- Rotation arrow: clockwise
- Note: `Picks up coating from reservoir`

**Coating Reservoir (below pickup roll, Y: 12.0"):**
- Rounded rect trough shape, fill `#E8A020` at 15%, border `#E8A020`
- Label: `COATING RESERVOIR` JetBrains Mono 11 pt `#F0EDE8`

**Strip (horizontal line between backup and applicator, Y: 6.8"):**
- Line, `#C8D0D8`, 3 pt weight
- Arrow: `STRIP TRAVEL -->` right-pointing
- Film thickness callout on the exit side: `WET FILM: 0.3-2.0 mil` JetBrains Mono 12 pt `#27AE60`

**Film transfer annotations:**
- Arrow from reservoir to pickup: `1. PICKUP` `#2EC4B6`
- Arrow from pickup to applicator: `2. TRANSFER` `#E8A020`
- Arrow from applicator to strip: `3. APPLY (REVERSE)` `#E8A020`

Right side callout (X: 17.0", Y: 6.0", W: 6.0"):
- Rounded rect, fill `#252B3D`, border `#E8A020`
- Title: `WHY REVERSE?` Barlow SemiBold 14 pt `#E8A020`
- Body: `The applicator roll rotates opposite to strip travel. This shearing action produces an extremely smooth, uniform film with minimal orange peel. Forward roll (same direction) produces rougher, less uniform films.` Inter Regular 12 pt `#F0EDE8`

Roll speed callout (Y: 13.0"):
- `Roll speed ratio (applicator:strip) = 1.05-1.25:1` JetBrains Mono 14 pt `#E8A020`
- `Higher ratio = thinner, smoother film  |  Lower ratio = thicker film` Inter Regular 12 pt `#F0EDE8`

---

### ZONE 4 -- Roll Coater Parameters

**Section label:** `PRIMER vs. FINISH COAT PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Comparison Table**

Y: 15.3" to 20.8". Column widths (23.0" total):
- Parameter (5.0") | Primer Coat (Stage 6) (8.5") | Finish Coat (Stage 8) (9.5")

| Parameter | Primer Coat (Stage 6) | Finish Coat (Stage 8) |
|---|---|---|
| Target DFT | 0.15-0.30 mil (4-8 microns) | 0.60-1.0 mil (15-25 microns) |
| Wet film thickness | 0.3-0.6 mil | 1.0-2.0 mil |
| Roll speed ratio (applicator:strip) | 1.05-1.25:1 | 1.05-1.25:1 |
| Roll pressure (nip) | 20-100 pli (pounds per linear inch) | 20-100 pli |
| Coating viscosity | 40-80 sec (Zahn #2) | 30-60 sec (Zahn #2) |
| Line speed | 200-700 ft/min | 200-700 ft/min |
| Purpose | Adhesion to conversion coating; corrosion barrier | Color, gloss, weathering, UV protection |
| Typical chemistry | Epoxy primer | Polyester, SMP, PVDF, or polyurethane |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

Footnote: `Nip pressure and roll speed ratio are the two primary controls for DFT. Viscosity is the secondary control. Adjust these three to hit target thickness.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 5 -- Coating Chemistry Families

**Section label:** `COATING CHEMISTRIES -- FROM ECONOMY TO PREMIUM` -- Y: 21.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Six-Row Chemistry Table**

Y: 21.8" to 27.3". Column widths (23.0" total):
- Chemistry (4.5") | DFT (2.5") | Flexibility (T-bend) (3.0") | Weathering (3.5") | Typical Use (9.5")

| Chemistry | DFT | Flexibility | Weathering | Typical Use |
|---|---|---|---|---|
| Polyester | 0.7-1.0 mil | Good (0-2T) | 15-25 years | Building panels, general industrial |
| Silicone-Modified Polyester (SMP) | 0.7-1.0 mil | Good | 25-30 years | Premium architectural, extended warranty |
| PVDF (Kynar 500) | 0.8-1.2 mil | Very good | 30-40 years | Premium architectural, color retention |
| Polyurethane | 0.7-1.0 mil | Excellent | Very good | Appliance housings, automotive trim |
| Epoxy primer (back coat) | 0.15-0.25 mil | Good | Interior only | Back-side protection, can liner |
| Plastisol (PVC) | 4-8 mils | Excellent | Moderate | Heavy-gauge roofing, rain goods |

Data: JetBrains Mono 11 pt. Chemistry names: Inter Medium 13 pt.

**T-Bend Explanation Callout (Y: 26.5"):**
- Pill, fill `#252B3D`, W: 23.0", H: 0.6"
- Text: `T-Bend (ASTM D4145): coated panel bent 180 deg. 0T = flat on itself (tightest). 1T = one metal thickness in the bend. The coating must survive this bend without cracking after forming.` Inter Regular 12 pt `#2EC4B6`

---

### ZONE 6 -- Application Defects

**Section label:** `WHAT GOES WRONG -- 4 APPLICATION DEFECTS` -- Y: 27.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 28.3" to 31.0")**

Each card: Rounded rect, W: 5.5", H: 2.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DFT VARIATION ACROSS WIDTH | Uneven nip pressure or roll deflection | Check roll alignment; adjust nip pressure profile across width |
| 2 | 6.33" | CHATTER MARKS (RIBBING) | Roll speed ratio too high or roll surface defect | Reduce roll speed ratio; inspect and re-grind roll surface |
| 3 | 12.16" | THIN EDGES | Edge effect from roll pressure profile | Adjust nip pressure at edges; check roll crown |
| 4 | 18.0" | VISCOSITY DRIFT | Temperature change in reservoir or solvent evaporation | Monitor viscosity continuously (Zahn cup); add solvent to target |

**Key insight callout (Y: 31.3" to 32.3"):**
- Text: `The reverse roll coater produces the most uniform thin film in industrial painting. But uniformity depends on three things you control: nip pressure, roll speed ratio, and viscosity. Change any one without adjusting the others and the film goes out of spec.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Application -- Coil Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Application Coil Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The reverse roll coater diagram is the centerpiece of this poster and arguably the most important mechanical diagram in the entire coil coating cluster. Three circles, three arrows, one strip -- but the relationship between rotation directions is the key insight. The "WHY REVERSE?" callout box answers the question everyone asks. The coating chemistry table in Zone 5 gives the coil coater a one-glance durability ladder from polyester (15 yr) to PVDF (40 yr). The T-bend callout grounds the flexibility column in a test the audience knows.

---

*Alaina -- Poster #699 -- Construction Workup v1.0 -- 2026-04-26*
