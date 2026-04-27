---
Project: Plating Posters Inc
Poster Number: 635
Title: "Furnace & Salt Bath Setup -- Austempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 9: Austempering, Section 9.5)"
Process Scope: Austenitizing furnace configuration and austempering salt bath setup -- equipment, salt chemistry, agitation, temperature control
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Austempering
  - FurnaceSetup
  - SaltBath
  - ConstructionWorkup
  - ClusterHT09
---

# Poster #635 -- Construction Workup
## Furnace & Salt Bath Setup -- Austempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Austempering requires two thermal stations: an austenitizing furnace (atmosphere or salt bath) running at 1500-1650 F and an austempering salt bath held at 400-750 F. The salt bath is the hero of austempering -- its composition, temperature uniformity, and agitation directly determine whether you get bainite or scrap. This poster covers both stations and the salt chemistry that makes the process work.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Two-station layout hero (Block B):** Schematic showing austenitizing furnace and austempering salt bath side by side with transfer path.
2. **Salt bath specification table (Block C):** Detailed salt chemistry and operating parameters.
3. **Austenitizing furnace options (Block D):** Comparison of atmosphere furnace vs. salt bath austenitizing.
4. **Agitation and uniformity panel (Block E):** Why agitation matters and uniformity targets.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.5" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- TWO-STATION LAYOUT HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- SALT BATH SPECIFICATION (14.5"--21.5" / ~7.0")
ZONE 5 -- AUSTENITIZING FURNACE OPTIONS (21.5"--28.0" / ~6.5")
ZONE 6 -- AGITATION & UNIFORMITY (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FURNACE & SALT BATH SETUP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Austempering -- Two-Station Configuration` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Two thermal stations, one fast transfer. The austenitizing furnace heats it -- the salt bath transforms it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 of 9 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Equipment configuration for austempering: furnace + salt bath + transfer mechanism`

---

### ZONE 3 -- Two-Station Layout Hero

**Section label:** `AUSTEMPERING EQUIPMENT CONFIGURATION` -- Y: 4.4".

**BLOCK B -- Two-Station Schematic**

Y: 5.0" to 14.0". Full-width schematic built with rectangles and connector arrows.

**Left station -- Austenitizing Furnace (X: 0.5", W: 10.0"):**

Rounded rect, H: 8.0", fill `#1E2435`, top accent 4 pt `#E8A020`, radius 8.

Title: `AUSTENITIZING FURNACE` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`

Internal labels (JetBrains Mono Regular, 14 pt, `#F0EDE8`):
```
Temperature: 1500--1650 F (816--899 C)
Atmosphere: Endothermic gas or N2
             (or neutral salt bath)
Hold time: 30--90 min (steel)
           60--120 min (ADI)
Furnace class: AMS 2750 Class 3 or 4
```

Bottom note: Inter Regular, 12 pt, `#F0EDE8` at 60%:
`Full austenitization required before transfer`

**Center -- Transfer Arrow (X: 11.0", W: 2.5"):**

Large arrow pointing right, 3 pt stroke `#E05C5C`, filled arrowhead.

Above arrow: `< 15 SEC` -- Barlow Condensed ExtraBold, 24 pt, `#E05C5C`
Below arrow: `RAPID TRANSFER` -- Inter Medium, 14 pt, `#E05C5C`

**Right station -- Austempering Salt Bath (X: 14.0", W: 9.5"):**

Rounded rect, H: 8.0", fill `#1E2435`, top accent 4 pt `#27AE60`, radius 8.

Title: `AUSTEMPERING SALT BATH` -- Barlow Condensed ExtraBold, 22 pt, `#27AE60`

Internal labels (JetBrains Mono Regular, 14 pt, `#F0EDE8`):
```
Temperature: 400--750 F (204--399 C)
Salt: 50/50 NaNO2/KNO3 eutectic
Melting point: ~290 F (~143 C)
Hold time: 30--120 min
Agitation: REQUIRED (propeller/pump)
Uniformity: +/-5 F (+/-3 C)
```

Bottom note: Inter Regular, 12 pt, `#F0EDE8` at 60%:
`Complete bainite transformation occurs HERE`

**Key insight callout (Y: 13.5"):**
- Rounded rect, full width, H: 0.6", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `The salt bath IS the process. Temperature determines whether you get lower bainite (hard, 50+ HRC) or upper bainite (tough, 35-42 HRC).` -- Inter Medium, 14 pt, `#27AE60`

---

### ZONE 4 -- Salt Bath Specification

**Section label:** `AUSTEMPERING SALT BATH -- DETAILED SPECIFICATION` -- Y: 14.7".

**BLOCK C -- Salt Bath Parameters Table**

Y: 15.3" to 21.3". Column widths (23.0" total):
- Parameter (6.0") | Value (8.0") | Notes (9.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Parameter | Value | Notes |
|---|---|---|
| Salt composition | 50/50 NaNO2/KNO3 (typical eutectic) | Nitrate/nitrite blend -- melts low, operates wide |
| Melting point | ~290 F (~143 C) | Salt must be fully molten before loading |
| Operating range | 300--1100 F (149--593 C) | Full range of salt; austempering uses 400--750 F |
| Austempering range (steel) | 400--750 F (204--399 C) | Lower = harder (lower bainite); higher = tougher (upper bainite) |
| Austempering range (ADI) | 450--750 F (232--399 C) | Ductile iron requires slightly higher minimum |
| Temperature uniformity | +/-5 F (+/-3 C) | Non-uniform bath = non-uniform transformation |
| Agitation | Propeller or pump -- REQUIRED | Without agitation, stagnant zones create hot/cold spots |
| H-Factor (agitated) | 0.25--0.45 | Adequate for most austempering applications |
| Salt maintenance | Monitor water content, organic contamination | Water = explosion risk; organics = fire risk |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Parameter names: Inter Medium, 13 pt.

**Warning callout below table:**
- Rounded rect, full width, H: 0.5", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `SALT IS AN OXIDIZER. Nitrate/nitrite reacts violently with oil, grease, or organic contamination. Zero tolerance for organics in the salt bath.` -- Barlow SemiBold, 14 pt, `#E05C5C`, Center

---

### ZONE 5 -- Austenitizing Furnace Options

**Section label:** `AUSTENITIZING FURNACE -- TWO OPTIONS` -- Y: 21.7".

**BLOCK D -- Side-by-Side Comparison**

Y: 22.3" to 27.8".

**Left -- Atmosphere Furnace (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`, radius 6.

Title: `ATMOSPHERE FURNACE` -- Barlow SemiBold, 20 pt, `#E8A020`
Subtitle: `Most Common for Steel` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Atmosphere | Endothermic gas or N2/methanol |
| Temperature | 1500--1650 F |
| Furnace type | Batch IQ, pit, or continuous |
| Scale control | Good with proper atmosphere |
| Transfer | Open-air transfer to salt bath |
| Best for | Steel parts; high-volume production |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

**Right -- Salt Bath Austenitizing (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`, radius 6.

Title: `SALT BATH AUSTENITIZE` -- Barlow SemiBold, 20 pt, `#E8A020`
Subtitle: `Direct Salt-to-Salt Transfer` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Salt type | Neutral salt (BaCl2-based) or proprietary |
| Temperature | 1500--1650 F |
| Scale control | Excellent -- parts submerged |
| Transfer | Salt-to-salt -- fastest possible |
| Caution | BaCl2 is toxic; cyanide can form |
| Best for | ADI; precision parts; shortest transfer |

Bottom note for salt bath option:
- `Salt-to-salt transfer is the fastest method -- minimal air exposure. But BaCl2 austenitizing salt requires strict safety protocols.` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 6 -- Agitation & Uniformity

**Section label:** `AGITATION -- WHY IT MATTERS` -- Y: 28.2".

**BLOCK E -- Agitation Panel**

Y: 28.8" to 32.3". Rounded rect, full width, H: 3.3", fill `#1E2435`, left accent `#27AE60`, radius 8.

Three-column layout inside:

**Column 1 -- Without Agitation (W: 7.0"):**
- Title: `NO AGITATION` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Body: `Stagnant zones form around parts. Salt near part surface heats up (from hot parts) and stays hot. Temperature non-uniformity of +/-15-25 F. Result: mixed microstructures, inconsistent hardness.` -- Inter Regular, 13 pt, `#F0EDE8`

**Column 2 -- With Agitation (W: 7.0"):**
- Title: `PROPER AGITATION` -- Barlow SemiBold, 16 pt, `#27AE60`
- Body: `Propeller or pump circulates salt continuously. Fresh salt sweeps past part surfaces. Temperature uniformity within +/-5 F. Result: uniform bainite transformation throughout the load.` -- Inter Regular, 13 pt, `#F0EDE8`

**Column 3 -- Agitation Methods (W: 7.0"):**
- Title: `AGITATION METHODS` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Body (JetBrains Mono Regular, 12 pt):
```
Propeller (submerged) -- most common
Pump circulation     -- best uniformity
Gas bubbling         -- rare, less uniform
Manual stirring      -- inadequate for
                        production
```

---

### ZONE 7 -- Footer

Standard. Title: `Furnace & Salt Bath Setup -- Austempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; ASTM A897. Salt compositions and furnace configurations vary by application and equipment manufacturer.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Furnace Salt Bath Setup Austempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The two-station schematic is the visual anchor -- it makes the dual-equipment requirement immediately obvious. The transfer arrow between stations is coral and oversized to reinforce the 15-second urgency. The salt bath specification table is the reference workhorse -- operators will check salt composition and temperature targets here daily. The agitation panel drives home why you cannot skip circulation.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #635 -- Construction Workup v1.0*
*2026-04-26*
