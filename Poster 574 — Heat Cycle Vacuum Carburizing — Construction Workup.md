---
Project: Plating Posters Inc
Poster Number: 574
Title: "Heat Cycle -- Vacuum Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC, Section 2.7)"
Technical Source: LPC heat cycle -- temperature ranges (1700-1900 F), case depth vs. time at 1800 F, high-temperature carburizing advantage, distortion comparison vs. gas carburizing. Per ASM Handbook Vol. 4 and AMS 2759/7.
Process Scope: Vacuum carburizing heat cycle (Stage 5 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - HeatCycle
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #574 -- Construction Workup
## Heat Cycle -- Vacuum Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The heat cycle poster for LPC. The big story here is temperature -- vacuum carburizing can run 100-200 F hotter than gas carburizing because there's no IGO risk, and every 100 F increase roughly doubles the diffusion rate. This poster hammers the case depth vs. time table (the production manager's favorite data), the distortion comparison, and the trade-off between speed and grain growth.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Case depth vs. time table (Block B -- HERO):** The money table -- ECD at 1800 F with comparison to gas at 1700 F.
2. **Temperature range visual (Block D):** Three temperature tiers with applications and trade-offs.
3. **Distortion comparison panel (Block E):** HPGQ vs. oil quench -- the LPC distortion advantage.
4. **Grain growth warning strip (Block F):** When higher temperatures become a problem.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- CASE DEPTH VS. TIME HERO (4.2"--15.5" / ~11.3")
  Block B: ECD table + gas comparison
ZONE 4 -- TEMPERATURE TIERS (15.5"--22.0" / ~6.5")
  Block D: Standard / High-Temp / Ultra-High
ZONE 5 -- DISTORTION COMPARISON (22.0"--28.5" / ~6.5")
  Block E: HPGQ vs. oil quench
ZONE 6 -- GRAIN GROWTH WARNING (28.5"--32.5" / ~4.0")
  Block F: Warning strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `HEAT CYCLE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vacuum Carburizing (LPC) -- Stage 5 of 9` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Higher temperature. Faster diffusion. Shorter cycles. Vacuum carburizing runs 100-200 F hotter than gas because there is no IGO penalty -- and the productivity gain is dramatic.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `30--50%` -- 72 pt `#E8A020`
- Label: `shorter cycle time vs. gas carburizing at 1700 F` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Furnace at temperature, recipe loaded  -->  After: Target ECD achieved, ready for quench`

---

### ZONE 3 -- Case Depth vs. Time (HERO)

**Section label:** `CASE DEPTH VS. TIME -- THE NUMBERS THAT MATTER` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Dual table (Y: 5.0" to 14.5")**

*Left table -- LPC at 1800 F / 982 C (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, border top 4 pt `#27AE60`.

Title: `LPC AT 1800 F (982 C)` Barlow SemiBold 20 pt `#27AE60`

| Target ECD (in.) | Target ECD (mm) | Total Boost+Diffuse Time |
|---|---|---|
| 0.020 | 0.51 | 0.5--1.0 hours |
| 0.030 | 0.76 | 1.0--1.5 hours |
| 0.040 | 1.02 | 1.5--2.5 hours |
| 0.060 | 1.52 | 3.0--5.0 hours |
| 0.080 | 2.03 | 5.0--8.0 hours |

JetBrains Mono 14 pt for data. Header `#3A4055`, alternating rows.

*Right table -- Gas Carburizing at 1700 F / 927 C (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, border top 4 pt `#E8A020`.

Title: `GAS AT 1700 F (927 C) -- FOR COMPARISON` Barlow SemiBold 20 pt `#E8A020`

| Target ECD (in.) | Target ECD (mm) | Approximate Time |
|---|---|---|
| 0.020 | 0.51 | 1.0--1.5 hours |
| 0.030 | 0.76 | 2.0--3.0 hours |
| 0.040 | 1.02 | 3.0--5.0 hours |
| 0.060 | 1.52 | 6.0--9.0 hours |
| 0.080 | 2.03 | 10--14 hours |

JetBrains Mono 14 pt for data.

*Below both tables (Y: 12.5" to 14.5"):*

Rounded rect fill `#252B3D`, left accent `#27AE60`.

Content (Inter Medium 15 pt `#F0EDE8`):
```
THE SQUARE ROOT RULE:
ECD = K x sqrt(time) -- doubling the case depth requires 4x the time
A 100 F increase in temperature roughly DOUBLES the diffusion coefficient
LPC at 1800 F achieves the same ECD in roughly HALF the time as gas at 1700 F
```

Key formulas in JetBrains Mono 14 pt `#27AE60`.

---

### ZONE 4 -- Temperature Tiers

**Section label:** `THREE TEMPERATURE TIERS` -- Y: 15.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Three tier cards (Y: 16.3" to 21.8")**

| Card | X | W | Tier | Accent |
|---|---|---|---|---|
| 1 | 0.5" | 7.33" | Standard (1700--1800 F) | `#2EC4B6` |
| 2 | 8.17" | 7.33" | High-Temp (1800--1900 F) | `#E8A020` |
| 3 | 15.83" | 7.67" | Ultra-High (>1900 F) | `#E05C5C` |

Each: Rounded rect H: 5.2", fill `#1E2435`, left accent 0.06".

*Card 1 -- Standard:*
- Title: `STANDARD: 1700--1800 F` Barlow SemiBold 18 pt `#2EC4B6`
- Stat: `927--982 C` JetBrains Mono 14 pt `#2EC4B6`
- Details:
```
- Same range as gas carburizing
- Well-established recipes
- Fine grain size maintained
- Suitable for all standard
  carburizing grades (8620, 9310)
- Default for new recipe development
```

*Card 2 -- High-Temp:*
- Title: `HIGH-TEMP: 1800--1900 F` Barlow SemiBold 18 pt `#E8A020`
- Stat: `982--1038 C -- THE SWEET SPOT` JetBrains Mono 14 pt `#E8A020`
- Details:
```
- 30--50% faster than standard
- Only practical in vacuum (no IGO)
- Moderate grain growth risk
- Use fine-grain steels (Al-killed)
- Most common production temperature
  for high-volume LPC operations
```

*Card 3 -- Ultra-High:*
- Title: `ULTRA-HIGH: >1900 F` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `>1038 C -- SPECIALTY ONLY` JetBrains Mono 14 pt `#E05C5C`
- Details:
```
- Up to 1950 F (1066 C)
- Maximum diffusion rate
- Significant grain growth risk
- Requires vacuum-grade fine-grain
  steels specifically designed for
  high-temperature stability
- Limited to specialty applications
```

---

### ZONE 5 -- Distortion Comparison

**Section label:** `DISTORTION: LPC WITH HPGQ vs. GAS WITH OIL QUENCH` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Two-column comparison (Y: 22.9" to 28.3")**

*Left -- HPGQ Advantage (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `HPGQ DISTORTION ADVANTAGE` Barlow SemiBold 18 pt `#27AE60`

Content:
```
HPGQ produces LESS distortion than oil:

- No film boiling (vapor blanket)
  Film boiling in oil causes non-uniform
  cooling = non-uniform distortion

- No liquid/vapor interface
  Gas quench is uniform around the part

- Controllable cooling rate
  Adjust pressure and gas velocity to
  balance hardness vs. distortion

- Typical reduction: 30--50% less
  distortion vs. oil quench
  (application-dependent)
```

*Right -- The Trade-Off (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `THE TRADE-OFF` Barlow SemiBold 18 pt `#E8A020`

Content:
```
HPGQ LIMITATIONS:

- Lower quench severity than oil
  H-factor: 0.10--0.40 (gas) vs.
  0.25--0.80 (agitated oil)

- May not harden thick sections
  Lean alloy steels >1.5" (38 mm)
  may not through-harden the case

- Helium is expensive
  He at 20 bar: H = 0.30--0.40
  N2 at 20 bar: H = 0.15--0.25
  He costs 5--10x more than N2

SOLUTION FOR THICK SECTIONS:
Transfer to integrated oil quench
(available on some furnace designs)
Accepts the distortion trade-off
for full case hardness
```

---

### ZONE 6 -- Grain Growth Warning

**Section label:** `GRAIN GROWTH -- THE HIGH-TEMPERATURE TRADE-OFF` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#E05C5C`.

**BLOCK F -- Full-width warning card (Y: 29.4" to 32.3")**

Rounded rect W: 23.0", H: 2.7", fill `#1E2435`, left accent `#E05C5C`.

Two-column:

*Left:*
```
THE PROBLEM:
Higher carburizing temperatures
accelerate grain growth. Large grains
reduce fatigue life and impact toughness.
Above 1900 F, grain growth becomes
the limiting factor.
```

*Right:*
```
THE SOLUTION:
- Use Al-killed fine-grain steels
  (ASTM grain size 5 or finer)
- Microalloy additions (Nb, Ti, V)
  pin grain boundaries
- Verify grain size per ASTM E112
  on every qualification load
- If grain size exceeds spec: reduce
  temperature, not time
```

---

### ZONE 7 -- Footer

Standard. Title: `Heat Cycle -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7E. Case depth times are approximate and depend on steel grade, part geometry, and specific recipe. Always validate with test loads. Distortion reduction is application-dependent.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Heat Cycle Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual case depth table is the centerpiece -- production managers will compare LPC and gas side by side and immediately see the cycle time advantage. The temperature tier cards give operators a framework for understanding when to use which temperature range. The distortion comparison honestly presents HPGQ's limitations alongside its advantages -- this builds credibility with experienced heat treaters who know there's always a trade-off.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #574 -- Construction Workup v1.0*
*2026-04-26*
