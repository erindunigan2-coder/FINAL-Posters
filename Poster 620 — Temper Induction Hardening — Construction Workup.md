---
Project: Plating Posters Inc
Poster Number: 620
Title: "Temper -- Induction Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7, Section 7.8)"
Technical Source: Tempering after induction hardening -- oven temper vs. induction temper, temperature ranges, time requirements, and the critical rule that tempering must follow quenching immediately. Induction temper is a unique capability that furnace processes cannot match.
Process Scope: Induction hardening -- temper
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - InductionHardening
  - Temper
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #620 -- Construction Workup
## Temper -- Induction Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Tempering after induction hardening follows the same metallurgical principles as tempering after any quench -- relieve residual stresses and trade a small amount of hardness for dramatically improved toughness. But induction has a trick that furnace hardening does not: induction temper. A second, lower-power induction pass can temper the part in seconds instead of hours. This poster covers both methods and when each is appropriate.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Oven vs. induction temper comparison (Block B -- HERO):** Side-by-side comparison of the two tempering methods with advantages and limitations.
2. **Temper parameter table (Block D):** Temperature, time, and hardness loss data.
3. **Hardness vs. temper temperature chart (Block E):** Visual showing how tempering temperature affects final hardness for typical induction steels.
4. **"Never Skip Temper" warning (Block F):** Consequences of untempered martensite.

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
ZONE 3 -- OVEN VS. INDUCTION TEMPER / HERO (4.2"--14.5" / ~10.3")
  Block B: Two-panel comparison
  Block C: "Temper Immediately" principle callout
ZONE 4 -- TEMPER PARAMETER TABLE (14.5"--22.0" / ~7.5")
  Block D: Temperature, time, and expected hardness
ZONE 5 -- HARDNESS CHART + NEVER SKIP WARNING (22.0"--32.5" / ~10.5")
  Block E: Hardness vs. temper temperature
  Block F: Untempered martensite warning
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TEMPER` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Induction Hardening -- Stage 8 of 9` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Trade a few points of hardness for dramatically improved toughness. Temper always follows quench -- no exceptions.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-quenched martensite (hard, brittle)  -->  After: Tempered martensite (hard, tough)`

---

### ZONE 3 -- Oven vs. Induction Temper (HERO)

**Section label:** `TWO TEMPERING METHODS -- WHEN TO USE EACH` -- Y: 4.4".

**BLOCK B -- Two-Panel Comparison**

Y: 5.0" to 12.5".

**Left -- Oven Temper (X: 0.5", W: 11.0"):**
- Rounded rect H: 7.0", fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `OVEN (FURNACE) TEMPER` -- Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `The Conventional Method` -- Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Temperature | 300--400 F (149--204 C) |
| Time | 1--2 hours at temperature |
| Equipment | Standard batch or conveyor oven |
| Atmosphere | Air (no protective atmosphere needed) |
| Uniformity | Excellent -- entire part at same temperature |
| Compliance | Required by most specifications (AMS 2759/12) |
| Throughput | Slow -- hours per batch |
| Best for | Specification compliance; complex geometries; mixed loads |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Still the standard for aerospace and specification-controlled work` -- Inter Medium 13 pt `#E8A020`

**Right -- Induction Temper (X: 12.0", W: 11.5"):**
- Rounded rect H: 7.0", fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `INDUCTION TEMPER` -- Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `The Production Method` -- Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Temperature | 350--500 F (177--260 C) -- higher to compensate for short time |
| Time | 5--30 seconds (rapid) |
| Equipment | Second induction coil at reduced power |
| Atmosphere | None needed |
| Uniformity | Good for symmetric parts; limited on complex shapes |
| Compliance | Not accepted by all specifications -- verify |
| Throughput | Fast -- seconds per part (inline) |
| Best for | High-volume production; automotive; inline processing |

Bottom highlight:
- Rounded rect W: 10.5", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Seconds instead of hours -- the induction shop's productivity advantage` -- Inter Medium 13 pt `#27AE60`

**BLOCK C -- Temper Immediately Callout**

Y: 12.8" to 14.3". Full-width callout.
- Rounded rect W: 23.0", H: 1.3", fill `#1E2435`, left accent 0.06" `#E05C5C`
- Text: `TEMPER IMMEDIATELY AFTER QUENCH. As-quenched martensite is under extreme internal stress. Delay increases cracking risk. For oven temper, load parts within 1 hour of quench. For induction temper, the part passes directly from the quench station to the temper coil -- seconds of delay.` -- Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Temper Parameter Table

**Section label:** `TEMPER PARAMETERS -- EXPECTED OUTCOMES` -- Y: 14.7".

**BLOCK D -- Parameter Table**

Y: 15.3" to 21.8". Column widths (23.0" total):
- Steel Grade (4.0") | As-Quenched HRC (3.5") | Temper Temp (3.5") | Time (2.5") | Tempered HRC (3.5") | Hardness Loss (3.0") | Notes (3.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Steel | As-Quenched | Temper Temp | Time | Tempered HRC | Loss | Notes |
|---|---|---|---|---|---|---|
| 1045 | 58--60 | 300 F (149 C) | 1 hr | 56--58 | 2 pts | Minimal loss at low temper |
| 1045 | 58--60 | 350 F (177 C) | 1 hr | 54--56 | 4 pts | Standard production |
| 1045 | 58--60 | 400 F (204 C) | 1 hr | 52--54 | 6 pts | Maximum stress relief |
| 4140 | 58--60 | 300 F (149 C) | 1 hr | 56--58 | 2 pts | Alloy retains hardness better |
| 4140 | 58--60 | 400 F (204 C) | 1 hr | 54--56 | 4 pts | Good toughness balance |
| 4340 | 60--62 | 350 F (177 C) | 1 hr | 58--60 | 2 pts | Premium alloy; best retention |

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".
Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Grade names: Inter Medium 13 pt.

Bottom note: `Higher temper temperatures reduce hardness but improve toughness. For induction temper, increase temperature by 50--100 F above oven values to compensate for the shorter soak time.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Hardness Chart + Never Skip Warning

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Hardness vs. Temper Temperature (X: 0.5", W: 11.0"):**

Section label: `HARDNESS VS. TEMPER TEMPERATURE` Barlow Condensed ExtraBold 24 pt.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E8A020`

Visual representation (text-based chart):
```
TEMPER TEMP   |  1045 HRC  |  4140 HRC  |  4340 HRC
--------------+------------+------------+-----------
As-quenched   |    60      |    60      |    62
250 F         |    59      |    59      |    61
300 F         |    57      |    58      |    60
350 F         |    55      |    56      |    59
400 F         |    53      |    55      |    57
450 F         |    50      |    53      |    55
500 F         |    47      |    50      |    53

TREND: Hardness decreases approximately
2 HRC per 50 F increase in temper temperature.
Alloy steels retain hardness better than
plain carbon steels.
```

Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Trend note: Inter Medium 13 pt `#E8A020`.

**Right -- Never Skip Temper (X: 12.0", W: 11.5"):**

Section label: `NEVER SKIP TEMPER` Barlow Condensed ExtraBold 24 pt `#E05C5C`.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E05C5C`

Warning content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
UNTEMPERED MARTENSITE IS A TICKING BOMB.

As-quenched martensite is:
  - Extremely hard (58--62 HRC)
  - Extremely brittle
  - Under severe internal stress
  - Prone to spontaneous cracking
    (especially at low temperatures)

WHAT HAPPENS IF YOU SKIP TEMPER:
  - Delayed cracking (hours, days, or weeks
    after quench)
  - Catastrophic brittle fracture under load
  - Stress corrosion cracking (in service)
  - Dimensional instability (martensite
    decomposes slowly at room temperature)

THE 1-HOUR RULE:
Parts must enter the temper furnace within
1 hour of quenching. No exceptions.
Parts must never be left as-quenched
overnight.

Some specifications require temper to begin
within 30 minutes of quench completion.
```

Bottom highlight: `Temper is not optional. It is not a nice-to-have. It is a mandatory metallurgical step. Untempered parts are nonconforming.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Footer

Standard footer. Title: `Temper -- Induction Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Temper parameters vary by steel grade, section size, and specification requirements. Values shown are typical ranges. Consult your process engineer and applicable specifications (AMS 2759/12, customer specs) for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Temper Induction Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The oven vs. induction temper comparison is the unique content on this poster. Most heat treat posters cover oven temper only -- the induction temper method is specific to this process and represents a genuine productivity advantage that shops should understand. The "Never Skip Temper" warning is standard metallurgical wisdom but cannot be overstated. Delayed cracking from untempered martensite is a real-world problem that costs shops money and puts parts at risk. The 1-hour rule is industry standard practice.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #620 -- Construction Workup v1.0*
*2026-04-26*
