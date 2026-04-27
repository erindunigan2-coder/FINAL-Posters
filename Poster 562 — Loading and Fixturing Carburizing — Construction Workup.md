---
Project: Plating Posters Inc
Poster Number: 562
Title: "Loading & Fixturing -- Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 1: Gas Carburizing, Section 1.8)"
Technical Source: Loading and fixturing for gas carburizing -- fixture materials (HT alloys), part spacing, orientation for gas flow and quench, weight limits. Per ASM Handbook Vol. 4 and production best practice.
Process Scope: Gas carburizing loading and fixturing (Stage 2 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GasCarburizing
  - Loading
  - Fixturing
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #562 -- Construction Workup
## Loading & Fixturing -- Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Loading and fixturing is the invisible art of carburizing. Nobody gets promoted for good fixturing -- but bad fixturing produces soft spots, distortion, and rejected loads. This poster covers fixture materials, part spacing requirements, orientation for uniform gas flow and quench, and the nesting problem.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Fixture material comparison (Block B -- HERO):** Four fixture alloy cards comparing Inconel 600, RA330, HH/HK cast alloy, and plain carbon steel (the wrong choice).
2. **Loading rules panel (Block D):** Spacing, orientation, and weight limit guidelines with visual diagrams.
3. **Nesting illustration (Block E):** Good vs. bad loading showing gas flow paths.
4. **Quench orientation strip (Block F):** How fixture orientation affects quench uniformity.

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
  Stage 2 highlighted (Teal)
ZONE 3 -- FIXTURE MATERIALS HERO (4.2"--14.5" / ~10.3")
  Block B: Four fixture material cards
ZONE 4 -- LOADING RULES (14.5"--22.0" / ~7.5")
  Block D: Spacing, orientation, weight limits
ZONE 5 -- NESTING: GOOD VS. BAD (22.0"--28.5" / ~6.5")
  Block E: Gas flow comparison diagrams
ZONE 6 -- QUENCH ORIENTATION (28.5"--32.5" / ~4.0")
  Block F: Fixturing for uniform quench
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING & FIXTURING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gas Carburizing -- Stage 2 of 9` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Fixtures fail silently. A nested part looks fine until inspection reveals a soft spot where gas never reached. Load with intention.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, masked parts  -->  After: Parts fixtured in HT alloy baskets, spaced for gas flow and quench`

---

### ZONE 3 -- Fixture Materials (HERO)

**Section label:** `FIXTURE MATERIALS -- CHOOSE WISELY OR REPLACE OFTEN` -- Y: 4.4".

**BLOCK B -- Four Material Cards (Y: 5.0" to 14.0")**

Four cards in a 2x2 grid:

| Card | X | Y | W | H | Material | Accent |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 5.0" | 11.0" | 4.2" | Inconel 600/601 | `#27AE60` |
| 2 | 12.0" | 5.0" | 11.5" | 4.2" | RA330 | `#2EC4B6` |
| 3 | 0.5" | 9.5" | 11.0" | 4.2" | Cast HH/HK Alloy | `#E8A020` |
| 4 | 12.0" | 9.5" | 11.5" | 4.2" | Plain Carbon Steel | `#E05C5C` |

Each: Rounded rect, fill `#1E2435`, left accent 0.06".

*Card 1 -- Inconel 600/601:*
- Title: `INCONEL 600 / 601` Barlow SemiBold 18 pt `#27AE60`
- Stat: `PREMIUM CHOICE` JetBrains Mono 14 pt `#27AE60`
- Details:
```
- Nickel-chromium alloy (72% Ni, 15% Cr)
- Max service temp: 2150 F (1175 C)
- Excellent carburization resistance
- Excellent oxidation resistance
- High creep strength at carburizing temps
- EXPENSIVE but longest service life
- Best for aerospace / critical applications
```

*Card 2 -- RA330:*
- Title: `RA330` Barlow SemiBold 18 pt `#2EC4B6`
- Stat: `WORKHORSE ALLOY` JetBrains Mono 14 pt `#2EC4B6`
- Details:
```
- 35% Ni, 19% Cr, 1.25% Si
- Max service temp: 2100 F (1150 C)
- Good carburization resistance
- Good balance of cost and performance
- Widely used in commercial heat treating
- Better than HH/HK for fixture life
```

*Card 3 -- Cast HH/HK Alloy:*
- Title: `CAST HH / HK ALLOY` Barlow SemiBold 18 pt `#E8A020`
- Stat: `COST-EFFECTIVE` JetBrains Mono 14 pt `#E8A020`
- Details:
```
- Heat-resistant cast alloy (25% Cr, 12-20% Ni)
- Max service temp: 2000 F (1095 C)
- Moderate carburization resistance
- Heavier than wrought alloys
- Castable into complex basket shapes
- Shorter service life vs. Inconel/RA330
```

*Card 4 -- Plain Carbon Steel (WRONG):*
- Title: `PLAIN CARBON STEEL` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `DO NOT USE` JetBrains Mono 18 pt `#E05C5C`
- Details:
```
- WILL CARBURIZE in the furnace atmosphere
- Becomes brittle and cracks after few cycles
- Warps and distorts under load at 1700 F
- No creep resistance at carburizing temps
- FALSE ECONOMY -- cheap to buy, expensive
  in rejected parts and fixture replacement
```

---

### ZONE 4 -- Loading Rules

**Section label:** `LOADING RULES -- SPACING, ORIENTATION, AND LIMITS` -- Y: 14.7".

**BLOCK D -- Three-column layout (Y: 15.3" to 21.8")**

Three callout boxes side by side:

*Left -- Spacing (X: 0.5", W: 7.33"):*
- Accent: `#2EC4B6`
- Title: `PART SPACING`
```
MINIMUM: 0.25" (6 mm) between parts

WHY:
- Gas must circulate around ALL surfaces
- Touching parts = blocked gas = soft spots
- Carbon only absorbs where gas contacts metal

LARGE PARTS: increase spacing proportionally
  (rule of thumb: 1" per foot of part length)

BARREL/BULK PARTS: avoid; not suitable
  for gas carburizing (unlike plating)
```

*Center -- Orientation (X: 8.17", W: 7.33"):*
- Accent: `#E8A020`
- Title: `PART ORIENTATION`
```
FOR GAS FLOW:
- Orient parts to promote uniform gas
  circulation on all surfaces
- Avoid stacking flat parts directly
  on top of each other
- Use spacers or grid trays between layers

FOR QUENCH:
- Thin sections should enter quench FIRST
  (orient accordingly in basket)
- Parts must not shift during quench
  transfer -- secure fixturing
- Holes and cavities should drain freely
```

*Right -- Weight Limits (X: 15.83", W: 7.67"):*
- Accent: `#E8A020`
- Title: `WEIGHT LIMITS`
```
TYPICAL LOAD CAPACITY:
500--2,000 lb per load
(depends on furnace size and fixture alloy)

CREEP IS THE ENEMY:
- Fixtures under load at 1700 F CREEP
  (slowly deform under sustained stress)
- Overloading accelerates fixture failure
- Track fixture cycles -- replace before
  dimensional tolerance is lost

THERMOCOUPLE PLACEMENT:
- Load thermocouple in densest part of load
- Verifies actual part temperature
  (not just furnace atmosphere temp)
```

---

### ZONE 5 -- Nesting: Good vs. Bad

**Section label:** `NESTING -- THE #1 CAUSE OF SOFT SPOTS` -- Y: 22.2".

**BLOCK E -- Side-by-side panels (Y: 22.9" to 28.3")**

*Left -- GOOD Loading (X: 0.5", W: 11.0"):*
- Rounded rect fill `#1E2435`, left accent `#27AE60`
- Title: `CORRECT: SPACED LOADING` Barlow SemiBold 16 pt `#27AE60`

Visual description (to be rendered as simplified diagram):
```
[Part]  gap  [Part]  gap  [Part]
  |            |            |
  v gas flow   v            v
All surfaces exposed to atmosphere
--> Uniform case depth on all parts
```

- Notes: `Gas circulates freely around each part. Every surface receives equal carbon exposure. Result: uniform ECD, consistent hardness.` Inter Regular 13 pt `#F0EDE8`.

*Right -- BAD Loading (X: 12.0", W: 11.5"):*
- Rounded rect fill `#1E2435`, left accent `#E05C5C`
- Title: `WRONG: NESTED / TOUCHING` Barlow SemiBold 16 pt `#E05C5C`

Visual description:
```
[Part][Part][Part] <-- touching
  |    XX    |
  v  blocked  v
Contact areas get ZERO carbon
--> Soft spots at every contact point
```

- Notes: `Parts touching each other create shadow zones where gas cannot reach. These areas will not carburize. Result: soft spots, failed inspection, scrapped parts.` Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Quench Orientation

**Section label:** `FIXTURING FOR THE QUENCH` -- Y: 28.7".

**BLOCK F -- Four quick-reference cards (Y: 29.4" to 32.3")**

| Card | X | W | Rule |
|---|---|---|---|
| 1 | 0.5" | 5.5" | `THIN SECTIONS FIRST: Orient thin edges to enter oil first -- thickest section last` |
| 2 | 6.33" | 5.5" | `DRAIN HOLES: Cavities, blind holes, and pockets must drain freely -- trapped oil = fire risk` |
| 3 | 12.16" | 5.5" | `NO SHIFTING: Parts must be secured so they cannot move during transfer to quench tank` |
| 4 | 18.0" | 5.5" | `UNIFORM COOLING: Space parts for oil flow -- dense center of load cools slower` |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#2EC4B6`.
Rule title (first phrase): Barlow SemiBold 14 pt `#2EC4B6`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Loading & Fixturing -- Gas Carburizing`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading Fixturing Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The fixture material comparison is the hero because wrong fixture selection is a surprisingly common and expensive mistake. The "DO NOT USE" card for plain carbon steel in Coral is intentionally dramatic -- operators sometimes grab whatever basket is available, and a poster saying "this will carburize and crack" might save someone from a bad load. The nesting section uses simplified diagrams to make the gas-flow concept visual.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #562 -- Construction Workup v1.0*
*2026-04-26*
