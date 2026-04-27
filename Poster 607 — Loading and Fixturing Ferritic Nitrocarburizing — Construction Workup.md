---
Project: Plating Posters Inc
Poster Number: 607
Title: "Loading & Fixturing -- Ferritic Nitrocarburizing (FNC / QPQ)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 6: FNC / QPQ, Section 6.4)"
Technical Source: FNC loading and fixturing -- low-carbon steel fixtures (fixtures also get treated), wire/rod/hook fixturing for salt bath immersion, orientation for salt drainage, part spacing less critical than gas nitriding (liquid salt provides uniform heat transfer). Per AMS 2753.
Process Scope: Ferritic nitrocarburizing loading and fixturing (Stage 2 continued)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FerriticNitrocarburizing
  - FNC
  - QPQ
  - Loading
  - Fixturing
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #607 -- Construction Workup
## Loading & Fixturing -- Ferritic Nitrocarburizing (FNC / QPQ)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Fixturing for salt bath FNC is fundamentally different from gas-phase processes. Parts are immersed in liquid, so heat transfer is uniform regardless of spacing -- the gas flow concerns that dominate carburizing and nitriding fixturing are irrelevant. Instead, the fixturing priorities are: orientation for salt drainage (no cupping), fixture material compatibility (low-carbon steel works but gets treated too), and safe handling during transfer between baths.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Fixture materials and lifecycle (Block B -- HERO):** Low-carbon steel fixtures, treatment effects, replacement schedule.
2. **Salt drainage orientation panel (Block D):** Why parts must drain cleanly and how to orient them.
3. **Transfer between baths (Block E):** The logistics of moving hot fixtures between FNC bath, oxidizing bath, and rinse.
4. **Loading rules strip (Block F):** Quick-reference loading rules for salt bath operations.

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
  Loading/fixturing context highlighted
ZONE 3 -- FIXTURE MATERIALS HERO (4.2"--14.5" / ~10.3")
  Block B: Fixture materials and lifecycle
ZONE 4 -- SALT DRAINAGE (14.5"--22.0" / ~7.5")
  Block D: Orientation for drainage
ZONE 5 -- BATH-TO-BATH TRANSFER (22.0"--28.5" / ~6.5")
  Block E: Transfer logistics and safety
ZONE 6 -- LOADING RULES (28.5"--32.5" / ~4.0")
  Block F: Quick-reference strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING & FIXTURING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ferritic Nitrocarburizing (FNC / QPQ) -- Salt Bath Operations` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Liquid salt provides uniform heat transfer -- spacing is less critical than gas-phase processes. But drainage is everything. A cupped part traps salt, and trapped salt means contaminated rinse, ruined polish, and failed corrosion performance.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Loading context highlighted: fill `#2EC4B6`, text `#1A1F2E`.
Below: `Before: Clean, preheated parts  -->  After: Parts fixtured for salt bath immersion with proper drainage orientation`

---

### ZONE 3 -- Fixture Materials (HERO)

**Section label:** `FIXTURE MATERIALS -- THE FIXTURES GET TREATED TOO` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Two large cards + one full-width note (Y: 5.0" to 14.0")**

*Card 1 -- Low-Carbon Steel Fixtures (X: 0.5", W: 11.0", H: 4.5"):*
- Title: `LOW-CARBON STEEL FIXTURES` Barlow SemiBold 18 pt `#2EC4B6`
- Accent: left `#2EC4B6`
- Stat: `STANDARD FIXTURE MATERIAL` JetBrains Mono 14 pt `#2EC4B6`
- Details:
```
MATERIAL: 1018, 1020, or similar
low-carbon steel wire, rod, and hooks

WHY IT WORKS:
- Inexpensive and readily fabricated
- Wire bending, welding, and hook-making
  are standard shop skills
- Corrosion resistance from FNC treatment
  extends fixture life

THE TRADE-OFF:
Fixtures get nitrocarburized along with
the parts. Over time, the compound zone
builds up, making fixtures brittle.
Periodic replacement required.
```

*Card 2 -- Fixture Types (X: 12.0", W: 11.5", H: 4.5"):*
- Title: `FIXTURE CONFIGURATIONS` Barlow SemiBold 18 pt `#E8A020`
- Accent: left `#E8A020`
- Stat: `WIRE / ROD / HOOK / BASKET` JetBrains Mono 14 pt `#E8A020`
- Details:
```
HANGING FIXTURES:
- Wire hooks for individual parts
- Rod racks for multiple parts in a row
- Best drainage orientation
- Parts hang vertically = salt drains off

BASKET FIXTURES:
- Wire mesh baskets for small parts
- Mesh must be open enough for salt
  circulation and drainage
- Avoid nesting -- parts trap salt

CUSTOM FIXTURES:
- Fabricated for specific part geometry
- Ensure all surfaces exposed to salt
- Account for drainage on removal
```

*Full-width note (X: 0.5", W: 23.0", Y: 10.0", H: 3.5"):*
- Rounded rect fill `#252B3D`, left accent `#E8A020`
- Title: `FIXTURE REPLACEMENT SCHEDULE` Barlow SemiBold 16 pt `#E8A020`
- Content:
```
Fixtures accumulate compound zone with each cycle. After 50--100+ cycles, the nitride layer makes the fixture
brittle and prone to cracking. Inspect fixtures before every load for cracks, distortion, and excessive buildup.
Replace when: hooks crack or break, wire becomes rigid and brittle, baskets distort under load weight.

COST NOTE: Low-carbon steel fixtures are inexpensive to fabricate. Budget for regular replacement rather than
trying to extend fixture life beyond safe limits. A broken fixture dropping parts into molten salt is a
safety incident, not just a quality issue.
```

---

### ZONE 4 -- Salt Drainage

**Section label:** `DRAINAGE ORIENTATION -- THE CRITICAL FIXTURING RULE` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Two-column layout (Y: 15.3" to 21.8")**

*Left -- Why Drainage Matters (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `WHY DRAINAGE MATTERS` Barlow SemiBold 18 pt `#27AE60`

Content:
```
WHAT HAPPENS WITH TRAPPED SALT:

1. Part removed from salt bath
2. Cup-shaped feature traps molten salt
3. Trapped salt carried into rinse tank
   = contaminated rinse water
4. Residual salt under polish step
   = uneven surface finish
5. Salt residue under Q2
   = staining, discoloration
6. Salt residue on finished part
   = corrosion initiation site

END RESULT:
Failed corrosion test, customer rejection

THE FIX:
Orient every part so that salt drains
freely when the fixture is lifted
from each bath. No cupping. No pockets.
```

*Right -- Orientation Rules (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `ORIENTATION GUIDELINES` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
GENERAL RULES:
- Open end DOWN for cups and cavities
- Bore axis at angle (not horizontal)
  to prevent salt pooling
- Drain holes at lowest point
- Flat parts oriented vertically or
  at angle for sheet drainage

SPECIFIC CASES:
- Cylinders: open end down or tilted
- Gears: hang from bore, teeth drain
- Shafts: vertical on hook
- Small parts in basket: single layer
  preferred; shake basket on removal

WHEN IN DOUBT:
Dip the fixtured load in water first
(before preheat). Watch where water
pools. Those are the salt traps.
Fix the orientation, then proceed.
```

---

### ZONE 5 -- Bath-to-Bath Transfer

**Section label:** `TRANSFER BETWEEN BATHS -- QPQ LOGISTICS` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Transfer sequence (Y: 22.9" to 28.3")**

Full-width rounded rect fill `#1E2435`.

Five-step horizontal flow (left to right):

| Step | Bath | Temp | Transfer Note |
|---|---|---|---|
| 1 | PREHEAT OVEN | 600--700 F | Transfer to FNC bath quickly -- minimize cooling |
| 2 | FNC SALT BATH | 1050--1075 F | Transfer to oxidizing bath quickly -- minimize air exposure |
| 3 | OXIDIZING QUENCH (Q1) | 700--800 F | Lift slowly -- allow salt drainage before rinse |
| 4 | HOT WATER RINSE | Hot | Agitate to remove all salt. Inspect before polish |
| 5 | POLISH -> Q2 -> FINAL RINSE | Various | Standard transfer; final inspection after last rinse |

Each step: Rounded rect W: 4.2", H: 4.5", fill `#252B3D`, top accent 4 pt in appropriate color.
Arrows between steps: 3 pt `#3A4055`.

Below flow:
- `Transfer time between FNC bath and oxidizing quench should be minimized. Extended air exposure between baths can affect compound zone quality.` Inter Medium 13 pt `#E8A020`
- `Always lift fixtures SLOWLY from salt baths to allow drainage and reduce splash risk.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Loading Rules

**Section label:** `LOADING RULES FOR SALT BATH FNC` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four quick-reference cards (Y: 29.4" to 32.3")**

| Card | X | W | Title | Content |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `SPACING` | Less critical than gas processes -- liquid salt provides uniform heat transfer. But avoid part-to-part contact (creates uncoated spots). |
| 2 | 6.33" | 5.5" | `DRAINAGE` | Orient ALL parts for free salt drainage on removal. No cupping. No trapped salt. This is the #1 fixturing priority. |
| 3 | 12.16" | 5.5" | `FIXTURE CONDITION` | Inspect before every load. Replace cracked, brittle, or distorted fixtures. A fixture failure in molten salt is a safety emergency. |
| 4 | 18.0" | 5.5" | `SLOW IMMERSION` | Lower fixtures into salt bath slowly and steadily. Rapid immersion causes splash. Two-person operation for heavy loads. |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Loading & Fixturing -- Ferritic Nitrocarburizing (FNC / QPQ)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2753, AMS 2755, salt bath equipment OEM documentation. Fixture designs vary by part geometry and salt bath configuration. Consult your equipment supplier for load capacity and fixture material recommendations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading Fixturing Ferritic Nitrocarburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Salt drainage is the star of this poster -- it's the fixturing equivalent of "moisture is the enemy" from the safety poster. The water-dip test suggestion in Zone 4 is a practical shop-floor trick that experienced operators use. The bath-to-bath transfer flow (Zone 5) is unique to QPQ and visually communicates the multi-step logistics that make this process more complex than a single-bath treatment.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #607 -- Construction Workup v1.0*
*2026-04-26*
