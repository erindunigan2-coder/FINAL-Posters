---
Project: Plating Posters Inc
Poster Number: 296
Title: "Cleaning -- Chromic Acid Anodizing (Type I)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 3, Section 3.2)"
Process Scope: Alkaline cleaning for chromic acid anodizing -- Stage 1 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - ChromicAcid
  - TypeI
  - Cleaning
  - ConstructionWorkup
  - ClusterAnodize03
---

# Poster #296 -- Construction Workup
## Cleaning -- Chromic Acid Anodizing (Type I)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for Type I has stricter requirements than other anodize types because the thin chromic acid coating (0.5--2.5 um) amplifies every surface contaminant. No silicates. No chlorides in the cleaner. Any organic residue becomes a bare spot the thin oxide cannot hide.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank cross-section hero (Block B):** Tank with immersion parts, air agitation lines, temperature indicator, and labeled cleaner components.
2. **Contaminant impact panel (Block D):** Three-column table -- contaminant, source, effect on Type I coating.
3. **Water-break test callout (Block E):** Visual showing water sheeting vs. beading on a part surface.
4. **Defect grid (Block F):** 6 cleaning-related failure modes.
5. **Cr(VI) safety reminder strip:** Small coral banner in footer zone.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINANT IMPACT + WATER BREAK TEST (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- TYPE I SPECIFIC REQUIREMENTS + SAFETY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromic Acid Anodizing (Type I) -- Stage 1 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `No silicates. No chlorides. Every contaminant you leave behind becomes a defect the thin Type I coating cannot hide.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Cr(VI) flag (right):** Same as Poster 295 -- `CONTAINS Cr(VI) -- CARCINOGEN` coral badge.

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-received part with oils, soils, shop contamination  -->  After: Clean, water-break-free surface ready for etch or desmut`

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE CLEANING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 13.5".

**Tank body:**
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 7.0"
- Fill: `#252B3D` (cleaner solution)
- Border: 3 pt `#C8D0D8`

**Parts on rack (center):**
- 3 vertical rects representing aluminum parts on a plating rack, X: 9.5"--14.5", Y: 6.5", H: 4.5"
- Fill: `#C8D0D8` at 40%, border 1 pt `#C8D0D8`
- Label: `ALUMINUM PARTS` Barlow SemiBold 13 pt `#C8D0D8`

**Air agitation (bottom of tank):**
- Dashed horizontal line at Y: 11.8"
- Small circles (bubbles) rising from line
- Label: `Air agitation (mild)` Inter Regular 11 pt `#F0EDE8` at 60%

**Heater symbol (left side):**
- Zigzag line element, X: 2.5", Y: 9.0"
- Label: `Immersion heater` Inter Regular 11 pt

**Bath parameter labels (right side, X: 15.5", Y: 7.0"):**
- `Non-silicated alkaline cleaner` JetBrains Mono 14 pt `#2EC4B6`
- `4--8 oz/gal (30--60 g/L)` JetBrains Mono 14 pt `#F0EDE8`
- `130--160 F (55--70 C)` JetBrains Mono 14 pt `#E8A020`
- `Soak: 3--10 min` JetBrains Mono 13 pt `#F0EDE8`
- `Spray: 1--3 min` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `pH: 9--12` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Key restriction callout (bottom, Y: 13.0"):**
- Rounded rect, W: 20.0", H: 0.8", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Text: `NEVER use silicated cleaners before anodizing -- silicate deposits are invisible but block oxide growth` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Contaminant Impact + Water Break Test

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Contaminant Impact Table (X: 0.5", W: 13.0"):**

Section label: `WHAT CONTAMINATION DOES TO TYPE I` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

| Contaminant | Source | Effect on Type I Coating |
|---|---|---|
| Silicates | Silicated cleaners | Invisible barrier -- bare spots, skip anodizing |
| Oils/grease | Machining, fingerprints | Bare spots, thin areas, poor dye (if used) |
| Chlorides | Tap water, cleaner residue | Pitting in chromic acid bath (< 10 ppm limit) |
| Buffing compound | Mechanical polishing | Embedded particles, orange peel |
| Drawing lubricant | Forming operations | Heavy organic load, requires solvent pre-clean |
| Shop soil | General handling | Uneven coating appearance |

Header: Barlow SemiBold 13 pt `#F0EDE8` on `#3A4055`. Data: Inter Regular 12 pt, alternating rows.

**Right -- Water Break Test (X: 14.0", W: 9.5"):**

Section label: `THE WATER BREAK TEST` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Visual: Two rounded rects representing aluminum panels side by side.

Left panel (PASS):
- Label: `PASS` Barlow SemiBold 16 pt `#27AE60`
- Fill: `#27AE60` at 10%
- Caption: `Continuous water film -- no beading. Surface is clean.` Inter Regular 13 pt `#27AE60`

Right panel (FAIL):
- Label: `FAIL` Barlow SemiBold 16 pt `#E05C5C`
- Fill: `#E05C5C` at 10%
- Small circles on surface (water droplets)
- Caption: `Water beads or breaks apart. Organic residue remains. Re-clean.` Inter Regular 13 pt `#E05C5C`

Below both: `Rinse the part and observe. A continuous, unbroken water film means the surface is free of organic contamination.` Inter Medium 13 pt `#F0EDE8` at 70%.

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 CLEANING FAILURES` -- Y: 20.7".

**BLOCK F -- 3x2 Grid**

Y: 21.3" to 26.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BARE SPOTS | `#E05C5C` | Organic residue left on surface | Re-clean; solvent pre-clean for heavy soil |
| R1C2 | SKIP ANODIZING | `#E05C5C` | Silicate deposit from wrong cleaner | Replace cleaner with non-silicated; re-process |
| R1C3 | STREAKING | `#E8A020` | Inadequate rinsing after clean | Improve cascade rinse; check water quality |
| R2C1 | PITTING (post-anodize) | `#E05C5C` | Chloride from cleaner or rinse water | Switch to Cl-free cleaner; use DI rinse |
| R2C2 | ORANGE PEEL | `#E8A020` | Embedded buffing compound | Add solvent pre-clean step |
| R2C3 | THIN AREAS | `#2EC4B6` | Partial organic film | Extend soak time; increase temperature |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- Type I Specific Requirements + Safety

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Type I Cleaning Rules (X: 0.5", W: 11.0"):**

Section label: `TYPE I CLEANING -- THE EXTRA RULES` Barlow Condensed ExtraBold 22 pt.

Callout box, fill `#1E2435`, left accent `#E8A020`:
- `1. Absolutely no silicated cleaners` Inter Medium 14 pt `#F0EDE8`
- `2. No chloride-containing cleaners` Inter Medium 14 pt `#F0EDE8`
- `3. Buffing compound may require solvent pre-clean` Inter Regular 13 pt `#F0EDE8` at 80%
- `4. Cleaner must be fully rinsed -- ANY drag-over contaminates the chromic acid bath` Inter Regular 13 pt `#F0EDE8` at 80%
- `5. For aerospace parts: cleaning per BAC 5763 or equivalent process spec` Inter Regular 13 pt `#F0EDE8` at 80%
- `6. Strongly alkaline cleaners (pH > 12) attack aluminum -- inhibitors are essential` Inter Regular 13 pt `#E8A020`

**Right -- Cr(VI) Process Reminder (X: 12.0", W: 11.5"):**

Coral-tinted callout, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`:
- Title: `Cr(VI) PROCESS REMINDER` Barlow SemiBold 18 pt `#E05C5C`
- `This cleaning stage prepares parts for a chromic acid (Cr6+) anodize bath.`
- `All downstream stages involve hexavalent chromium.`
- `Ensure Cr(VI) engineering controls and PPE are in place before parts enter the anodize tank.`
- `OSHA PEL: 0.005 mg/m3 | Medical surveillance required`

Inter Regular 13 pt `#F0EDE8`, line height 155%.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Chromic Acid Anodizing (Type I)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical industry values. Specific cleaning procedures vary by facility and specification. Chromic acid anodizing involves Cr(VI) -- a confirmed carcinogen. Consult your facility's EHS program.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (same as Poster 295).
**Export:** Six files -- `Cleaning Type I -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The key message: cleaning for Type I is cleaning for ANY anodize process, but with tighter restrictions. The thin coating amplifies every contamination defect. The water-break test visual is the single most useful diagnostic on this poster -- a shop operator can perform it in 5 seconds. The Cr(VI) reminder on a cleaning poster may seem premature, but it sets the safety context for the entire cluster.

---

*Alaina -- Plating Posters Inc*
*Poster #296 -- Construction Workup v1.0*
*2026-04-26*
