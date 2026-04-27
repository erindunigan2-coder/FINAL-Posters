---
Project: Plating Posters Inc
Poster Number: 570
Title: "Part Preparation -- Vacuum Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC, Section 2.3)"
Technical Source: Part preparation for vacuum carburizing -- cleaning (no moisture, no chlorinated solvents), masking (copper plate + mechanical masking), surface condition, reduced grinding stock (no IGO). Per ASM Handbook Vol. 4 and AMS 2759/7.
Process Scope: Vacuum carburizing part preparation (Stage 1 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - PartPreparation
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #570 -- Construction Workup
## Part Preparation -- Vacuum Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Part prep for vacuum carburizing shares the fundamentals with gas carburizing (clean, mask, inspect) but adds a critical requirement: absolute dryness. Moisture degrades vacuum pump oil and contaminates the chamber. Chlorinated solvents are forbidden. And the masking story includes mechanical masking options that work better in vacuum than in atmosphere. The big payoff? Less grinding stock needed post-carburize because there's no IGO layer to remove.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-pillar layout (Block B -- HERO):** Cleaning, Masking, Surface Condition -- same structure as DH-01 Poster #561 for consistency, but with LPC-specific content.
2. **Vacuum-specific requirements panel (Block D):** What's different about prep for vacuum vs. gas.
3. **Grinding stock comparison (Block E):** LPC vs. gas carburizing -- the IGO advantage quantified.
4. **Checklist strip (Block F):** Pre-load inspection checklist for vacuum carburizing.

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
  Stage 1 highlighted (Teal)
ZONE 3 -- THREE PILLARS HERO (4.2"--14.5" / ~10.3")
  Block B: Cleaning | Masking | Surface Condition
ZONE 4 -- VACUUM-SPECIFIC REQUIREMENTS (14.5"--22.0" / ~7.5")
  Block D: What's different for LPC
ZONE 5 -- GRINDING STOCK COMPARISON (22.0"--28.5" / ~6.5")
  Block E: LPC vs. gas -- the IGO advantage
ZONE 6 -- PRE-LOAD CHECKLIST (28.5"--32.5" / ~4.0")
  Block F: Checklist strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vacuum Carburizing (LPC) -- Stage 1 of 9` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Same fundamentals as gas carburizing -- clean, mask, inspect. But vacuum adds one non-negotiable: absolute dryness. Moisture is the enemy of every vacuum system.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw machined or forged part  -->  After: Clean, dry, masked, ready for vacuum chamber loading`

---

### ZONE 3 -- Three Pillars (HERO)

**Section label:** `THE THREE PILLARS OF PART PREPARATION -- VACUUM EDITION` -- Y: 4.4".

**BLOCK B -- Three Pillar Boxes (Y: 5.0" to 14.0")**

| Pillar | X | W | Accent | Title |
|---|---|---|---|---|
| Cleaning | 0.5" | 7.33" | `#2EC4B6` | CLEANING |
| Masking | 8.17" | 7.33" | `#E8A020` | MASKING |
| Surface Condition | 15.83" | 7.67" | `#27AE60` | SURFACE CONDITION |

Each box: Rounded rect H: 8.8", fill `#1E2435`, left accent 0.06".

*Cleaning pillar:*
- Title: `CLEANING` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Clean AND Dry -- Both Are Non-Negotiable` JetBrains Mono 12 pt `#F0EDE8` at 60%

Content:
```
STANDARD REQUIREMENTS:
Oil-free, grease-free, scale-free
(same as gas carburizing)

VACUUM-SPECIFIC:
- Parts must be COMPLETELY DRY
- Moisture contaminates vacuum pump oil
- Moisture degrades vacuum quality
- Moisture causes outgassing during heating

FORBIDDEN:
- Chlorinated solvents (trichloroethylene,
  methylene chloride) -- degrades pump oil
  and creates toxic byproducts in vacuum
- Silicone-based lubricants (contaminates
  chamber and subsequent loads)

RECOMMENDED CLEANING:
- Hydrocarbon solvent wash (mineral spirits)
- Alkaline wash + thorough rinse
- Forced-air dry or vacuum dry
- Water-break test, then verify DRY
```

*Masking pillar:*
- Title: `MASKING` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Copper Plate + Mechanical Options` JetBrains Mono 12 pt `#F0EDE8` at 60%

Content:
```
COPPER ELECTROPLATE:
- 0.001--0.002" Cu minimum (same as gas)
- Remains the standard for selective
  carburizing in vacuum
- Effective carbon diffusion barrier

MECHANICAL MASKING:
- Tight-fitting metal caps or plugs
- MORE EFFECTIVE in vacuum than in gas:
  low operating pressure means gas does
  not penetrate tight mechanical seals
- Used for bores, threads, blind holes
- Advantage: no plating setup required

STOP-OFF PAINT:
- Same commercial products as gas carb
- Verify paint is vacuum-compatible
  (no volatile binders that outgas)
- Less common in LPC -- mechanical
  masking is preferred
```

*Surface Condition pillar:*
- Title: `SURFACE CONDITION` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `Same Standards, Better Outcome` JetBrains Mono 12 pt `#F0EDE8` at 60%

Content:
```
ACCEPTABLE:
- Machined, ground, or formed surfaces
- Scale removed (no heavy oxide)
- Deburring complete

NOT ACCEPTABLE:
- Rust, corrosion, or pitting
- Heavy mill scale
- Residual EDM recast layer
- Decarburized layer from prior heat treat

THE PAYOFF:
Because LPC produces NO IGO, the
post-carburize grinding stock can be
REDUCED by 0.001--0.002" per surface
vs. gas carburizing.

This means less pre-carburize oversize
= less total machining = cost savings.
```

---

### ZONE 4 -- Vacuum-Specific Requirements

**Section label:** `WHAT'S DIFFERENT ABOUT PREP FOR VACUUM?` -- Y: 14.7".

**BLOCK D -- Two-column layout (Y: 15.3" to 21.8")**

*Left -- Critical Differences (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#E05C5C`.

Title: `VACUUM-CRITICAL REQUIREMENTS` Barlow SemiBold 18 pt `#E05C5C`

Content:
```
1. ABSOLUTE DRYNESS
   Any residual moisture will:
   - Degrade vacuum pump oil
   - Increase pump-down time
   - Cause outgassing during heating
   - Affect vacuum quality (base pressure)
   - Potentially oxidize part surfaces

2. NO CHLORINATED SOLVENTS
   Chlorinated compounds decompose in
   vacuum to produce:
   - Hydrochloric acid (corrodes chamber)
   - Toxic chlorine gas
   - Pump oil contamination

3. NO SILICONE CONTAMINATION
   Silicone forms SiO2 on hot surfaces
   that contaminates the chamber and
   transfers to subsequent loads.

4. OUTGASSING AWARENESS
   Any volatile material on the part
   will evaporate in vacuum and either:
   - Contaminate the chamber
   - Affect the acetylene atmosphere
   - Deposit on cold surfaces (viewport)
```

*Right -- Best Practices (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `BEST PRACTICES FOR VACUUM PREP` Barlow SemiBold 18 pt `#27AE60`

Content:
```
CLEANING SEQUENCE:
1. Alkaline soak clean (140--160 F, 10 min)
2. Hot rinse (min 2 stages)
3. Forced-air dry (150+ F air)
4. Vacuum dry (if available -- best method)
5. Visual inspection: no water droplets,
   no staining, no residue

STORAGE AFTER CLEANING:
- Process within 4 hours of cleaning
- If delay >4 hours: re-clean and dry
- Store in clean, dry environment
- Cover with clean kraft paper or
  lint-free cloth (not plastic wrap)

HANDLING:
- Clean gloves only (no fingerprints)
- No bare-hand contact after cleaning
- Fingerprints = localized contamination
  = non-uniform carburizing
```

---

### ZONE 5 -- Grinding Stock Comparison

**Section label:** `THE IGO ADVANTAGE -- LESS GRINDING, LESS MACHINING, LESS COST` -- Y: 22.2".

**BLOCK E -- Side-by-side panels (Y: 22.9" to 28.3")**

*Left -- Gas Carburizing (X: 0.5", W: 11.0"):*
Rounded rect fill `#1E2435`, left accent `#E8A020`.
Title: `GAS CARBURIZING` Barlow SemiBold 18 pt `#E8A020`

Content:
```
IGO LAYER: 0.0005--0.001" (0.013--0.025 mm)
at surface, along grain boundaries

GRINDING STOCK REQUIRED:
0.005--0.015" (0.13--0.38 mm) per surface

WHY:
- IGO layer MUST be removed by grinding
- IGO weakens the case at the surface
- AGMA requires min 0.002" removal
  to eliminate IGO on gear teeth

COST IMPACT:
- More pre-carburize machining (oversize)
- More post-carburize grinding
- More material removed = more time
```

*Right -- Vacuum Carburizing (X: 12.0", W: 11.5"):*
Rounded rect fill `#1E2435`, left accent `#27AE60`.
Title: `VACUUM CARBURIZING (LPC)` Barlow SemiBold 18 pt `#27AE60`

Content:
```
IGO LAYER: ZERO
No O2, CO2, or H2O in vacuum atmosphere
= no intergranular oxidation

GRINDING STOCK REQUIRED:
0.003--0.010" (0.08--0.25 mm) per surface
(reduced by 0.001--0.002" vs. gas)

WHY:
- No IGO to remove
- Grinding stock only for dimensional
  control and surface finish
- Some specs allow as-carburized surface
  for non-critical areas

COST SAVINGS:
- Less pre-carburize oversize machining
- Less post-carburize grinding time
- Savings compound on high-volume parts
```

Bottom callout (Y: 27.8" to 28.3"):
- Pill bar, fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `Zero IGO is not just a metallurgical advantage -- it's a manufacturing cost advantage. Less grinding stock = less total machining on every part.` Inter Medium 14 pt `#27AE60`, center.

---

### ZONE 6 -- Pre-Load Checklist

**Section label:** `PRE-LOAD INSPECTION CHECKLIST -- VACUUM CARBURIZING` -- Y: 28.7".

**BLOCK F -- Checklist strip (Y: 29.4" to 32.3")**

Rounded rect full width, fill `#1E2435`. Eight items in two columns:

Left:
```
[ ] Parts visually clean -- no oil, grease, or fingerprints
[ ] Parts COMPLETELY DRY -- no water droplets or staining
[ ] All masked areas verified -- Cu plate or mechanical caps
[ ] No chlorinated solvent residue (verify cleaning method)
```

Right:
```
[ ] Surface condition acceptable per drawing
[ ] Parts handled with clean gloves only
[ ] Parts identified / lot tracked
[ ] Time since cleaning < 4 hours (re-clean if exceeded)
```

Checkbox: Rounded rect 0.25" x 0.25", border 1 pt `#2EC4B6`, no fill.
Text: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Part Preparation -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2759/7, ASM Handbook Vol. 4, vacuum furnace OEM best practices. Cleaning and dryness requirements may vary by furnace manufacturer -- consult your OEM manual.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Preparation Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "absolute dryness" theme runs through this poster like a drumbeat. Gas carburizing operators may not realize how critical moisture control is for vacuum systems -- it's not just about part quality, it's about protecting a very expensive piece of equipment. The grinding stock comparison (Zone 5) quantifies the IGO advantage in terms any machinist or production manager understands: less stock removal = less time = less money. The mechanical masking option is a genuine LPC advantage that operators transitioning from gas carburizing should know about.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #570 -- Construction Workup v1.0*
*2026-04-26*
