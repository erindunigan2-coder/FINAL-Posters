---
Project: Plating Posters Inc
Poster Number: 98
Title: "Activation -- Copper (Acid)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Acid activation / acid dip for acid copper sulfate plating line (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - CopperPlating
  - AcidCopper
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP09
---

# Poster #98 -- Construction Workup
## Activation -- Copper (Acid)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of the acid copper process. Activation for acid copper is substrate-dependent. Copper and brass substrates get a dilute sulfuric acid dip. Steel that has already received a copper strike gets a mild H2SO4 dip before entering the acid copper tank. PCBs use a microetch (sodium persulfate or H2O2/H2SO4). Zinc die castings cannot go into acid copper at all without a cyanide or alkaline non-cyanide copper strike first -- there is no "acid activation" that solves the immersion deposit problem.

Hero visual: a substrate decision matrix showing which acid treatment matches which substrate.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate decision matrix hero (Block B):** A visual table/grid showing substrate vs. acid type. Large format, color-coded.
2. **Orientation strip (Block C):** Stage 3 highlighted.
3. **Activation parameter table (Block D).**
4. **Immersion deposit warning callout (Block E):** A coral-accented warning about steel and zinc in acid copper.
5. **Problems table + Safety callout.**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted
ZONE 3 -- SUBSTRATE DECISION MATRIX HERO (4.2"--14.0")
ZONE 4 -- ACTIVATION PARAMETERS (14.0"--20.5")
ZONE 5 -- IMMERSION DEPOSIT WARNING + PROBLEMS (20.5"--27.0")
ZONE 6 -- SAFETY CALLOUT (27.0"--32.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Copper (Acid) -- Stage 3 of 8` -- 34 pt `#E8A020` (Amber). Y: 1.4".

**Tagline:** `The right acid for the right substrate. Get this wrong on steel or zinc and the deposit peels off in your hand.` -- 20 pt at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted (fill `#E8A020`, text `#1A1F2E`). Others dimmed.

Below strip: `Before: Clean, rinsed surface  -->  After: Oxide-free, activated metal ready for plating`

---

### ZONE 3 -- Substrate Decision Matrix Hero

**Section label:** `ACTIVATION BY SUBSTRATE -- WHICH ACID, WHICH PATH` -- Y: 4.4".

**BLOCK B -- Decision Matrix (Y: 5.0" to 13.5")**

A large table-style grid. Each row is a substrate, each column shows the activation treatment, the acid used, and the path to acid copper.

Five rows, each in a rounded rect card (full width, H: 1.5", fill `#1E2435`):

**Row 1 -- Copper / Brass (X: 0.5", Y: 5.0"):**
- Left accent: `#27AE60`
- Substrate: `COPPER / BRASS` -- Barlow SemiBold 20 pt `#27AE60`
- Acid: `5--10% H2SO4, ambient, 15--30 sec` -- JetBrains Mono 14 pt `#F0EDE8`
- Path: `Activate -> Rinse -> ACID COPPER (direct)` -- Inter Medium 14 pt `#27AE60`
- Note: `Easiest substrate. No strike needed.` -- Inter Regular 12 pt `#F0EDE8` at 60%

**Row 2 -- Nickel (X: 0.5", Y: 6.7"):**
- Left accent: `#27AE60`
- Substrate: `NICKEL` -- Barlow SemiBold 20 pt `#27AE60`
- Acid: `5--10% H2SO4 or mild HCl dip, 15--30 sec` -- JetBrains Mono 14 pt
- Path: `Activate -> Rinse -> ACID COPPER (direct)`
- Note: `Common in decorative stacks (Ni under Cu over Ni).`

**Row 3 -- Steel (with copper strike) (X: 0.5", Y: 8.4"):**
- Left accent: `#E8A020`
- Substrate: `STEEL (after Cu strike)` -- Barlow SemiBold 20 pt `#E8A020`
- Acid: `3--5% H2SO4, 10--30 sec` -- JetBrains Mono 14 pt
- Path: `Strike -> Rinse -> Activate -> Rinse -> ACID COPPER`
- Note: `Strike provides barrier. Mild activation removes light tarnish.`

**Row 4 -- Zinc Die Cast (X: 0.5", Y: 10.1"):**
- Left accent: `#E05C5C`
- Substrate: `ZINC DIE CAST` -- Barlow SemiBold 20 pt `#E05C5C`
- Acid: `COPPER STRIKE MANDATORY -- no acid activation alone` -- JetBrains Mono 14 pt `#E05C5C`
- Path: `CN or alk. Cu strike -> Rinse -> Mild H2SO4 dip -> ACID COPPER`
- Note: `Acid copper on bare zinc = immersion deposit = peel failure.`

**Row 5 -- ABS Plastic (after electroless) (X: 0.5", Y: 11.8"):**
- Left accent: `#2EC4B6`
- Substrate: `ABS PLASTIC (after electroless Cu/Ni)` -- Barlow SemiBold 20 pt `#2EC4B6`
- Acid: `Mild H2SO4 dip, 10--20 sec` -- JetBrains Mono 14 pt
- Path: `Electroless -> Rinse -> Mild dip -> ACID COPPER`
- Note: `Electroless copper provides conductive base for electroplating.`

---

### ZONE 4 -- Activation Parameters

**Section label:** `ACTIVATION PARAMETERS -- DETAILED` -- Y: 14.2".

**Full-width table (X: 0.5", W: 23.0"):**

| Parameter | H2SO4 Dip | HCl Dip | Microetch (PCB) |
|---|---|---|---|
| Concentration | 5--10% v/v | 10--50% v/v (typ. 25--33%) | Na persulfate 100--200 g/L or H2O2/H2SO4 |
| Temperature | Ambient (65--85 F) | Ambient | Ambient to 95 F |
| Time | 15--30 sec | 15--60 sec | 30--90 sec |
| Primary substrate | Copper, brass, after-strike steel | Steel (direct, before strike) | PCBs only |
| Purpose | Remove light oxide, activate surface | Remove heavier oxide/scale | Create micro-roughness for adhesion |
| Agitation | None to mild | None to mild | Moderate |
| Key control | Do not over-etch copper substrates | Minimize time on high-strength steel | Etch depth: 0.5--1.0 um |

Header: `#3A4055`. Data: JetBrains Mono 12 pt. Rows alternate `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Immersion Deposit Warning + Problems

**BLOCK E -- Immersion Deposit Warning (Y: 20.7" to 23.5")**

Full-width callout, rounded rect, fill `#1E2435`, border 2 pt `#E05C5C`, left accent 0.06" `#E05C5C`.

Title: `WARNING: IMMERSION DEPOSITION` -- Barlow Condensed ExtraBold 24 pt `#E05C5C`

Body (Inter Regular 14 pt `#F0EDE8`, line height 150%):

> When a more active metal (steel, zinc) contacts an acid copper solution without current, copper spontaneously deposits by displacement -- the base metal dissolves and copper precipitates on the surface. This "immersion deposit" is red, powdery, and has ZERO adhesion. It peels on the slightest stress.
>
> This is why steel and zinc die castings MUST have a copper strike (cyanide or alkaline non-cyanide) before entering acid copper. The strike provides a bonded copper layer that prevents immersion deposition.

Key rule: `No strike on steel or zinc = guaranteed peel failure. No exceptions.` -- Inter Medium 16 pt `#E05C5C`

**BLOCK F -- Problem Table (Y: 23.8" to 26.8")**

| Problem | Cause | Fix |
|---|---|---|
| Red powdery deposit on steel | No copper strike -- immersion deposit | Apply CN or alk. non-CN copper strike first |
| Over-etched copper substrate | H2SO4 too strong or time too long | Reduce concentration to 5%; limit to 15 sec |
| Staining after activation | Acid residue drying on surface | Rinse immediately; reduce drain time |
| Pitting in copper plate | Contaminated acid dip (dissolved metals) | Replace activation acid; filter |

Problem: `#E05C5C`. Fix: `#27AE60`.

---

### ZONE 6 -- Safety Callout

**Left -- Acid Handling (X: 0.5", W: 11.0"):**
- Title: `ACID SAFETY` -- `#E05C5C`
- `H2SO4: corrosive -- severe burns. Always add acid to water.`
- `HCl: corrosive, generates HCl fumes -- ventilation required`
- `Microetch (persulfate): oxidizer -- keep away from organics`
- `H2O2/H2SO4 microetch: exothermic -- temperature control critical`

**Right -- PPE (X: 12.0", W: 11.5"):**
- Title: `REQUIRED PPE` -- `#E8A020`
- `Chemical splash goggles or face shield`
- `Acid-resistant gloves (butyl rubber or neoprene)`
- `Acid-resistant apron`
- `Eyewash and emergency shower within 10 sec`
- `Local exhaust ventilation over HCl tanks`

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Copper (Acid)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table. **Export:** Six files -- `Activation Copper Acid -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The hero of this poster is the substrate decision matrix -- it answers the most common question a plater has at this stage: "what acid do I use for my substrate?" The immersion deposit warning is given full-width coral treatment because this is the single most common mistake in acid copper plating. Every job shop has a story about peeling copper on steel because someone forgot the strike.

---

*Alaina -- Poster #98 -- Construction Workup v1.0 -- 2026-04-26*
