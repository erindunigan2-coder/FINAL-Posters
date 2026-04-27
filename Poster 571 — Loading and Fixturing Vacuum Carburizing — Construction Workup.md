---
Project: Plating Posters Inc
Poster Number: 571
Title: "Loading & Fixturing -- Vacuum Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC, Section 2.4)"
Technical Source: Loading and fixturing for vacuum carburizing -- CFC (carbon fiber composite) fixtures, ceramic supports, NO alloy steel fixtures, optical pyrometry, blind hole advantage. Per ASM Handbook Vol. 4 and vacuum furnace OEM practice.
Process Scope: Vacuum carburizing loading and fixturing (Stage 2 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - Loading
  - Fixturing
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #571 -- Construction Workup
## Loading & Fixturing -- Vacuum Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Fixturing for vacuum carburizing is a completely different world from gas carburizing. The workhorse alloy fixtures (Inconel, RA330, cast HH/HK) that live in atmosphere furnaces would absorb carbon from the acetylene and self-destruct. Instead, LPC uses CFC (carbon fiber composite) and ceramic fixtures -- lighter, more expensive, but immune to carburization. This poster covers the fixture material story, the blind hole advantage unique to LPC, and temperature measurement in vacuum.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Fixture material comparison (Block B -- HERO):** Three fixture material cards -- CFC, ceramic, and alloy steel (the wrong choice). Mirrors DH-01 #562 structure.
2. **Blind hole advantage panel (Block D):** Why LPC carburizes blind holes better than gas.
3. **Temperature measurement in vacuum (Block E):** Thermocouples vs. optical pyrometry.
4. **Loading rules strip (Block F):** Spacing, orientation, load density.

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
  Block B: Three fixture material cards
ZONE 4 -- BLIND HOLE ADVANTAGE (14.5"--22.0" / ~7.5")
  Block D: LPC mean free path effect
ZONE 5 -- TEMPERATURE MEASUREMENT (22.0"--28.5" / ~6.5")
  Block E: Thermocouples vs. optical pyrometry
ZONE 6 -- LOADING RULES (28.5"--32.5" / ~4.0")
  Block F: Quick-reference loading rules
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING & FIXTURING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vacuum Carburizing (LPC) -- Stage 2 of 9` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Forget everything you know about alloy steel fixtures. In vacuum carburizing, the fixtures are carbon -- CFC and graphite. Steel would carburize itself to destruction in the first cycle.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, dry, masked parts  -->  After: Parts fixtured in CFC/ceramic trays, ready for vacuum chamber`

---

### ZONE 3 -- Fixture Materials (HERO)

**Section label:** `FIXTURE MATERIALS -- CARBON MEETS CARBON (AND THAT'S OK)` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Three Material Cards (Y: 5.0" to 14.0")**

Three cards -- first two in top row, third full-width below:

| Card | X | Y | W | H | Material | Accent |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 5.0" | 11.0" | 4.2" | CFC (Carbon Fiber Composite) | `#27AE60` |
| 2 | 12.0" | 5.0" | 11.5" | 4.2" | Ceramic (SiC / Alumina) | `#2EC4B6` |
| 3 | 0.5" | 9.5" | 23.0" | 4.2" | Alloy Steel -- DO NOT USE | `#E05C5C` |

Each: Rounded rect, fill `#1E2435`, left accent 0.06".

*Card 1 -- CFC:*
- Title: `CFC (CARBON FIBER COMPOSITE)` Barlow SemiBold 18 pt `#27AE60`
- Stat: `PRIMARY FIXTURE MATERIAL FOR LPC` JetBrains Mono 14 pt `#27AE60`
- Details (Inter Regular 13 pt `#F0EDE8`):
```
- Carbon-based: does NOT absorb additional carbon
  from acetylene atmosphere (already saturated)
- Lightweight: 70--80% lighter than alloy steel
  fixtures (faster heating, less energy)
- High-temperature stable: maintains dimensions
  at 1900+ F without creep
- Long fixture life: no carburization degradation
- Machinable: CFC trays, grids, and pins can be
  custom-machined to part geometry
- EXPENSIVE: 5--10x cost of alloy steel fixtures
  BUT lasts 10--50x longer in LPC service
```

*Card 2 -- Ceramic:*
- Title: `CERAMIC (SiC / ALUMINA)` Barlow SemiBold 18 pt `#2EC4B6`
- Stat: `SUPPORT AND PIN MATERIAL` JetBrains Mono 14 pt `#2EC4B6`
- Details:
```
- Silicon carbide (SiC) and alumina (Al2O3)
  pins, rails, and supports
- Chemically inert in acetylene atmosphere
- Excellent high-temperature strength
- Used for: support pins, spacers, rails
  in CFC tray assemblies
- Brittle: handle carefully during loading
- Cannot be machined to complex shapes
  like CFC -- limited to simple geometries
```

*Card 3 -- Alloy Steel (WRONG):*
- Title: `ALLOY STEEL FIXTURES` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `DO NOT USE IN VACUUM CARBURIZING` JetBrains Mono 20 pt `#E05C5C`
- Details (two-column inside card):

Left column:
```
WHY NOT:
- Steel absorbs carbon from acetylene
- Fixtures carburize in the first cycle
- Carburized fixtures become brittle
- Brittle fixtures crack and distort
- Fixture fragments contaminate chamber
```

Right column:
```
THE MATH:
Gas carburizing: steel fixtures last
100--500 cycles in alloy steel
Vacuum carburizing: steel fixtures
may fail in 1--5 cycles

Even Inconel 600 and RA330 are
NOT suitable for LPC service.
CFC is the only correct answer.
```

---

### ZONE 4 -- Blind Hole Advantage

**Section label:** `THE BLIND HOLE ADVANTAGE -- WHY LPC EXCELS AT COMPLEX GEOMETRY` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Two-column layout (Y: 15.3" to 21.8")**

*Left -- The Physics (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `MEAN FREE PATH EFFECT` Barlow SemiBold 18 pt `#2EC4B6`

Content (Inter Regular 13 pt `#F0EDE8`):
```
AT ATMOSPHERIC PRESSURE (gas carburizing):
Gas molecules collide frequently -- mean
free path is very short (~0.0003" / 0.07 um)

Gas has difficulty penetrating:
- Deep blind holes
- Narrow bores
- Internal cavities
- Areas with restricted access

Result: non-uniform case depth in
complex geometry parts

AT 5--15 MBAR (vacuum carburizing):
Mean free path increases dramatically
(~0.1--0.3" / 3--8 mm)

Acetylene molecules travel farther between
collisions and penetrate into:
- Blind holes
- Deep bores
- Internal passages
- Tight geometries

Result: MORE UNIFORM case depth on
complex parts
```

*Right -- Practical Impact (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `WHAT THIS MEANS IN PRACTICE` Barlow SemiBold 18 pt `#27AE60`

Content:
```
PARTS THAT BENEFIT MOST FROM LPC:
- Gears with internal splines
- Shafts with cross-drilled holes
- Parts with keyways and slots
- Fuel injector components
- Any part with L/D ratio > 3:1

GAS CARBURIZING WORKAROUND:
- Requires aggressive agitation
- Fan speed adjustments
- Part orientation optimization
- Still may not achieve uniformity
  in deep blind holes

LPC SOLUTION:
- Low-pressure gas naturally penetrates
- Multiple boost/diffuse pulses ensure
  saturation of complex surfaces
- Uniformity verified by simulation
  software before production
```

Bottom callout (Y: 21.3" to 21.8"):
- Pill bar, fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- `If your part has a blind hole deeper than 3x its diameter, vacuum carburizing will produce a more uniform case than gas carburizing. That is physics, not marketing.` Inter Medium 14 pt `#2EC4B6`, center.

---

### ZONE 5 -- Temperature Measurement

**Section label:** `TEMPERATURE MEASUREMENT IN VACUUM` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Two-column comparison (Y: 22.9" to 28.3")**

*Left -- Thermocouples (X: 0.5", W: 11.0"):*
Rounded rect fill `#1E2435`, left accent `#E8A020`.
Title: `SHEATHED THERMOCOUPLES` Barlow SemiBold 18 pt `#E8A020`

Content:
```
STANDARD METHOD:
- Type K or N base metal TCs
- Must be SHEATHED (ceramic or metal)
  to prevent damage to vacuum system
- Bare TC wire can outgas and contaminate
  the vacuum chamber

PLACEMENT:
- Load TC in heaviest section of load
- Representative of actual part temperature
- Per AMS 2750 requirements

LIMITATION:
- TC sheaths add thermal mass
- Contact resistance between TC and part
  creates measurement lag
- Multiple TCs needed for large loads
```

*Right -- Optical Pyrometry (X: 12.0", W: 11.5"):*
Rounded rect fill `#1E2435`, left accent `#2EC4B6`.
Title: `OPTICAL PYROMETRY` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
EMERGING METHOD:
- Non-contact temperature measurement
  through viewport
- Infrared sensor reads surface temp
  of parts or fixtures directly

ADVANTAGES:
- No physical contact with load
- Real-time surface temperature
- No contamination risk
- Faster response than sheathed TC

LIMITATIONS:
- Requires clean viewport (soot and
  condensation degrade accuracy)
- Emissivity must be known for the
  part surface at temperature
- Not yet accepted by all specs
  (AMS 2750 primarily references TCs)

TREND:
Increasingly used alongside TCs for
cross-verification. May become primary
method as standards evolve.
```

---

### ZONE 6 -- Loading Rules

**Section label:** `LOADING RULES FOR VACUUM CARBURIZING` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four quick-reference cards (Y: 29.4" to 32.3")**

| Card | X | W | Title | Content |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `SPACING` | Same as gas: min 0.25--0.5" between parts. Dense loads may need more boost/diffuse cycles. Uniformity verified by simulation. |
| 2 | 6.33" | 5.5" | `CFC TRAYS` | Handle CFC carefully -- it's strong but brittle at edges. Inspect for cracks before every load. Replace damaged trays immediately. |
| 3 | 12.16" | 5.5" | `ORIENTATION` | Orient parts to promote gas access to all surfaces. Bores open-end-up for acetylene penetration. Drain holes clear. |
| 4 | 18.0" | 5.5" | `LOAD WEIGHT` | CFC trays are lighter than alloy steel = faster heat-up. But maximum load mass still limited by furnace capacity and HPGQ cooling performance. |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#2EC4B6`.
Title: Barlow SemiBold 14 pt `#2EC4B6`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Loading & Fixturing -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7, vacuum furnace OEM documentation. CFC fixture specifications vary by manufacturer -- consult your fixture supplier for load capacity and replacement criteria.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading Fixturing Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "DO NOT USE alloy steel" card is the star of this poster -- it's the single biggest mistake an operator transitioning from gas to vacuum carburizing can make. Making it full-width and Coral-dominant ensures it cannot be missed. The blind hole advantage section (Zone 4) is the technical differentiator that justifies LPC for complex geometry parts -- the mean free path physics is real and the practical impact is significant. The optical pyrometry section plants a forward-looking seed for operators who may see this technology in newer furnaces.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #571 -- Construction Workup v1.0*
*2026-04-26*
