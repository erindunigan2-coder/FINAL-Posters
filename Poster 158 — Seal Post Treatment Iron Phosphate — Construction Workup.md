---
Project: Plating Posters Inc
Poster Number: 158
Title: "Seal / Post Treatment -- Iron Phosphate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-01 technical reference (iron phosphate conversion coating)"
Process Scope: Seal rinse, post-treatment, and dry-off oven for iron phosphate pretreatment (Stages 5--6)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IronPhosphate
  - SealRinse
  - PostTreatment
  - ConstructionWorkup
  - ClusterCC01
---

# Poster #158 -- Construction Workup
## Seal / Post Treatment -- Iron Phosphate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final stages: seal rinse and dry-off oven. The seal rinse fills micropores in the iron phosphate film and provides the corrosion resistance boost that the thin amorphous coating cannot deliver on its own. Legacy chrome seals (CrO3) are being replaced by non-chrome alternatives -- zirconium, silane, and organic polymer sealers. The dry-off oven must dry completely without degrading the phosphate film (stay below 400 F).

This poster covers the transition from legacy chrome to non-chrome sealers, DI water requirements, dry-off parameters, and the relevant specifications (TT-C-490, ASTM D2092, OEM specs).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Seal rinse mechanism hero (Block B -- HERO):** Visual showing the seal rinse filling micropores in the phosphate film.
2. **Chrome vs. non-chrome comparison (Block D):** Legacy vs. current sealer chemistry.
3. **Dry-off oven parameters (Block E):** Temperature limits and timing.
4. **Specifications reference (Block F):** Standards table.
5. **Common defects (Block G):** Post-treatment failures.

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
  Seal/dry stages highlighted (Emerald)
ZONE 3 -- SEAL RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CHROME vs. NON-CHROME (14.5"--20.5" / ~6.0")
ZONE 5 -- DRY-OFF OVEN + SPECIFICATIONS (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECTS + FINAL CHECKLIST (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SEAL / POST TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Iron Phosphate -- The Final Stages Before Paint` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The phosphate makes paint stick. The seal rinse makes the phosphate last. The oven makes it all dry. Skip any step and the paint fails in the field.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Seal/dry stages highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed iron phosphate coating  -->  After: Sealed, dried surface ready for paint or powder coat`

---

### ZONE 3 -- Seal Rinse Hero

**Section label:** `THE SEAL RINSE -- FILLING THE GAPS` -- Y: 4.4".

**BLOCK B -- Seal Mechanism Visual (Y: 5.0" to 10.0")**

Two large cross-section panels showing the phosphate film before and after sealing:

**Left -- Before Seal (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `BEFORE SEAL` Barlow SemiBold 18 pt `#E8A020`
- Visual: steel base layer + amorphous phosphate film layer with visible micropores (small gaps)
- Label on pores: `Micropores -- entry points for moisture and corrosion` Inter Regular 12 pt `#E05C5C`
- `Bare salt spray: 2--24 hours` JetBrains Mono 14 pt `#E05C5C`

**Right -- After Seal (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.5", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `AFTER SEAL` Barlow SemiBold 18 pt `#27AE60`
- Visual: steel base + phosphate film + seal layer filling all pores
- Label on seal: `Seal fills micropores and passivates exposed metal` Inter Regular 12 pt `#27AE60`
- `Sealed corrosion resistance: 2--5x improvement` JetBrains Mono 14 pt `#27AE60`

**BLOCK B2 -- Seal Parameters (Y: 10.5" to 14.0")**

Full-width parameter panel, rounded rect, fill `#1E2435`:

| Parameter | Non-Chrome Seal | Legacy Chrome Seal |
|---|---|---|
| Chemistry | Zr, silane, or organic polymer | 0.01--0.05% CrO3 |
| Concentration | 0.5--3.0% in DI water | Per supplier |
| Temperature | Ambient to 100 F (38 C) | Ambient to 100 F |
| pH | 3.5--5.5 | 1.5--3.0 |
| Time | 30 sec--2 min | 15--30 sec |
| DI water required? | YES (< 50 uS/cm) | YES |

Header: Barlow SemiBold 14 pt. Data: JetBrains Mono 12 pt.

---

### ZONE 4 -- Chrome vs. Non-Chrome

**Section label:** `THE CHROME TRANSITION` -- Y: 14.7".

**BLOCK D -- Comparison (Y: 15.3" to 20.3")**

**Left -- Legacy Chrome Seal (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `CHROME SEAL (LEGACY)` Barlow SemiBold 20 pt `#E05C5C`
- Badge: `BEING PHASED OUT` Barlow Condensed ExtraBold 12 pt, fill `#E05C5C`, text `#1A1F2E`

| Property | Value |
|---|---|
| Active chemistry | Hexavalent chromic acid (CrO3) |
| Mechanism | Cr(VI) passivates micropores in phosphate |
| Performance | Excellent -- 2--5x improvement in SST |
| Regulatory status | Restricted (REACH, RoHS, OSHA) |
| Health hazard | Cr(VI) is a known human carcinogen |
| Future | Replacement is mandatory for most industries |

**Right -- Non-Chrome Seal (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `NON-CHROME SEAL (CURRENT)` Barlow SemiBold 20 pt `#27AE60`
- Badge: `INDUSTRY STANDARD` Barlow Condensed ExtraBold 12 pt, fill `#27AE60`, text `#1A1F2E`

| Property | Value |
|---|---|
| Options | Zr-based, silane/siloxane, organic polymer |
| Mechanism | Nano-oxide or polymer fills micropores |
| Performance | Good to excellent (approaches chrome in many systems) |
| Regulatory status | Compliant with REACH, RoHS |
| Health hazard | Minimal compared to chrome |
| Future | Continuing improvement; fully replacing chrome |

Bottom banner (full width):
- Rounded rect, fill `#27AE60` at 10%, border 1 pt `#27AE60`, radius 999 pt
- `If your spec does not explicitly require chrome seal, use non-chrome. The performance gap has closed.` Inter Medium 14 pt `#27AE60`

---

### ZONE 5 -- Dry-Off Oven + Specifications

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Dry-Off Oven (X: 0.5", W: 11.0"):**

Section label: `DRY-OFF OVEN` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#E8A020` 0.06".

| Parameter | Value |
|---|---|
| Temperature | 250--350 F (121--177 C) |
| Time | 5--15 min (substrate dependent) |
| Maximum | DO NOT EXCEED 400 F (204 C) |

Key points:
- `Parts must dry completely before paint -- moisture under paint = blistering and adhesion failure.` Inter Regular 14 pt `#F0EDE8`
- `Some non-chrome sealers are designed as the last wet stage -- no final DI rinse needed after seal.` Inter Regular 13 pt `#F0EDE8` at 70%
- `Spot-free drying is critical for appearance-sensitive parts.` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Specifications (X: 12.0", W: 11.5"):**

Section label: `APPLICABLE STANDARDS` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#2EC4B6` 0.06".

| Standard | Scope |
|---|---|
| TT-C-490 | Fed spec -- chemical conversion coatings on ferrous metals |
| ASTM D2092 | Guide for preparation of zinc-coated/galvanized steel for painting |
| GM / Ford / Chrysler | OEM phosphate pretreatment specs (vary by plant) |
| Caterpillar / John Deere | Heavy equipment OEM specs |

Note: `OEM specs vary widely. Always confirm the specific pretreatment specification for your customer before establishing process parameters.` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 6 -- Defects + Final Checklist

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Post-Treatment Defects (X: 0.5", W: 11.0"):**

Section label: `POST-TREATMENT FAILURES` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| Defect | Cause | Fix |
|---|---|---|
| Water spots after dry | Contaminated rinse; hard water; dirty seal | Use DI water; clean seal bath |
| Paint blistering | Moisture not fully removed; oven temp too low | Increase oven time/temp; verify dryness |
| Seal not adhering | Contaminated post-coat rinse; wrong pH | Clean rinse tank; check seal pH |
| Coating degraded | Oven > 400 F; excessive time | Reduce oven temp; check thermocouple |

**Right -- Pre-Paint Checklist (X: 12.0", W: 11.5"):**

Section label: `READY FOR PAINT?` Barlow Condensed ExtraBold 22 pt `#27AE60`.

Six-item checklist:

| Check | Target |
|---|---|
| Coating weight | 40--60 mg/ft2 |
| Coating appearance | Iridescent blue/gold -- uniform |
| Surface feel | Smooth, non-powdery |
| Dry to touch | Completely dry, no moisture |
| No flash rust | No orange/brown staining |
| No water spots | Clean, spot-free surface |

Pass indicator: `#27AE60` checkmark. Each item: Inter Medium 14 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Seal / Post Treatment -- Iron Phosphate`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Products Finishing; TT-C-490; ASTM D2092. Non-chrome seal technology is rapidly evolving -- consult your supplier for latest formulations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Seal Post Treatment Iron Phosphate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chrome-to-non-chrome transition is the most timely content on this poster. Many shops are still running legacy chrome seals because "they work." This poster provides the technical rationale for switching and the reassurance that non-chrome performance has closed the gap. The before/after seal visual is the hook -- showing micropores filled is more persuasive than any spec sheet.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #158 -- Construction Workup v1.0*
*2026-04-26*
