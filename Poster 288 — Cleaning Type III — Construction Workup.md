---
Project: Plating Posters Inc
Poster Number: 288
Title: "Cleaning -- Hardcoat Anodizing (Type III)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 2, Section 2.2)"
Process Scope: Alkaline cleaning for hardcoat anodizing -- Stage 1 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeIII
  - Hardcoat
  - Cleaning
  - ConstructionWorkup
  - ClusterAnodize02
---

# Poster #288 -- Construction Workup
## Cleaning -- Hardcoat Anodizing (Type III)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for hardcoat is the same alkaline soak as Type II, but the stakes are higher. At 24--36 ASF and near-freezing temperatures, any contamination nucleates burning at the defect site. A fingerprint that would cause a faint shadow on Type II becomes a white powdery burn mark on Type III. Ultrasonic cleaning is specified for critical aerospace parts. The concept hook: same cleaner, but the consequences of failure are amplified by the extreme operating conditions downstream.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank cross-section hero (Block B):** Tank with immersion parts, air agitation lines, temperature indicator, and labeled cleaner components. Same visual language as Poster 296 but with hardcoat-specific callouts.
2. **Contamination amplification panel (Block D):** Side-by-side showing same defect on Type II (minor) vs. Type III (catastrophic).
3. **Water-break test callout (Block E):** Same visual as Poster 296.
4. **Defect grid (Block F):** 6 cleaning-related failure modes specific to hardcoat consequences.
5. **Ultrasonic cleaning callout (Block G):** When and why ultrasonic pre-clean is specified.

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
ZONE 4 -- CONTAMINATION AMPLIFICATION + WATER BREAK TEST (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- ULTRASONIC + HARDCOAT-SPECIFIC RULES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hardcoat Anodizing (Type III) -- Stage 1 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Same cleaner as Type II -- but at 24--36 ASF, every fingerprint becomes a burn mark. Clean like the coating depends on it. Because it does.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Stages labeled: `1. Clean` | `2. Rinse` | `3. Etch` | `4. Desmut` | `5. Rinse` | `6. Hard Anodize` | `7. Rinse` | `8. Seal`

Below: `Before: As-received part with oils, soils, shop contamination  -->  After: Clean, water-break-free surface ready for etch or direct desmut`

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
- Label: `Air agitation (mild to moderate)` Inter Regular 11 pt `#F0EDE8` at 60%

**Heater symbol (left side):**
- Zigzag line element, X: 2.5", Y: 9.0"
- Label: `Immersion heater` Inter Regular 11 pt

**Bath parameter labels (right side, X: 15.5", Y: 7.0"):**
- `Non-etch alkaline soak cleaner` JetBrains Mono 14 pt `#2EC4B6`
- `4--8 oz/gal (30--60 g/L)` JetBrains Mono 14 pt `#F0EDE8`
- `130--160 F (55--70 C)` JetBrains Mono 14 pt `#E8A020`
- `Soak: 3--10 min (rack)` JetBrains Mono 13 pt `#F0EDE8`
- `Soak: 2--5 min (barrel)` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `pH: 9--11` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Key restriction callout (bottom, Y: 13.0"):**
- Rounded rect, W: 20.0", H: 0.8", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Text: `NEVER use silicated cleaners before anodizing -- silicate deposits are invisible but block oxide growth` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Contamination Amplification + Water Break Test

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Contamination Amplification (X: 0.5", W: 13.0"):**

Section label: `WHY CLEANING IS MORE CRITICAL FOR TYPE III` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#E8A020`:

| Contamination | Effect on Type II (12--18 ASF) | Effect on Type III (24--36 ASF) |
|---|---|---|
| Fingerprint | Faint shadow in coating | White burn mark -- coating dissolved at defect |
| Oil film | Thin spot, cosmetic defect | Bare spot with aggressive burning around edges |
| Silicate deposit | Skip anodizing, bare patch | No oxide growth; adjacent area over-anodizes and burns |
| Embedded particle | Minor inclusion | Delamination under thick, stressed coating |

Header: Barlow SemiBold 12 pt `#F0EDE8` on `#3A4055`. Data: Inter Regular 12 pt, alternating rows.

Below table: `High current density concentrates at any discontinuity. What Type II tolerates, Type III punishes.` Inter Medium 13 pt `#E8A020`.

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
| R1C1 | BURNING AT DEFECT SITES | `#E05C5C` | Organic residue concentrates current at defect | Re-clean; ultrasonic for critical parts |
| R1C2 | SKIP ANODIZING | `#E05C5C` | Silicate deposit from wrong cleaner | Replace cleaner with non-silicated; strip and re-process |
| R1C3 | DELAMINATION | `#E05C5C` | Embedded particles under thick oxide | Solvent pre-clean; ultrasonic; inspect before anodize |
| R2C1 | POWDERY COATING (localized) | `#E8A020` | Partial oil film causes local overheating | Extend soak time; increase temperature; verify agitation |
| R2C2 | STREAKING | `#E8A020` | Inadequate rinsing after clean | Improve cascade rinse; check water quality |
| R2C3 | NON-UNIFORM COLOR | `#2EC4B6` | Uneven soil removal across part surface | Improve agitation; verify cleaner concentration |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- Ultrasonic + Hardcoat-Specific Rules

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Hardcoat Cleaning Rules (X: 0.5", W: 11.0"):**

Section label: `TYPE III CLEANING -- THE EXTRA RULES` Barlow Condensed ExtraBold 22 pt.

Callout box, fill `#1E2435`, left accent `#E8A020`:
- `1. Same non-etch alkaline cleaner as Type II -- no special chemistry` Inter Medium 14 pt `#F0EDE8`
- `2. Extend soak time for heavily soiled parts (machining oils, coolants)` Inter Medium 14 pt `#F0EDE8`
- `3. Solvent pre-clean for buffing/polishing compounds` Inter Regular 13 pt `#F0EDE8` at 80%
- `4. Ultrasonic cleaning for precision aerospace/hydraulic parts` Inter Regular 13 pt `#F0EDE8` at 80%
- `5. Water-break test is MANDATORY before proceeding` Inter Regular 13 pt `#F0EDE8` at 80%
- `6. Any drag-over from cleaner dilutes the low-concentration anodize bath` Inter Regular 13 pt `#E8A020`

**Right -- Ultrasonic Cleaning (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`:

Title: `WHEN TO ADD ULTRASONIC` Barlow SemiBold 18 pt `#2EC4B6`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Ultrasonic cleaning uses high-frequency sound waves (20--40 kHz) to create cavitation bubbles that dislodge contaminants from surface features.`
- ``
- `WHEN TO USE:`
- `-- Blind holes, recesses, and complex geometries`
- `-- Parts with embedded buffing compound`
- `-- Aerospace parts per AMS 2469 or customer spec`
- `-- Any part where water-break test fails after soak clean`
- ``
- `Parameters: 25--40 kHz, 130--150 F, 3--10 min`
- `Use AFTER alkaline soak clean, not as a replacement`

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Hardcoat Anodizing (Type III)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical industry values. Specific cleaning procedures vary by facility and specification. Consult your process supplier and applicable spec for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (same as Poster 279).
**Export:** Six files -- `Cleaning Type III -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The key differentiator from Poster 296 (Type I Cleaning) is the contamination amplification message. Type I's cleaning poster focuses on thin-coating sensitivity and Cr(VI) safety context. Type III's cleaning poster focuses on high-current-density amplification -- the same contaminant that Type II shrugs off becomes catastrophic at 24--36 ASF. The ultrasonic callout is unique to this poster. The water-break test visual is reused from the Type I and Type II cleaning posters because it is universally applicable and the single most useful shop-floor diagnostic.

---

*Alaina -- Plating Posters Inc*
*Poster #288 -- Construction Workup v1.0*
*2026-04-26*
