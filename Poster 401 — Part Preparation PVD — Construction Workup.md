---
Project: Plating Posters Inc
Poster Number: 401
Title: "Part Preparation -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Section 1.4)"
Technical Source: PVD substrate preparation including material compatibility, temperature limitations, edge preparation, masking, and surface condition requirements.
Process Scope: PVD part preparation (Stage 1 of 10)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PVD
  - PartPreparation
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #401 -- Construction Workup
## Part Preparation -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 10. Before anything touches the vacuum chamber, the substrate must be verified for material compatibility, temperature tolerance, edge condition, and masking requirements. This poster covers the critical "go/no-go" decisions that happen at the incoming inspection bench -- before cleaning even begins.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate compatibility matrix (Block B -- HERO):** Table showing substrate materials vs. max PVD temperature and compatible coatings.
2. **Temperature limitation chart (Block D):** Visual bar chart showing substrate max temps vs. coating deposition temps.
3. **Edge preparation callout (Block E):** Before/after edge honing visual with parameters.
4. **Incoming inspection checklist (Block F):** Go/no-go checklist for parts entering PVD.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal -- preparation)
ZONE 3 -- SUBSTRATE COMPATIBILITY MATRIX / HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- TEMPERATURE LIMITATION CHART (15.0"--21.0" / ~6.0")
ZONE 5 -- EDGE PREPARATION (21.0"--27.0" / ~6.0")
ZONE 6 -- INCOMING INSPECTION CHECKLIST (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PVD -- Stage 1 of 10 -- Substrate Verification and Incoming Inspection` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The coating is only as good as the substrate beneath it. Wrong material, wrong temperature, wrong edge -- the coating fails before it starts.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw incoming parts --> After: Verified, prepped, and approved for cleaning`

---

### ZONE 3 -- Substrate Compatibility Matrix (HERO)

**Section label:** `SUBSTRATE COMPATIBILITY -- WHAT CAN BE PVD COATED?` -- Y: 4.4".

**BLOCK B -- Matrix Table (Y: 5.0" to 14.8")**

Wide table spanning full width. 8 rows of substrate materials.

Header: Barlow SemiBold 14 pt `#F0EDE8`, fill `#3A4055`.
Columns: Substrate (4.0") | Max Temp (2.5") | TiN (2.0") | TiAlN (2.0") | CrN (2.0") | DLC (2.0") | Notes (8.5")

| Substrate | Max Temp | TiN | TiAlN | CrN | DLC | Notes |
|---|---|---|---|---|---|---|
| Cemented carbide (WC-Co) | 500 C | YES | YES | YES | YES | Primary PVD substrate -- no temperature issues |
| HSS (M2, M42) | < 550 C | YES | YES | YES | YES | Must stay below tempering temp; verify grade |
| Tool steel (H13, D2) | < 520 C | YES | YES | YES | YES | Pre-hardened; do not exceed temper |
| Stainless steel (300 series) | 500 C | YES | YES | YES | YES | Austenitic SS -- good candidate |
| Titanium alloys (Ti-6Al-4V) | < 500 C | YES | LIMITED | YES | YES | Avoid TiAlN above 450 C on some alloys |
| Aluminum alloys | < 200 C | NO | NO | NO | LIMITED | Severe temp limitation -- only low-temp DLC possible |
| Copper alloys | < 250 C | NO | NO | NO | LIMITED | Low melting point; specialty processes only |
| Polymers / plastics | < 100 C | NO | NO | NO | NO | Not PVD compatible (standard); PECVD alternative |

Compatibility indicators:
- YES: `#27AE60` (Emerald), bold
- LIMITED: `#E8A020` (Amber), bold
- NO: `#E05C5C` (Coral), bold

Data: JetBrains Mono Regular 12 pt. Notes: Inter Regular 12 pt `#F0EDE8` at 70%.
Alternating rows `#1E2435` / `#252B3D`.

---

### ZONE 4 -- Temperature Limitation Chart

**Section label:** `TEMPERATURE IS THE GATEKEEPER` -- Y: 15.2".

**BLOCK D -- Visual Bar Chart (Y: 15.8" to 20.8")**

Horizontal bar chart showing substrate max temperatures vs. coating deposition temperature ranges.

Left axis labels (substrate names): Inter Medium 14 pt `#F0EDE8`.
Bars: Rounded rectangles, H: 0.5", proportional width to temperature.

| Substrate | Bar Width (proportional to temp) | Color | Max Temp Label |
|---|---|---|---|
| WC-Co | Full bar | `#27AE60` | 500 C |
| HSS | ~90% | `#27AE60` | 550 C |
| Tool steel | ~85% | `#27AE60` | 520 C |
| Stainless | Full bar | `#27AE60` | 500 C |
| Ti alloys | ~80% | `#E8A020` | 500 C |
| Aluminum | ~30% | `#E05C5C` | 200 C |

Overlay zone markers:
- `PVD deposition range: 200-500 C` -- dashed vertical lines at 200 C and 500 C, `#E8A020`
- `Ion etch: 200-400 C` -- lighter zone

Callout below chart:
- `Aluminum is the most common "surprise reject" -- customers assume PVD works on everything. It does not. Below 200 C, only specialized low-temp DLC is feasible.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 5 -- Edge Preparation

**Section label:** `EDGE PREPARATION -- RADIUS BEFORE COATING` -- Y: 21.2".

**BLOCK E -- Two-Panel Layout (Y: 21.8" to 26.8")**

**Left panel -- Why Edge Prep Matters (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `WHY EDGE PREP?` Barlow SemiBold 20 pt `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
- `Sharp edges concentrate stress in the coating`
- `PVD coatings are thinner at sharp edges (line-of-sight process)`
- `Result: premature chipping and delamination at cutting edge`
- `Edge honing creates a controlled radius for uniform coating buildup`

Key spec callout:
- `Typical edge radius: 10-50 um before PVD` JetBrains Mono 16 pt `#E8A020`
- `Drag finishing, brushing, or micro-blasting` Inter Regular 13 pt `#F0EDE8` at 70%

**Right panel -- Masking Requirements (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `MASKING -- WHAT NOT TO COAT` Barlow SemiBold 20 pt `#2EC4B6`

Content:
- `Threads, bores, and mating surfaces often must remain uncoated`
- `Masking methods: stainless steel caps, high-temp tape, fixture shadowing`
- `Mask must withstand full PVD cycle temperature (200-500 C)`
- `Mask removal after coating -- inspect for edge effects`

Caution callout:
- `Masking materials that outgas in vacuum will contaminate the entire batch` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Incoming Inspection Checklist

**Section label:** `INCOMING INSPECTION -- GO / NO-GO` -- Y: 27.2".

**BLOCK F -- Checklist (Y: 27.8" to 32.3")**

Two-column checklist. Each item is a rounded rect W: 11.0", H: 0.8", fill `#1E2435`.

| Column | Check Item | Go Indicator |
|---|---|---|
| Left 1 | Substrate material identified and temp-compatible | `#27AE60` GO |
| Left 2 | Part drawing specifies coating type and thickness | `#27AE60` GO |
| Left 3 | Edges honed to specified radius | `#27AE60` GO |
| Left 4 | No visible rust, scale, or heavy oxide | `#27AE60` GO |
| Left 5 | Masking applied where required | `#27AE60` GO |
| Right 1 | No burrs or machining damage | `#27AE60` GO |
| Right 2 | Parts fit on available fixtures | `#27AE60` GO |
| Right 3 | Heat treat / hardness verified (tool steels) | `#27AE60` GO |
| Right 4 | Customer spec reviewed for special requirements | `#27AE60` GO |
| Right 5 | Batch quantity confirmed and documented | `#27AE60` GO |

Check item: Inter Medium 13 pt `#F0EDE8`. Go indicator: Barlow SemiBold 13 pt in color shown.

Bottom note: `Any NO-GO = stop and resolve before proceeding to cleaning (Stage 2)` Inter Medium 14 pt `#E05C5C`

---

### ZONE 7 -- Footer

Standard footer. Title: `Part Preparation -- PVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Preparation PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is the first gatekeeper in the PVD process. The substrate compatibility matrix is the hero because it answers the most common question: "can we PVD coat this part?" The temperature bar chart makes the limitation visual and intuitive. The aluminum callout is critical -- it is the most common customer misunderstanding. Edge preparation is often overlooked and directly causes premature coating failure.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #401 -- Construction Workup v1.0*
*2026-04-26*
