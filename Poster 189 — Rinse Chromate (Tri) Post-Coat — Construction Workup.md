---
Project: Plating Posters Inc
Poster Number: 189
Title: "Rinse -- Chromate (Tri) -- Post-Coat"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-05 Section 5.7)"
Technical Source: Post-coat rinse for trivalent chromate conversion coating on aluminum. Removes residual coating solution. Coating is more robust than fresh hex but still requires careful handling. Stage 6 of 7.
Process Scope: Post-coat rinse -- Stage 6 of trivalent chromate conversion on aluminum
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - TrivalentChromate
  - Rinse
  - PostCoat
  - ConstructionWorkup
  - ClusterCC05
---

# Poster #189 -- Construction Workup
## Rinse -- Chromate (Tri) -- Post-Coat

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 7. The post-coat rinse removes residual trivalent chromate solution from the freshly coated surface. Compared to hex chromate post-coat rinse, this is slightly less delicate -- tri coatings are more mechanically robust than fresh hex gel. However, the film is ultra-thin (0.02--0.10 um) and must still be handled with care.

Hero visual: a gentle rinse operation with labeled parameters and a "handling window" callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse operation hero (Block B):** Single or double rinse tank with gentle immersion of coated aluminum parts, water quality labels, and handling caution notes.
2. **Tri vs. Hex post-coat handling comparison (Block D):** What you can and cannot do with a freshly coated tri part vs. hex.
3. **Water quality panel (Block E):** DI water preference and why.
4. **Failure mode strip (Block F):** 4 post-coat rinse problems.

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
  Stage 6 highlighted (Teal)
ZONE 3 -- POST-COAT RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- HANDLING COMPARISON + WATER QUALITY (14.5"--20.5" / ~6.0")
ZONE 5 -- OPERATING PARAMETERS TABLE (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Trivalent Chromate on Aluminum -- Post-Coat -- Stage 6 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The coating is on. Now rinse off what is not part of the film -- gently. DI water preferred.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly coated aluminum with residual chromate solution  -->  After: Clean coated surface ready for air dry`

---

### ZONE 3 -- Post-Coat Rinse Hero

**Section label:** `THE POST-COAT RINSE` -- Y: 4.4".

**BLOCK B -- Rinse Operation**

Y: 5.0" to 14.0".

**Rinse tank:**
- Rounded rect, X: 3.0", Y: 5.5", W: 18.0", H: 6.5"
- Fill: `#252B3D` (rinse water)
- Border: 2 pt `#C8D0D8`
- Label above: `POST-COAT RINSE` Barlow SemiBold 16 pt `#2EC4B6`

**Coated workpiece (center):**
- Vertical rect, X: 10.0", Y: 6.0", W: 4.0", H: 5.0"
- Fill: `#C8D0D8` at 30% (aluminum)
- Thin overlay layer on surface: 2 pt `#27AE60` (representing the tri chromate film)
- Border: 2 pt `#C8D0D8`
- Label: `COATED ALUMINUM` Barlow SemiBold 14 pt `#27AE60`
- Sub-label: `0.02--0.10 um Cr3+/Zr mixed oxide film` JetBrains Mono 11 pt `#F0EDE8` at 60%

**Water parameters (inside tank):**
Right side:
- `Ambient to 100 F (38 C)` JetBrains Mono 14 pt `#F0EDE8`
- `15--60 sec immersion` JetBrains Mono 14 pt `#F0EDE8`
- `DI water final rinse preferred` JetBrains Mono 13 pt `#27AE60`

Left side:
- `Gentle -- no aggressive spray` Inter Medium 13 pt `#E8A020`
- `Film is ultra-thin but more robust than fresh hex` Inter Regular 13 pt `#F0EDE8` at 70%

**Handling caution banner (below tank, Y: 12.5"):**
- Rounded rect, X: 3.0", W: 18.0", H: 1.0", fill `#E8A020` at 10%, border 1 pt `#E8A020`
- `HANDLE WITH CARE: The coating is thin but durable once cured (24 hr). First few hours are the most vulnerable.`
- Inter Medium 14 pt `#E8A020`

**Bottom callout (Y: 13.8"):**
- `Tri coatings tolerate warm water rinse better than hex. Hex must be cold-water-only to protect Cr6+ content.`
- Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Handling Comparison + Water Quality

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Tri vs. Hex Post-Coat Handling (X: 0.5", W: 11.0"):**

Section label: `POST-COAT HANDLING: TRI VS. HEX` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

Comparison table (Y: 15.3" to 19.5"):

| Handling Factor | Trivalent (Tri) | Hexavalent (Hex) |
|---|---|---|
| Rinse temperature | Ambient to 100 F OK | Cold only (< 77 F / 25 C) |
| Rinse duration | 15--60 sec | 15--30 sec |
| Agitation tolerance | Mild agitation OK | Minimal -- gel is soft |
| Touch/handle after | Handle carefully 2--4 hr | NO touch for 24 hr minimum |
| Full cure time | 24 hr ambient | 24--72 hr ambient |
| DI water needed? | Preferred (aerospace required) | Preferred (aerospace required) |

Tri column header: `#27AE60`. Hex column header: `#E05C5C`.
Data: JetBrains Mono 12 pt. Alternating rows.

**Right -- Water Quality (X: 12.0", W: 11.5"):**

Section label: `WATER QUALITY MATTERS` Barlow Condensed ExtraBold 22 pt `#2EC4B6`. Y: 14.7".

Callout box: Rounded rect, H: 4.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Content (Inter Regular 14 pt `#F0EDE8`, line height 165%):

- `Tri chromate film is ULTRA-THIN (0.02--0.10 um)`
- `Any mineral deposit from hard water is VISIBLE through the film`
- `DI water (< 50 uS/cm) eliminates water spotting`
- `Aerospace specs (NADCAP) require DI or RO final rinse`

Water quality targets:

| Parameter | Target |
|---|---|
| Conductivity | < 50 uS/cm (DI) |
| pH | 6.0--8.0 |
| Chloride | < 10 ppm |
| TDS | < 25 ppm |

Data: JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 5 -- Operating Parameters Table

**Section label:** `OPERATING PARAMETERS` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 20.7".

**Parameter table (Y: 21.3" to 26.3"):**

| Parameter | Value | Notes |
|---|---|---|
| Rinse stages | 1--2 (DI final rinse standard) | Double rinse for aerospace |
| Water type | DI or RO (final stage) | Tap water acceptable for first stage only |
| Temperature | Ambient to 100 F (38 C) | Warmer than hex is acceptable |
| Time | 15--60 sec immersion | Brief is fine -- coating is set |
| Agitation | Mild -- no aggressive spray | Ultra-thin film can be mechanically disturbed |
| pH | 6.0--8.0 (neutral) | Should be neutral after proper rinse |
| Handling after rinse | Careful for 2--4 hr; full cure 24 hr | Rack/hang to dry; avoid stacking |

Data: JetBrains Mono 12 pt. Alternating rows.

---

### ZONE 6 -- Failure Modes

**Section label:** `WHAT GOES WRONG -- 4 POST-COAT RINSE FAILURES` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 26.7".

**4-card row (Y: 27.3" to 32.3"):**

| Card | X | Problem | Cause | Effect |
|---|---|---|---|---|
| 1 | 0.5" | WATER SPOTS | Hard water rinse; no DI; poor drainage | Visible marks on finished part |
| 2 | 6.33" | COATING DAMAGE | Aggressive spray or mechanical contact | Film removed or thinned at contact points |
| 3 | 12.16" | RESIDUAL CHROMATE | Insufficient rinse; low flow rate | Staining; uneven appearance |
| 4 | 18.0" | HANDLING MARKS | Touching before cure; stacking too soon | Permanent fingerprints or abrasion marks |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Effect: Inter Medium, 13 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Chromate (Trivalent) -- Post-Coat`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Chromate Tri Post-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The key differentiator for this rinse poster: tri is slightly more forgiving than hex at this stage (warmer rinse OK, less fragile gel), but the ultra-thin film means water quality matters MORE for appearance. The handling comparison table gives a quick "what changed?" reference for shops transitioning from hex to tri.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #189 -- Construction Workup v1.0*
*2026-04-26*
