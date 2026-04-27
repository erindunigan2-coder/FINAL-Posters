---
Project: Plating Posters Inc
Poster Number: 190
Title: "Drying / Post Treatment -- Chromate (Tri)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-05 Section 5.8)"
Technical Source: Air drying, sealer application, and post-treatment for trivalent chromate conversion coating on aluminum. Supplementary sealers are more important for tri than hex because no self-healing. Stage 7 of 7.
Process Scope: Drying and post-treatment -- Stage 7 of trivalent chromate conversion on aluminum
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - TrivalentChromate
  - Drying
  - PostTreatment
  - ConstructionWorkup
  - ClusterCC05
---

# Poster #190 -- Construction Workup
## Drying / Post Treatment -- Chromate (Tri)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 7. The final stage: air drying and optional sealer application. Trivalent coatings lack the self-healing property of hex chromate, so supplementary sealers (silane/siloxane, Zr-based, organic polymer) are significantly more important. Some tri coatings tolerate mild heat (up to 150 F), unlike hex which must never be heated above 140 F.

Hero visual: a drying/curing timeline showing the 24-hour cure progression, sealer options, and paint application window.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cure timeline hero (Block B):** Horizontal timeline from 0 to 72 hours showing coating hardness progression, handling windows, and paint application deadlines.
2. **Sealer options panel (Block D):** Three sealer types with when/why to use each.
3. **"No Self-Healing -- Sealers Compensate" callout (Block E):** Why sealers matter more for tri.
4. **Standards and specs reference (Block F):** MIL-DTL-5541F Type II, AMS 2487, NADCAP.
5. **Failure mode strip (Block G):** 4 drying/post-treatment failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 19.5" / 25.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Amber)
ZONE 3 -- CURE TIMELINE HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- SEALER OPTIONS + "NO SELF-HEALING" (14.0"--19.5" / ~5.5")
ZONE 5 -- SPECIFICATIONS + PAINT WINDOW (19.5"--25.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS (25.5"--32.5" / ~7.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DRY / POST-TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Trivalent Chromate on Aluminum -- Stage 7 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Air dry. Seal if needed. No self-healing means the sealer is your safety net. Paint within 72 hours.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed, freshly coated aluminum  -->  After: Cured, sealed conversion coating (or ready for paint)`

---

### ZONE 3 -- Cure Timeline Hero

**Section label:** `THE CURE TIMELINE -- FROM WET TO DONE` -- Y: 4.4".

**BLOCK B -- Horizontal Timeline**

Y: 5.0" to 13.5".

**Timeline bar:**
- Rounded rect, X: 0.5", Y: 7.5", W: 23.0", H: 0.6", fill `#3A4055`
- Gradient from `#E8A020` (left, 0 hr) to `#27AE60` (right, 72 hr)

**Time markers (evenly spaced along bar):**

| Time | Y Above | Label | Status Color | Description |
|---|---|---|---|---|
| 0 hr | 5.5" | `IMMERSION COMPLETE` | `#E8A020` | Wet coating; begin air dry |
| 1 hr | 5.5" | `SURFACE DRY` | `#E8A020` | Dry to touch; still soft |
| 4 hr | 5.5" | `HANDLE WITH CARE` | `#E8A020` | Can rack/transfer; avoid rubbing |
| 24 hr | 5.5" | `FULL CURE` | `#27AE60` | Full hardness; sealer may be applied |
| 72 hr | 5.5" | `PAINT DEADLINE` | `#E05C5C` | Paint must be applied by now (most specs) |

Each marker: vertical line from bar up to label. Labels: Barlow SemiBold 14 pt in status color. Description: Inter Regular 12 pt `#F0EDE8` at 70%.

**Below timeline -- Drying method options (Y: 9.0" to 12.5"):**

Three side-by-side boxes:

| Method | X | W | Accent | Details |
|---|---|---|---|---|
| Ambient Air Dry | 0.5" | 7.33" | `#27AE60` | Preferred. Room temp, clean air. Forced air OK. Full cure 24 hr. |
| Mild Heat (Tri Only) | 8.0" | 7.33" | `#E8A020` | Some tri coatings tolerate up to 150 F (66 C). Check supplier TDS. Not all formulations allow this. |
| NEVER: Oven Dry > 160 F | 15.5" | 8.0" | `#E05C5C` | Hex chromate degrades above 140 F. Some tri coatings also degrade at high temp. When in doubt, air dry. |

Each box: Rounded rect, H: 3.0", fill `#1E2435`, left accent 0.06".
Method name: Barlow SemiBold 16 pt in accent color. Details: Inter Regular 13 pt `#F0EDE8`.

**Bottom callout (Y: 13.0"):**
- `Key advantage of tri over hex: tri coatings are inherently more thermally stable because there is no Cr6+ to decompose. But "more stable" is not "indestructible" -- respect the supplier's max temp.`
- Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Sealer Options + "No Self-Healing"

**Two-column layout (Y: 14.2" to 19.3"):**

**Left -- Sealer Options (X: 0.5", W: 12.0"):**

Section label: `SUPPLEMENTARY SEALERS` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.2".

Three sealer callout boxes (Y: 14.8" to 19.0"):

| Sealer Type | Accent | Mechanism | Performance |
|---|---|---|---|
| Silane/Siloxane | `#2EC4B6` | Hydrophobic organic barrier; bonds to oxide surface | Most common; extends bare SST from 168 to 500+ hr |
| Zirconium-Based | `#27AE60` | Inorganic oxide topcoat over chromate film | Good chemical resistance; aerospace-qualified |
| Organic Polymer | `#E8A020` | Waterborne or solvent-borne polymer topcoat | Additional barrier; may affect paint adhesion if painted over |

Each box: Rounded rect, H: 1.3", fill `#1E2435`, left accent 0.06".

Note below: `Sealer is OPTIONAL per MIL-DTL-5541 -- but strongly recommended for tri coatings, especially in harsh service environments.` Inter Medium 13 pt `#E8A020`.

**Right -- "No Self-Healing -- Sealers Compensate" (X: 13.0", W: 10.5"):**

Section label: `NO SELF-HEALING` Barlow Condensed ExtraBold 22 pt `#E05C5C`. Y: 14.2".

Callout box: Rounded rect, H: 4.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Content (Inter Regular 14 pt `#F0EDE8`, line height 165%):

- `Hex chromate self-heals: Cr6+ leaches from the film to repassivate scratches and damage`
- `Tri chromate CANNOT self-heal: once the barrier is breached, corrosion starts`
- `Sealers fill this gap -- they add a second protective layer over the chromate film`
- `A sealed tri coating can match or exceed hex performance in many environments`

Key stat:
- `168 hr --> 500+ hr` Barlow Condensed ExtraBold 36 pt `#27AE60`
- `bare salt spray improvement with silane sealer` Inter Medium 13 pt `#F0EDE8` at 70%

---

### ZONE 5 -- Specifications + Paint Window

**Two-column layout (Y: 19.7" to 25.3"):**

**Left -- Standards Reference (X: 0.5", W: 11.0"):**

Section label: `APPLICABLE STANDARDS` Barlow Condensed ExtraBold 22 pt `#2EC4B6`. Y: 19.7".

| Standard | Description |
|---|---|
| MIL-DTL-5541F, Type II | Trivalent chromate conversion on aluminum |
| Class 1A | Corrosion protection (168 hr SST minimum) |
| Class 3 | Low electrical resistance |
| AMS 2487 | Trivalent chromium conversion coating |
| SAE ARP 6584 | Trivalent chromium process qualification |
| ASTM B921 | Non-hex conversion coatings on aluminum |
| NADCAP AC7108 | Aerospace chemical processing accreditation |
| ASTM B117 | Salt spray test method |

Data: JetBrains Mono 12 pt `#F0EDE8`. Standard code: `#2EC4B6`. Alternating rows.

**Right -- Paint Application Window (X: 12.0", W: 11.5"):**

Section label: `PAINT APPLICATION WINDOW` Barlow Condensed ExtraBold 22 pt `#E8A020`. Y: 19.7".

Callout box: Rounded rect, H: 5.0", fill `#1E2435`, left accent 0.06" `#E8A020`.

Content:
- `Apply paint within 72 hours of coating (most aerospace specs)` Barlow SemiBold 16 pt `#E8A020`
- `Tri chromate is an excellent paint base -- comparable to hex for most paint systems` Inter Regular 14 pt `#F0EDE8`
- `Primer must be qualified over trivalent chem film (not just hex)` Inter Medium 13 pt `#E05C5C`
- `Some specs allow 7--14 days if stored properly (clean, dry, controlled environment)` Inter Regular 13 pt `#F0EDE8` at 70%

Paint prep checklist:
- `Surface must be dry (24 hr cure minimum)`
- `No handling marks or contamination`
- `Store in clean, low-humidity environment`
- `Document coating-to-paint interval`
Inter Regular 13 pt `#F0EDE8`, with `#27AE60` check marks.

---

### ZONE 6 -- Defect Diagnosis

**Section label:** `WHAT GOES WRONG -- 4 POST-TREATMENT FAILURES` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 25.7".

**4-card row (Y: 26.3" to 32.3"):**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | COATING DEGRADATION | Over-temperature drying (> 160 F) | Air dry only; check supplier TDS for max temp |
| 2 | 6.33" | POOR PAINT ADHESION | Paint applied > 72 hr; wrong primer; contaminated surface | Paint within window; qualify primer over tri |
| 3 | 12.16" | PREMATURE CORROSION | No sealer; scratch damage with no self-healing | Add sealer; improve handling procedures |
| 4 | 18.0" | HANDLING MARKS | Parts stacked or touched before full cure | 24 hr cure before handling; use clean gloves |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Drying / Post Treatment -- Chromate (Trivalent)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Drying Post Treatment Chromate Tri -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The cure timeline is the hero -- it gives operators a clear visual of when they can handle, seal, and paint. The "No Self-Healing" callout with the 168 --> 500+ hr stat makes the sealer argument quantitative. The paint application window section addresses the aerospace workflow where chromate coating and primer application are separate operations with a documented time gap.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #190 -- Construction Workup v1.0*
*2026-04-26*
