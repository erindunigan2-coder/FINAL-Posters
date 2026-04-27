---
created: 2026-04-03T00:00:00
updated: 2026-04-11
version: v2
poster: "#9 — Anodizing Fundamentals: Type I, II, and III at a Glance"
tags:
  - Anodizing
  - PosterResearch
  - ResearchBrief
---

# Anodizing Fundamentals — Alaina Research Brief

**Poster**: #9 — Anodizing Fundamentals: Type I, II, and III at a Glance
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-03 (v1); 2026-04-11 (v2)
**Version**: v2 -- publishable quality; collaboration flags resolved; product names removed from poster content per standing rule; operating parameters cross-verified against MIL-A-8625F via AAC (anodizing.org) and Products Finishing; Type II CD range confirmed at 12--18 ASF per MIL-A-8625 standard; Type III voltage and CD verified; alloy compatibility table confirmed; sticky facts section added
**Source documents**: MIL-A-8625F (Anodic Coatings for Aluminum and Aluminum Alloys); AAC -- Aluminum Anodizers Council (anodizing.org); Products Finishing anodizing references (pfonline.com); 1993 Metal Finishing Guidebook and Directory (vault); Drew's Quick Reference Metal Finishing Notes (vault); domain expertise

---

## Why This Poster Matters

Anodizing is one of the most widely used surface finishing processes for aluminum, yet it is frequently confused with electroplating. Many operators, engineers, and customers do not understand the difference. This poster clarifies what anodizing is, the three standard types, and when each is used -- in a single visual reference.

---

## The Core Concept -- How Anodizing Differs from Electroplating

| Feature | Electroplating | Anodizing |
|---|---|---|
| What is the part? | **Cathode** (negative) | **Anode** (positive) |
| What happens? | Metal ions from solution deposit on the part | Aluminum surface oxidizes -- grows Al2O3 from the substrate |
| Coating material | A different metal (Zn, Ni, Cu, Cr, etc.) | Aluminum oxide (Al2O3) -- integral to the base metal |
| Coating source | Solution (electrolyte supplies the metal) | The part itself (aluminum is consumed to form the oxide) |
| Coating bond | Mechanical/electrochemical adhesion | Integral -- the oxide IS the aluminum, chemically converted |
| Dimensional effect | Adds thickness on top of substrate | Grows ~50% outward and ~50% inward (net gain ~ 50% of total oxide thickness) |
| Applicable substrates | Almost any conductive metal | Aluminum and aluminum alloys (titanium anodizing exists but is a separate process) |

**The key sentence**: "In anodizing, the part IS the anode -- the aluminum surface is electrochemically converted to aluminum oxide (Al2O3), a hard, porous ceramic."

---

## The Anodizing Reaction

At the anode (the aluminum part):

```
2Al + 3H2O --> Al2O3 + 6H+ + 6e-
```

Aluminum atoms at the surface react with water to form aluminum oxide, releasing hydrogen ions and electrons. The oxide grows into the surface (penetrating the aluminum) and outward simultaneously.

At the cathode (typically lead or aluminum counter-electrode):

```
6H+ + 6e- --> 3H2 (gas)
```

Hydrogen gas evolves at the cathode -- not at the part. This is the reverse of electroplating, where H2 evolves at the part.

---

## The Three Types -- MIL-A-8625

### Type I: Chromic Acid Anodize

| Parameter | Value |
|---|---|
| **Electrolyte** | Chromic acid (CrO3), 3--10% w/v |
| **Temperature** | 90--100 deg F (32--38 deg C) |
| **Voltage** | Ramped from 0 to 40 V over 10 min; held at 40 V for 20--35 min |
| **Current density** | 5--10 ASF (voltage-controlled process) |
| **Oxide thickness** | 0.03--0.10 mil (0.8--2.5 um) |
| **Hardness** | Moderate |
| **Color** | Gray to dark gray (undyed); limited dye absorption |
| **Sealing** | Hot water or nickel acetate seal |
| **Key properties** | Excellent fatigue resistance (thin coating = minimal stress); good paint adhesion base; non-conductive |
| **Environmental** | Contains hexavalent chromium -- restricted under RoHS/REACH |

**Primary applications**: Aerospace structural components where fatigue life is critical; paint adhesion base; substrate inspection (thin, somewhat translucent coating allows flaws to show through).

**MIL-A-8625 Class**: Type I, Class 1 (undyed) or Class 2 (dyed)

### Type II: Sulfuric Acid Anodize (Most Common)

| Parameter | Value |
|---|---|
| **Electrolyte** | Sulfuric acid (H2SO4), 15--20% w/v (specific gravity 1.10--1.14) |
| **Temperature** | 68--72 deg F (20--22 deg C) -- temperature control critical |
| **Current density** | 12--18 ASF (1.2--1.8 ASD) |
| **Voltage** | 15--21 V typical |
| **Oxide thickness** | 0.2--1.0 mil (5--25 um) |
| **Hardness** | 300--400 HV (Vickers) |
| **Color** | Clear/transparent (undyed); wide range of dyed colors (black, red, blue, gold, green, etc.) |
| **Sealing** | Hot water seal (200--212 deg F), nickel acetate seal, or dichromate seal |
| **Key properties** | Good corrosion resistance; excellent dye absorption; moderate wear resistance; electrical insulation |

**Primary applications**: Architectural (building facades, window frames); consumer electronics (laptop/phone cases); decorative hardware; general corrosion protection; dyed color finishes.

**MIL-A-8625 Class**: Type II, Class 1 (undyed -- "clear anodize") or Class 2 (dyed)

### Type III: Hard Coat Anodize (Hard Anodize)

| Parameter | Value |
|---|---|
| **Electrolyte** | Sulfuric acid (H2SO4), 10--12% w/v (lower concentration than Type II) |
| **Temperature** | 28--36 deg F (-2 to +2 deg C) -- near freezing; refrigeration required |
| **Current density** | 24--36 ASF (2.4--3.6 ASD) |
| **Voltage** | 40--75+ V (can exceed 100 V on some alloys) |
| **Oxide thickness** | 1.0--4.0 mil (25--100 um); default 2.0 mil if unspecified per MIL-A-8625 |
| **Hardness** | 500--700 HV (Vickers); up to 70 HRC equivalent |
| **Color** | Natural: dark bronze to black (thicker = darker); limited dyeing (dense structure) |
| **Sealing** | Hot water, nickel acetate, or PTFE impregnation for lubricity |
| **Key properties** | Extreme hardness and wear resistance; excellent abrasion resistance; high dielectric strength; corrosion resistant |

**Primary applications**: Hydraulic cylinders; military weapons components; aerospace actuator bores; precision sliding surfaces; pump components; tooling; any application requiring extreme wear resistance on aluminum.

**MIL-A-8625 Class**: Type III, Class 1 (undyed) or Class 2 (dyed -- limited to dark colors)

---

## Comparison Table -- All Three Types at a Glance

| Parameter | Type I (Chromic) | Type II (Sulfuric) | Type III (Hard Coat) |
|---|---|---|---|
| **Electrolyte** | Chromic acid | Sulfuric acid (15--20%) | Sulfuric acid (10--12%) |
| **Temperature** | 90--100 deg F | 68--72 deg F | 28--36 deg F |
| **Current density** | 5--10 ASF | 12--18 ASF | 24--36 ASF |
| **Voltage** | 0--40 V ramp | 15--21 V | 40--75+ V |
| **Thickness** | 0.03--0.10 mil | 0.2--1.0 mil | 1.0--4.0 mil |
| **Hardness** | Moderate | 300--400 HV | 500--700 HV |
| **Dyeability** | Limited | Excellent | Limited (dark only) |
| **Fatigue impact** | Minimal (thin) | Moderate | Significant (thick, brittle) |
| **Environmental** | Cr6+ -- restricted | No Cr6+ | No Cr6+ |
| **Primary use** | Aerospace/fatigue-critical | Decorative/general | Wear/engineering |

---

## The Porous Structure and Sealing

### The Hexagonal Cell Structure

Sulfuric acid anodize (Types II and III) produces a characteristic **honeycomb-like porous structure** -- millions of hexagonal cells with a central pore in each cell. This pore structure is the key to anodizing's unique properties:

- **Dye absorption**: Organic or inorganic dyes are absorbed into the pores, producing permanent color (trapped inside the oxide, not painted on top)
- **Sealing**: The pores must be sealed after dyeing (or after anodizing, even without dye) to close the pore structure and maximize corrosion resistance

### Sealing Methods

| Method | Mechanism | Temperature | Typical Use |
|---|---|---|---|
| **Hot water seal** | Pore walls hydrate and swell (Al2O3 --> AlOOH boehmite) | 200--212 deg F (93--100 deg C) | Standard; most common |
| **Nickel acetate seal** | Nickel hydroxide precipitates in pores + partial hydration | 180--200 deg F (82--93 deg C) | Superior corrosion resistance; aerospace |
| **Dichromate seal** | Chromium compounds fill pores | 190--210 deg F | Military/aerospace; contains Cr6+ |
| **Cold seal (nickel fluoride)** | Room-temperature pore closure | 75--85 deg F | Energy savings; faster cycle |
| **PTFE impregnation** | PTFE particles fill pores; provides lubricity | Variable | Hard coat -- sliding surfaces |

---

## Alloy Effects on Anodizing

Not all aluminum alloys anodize equally:

| Alloy Series | Example | Anodizing Quality | Notes |
|---|---|---|---|
| **1xxx** (pure Al) | 1100 | Excellent | Clear, consistent oxide; best dye absorption |
| **5xxx** (Al-Mg) | 5052 | Very good | Clear to slightly gray; good general anodizing |
| **6xxx** (Al-Mg-Si) | 6061, 6063 | Very good | 6063 is the standard architectural anodizing alloy |
| **2xxx** (Al-Cu) | 2024 | Fair to poor | High copper content produces yellowish, less protective oxide |
| **7xxx** (Al-Zn) | 7075 | Fair | Zinc/copper content affects color and consistency |
| **Cast alloys** | A356, 380 | Variable | Silicon content produces dark, grainy oxide; cosmetic limitations |

**Key point**: The higher the alloying element content (especially copper and silicon), the less consistent and less protective the anodize will be. Pure aluminum and low-alloy 5xxx/6xxx series produce the best results.

---

## Pre-Treatment for Anodizing

The pre-treatment sequence for anodizing differs from electroplating:

```
SOAK CLEAN --> Rinse --> CAUSTIC ETCH (NaOH, 4--8 oz/gal, 140 deg F, 1--5 min) --> Rinse --> DESMUT (HNO3 or HNO3/HF, room temp, 15--60 sec) --> Rinse --> ANODIZE
```

The caustic etch step dissolves a thin layer of aluminum to create a uniform, matte surface. The desmut step removes the dark smut (insoluble alloying element residue) left behind by etching. Both steps are critical for uniform anodize quality.

---

## Common Anodizing Defects

| Defect | Cause | Type Most Affected |
|---|---|---|
| **Uneven color after dyeing** | Inconsistent oxide thickness; alloy variation | Type II |
| **Chalky or powdery oxide** | Temperature too high; acid too concentrated; excessive time | Type II, III |
| **Burning (dissolved oxide)** | Temperature too high; current density too high; poor contact | Type III especially |
| **Soft or thin coating** | Temperature too high; concentration too low; insufficient time | Type III |
| **Poor dye absorption** | Oxide too thin; over-sealed; oxide structure too dense | Type II |
| **Crazing / cracking** | Oxide too thick on thin substrate; thermal shock | Type III |
| **Streaking** | Poor cleaning; alloy segregation; uneven etch | All types |

---

## Visual / Diagram Opportunities for Poster Design

### 1. The Three-Column Comparison (HERO visual)

Three columns (Type I | Type II | Type III) with rows for each parameter. Use the locked palette:
- Type I: Amber `#E8A020` (caution -- Cr6+)
- Type II: Teal `#2EC4B6` (standard, versatile)
- Type III: Emerald `#27AE60` (heavy-duty)

### 2. The Pore Structure Cross-Section

A magnified cross-section showing:
- Aluminum substrate at bottom
- Barrier layer (dense, thin oxide at the base)
- Porous columnar structure (hexagonal cells with central pores)
- Dye molecules trapped in pores (Type II)
- Sealed pore tops (after sealing step)

This is one of the most iconic diagrams in surface finishing.

### 3. The "Part = Anode" Concept Diagram

A simple circuit diagram:
- Part connected to (+) terminal -- labeled "ANODE -- the part IS the anode"
- Counter-electrode connected to (-) terminal
- Arrow: "Oxide grows FROM the aluminum surface"
- Contrast callout: "In electroplating, the part is the CATHODE"

### 4. The Thickness Scale Bar

A horizontal strip showing relative oxide thicknesses:
- Type I: thin sliver (0.03--0.10 mil)
- Type II: medium bar (0.2--1.0 mil)
- Type III: thick bar (1.0--4.0 mil)
- Reference: human hair (~3 mil) for scale

### 5. The Temperature Gradient Strip

A thermometer or color-gradient strip:
- Type I: 90--100 deg F (warm)
- Type II: 68--72 deg F (room temp)
- Type III: 28--36 deg F (near freezing!)

Caption: "Type III runs near freezing -- refrigeration required."

### 6. The Color Wheel (Type II)

A color wheel or palette showing dyed colors available in Type II: black, red, blue, gold, green, bronze, etc. Caption: "Type II's porous structure absorbs dye for permanent color."

### 7. The Hardness Comparison Bar

Horizontal bars:
- Pure aluminum: ~30 HV
- Type II anodize: 300--400 HV
- Type III hard coat: 500--700 HV
- Hard chrome (reference): 900--1100 HV

### 8. The Alloy Compatibility Chart

A small table or grid showing which alloy series anodize well (green) and which are problematic (amber/coral).

### 9. The MIL-A-8625 Specification Badge

A prominent callout: "MIL-A-8625F -- the governing specification for anodic coatings on aluminum."

---

## Key Data Points for Callouts

**The defining difference**:
- "The part IS the anode -- oxide grows from the aluminum itself."

**Type II parameters (most common)**:
- Sulfuric acid: `15--20%`
- Temperature: `68--72 deg F`
- Current density: `12--18 ASF`
- Thickness: `0.2--1.0 mil`

**Type III parameters (hard coat)**:
- Temperature: `28--36 deg F` -- near freezing
- Current density: `24--36 ASF`
- Voltage: `40--75+ V`
- Thickness: `1.0--4.0 mil` (default 2.0 mil per MIL-A-8625)
- Hardness: `500--700 HV`

**Type I (chromic)**:
- Thinnest: `0.03--0.10 mil`
- Cr6+ -- restricted substance

**Governing specification**:
- `MIL-A-8625F`

**Alloy rule of thumb**:
- `6063` = best architectural anodizing alloy
- `2024` = poor anodizing (high copper)

**Dimensional growth**:
- ~50% outward, ~50% inward; net dimensional gain ~ 50% of total oxide thickness

---

## Poster-Worthy Sticky Facts

1. **"The part IS the anode"** -- in anodizing, the workpiece is connected to the positive terminal. The aluminum surface is electrochemically oxidized -- converted into aluminum oxide (Al2O3) ceramic. This is the opposite of electroplating, where the part is the cathode and receives metal from solution. One sentence distinguishes the two processes forever.

2. **"28 degrees -- near freezing"** -- Type III hard coat anodize runs at 28--36 deg F (-2 to +2 deg C). The bath must be refrigerated. This extreme cold is what produces the dense, hard oxide (500--700 HV). Type II runs at room temperature (68--72 deg F). Type I runs warm (90--100 deg F). Three processes, three completely different thermal regimes.

3. **"0.03 mil to 4.0 mil -- a 130x thickness range"** -- Type I produces the thinnest coating (0.03--0.10 mil) for fatigue-critical aerospace parts. Type III produces the thickest (1.0--4.0 mil) for extreme wear resistance. The same fundamental reaction -- aluminum oxidation in acid -- scaled across two orders of magnitude by controlling temperature, concentration, and current.

4. **"6063 is the gold standard"** -- the 6063 aluminum alloy is the preferred substrate for architectural anodizing worldwide. Low alloy content produces a clear, consistent, dye-receptive oxide. High-copper alloys like 2024 produce yellowish, inconsistent coatings. Alloy selection determines anodize quality before the part ever touches the tank.

5. **"The honeycomb holds the color"** -- Type II anodize produces millions of hexagonal pores in the oxide surface. Dye molecules are absorbed into these pores, then sealed in by hot water hydration. The color is inside the ceramic, not painted on top. It cannot be scratched off because it is embedded in the oxide structure itself.

6. **"Seal or fail"** -- an unsealed anodize is a porous sponge that absorbs moisture, stains, and corrodes. Sealing (hot water, nickel acetate, or dichromate) closes the pores and converts the oxide surface to boehmite (AlOOH), creating a dense, corrosion-resistant barrier. Skipping the seal step is one of the most common anodizing failures.

7. **"500--700 HV -- approaching hard chrome territory"** -- Type III hard coat at 500--700 HV rivals many hard chrome deposits (900--1100 HV) for wear resistance. For aluminum components that cannot be chrome plated, hard coat anodize is the primary engineering solution. Add PTFE impregnation and you get both hardness and lubricity.

8. **"MIL-A-8625F -- one spec, three types"** -- the single military specification that governs all three anodizing types. If a drawing calls out anodizing, it references this document. Type + Class defines everything: Type I/II/III for the process, Class 1 (undyed) or Class 2 (dyed) for appearance.

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-04-11. Sources: MIL-A-8625F specification; AAC -- Aluminum Anodizers Council (anodizing.org); Products Finishing anodizing references (pfonline.com); 1993 Metal Finishing Guidebook and Directory (vault); Drew's Quick Reference Metal Finishing Notes (vault); domain expertise. Type I thickness range updated to 0.03--0.10 mil per MIL-A-8625F and AAC guidance. All operating parameters are specification-typical -- verify against specific product TDS for production use.*
