---
Project: Plating Posters Inc
Poster Number: 629
Title: "Temper -- Flame Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 8, Section 8.8)"
Technical Source: Flame hardening temper parameters -- low-temperature temper (300--400 F) to relieve quench stress and improve toughness without significant hardness loss. Temper must follow quench promptly. Oven temper is standard; flame temper (torch back-pass) is a field method for large parts.
Process Scope: Flame hardening -- temper stage
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FlameHardening
  - Temper
  - ConstructionWorkup
  - ClusterHT08
---

# Poster #629 -- Construction Workup
## Temper -- Flame Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Tempering after flame hardening is the same metallurgy as any martensite temper -- heat the as-quenched part to 300--400 F for 1--2 hours and let the martensite relax into tempered martensite. What makes flame hardening tempering interesting is the field option: on parts too large for an oven (think machine ways, large rolls, ship components), a second pass with a softer flame can serve as a temper. It is less controlled than oven tempering but sometimes the only practical method. This poster covers both approaches.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Temper methods comparison (Block B -- HERO):** Oven temper vs. flame temper side-by-side with specifications.
2. **Hardness vs. temper temperature chart (Block C):** Showing the curve for medium-carbon steels.
3. **Timing rule callout (Block D):** Why temper must happen within 1 hour of quench.
4. **Temper defect cards (Block E):** Common failures from improper tempering.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber)
ZONE 3 -- TEMPER METHODS / HERO (4.2"--14.5" / ~10.3")
  Block B: Oven temper vs. flame temper
  Block C: Hardness vs. temper temperature
ZONE 4 -- TIMING RULE + TEMPER GUIDELINES (14.5"--22.0" / ~7.5")
  Block D: One-hour rule callout
  Block D2: Temper parameter table
ZONE 5 -- TEMPER DEFECTS (22.0"--28.5" / ~6.5")
  Block E: Four defect cards
ZONE 6 -- FOOTER BAND (28.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TEMPER` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flame Hardening -- Stage 8 of 9` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Martensite is hard but brittle. Temper trades a few HRC points for toughness. Oven is standard -- flame temper is the field option for oversized parts.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-quenched martensite, maximum hardness, maximum brittleness  -->  After: Tempered martensite, target hardness, improved toughness`

---

### ZONE 3 -- Temper Methods (HERO)

**Section label:** `TWO TEMPER METHODS` -- Y: 4.4".

**BLOCK B -- Oven Temper vs. Flame Temper**

Y: 5.0" to 10.5". Two side-by-side panels.

**Left -- Oven Temper (X: 0.5", W: 11.0"):**

Rounded rect, H: 5.0", fill `#1E2435`, top accent 4 pt `#E8A020`, radius 8.

Title: `OVEN TEMPER (STANDARD)` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`

Labels (JetBrains Mono Regular, 13 pt, `#F0EDE8`):
```
Temperature:  300--400 F (149--204 C)
Time:         1--2 hours at temperature
Atmosphere:   Air (standard oven)
Heating rate: Gradual -- avoid thermal shock
Cooling:      Air cool to room temp
Hardness loss: 1--3 HRC from as-quenched
```

Advantage callout: Inter Medium 13 pt `#27AE60`:
`BEST CONTROL: Uniform temperature across entire part. Repeatable. Documented.`

**Right -- Flame Temper (X: 12.0", W: 11.5"):**

Rounded rect, H: 5.0", fill `#1E2435`, top accent 4 pt `#2EC4B6`, radius 8.

Title: `FLAME TEMPER (FIELD METHOD)` -- Barlow Condensed ExtraBold, 22 pt, `#2EC4B6`

Labels (JetBrains Mono Regular, 13 pt, `#F0EDE8`):
```
Method:       Second pass with reduced flame
Temperature:  Straw to light blue temper color
              (430--600 F / 221--316 C)
Control:      Visual -- temper colors only
Speed:        Same traverse as hardening pass
              or slightly faster
Cooling:      Air cool
```

Caution callout: Inter Medium 13 pt `#E05C5C`:
`LESS PRECISE: Temperature control is visual only. Use pyrometer to verify. Reserve for parts that cannot be oven-tempered.`

**BLOCK C -- Hardness vs. Temper Temperature**

Y: 11.0" to 14.3". Full-width panel.

- Rounded rect W: 23.0", H: 3.0", fill `#1E2435`, radius 6

Section label: `TYPICAL HARDNESS RESPONSE -- MEDIUM-CARBON STEEL (1045/4140)` Barlow SemiBold 16 pt `#F0EDE8`.

Table format (since we cannot render curves):

| Temper Temp F (C) | As-Quenched HRC | Tempered HRC (1045) | Tempered HRC (4140) | Color |
|---|---|---|---|---|
| As-quenched | 62--65 | 62--65 | 62--65 | -- |
| 300 F (149 C) | -- | 60--62 | 60--63 | Faint straw |
| 400 F (204 C) | -- | 57--60 | 58--61 | Light straw |
| 500 F (260 C) | -- | 54--57 | 55--58 | Dark straw |
| 600 F (316 C) | -- | 50--53 | 52--55 | Light blue |
| 700 F (371 C) | -- | 46--49 | 48--52 | Dark blue |
| 800 F (427 C) | -- | 42--45 | 44--48 | Gray |

Header: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`, H: 0.35".
Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Color column: Inter Medium 11 pt `#E8A020`.

Note: `Standard flame hardening temper: 300--400 F. Higher tempers sacrifice hardness for toughness -- only when the application demands it.` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 4 -- Timing Rule + Temper Guidelines

**Section label:** `TEMPER TIMING AND GUIDELINES` -- Y: 14.7".

**BLOCK D -- One-Hour Rule Callout**

Y: 15.3" to 17.0". Full-width panel.

- Rounded rect W: 23.0", H: 1.5", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8

Content (centered):
- Title: `THE ONE-HOUR RULE` -- Barlow Condensed ExtraBold 28 pt `#E05C5C`
- Text: `Temper within 1 hour of quench. As-quenched martensite is under extreme internal stress. Delayed tempering risks spontaneous cracking -- especially on parts with section changes, keyways, or sharp corners.` -- Inter Medium, 15 pt, `#F0EDE8`

**BLOCK D2 -- Temper Parameter Table**

Y: 17.5" to 21.8".

| Parameter | Value | Notes |
|---|---|---|
| Standard temper range | 300--400 F (149--204 C) | Most flame hardening applications |
| High-toughness temper | 400--600 F (204--316 C) | Impact-loaded parts; sacrifice 3--8 HRC |
| Temper time | 1--2 hours at temperature | Minimum 1 hour; longer for heavy sections |
| Number of tempers | 1 (standard) | Double temper only for high-alloy steels |
| Heating rate | Gradual -- no faster than 200 F/hr | Prevents thermal shock on large parts |
| Cooling after temper | Air cool (standard) | No water quench after temper |
| Maximum delay (quench to temper) | 1 hour | Cracking risk increases beyond this |

Header: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".
Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Parameter: Inter Medium 13 pt.

---

### ZONE 5 -- Temper Defects

**Section label:** `TEMPER-RELATED DEFECTS` -- Y: 22.2".

**BLOCK E -- Four Defect Cards**

Y: 22.9" to 28.3". Four cards in a row. Gap: 0.25".

Each card: Rounded rect, W: 5.5", H: 5.0", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Defect | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DELAYED CRACKING | Temper delayed beyond 1 hour; high internal stress in as-quenched martensite | Temper immediately; stage parts directly from quench to temper oven |
| 2 | 6.25" | EXCESSIVE SOFTENING | Temper temperature too high; time too long; thermocouple error | Verify oven calibration; reduce temperature; reduce time |
| 3 | 12.0" | NON-UNIFORM TEMPER | Flame temper with inconsistent traverse speed; oven hot/cold spots | Use oven temper when possible; verify oven uniformity per AMS 2750 |
| 4 | 17.75" | TEMPER EMBRITTLEMENT | Temper in 500--700 F range on susceptible alloys (tempered martensite embrittlement) | Avoid 500--700 F range for alloy steels; if required, cool rapidly through this range |

Interior per card:
- Defect: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer

Standard footer. Title: `Temper -- Flame Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Temper temperatures and times vary by steel grade and application requirements. Hardness values shown are typical ranges for medium-carbon steels. Consult your metallurgist for grade-specific temper parameters. Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Temper Flame Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The oven-vs-flame temper comparison is the educational anchor here. Most operators know about oven tempering, but flame tempering (a second pass with a softer flame, reading temper colors) is an old-school field technique that's rarely documented. The hardness-vs-temperature table substitutes for a curve diagram and gives operators a practical lookup. The one-hour rule callout is deliberately oversized and in Coral -- cracking from delayed temper is one of the most common preventable failures in flame hardening shops.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #629 -- Construction Workup v1.0*
*2026-04-26*
