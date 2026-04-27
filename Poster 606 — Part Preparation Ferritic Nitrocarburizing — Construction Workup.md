---
Project: Plating Posters Inc
Poster Number: 606
Title: "Part Preparation -- Ferritic Nitrocarburizing (FNC / QPQ)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 6: FNC / QPQ, Section 6.3)"
Technical Source: FNC part preparation -- no pre-Q&T required (unlike gas nitriding), surface cleanliness and dryness critical (moisture/salt explosion), masking options (mechanical only -- copper plate NOT effective), preheat as safety-critical step. Per AMS 2753.
Process Scope: Ferritic nitrocarburizing part preparation (Stages 1-2 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FerriticNitrocarburizing
  - FNC
  - QPQ
  - PartPreparation
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #606 -- Construction Workup
## Part Preparation -- Ferritic Nitrocarburizing (FNC / QPQ)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Part prep for FNC is simpler than gas nitriding in one critical way: parts do NOT need to be pre-quenched-and-tempered. FNC can be applied to as-machined, normalized, or annealed parts. But the cleanliness and dryness requirements are extreme -- not because of metallurgical concerns but because moisture + molten salt = explosion. The preheat step is a safety procedure as much as a process step.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-pillar layout (Block B -- HERO):** Cleaning, Preheat (safety-critical), Masking.
2. **No pre-Q&T required callout (Block D):** The big advantage over gas nitriding.
3. **Preheat detail panel (Block E):** Why preheat is mandatory and what happens if you skip it.
4. **Checklist strip (Block F):** Pre-immersion inspection checklist.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 18.5" / 25.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 1 and 2 highlighted
ZONE 3 -- THREE PILLARS HERO (4.2"--14.5" / ~10.3")
  Block B: Cleaning | Preheat | Masking
ZONE 4 -- NO PRE-Q&T CALLOUT (14.5"--18.5" / ~4.0")
  Block D: FNC vs. gas nitriding prep comparison
ZONE 5 -- PREHEAT DETAIL (18.5"--25.5" / ~7.0")
  Block E: Why preheat is mandatory
ZONE 6 -- PRE-IMMERSION CHECKLIST (25.5"--32.5" / ~7.0")
  Block F: Checklist strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ferritic Nitrocarburizing (FNC / QPQ) -- Stages 1 and 2 of 9` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `No pre-quench-and-temper needed -- FNC works on as-machined parts. But every surface must be clean and absolutely dry before it goes near molten salt. The preheat step is not optional -- it is the line between a safe immersion and a steam explosion.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 1 and 2 highlighted: Stage 1 fill `#2EC4B6` (Clean), Stage 2 fill `#E8A020` (Preheat). Others dimmed.
Below: `Before: Raw parts from machining  -->  After: Clean, preheated, ready for salt bath immersion`

---

### ZONE 3 -- Three Pillars (HERO)

**Section label:** `THREE REQUIREMENTS: CLEAN, DRY, AND DRY AGAIN` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Three Pillar Cards (Y: 5.0" to 14.0")**

| Card | X | Y | W | H | Pillar | Accent |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 5.0" | 7.33" | 8.5" | Cleaning | `#2EC4B6` |
| 2 | 8.17" | 5.0" | 7.33" | 8.5" | Preheat | `#E8A020` |
| 3 | 15.83" | 5.0" | 7.67" | 8.5" | Masking | `#C8D0D8` |

Each: Rounded rect, fill `#1E2435`, left accent 0.06".

*Card 1 -- Cleaning:*
- Title: `CLEANING` Barlow SemiBold 20 pt `#2EC4B6`
- Stat: `CLEAN + DRY = SAFE` JetBrains Mono 14 pt `#2EC4B6`
- Details:
```
ALKALINE WASH:
- Aqueous alkaline solution
- Remove all oils, cutting fluids,
  chips, and surface contaminants
- Rinse thoroughly

DRY COMPLETELY:
- Forced air or oven drying
- No visible moisture anywhere
- Check blind holes, threads,
  and internal cavities for
  trapped water

CONTAMINANTS TO REMOVE:
- Cutting fluid residue
- Rust preventative oils
- Fingerprints (handle with gloves)
- Paint or marking compounds
- Soap residue from wash

WHY IT MATTERS:
- Cutting fluid residue contaminates
  the salt bath (organic buildup)
- Soap residue causes foaming
- Any moisture causes steam explosion
```

*Card 2 -- Preheat:*
- Title: `PREHEAT` Barlow SemiBold 20 pt `#E8A020`
- Stat: `600--700 F / 316--371 C` JetBrains Mono 18 pt `#E8A020`
- Details:
```
MANDATORY SAFETY STEP:

Temperature: 600--700 F (316--371 C)
Atmosphere: Air or protective
Time: Until parts reach temperature
  throughout (15--30 min typical)

PURPOSE:
- Drives off ALL residual moisture
  that cleaning and drying missed
- Evaporates moisture trapped in
  blind holes and deep features
- Brings parts to temperature to
  reduce thermal shock in salt bath

THIS IS NOT OPTIONAL:
The preheat step prevents steam
explosions. It is a safety procedure
first, a process step second.

VERIFY:
Parts must be visibly dry and at
preheat temperature BEFORE transfer
to the nitrocarburizing salt bath.
```

*Card 3 -- Masking:*
- Title: `MASKING` Barlow SemiBold 20 pt `#C8D0D8`
- Stat: `MECHANICAL MASKING ONLY` JetBrains Mono 14 pt `#C8D0D8`
- Details:
```
WHAT WORKS:
- Tight-fitting metal caps/plugs
- Threaded plugs in tapped holes
- Close-tolerance mechanical masks
  that exclude salt from protected
  areas

WHAT DOES NOT WORK:
- Copper plate (NOT effective
  as stop-off for FNC -- nitrogen
  diffuses through copper)
- Standard stop-off paints
  (dissolve in molten salt)

PRACTICAL NOTE:
Most FNC/QPQ parts are fully
treated -- masking is less common
than in carburizing or nitriding.
When selective treatment IS needed,
mechanical masking is the only
reliable option.
```

---

### ZONE 4 -- No Pre-Q&T Callout

**BLOCK D -- Full-width comparison (Y: 14.7" to 18.3")**

Rounded rect fill `#1E2435`, left accent `#27AE60`, H: 3.3".

Title: `FNC DOES NOT REQUIRE PRE-QUENCH-AND-TEMPER` Barlow SemiBold 20 pt `#27AE60`

Two-column:

*Left -- GAS NITRIDING:*
```
Part MUST be quenched and tempered
BEFORE nitriding. Temper temp must
exceed nitriding temp by 50 F minimum.
Core hardness set before process.

This adds a full heat treat cycle
before the nitriding operation.
```
Inter Regular 13 pt `#F0EDE8`. Label: `#E8A020`.

*Right -- FNC / QPQ:*
```
Part can be as-machined, normalized,
or annealed. No pre-Q&T required.

FNC operates below Ac1 -- no phase
transformation occurs. The existing
microstructure is preserved.

Saves an entire heat treat cycle
and simplifies the supply chain.
```
Inter Regular 13 pt `#F0EDE8`. Label: `#27AE60`.

---

### ZONE 5 -- Preheat Detail

**Section label:** `PREHEAT: THE SAFETY-CRITICAL STEP` -- Y: 18.7". Barlow Condensed ExtraBold 28 pt `#E8A020`.

**BLOCK E -- Two-column layout (Y: 19.3" to 25.3")**

*Left -- What Happens If You Skip It (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#E05C5C`.

Title: `IF PREHEAT IS SKIPPED` Barlow SemiBold 18 pt `#E05C5C`

Content:
```
SCENARIO: Part with residual moisture
(even condensation) immersed directly
into 1050 F salt bath.

WHAT HAPPENS:
1. Water contacts molten salt
2. Water flashes to steam instantly
   (1,600x volume expansion)
3. Steam explosion ejects molten salt
   from the bath
4. Salt spray radius: 6+ feet
5. Personnel in splash zone receive
   severe burns from adhering salt
6. Equipment damage, floor contamination
7. Regulatory investigation

THIS HAS HAPPENED.
It will happen again wherever preheat
is treated as optional.
```

*Right -- Correct Preheat Procedure (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `CORRECT PREHEAT PROCEDURE` Barlow SemiBold 18 pt `#27AE60`

Content:
```
1. Parts cleaned and dried (Stage 1)

2. Load parts on fixtures/racks

3. Place in preheat oven or furnace
   at 600--700 F (316--371 C)

4. Hold until parts reach temperature
   throughout (15--30 minutes for
   typical load sizes)

5. Inspect for visible moisture:
   - Check blind holes
   - Check threads and keyways
   - Check between nested parts
   - Any doubt? Extend preheat time.

6. Transfer DIRECTLY to salt bath
   Minimize time between preheat
   and immersion (condensation risk
   in humid environments)

7. Immerse SLOWLY -- controlled lowering
   into salt bath to avoid splash
```

---

### ZONE 6 -- Pre-Immersion Checklist

**Section label:** `PRE-IMMERSION CHECKLIST` -- Y: 25.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Six checklist cards (Y: 26.4" to 32.3")**

Two rows of three cards:

| Position | Title | Content |
|---|---|---|
| R1C1 | CLEANED? | Alkaline wash complete. No visible oil, chips, or cutting fluid residue on any surface. |
| R1C2 | DRIED? | Force air or oven dried. No visible moisture. Blind holes and threads inspected. |
| R1C3 | PREHEATED? | Parts at 600--700 F throughout. Held for minimum 15 minutes. Transfer without delay. |
| R2C1 | MASKED? | If selective treatment: mechanical masks installed and tight-fitting. No copper plate. |
| R2C2 | FIXTURED? | Parts oriented to allow salt drainage on removal. No cupping. Drain holes clear. |
| R2C3 | SALT BATH READY? | Bath at 1050--1075 F. Cyanate content verified (35--40% CNO). Sludge cleared. |

Each: Rounded rect W: 7.33", H: 2.7", fill `#1E2435`, left accent `#2EC4B6`.
Title: Barlow SemiBold 14 pt `#2EC4B6`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Part Preparation -- Ferritic Nitrocarburizing (FNC / QPQ)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2753, AMS 2755, salt bath equipment OEM documentation. Preheat procedures are safety-critical -- consult your EHS department and equipment supplier for site-specific requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Preparation Ferritic Nitrocarburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The preheat step dominates this poster -- by design. It appears in the three-pillar hero, the comparison callout, the detailed Zone 5 panel, and the checklist. Repetition is intentional: in a shop environment, the operator who remembers "preheat is mandatory" is the operator who prevents the steam explosion. The "no pre-Q&T required" callout (Zone 4) is the metallurgical payoff -- it's the reason FNC is commercially attractive compared to gas nitriding for many applications.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #606 -- Construction Workup v1.0*
*2026-04-26*
