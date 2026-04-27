---
Project: Plating Posters Inc
Poster Number: 133
Title: "Rinse -- Silver -- Post-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Post-plate rinse for cyanide silver plating (Stage 7 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - SilverPlating
  - Cyanide
  - Rinse
  - ConstructionWorkup
  - ClusterEP13
---

# Poster #133 -- Construction Workup
## Rinse -- Silver -- Post-Plate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 8. The post-plate rinse removes cyanide drag-out from the freshly plated silver surface before anti-tarnish treatment. Two critical concerns: (1) cyanide waste segregation -- the first rinse captures CN-bearing drag-out and must route to cyanide waste treatment, not general drain; (2) silver recovery -- rinse water containing dissolved silver is economically worth recovering.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse system diagram (Block B -- HERO):** Double counterflow rinse system with cyanide waste routing and silver recovery side loop.
2. **Waste segregation panel (Block D):** CN waste stream routing diagram.
3. **Silver recovery callout (Block E):** Economics of silver recovery from rinse water.
4. **Rinse quality and common errors (Block F).**
5. **CYANIDE SAFETY badge:** Header zone.

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
  Stage 7 highlighted (Teal)
ZONE 3 -- RINSE SYSTEM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- WASTE SEGREGATION (14.5"--20.5" / ~6.0")
ZONE 5 -- SILVER RECOVERY (20.5"--26.5" / ~6.0")
ZONE 6 -- RINSE QUALITY + COMMON ERRORS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Silver Plating -- Post-Plate -- Stage 7 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Cyanide comes out with the parts. This rinse captures it, segregates it, and routes it to treatment. Silver recovery pays for itself.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".
**CYANIDE SAFETY badge:** Same spec as Poster #127.

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Silver-plated part with cyanide drag-out film  -->  After: Rinsed surface ready for anti-tarnish`

---

### ZONE 3 -- Rinse System Hero

**Section label:** `POST-PLATE RINSE SYSTEM -- DOUBLE COUNTERFLOW` -- Y: 4.4".

**BLOCK B -- Two-Tank Rinse Diagram**

Y: 5.0" to 14.0".

**Tank 1 -- First Rinse (Cyanide Capture):**
- Rounded rect, X: 1.5", Y: 5.5", W: 10.0", H: 5.0"
- Fill: `#E05C5C` at 8% (tinted -- contaminated)
- Border: 2 pt `#E05C5C`
- Label: `RINSE 1 -- CYANIDE CAPTURE` Barlow SemiBold 16 pt `#E05C5C`
- Parameters: `Captures CN drag-out` / `Routes to CN waste treatment` / `NOT to general drain`
- Arrow out bottom: `TO CYANIDE WASTE TREATMENT` `#E05C5C` with arrow

**Tank 2 -- Final Rinse (DI Water):**
- Rounded rect, X: 12.5", Y: 5.5", W: 10.0", H: 5.0"
- Fill: `#2EC4B6` at 8% (clean)
- Border: 2 pt `#2EC4B6`
- Label: `RINSE 2 -- DI WATER FINAL` Barlow SemiBold 16 pt `#2EC4B6`
- Parameters: `DI water preferred` / `Fresh water counterflow from Rinse 2 to Rinse 1` / `Produces clean surface for anti-tarnish`

**Counterflow arrows between tanks:**
- Arrow from Rinse 2 overflow to Rinse 1: `COUNTERFLOW` JetBrains Mono 12 pt `#2EC4B6`

**Silver recovery side loop (below Tank 1):**
- Small box: `SILVER RECOVERY` Barlow SemiBold 12 pt `#E8A020`
- `Electrolytic cell or ion exchange on Rinse 1 overflow`
- `Economically justified at > 5 ppm Ag`

**Bottom callout:**
- `Double counterflow: uses less water, captures more silver, keeps cyanide segregated.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Waste Segregation

**Section label:** `CYANIDE WASTE -- SEGREGATION IS MANDATORY` -- Y: 14.7".

**BLOCK D -- Waste Routing Diagram (Y: 15.3" to 20.3")**

Three-column layout:

**Left -- Cyanide Waste Stream (X: 0.5", W: 7.33"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `CN WASTE STREAM` Barlow SemiBold 18 pt `#E05C5C`
- `Source: Rinse 1 overflow + bath dumps`
- `Treatment: Alkaline chlorination (two-stage)`
- `Stage 1: CN- --> CNO- (pH > 10, ORP +350 mV)`
- `Stage 2: CNO- --> CO2 + N2 (pH 8--9, ORP +600 mV)`
- `NEVER mix CN waste with acid waste`

**Center -- Silver Recovery (X: 8.16", W: 7.33"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `SILVER RECOVERY` Barlow SemiBold 18 pt `#E8A020`
- `Method: Electrolytic cell or ion exchange`
- `Feed: Rinse 1 water (highest Ag concentration)`
- `Recovery rate: 90--95% of dissolved Ag`
- `Payback: Silver is a precious metal -- recovery pays for the equipment`

**Right -- Final Discharge (X: 15.83", W: 7.67"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `FINAL DISCHARGE` Barlow SemiBold 18 pt `#27AE60`
- `After CN destruction + silver removal`
- `Test for: residual CN (< 0.1 mg/L), Ag (< 0.05 mg/L), pH (6--9)`
- `Discharge per local POTW permit`

---

### ZONE 5 -- Silver Recovery

**Section label:** `THE ECONOMICS OF SILVER RECOVERY` -- Y: 20.7".

**BLOCK E -- Full-Width Panel (Y: 21.3" to 26.3")**

- Rounded rect, X: 0.5", W: 23.0", H: 4.5", fill `#1E2435`, left accent `#E8A020`

**Left side -- Why Recover:**
- `Silver spot price fluctuates but is consistently valuable`
- `A busy silver plating line loses 5--15 g/L drag-out per rack`
- `Over a year, this adds up to kilograms of recoverable metal`
- `Electrolytic recovery: low operating cost, continuous`
- `Ion exchange: batch process, resin regeneration required`

**Right side -- Methods Comparison:**

| Method | Capital Cost | Operating Cost | Recovery Rate | Best For |
|---|---|---|---|---|
| Electrolytic cell | Moderate | Low | 90--95% | Continuous, high-volume |
| Ion exchange | Low | Moderate | 85--95% | Batch, lower volume |
| Evaporative recovery | High | High | 95%+ | Maximum recovery |

JetBrains Mono 12 pt for data.

---

### ZONE 6 -- Rinse Quality + Common Errors

**Section label:** `COMMON ERRORS` -- Y: 26.7".

**BLOCK F -- Four Cards (Y: 27.3" to 32.3")**

| Card | Problem | Cause | Fix |
|---|---|---|---|
| 1 | CN DRAG-OUT TO ANTI-TARNISH | Inadequate rinse | Extend rinse; add second stage |
| 2 | SILVER LOSS TO DRAIN | No recovery system | Install electrolytic cell or IX |
| 3 | CN WASTE IN GENERAL DRAIN | Rinse 1 not segregated | Replumb immediately -- regulatory violation |
| 4 | WATER SPOTS ON SILVER | Hard water in final rinse | Use DI water for final rinse |

Standard card style, left accent `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Silver -- Post-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Silver Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The post-plate rinse in silver plating has two unique aspects not present in most other plating clusters: mandatory cyanide waste segregation and economically justified precious metal recovery. The waste routing diagram is the hero concept -- operators need to understand that Rinse 1 is NOT general rinse water. The silver recovery panel adds business value to the poster beyond just safety compliance.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #133 -- Construction Workup v1.0*
*2026-04-26*
