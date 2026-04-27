---
Project: Plating Posters Inc
Poster Number: 644
Title: "Furnace & Quench Bath Setup -- Martempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 10: Martempering, Section 10.5)"
Process Scope: Austenitizing furnace and quench bath (salt or hot oil) equipment setup -- specifications, H-factors, and comparison of quench media options
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Martempering
  - FurnaceSetup
  - QuenchBath
  - ConstructionWorkup
  - ClusterHT10
---

# Poster #644 -- Construction Workup
## Furnace & Quench Bath Setup -- Martempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Martempering equipment is conceptually identical to austempering -- austenitizing furnace plus hot quench bath -- but the quench bath has two options: molten salt (classic) or hot oil (marquench oil). This poster covers both setups with detailed specifications, H-factor comparison across all quench media, and the trade-offs that determine which medium to select.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Two-station layout hero (Block B):** Austenitizing furnace + quench bath schematic (same layout concept as Poster 635).
2. **Salt bath vs. hot oil specification tables (Block C):** Parallel specification tables.
3. **H-factor comparison table (Block D):** Comprehensive quench severity reference across all media.
4. **Media selection decision guide (Block E):** When to choose salt vs. oil.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 21.5" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- TWO-STATION LAYOUT HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- QUENCH MEDIA SPECIFICATIONS (14.0"--21.5" / ~7.5")
ZONE 5 -- H-FACTOR REFERENCE TABLE (21.5"--28.0" / ~6.5")
ZONE 6 -- MEDIA SELECTION GUIDE (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FURNACE & QUENCH BATH SETUP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Martempering -- Salt Bath & Hot Oil Options` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Austenitize in the furnace. Equalize in the quench bath. Salt or oil -- pick your medium.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 of 9 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Equipment setup: austenitizing furnace + quench bath (salt or hot oil) + transfer mechanism`

---

### ZONE 3 -- Two-Station Layout Hero

**Section label:** `MARTEMPERING EQUIPMENT CONFIGURATION` -- Y: 4.4".

**BLOCK B -- Two-Station Schematic**

Y: 5.0" to 13.5". Full-width schematic built with rectangles and connector arrows.

**Left station -- Austenitizing Furnace (X: 0.5", W: 10.0"):**

Rounded rect, H: 7.5", fill `#1E2435`, top accent 4 pt `#E8A020`, radius 8.

Title: `AUSTENITIZING FURNACE` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`

Labels (JetBrains Mono Regular, 13 pt, `#F0EDE8`):
```
Temperature: 1475--1600 F (802--871 C)
             (up to 2225 F for HSS)
Atmosphere:  Endothermic gas, N2,
             or salt bath
Hold time:   30--90 min
Furnace class: AMS 2750 Class 3 or 4
Type: Batch IQ, pit, or continuous
```

**Center -- Transfer Arrow (X: 11.0", W: 2.5"):**

Arrow pointing right, 3 pt `#E05C5C`, filled arrowhead.
Above: `< 15 SEC` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`
Below: `RAPID TRANSFER` -- Inter Medium, 13 pt, `#E05C5C`

**Right station -- Quench Bath (X: 14.0", W: 9.5"):**

Rounded rect, H: 7.5", fill `#1E2435`, top accent 4 pt `#27AE60`, radius 8.

Title: `QUENCH BATH` -- Barlow Condensed ExtraBold, 22 pt, `#27AE60`
Subtitle: `(Salt or Hot Oil)` -- Inter Regular, 14 pt, `#F0EDE8` at 50%

Labels (JetBrains Mono Regular, 13 pt, `#F0EDE8`):
```
Temperature: Just above Ms
             (350--600 F typical)
Hold time:   5--15 min
             (EQUALIZATION ONLY)
Purpose:     Equalize surface + core
             temperature BEFORE
             martensite transformation
Agitation:   Required
```

Bottom note: Inter Regular, 12 pt, `#F0EDE8` at 60%:
`After equalization: remove from bath --> air cool --> martensite forms uniformly`

**Key callout (Y: 13.0"):**
- Rounded rect, full width, H: 0.6", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `The quench bath is NOT where transformation occurs. It is an equalization chamber. Martensite forms during the subsequent air cool.` -- Inter Medium, 14 pt, `#27AE60`

---

### ZONE 4 -- Quench Media Specifications

**Section label:** `QUENCH MEDIA -- DETAILED SPECIFICATIONS` -- Y: 14.2".

**BLOCK C -- Parallel Specification Tables**

Y: 14.8" to 21.3". Side-by-side tables.

**Left -- Salt Bath Specs (X: 0.5", W: 11.0"):**

Title: `MARTEMPERING SALT BATH` -- Barlow SemiBold, 18 pt, `#E8A020`

| Parameter | Value |
|---|---|
| Salt type | Nitrate/nitrite eutectic (same as austempering) |
| Composition | 50/50 NaNO2/KNO3 (typical) |
| Melting point | ~290 F (~143 C) |
| Operating range | 350--600 F (177--316 C) for martempering |
| Hold time | 5--15 min (equalization only) |
| Agitation | Required -- propeller or pump |
| Temperature uniformity | +/-5 F (+/-3 C) |
| H-Factor (agitated) | 0.30--0.50 |
| Advantages | Wide temp range; excellent uniformity; high H-factor |
| Disadvantages | Corrosive; salt cleanup required; oxidizer hazard |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Parameter: Inter Medium, 12 pt.

**Right -- Hot Oil Specs (X: 12.0", W: 11.5"):**

Title: `MARQUENCH OIL (HOT OIL)` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Parameter | Value |
|---|---|
| Oil type | Marquench oil (high-temperature quench oil) |
| Composition | Proprietary petroleum base stock |
| Operating range | 250--400 F (121--204 C) |
| Flash point | Must exceed operating temp by 50+ F |
| Hold time | 5--15 min (equalization only) |
| Agitation | Required -- propeller agitation |
| Temperature uniformity | +/-10 F typical (less uniform than salt) |
| H-Factor (agitated) | 0.20--0.35 |
| Advantages | Lower cost; no corrosion; easier cleanup |
| Disadvantages | Narrower temp range; lower H-factor; fire risk |

---

### ZONE 5 -- H-Factor Reference Table

**Section label:** `GROSSMANN H-FACTOR COMPARISON -- ALL QUENCH MEDIA` -- Y: 21.7".

**BLOCK D -- H-Factor Table**

Y: 22.3" to 27.8". Column widths (23.0" total):
- Quench Medium (7.0") | Condition (5.5") | H-Factor (3.5") | Visual Bar (7.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Medium | Condition | H-Factor | Bar Width (proportional) |
|---|---|---|---|
| Still air | -- | 0.02 | Tiny |
| Forced air (fan) | -- | 0.05--0.10 | Very small |
| Marquench oil | 250--400 F, agitated | 0.20--0.35 | Small-medium |
| Martempering salt | 350--600 F, agitated | 0.30--0.50 | Medium |
| Still oil | Room temp | 0.25--0.30 | Small-medium |
| Agitated oil | Room temp, moderate | 0.35--0.50 | Medium |
| Agitated oil | Room temp, vigorous | 0.50--0.80 | Medium-large |
| Polymer (10% PAG) | Agitated | 0.30--0.50 | Medium |
| Still water | Room temp | 1.0 | Large |
| Agitated water | Room temp | 1.0--1.5 | Largest |

Visual bars: horizontal rounded rects, fill `#E8A020`, proportional to H-factor max.
Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Medium: Inter Medium, 13 pt.

Highlight rows for martempering salt and marquench oil with left accent `#27AE60`.

**Note below table:**
- `H-Factor (Grossmann) measures quench severity. Higher = faster heat extraction. Martempering media (salt 0.30-0.50, oil 0.20-0.35) are moderate -- fast enough to avoid pearlite in high-hardenability steels, gentle enough to minimize distortion.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 6 -- Media Selection Guide

**Section label:** `WHEN TO CHOOSE SALT vs. HOT OIL` -- Y: 28.2".

**BLOCK E -- Decision Guide**

Y: 28.8" to 32.3". Rounded rect, full width, H: 3.3", fill `#1E2435`, left accent `#E8A020`, radius 8.

Two-column layout:

**Left -- Choose SALT When (W: 11.0"):**
- Title: `CHOOSE SALT` -- Barlow SemiBold, 16 pt, `#E8A020`
- Items (Inter Medium 13 pt `#F0EDE8`):
```
Maximum quench uniformity is critical (bearings, gears)
Salt bath temp > 400 F is required (for steels with high Ms)
Highest possible H-factor within martempering media
Existing salt bath infrastructure in the shop
Parts can be washed after treatment (salt residue removal)
```

**Right -- Choose HOT OIL When (W: 11.0"):**
- Title: `CHOOSE HOT OIL` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Items (Inter Medium 13 pt `#F0EDE8`):
```
Salt bath infrastructure not available
Lower operating cost preferred
Salt residue cleanup is problematic for part geometry
Lower quench severity is acceptable (high-hardenability steel)
Temp requirement is 250-400 F (within oil operating range)
Oil quench tank already exists -- can be repurposed
```

---

### ZONE 7 -- Footer

Standard. Title: `Furnace & Quench Bath Setup -- Martempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; Grossmann H-factor tables. Quench media selection depends on application requirements, equipment availability, and steel hardenability.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Furnace Quench Bath Setup Martempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The H-factor table is the reference heavyweight on this poster -- it puts martempering media in context against all other quench options, showing operators exactly where salt and oil sit on the severity spectrum. The visual bars make it scannable at distance. The side-by-side salt vs. oil specs give a direct comparison that helps the process engineer make the media selection decision.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #644 -- Construction Workup v1.0*
*2026-04-26*
