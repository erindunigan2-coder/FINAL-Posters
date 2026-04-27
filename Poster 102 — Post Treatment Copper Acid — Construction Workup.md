---
Project: Plating Posters Inc
Poster Number: 102
Title: "Post Treatment -- Copper (Acid)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Post-treatment (anti-tarnish, decorative stack, dry) for acid copper sulfate line (Stage 7--8 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - CopperPlating
  - AcidCopper
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEP09
---

# Poster #102 -- Construction Workup
## Post Treatment -- Copper (Acid)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stages 7--8 of the acid copper process. Unlike zinc (where post-treatment is passivation), acid copper post-treatment depends entirely on the application. Decorative copper proceeds to nickel then chrome (the classic Cu-Ni-Cr stack). PCB copper proceeds to solder mask and etching. Standalone copper gets an anti-tarnish treatment. This poster covers all three pathways, with emphasis on the anti-tarnish chemistry and the decorative stack overview.

Hero visual: three application pathway cards (decorative, PCB, standalone) and an anti-tarnish treatment panel.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-pathway hero (Block B):** Three large cards showing decorative, PCB, and standalone copper pathways.
2. **Orientation strip (Block C):** Stages 7+8 highlighted.
3. **Anti-tarnish parameters (Block D).**
4. **The decorative stack diagram (Block E):** Cross-section showing Cu-Ni-Cr layer buildup.
5. **Problems and safety panels.**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stages 7+8 highlighted
ZONE 3 -- APPLICATION PATHWAYS HERO (4.2"--15.0")
ZONE 4 -- ANTI-TARNISH + DRY PARAMETERS (15.0"--21.5")
ZONE 5 -- DECORATIVE STACK DIAGRAM (21.5"--27.0")
ZONE 6 -- PROBLEMS + SAFETY (27.0"--32.5")
ZONE 7 -- FOOTER (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header

**Headline:** `POST TREATMENT` -- 76 pt `#F0EDE8`. Y: 0.5".
**Subheading:** `Copper (Acid) -- Anti-Tarnish, Stack, Dry -- Stages 7 & 8` -- 30 pt `#E8A020`. Y: 1.4".
**Tagline:** `Copper tarnishes in hours. What happens after the plate determines whether it stays bright -- or turns brown by Tuesday.` -- 20 pt at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 7 AND 8 both highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Bright copper deposit (no protection)  -->  After: Tarnish-protected, sealed, or ready for next layer`

---

### ZONE 3 -- Application Pathways Hero

**Section label:** `THREE PATHS AFTER ACID COPPER` -- Y: 4.4".

**BLOCK B -- Three Pathway Cards (Y: 5.0" to 14.5")**

Three tall cards side by side:

**Card 1 -- Decorative (X: 0.5", W: 7.33", H: 9.0"):**
- Rounded rect, fill `#1E2435`, border 2 pt `#27AE60`
- Left accent: `#27AE60`, 0.06"
- Title: `DECORATIVE` -- Barlow SemiBold 22 pt `#27AE60`
- Subtitle: `Cu + Ni + Cr Stack` -- Inter Medium 14 pt `#F0EDE8` at 60%

Body (Inter Regular 14 pt, line height 150%):
```
After acid copper:
  1. Rinse
  2. Nickel plate (5--25 um)
  3. Rinse
  4. Chrome plate (0.25--0.75 um)
  5. Rinse + Dry

No anti-tarnish needed --
copper goes directly to nickel.

The copper layer provides:
- Leveling over substrate defects
- Ductility (thermal cycling)
- Corrosion barrier under Ni
```

Application note: `Automotive trim, plumbing fixtures, hardware, consumer electronics` -- Inter Medium 12 pt `#27AE60`

**Card 2 -- PCB / Electronics (X: 8.17", W: 7.33", H: 9.0"):**
- Rounded rect, fill `#1E2435`, border 2 pt `#2EC4B6`
- Left accent: `#2EC4B6`
- Title: `PRINTED CIRCUITS` -- Barlow SemiBold 22 pt `#2EC4B6`
- Subtitle: `Through-Hole and Pattern Plating` -- Inter Medium 14 pt at 60%

Body:
```
After acid copper:
  1. Rinse
  2. Tin or tin-lead plate (etch resist)
  3. Strip photoresist
  4. Etch exposed copper
  5. Strip tin resist
  6. Solder mask + finishing

The copper fill provides:
- Barrel connection (through-holes)
- Trace buildup to spec thickness
- Conductor for circuit paths
```

Application note: `PCBs, flex circuits, RF shielding, semiconductor packaging` -- `#2EC4B6`

**Card 3 -- Standalone Copper (X: 15.83", W: 7.67", H: 9.0"):**
- Rounded rect, fill `#1E2435`, border 2 pt `#E8A020`
- Left accent: `#E8A020`
- Title: `STANDALONE` -- Barlow SemiBold 22 pt `#E8A020`
- Subtitle: `Anti-Tarnish Required` -- Inter Medium 14 pt at 60%

Body:
```
After acid copper:
  1. Rinse
  2. Anti-tarnish dip (15--60 sec)
  3. Rinse (gentle)
  4. Dry (forced air or oven)

The anti-tarnish provides:
- Thin inhibitor film (chromate or organic)
- Prevents Cu oxidation (tarnish)
- Maintains bright appearance

Without anti-tarnish:
- Copper tarnishes in hours
- Brown/green oxide in days
```

Application note: `Electroforming, EMI shielding, heatsinks, salvage/buildup` -- `#E8A020`

---

### ZONE 4 -- Anti-Tarnish + Dry Parameters

**Section label:** `ANTI-TARNISH & DRY PARAMETERS` -- Y: 15.2".

**Two side-by-side panels:**

**Left -- Anti-Tarnish (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, accent `#E8A020`
- Title: `ANTI-TARNISH TREATMENT` Barlow SemiBold 20 pt `#E8A020`

| Parameter | Value |
|---|---|
| Type | Chromate-based or organic inhibitor (benzotriazole type) |
| Temperature | Ambient (65--85 F) |
| Time | 15--60 sec immersion |
| pH | Varies by product (typically 2--4 for chromate) |
| Application | Immersion dip or spray |
| Function | Thin protective film prevents Cu oxidation |
| Rinse after | Gentle flowing rinse -- do not scrub off film |
| Shelf life | Chromate: weeks to months. Organic: days to weeks. |
| Note | Skip if proceeding directly to nickel or solder |

**Right -- Dry (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, accent `#2EC4B6`
- Title: `DRY` Barlow SemiBold 20 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Method | Forced air, oven, or centrifugal (barrel parts) |
| Temperature | Ambient to 150 F (66 C) -- do not overheat copper |
| Time | Until visually dry |
| Caution | Copper oxidizes faster when hot and wet |
| Best practice | Dry quickly -- minimize wet dwell time |
| Inspection | Check for tarnish, water spots, staining |
| Note | Barrel parts: centrifugal spin preferred over oven |

---

### ZONE 5 -- Decorative Stack Diagram

**Section label:** `THE DECORATIVE COPPER-NICKEL-CHROME STACK` -- Y: 21.7".

**BLOCK E -- Layer Cross-Section (Y: 22.3" to 26.8")**

A horizontal layer diagram showing a cross-section of the classic decorative plating stack. Built with stacked horizontal rectangles:

| Layer | Height (visual) | Fill | Label | Thickness |
|---|---|---|---|---|
| Substrate (steel or plastic) | Tallest (base) | `#3A4055` | `SUBSTRATE` | Bulk |
| Copper (from acid copper) | Medium | `#E8A020` at 60% | `COPPER` | 10--25 um (0.4--1.0 mil) |
| Semi-bright Nickel | Medium | `#C8D0D8` at 50% | `SEMI-BRIGHT Ni` | 15--20 um |
| Bright Nickel | Thinner | `#C8D0D8` at 80% | `BRIGHT Ni` | 10--15 um |
| Chrome | Thinnest | `#2EC4B6` at 40% | `CHROME` | 0.25--0.75 um |

Stacked from bottom (substrate) to top (chrome). X: 2.0", W: 20.0". Each layer is a rounded rect with labeled thickness on the right side.

Function labels on the left side of each layer:
- Substrate: `Base material`
- Copper: `Leveling + ductility + corrosion barrier`
- Semi-bright Ni: `Corrosion protection (columnar structure, active)`
- Bright Ni: `Brightness + hardness (layered structure, noble)`
- Chrome: `Wear resistance + appearance + final protection`

Bottom note: `The Cu layer makes or breaks decorative plating. It fills pits, levels defects, and provides the ductile base that lets the stack survive thermal cycling.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Problems + Safety

**Left -- Problems (X: 0.5", W: 14.0"):**

| Problem | Cause | Fix |
|---|---|---|
| Tarnish within hours | No anti-tarnish applied | Apply anti-tarnish immediately after rinse |
| Hazy anti-tarnish film | Over-immersion or contaminated bath | Reduce time; replace anti-tarnish bath |
| Water spots after dry | Hard water in final rinse | Use DI water; dry faster |
| Peeling at Cu-Ni interface | Surface tarnish before nickel | Minimize transfer time; keep parts wet |
| Green/brown corrosion | Anti-tarnish worn off; humidity exposure | Reapply anti-tarnish; improve packaging |

Problem: `#E05C5C`. Fix: `#27AE60`.

**Right -- Safety (X: 15.0", W: 8.5"):**
- Title: `SAFETY -- POST-TREATMENT` `#E8A020`
- `Anti-tarnish baths (chromate): acidic -- handle as acid`
- `Organic inhibitors (benzotriazole): mild irritant`
- `Copper sulfate on skin: wash immediately -- blue staining`
- `Oven drying: burn hazard -- gloves for part handling`
- `Copper dust (from dry barrel parts): respiratory hazard -- ventilation`
- `Copper in wastewater: regulated -- treat before discharge`

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- Copper (Acid)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table. **Export:** Six files -- `Post Treatment Copper Acid -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is unique in the series because acid copper post-treatment splits into three completely different pathways depending on application. The decorative stack diagram is the visual centerpiece for the shop audience -- almost every decorative plating line runs Cu-Ni-Cr, and the layer cross-section makes the purpose of each layer immediately visible. The "copper tarnishes in hours" message is the practical takeaway that every plater needs to internalize.

---

*Alaina -- Poster #102 -- Construction Workup v1.0 -- 2026-04-26*
