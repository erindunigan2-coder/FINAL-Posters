---
created: 2026-04-26T00:00:00
version: v1
subject: "Anodizing Process Clusters -- 8 Clusters x 8 Posters = 64 Posters"
tags:
  - Anodizing
  - PosterResearch
  - ResearchBrief
  - ClusterBrief
---

# Anodizing Clusters -- Watson Research Brief

**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-26
**Version**: v1
**Purpose**: Comprehensive technical research brief covering 8 anodizing process clusters (64 total posters). Alaina will use this brief to write Construction Workups for each poster.
**Sources**: MIL-A-8625F; Boeing BAC 5555 / BAC 5632; AAC -- Aluminum Anodizers Council (anodizing.org); Products Finishing (pfonline.com); finishing.com forums; OSHA hexavalent chromium standards (29 CFR 1910.1026); ASTM B580; ASTM B117; ASTM B921; domain expertise; Watson Poster #9 research brief (vault). Gemini quota exhausted -- all data sourced from web search, web fetch, and domain expertise.

---

## Table of Contents

1. [Cluster 1 -- Sulfuric Acid Anodizing (Type II)](#cluster-1----sulfuric-acid-anodizing-type-ii)
2. [Cluster 2 -- Hardcoat Anodizing (Type III)](#cluster-2----hardcoat-anodizing-type-iii)
3. [Cluster 3 -- Chromic Acid Anodizing (Type I)](#cluster-3----chromic-acid-anodizing-type-i)
4. [Cluster 4 -- Boric-Sulfuric Acid Anodizing (BSAA)](#cluster-4----boric-sulfuric-acid-anodizing-bsaa)
5. [Cluster 5 -- Phosphoric Acid Anodizing (PAA)](#cluster-5----phosphoric-acid-anodizing-paa)
6. [Cluster 6 -- Bright Anodizing](#cluster-6----bright-anodizing)
7. [Cluster 7 -- Integral Color Anodizing](#cluster-7----integral-color-anodizing)
8. [Cluster 8 -- Two-Step (Electrolytic) Color Anodizing](#cluster-8----two-step-electrolytic-color-anodizing)
9. [Cross-Cluster Reference: Safety and Regulatory](#cross-cluster-reference-safety-and-regulatory)
10. [Cross-Cluster Reference: Alloy Compatibility Master Table](#cross-cluster-reference-alloy-compatibility-master-table)
11. [Cross-Cluster Reference: Sealing Methods Master Table](#cross-cluster-reference-sealing-methods-master-table)

---

# Cluster 1 -- Sulfuric Acid Anodizing (Type II)

*The workhorse. Most common anodizing process worldwide. Decorative, protective, and dye-receptive.*

## 1.1 Process Flow Poster Data

### What It Is
Type II sulfuric acid anodizing electrochemically converts the aluminum surface into aluminum oxide (Al2O3) by making the workpiece the anode in a dilute sulfuric acid electrolyte. The oxide grows both inward (~50%) and outward (~50%) from the original surface, producing a porous columnar structure with hexagonal cells. This porous structure absorbs dyes and, after sealing, provides excellent corrosion resistance.

### What It Produces
- A porous aluminum oxide coating 0.2--1.0 mil (5--25 um) thick
- Hardness: 300--400 HV
- Clear/transparent when undyed; accepts a wide range of organic and inorganic dyes
- Electrically insulating; corrosion-resistant; wear-resistant (moderate)

### Best/Worst Alloys

| Rating | Alloy Series | Examples | Notes |
|---|---|---|---|
| Excellent | 1xxx (pure Al) | 1100 | Clearest, most uniform oxide; best dye uptake |
| Very Good | 5xxx (Al-Mg) | 5052, 5005 | Clear to slightly gray; reliable |
| Very Good | 6xxx (Al-Mg-Si) | 6061, 6063 | 6063 = gold standard for architectural anodizing |
| Fair | 7xxx (Al-Zn) | 7075 | Zinc/copper affect color consistency |
| Poor | 2xxx (Al-Cu) | 2024 | High copper = yellowish, less protective oxide |
| Variable | Cast alloys | A356, 380 | High silicon = dark, grainy, cosmetically limited |

### Full Process Sequence

```
Receiving/Racking --> Soak Clean (alkaline, non-etch) --> Rinse --> Caustic Etch (NaOH) --> Rinse -->
Desmut/Deoxidize (acid) --> Rinse --> Anodize (H2SO4) --> Rinse --> [Dye (optional)] --> Rinse -->
Seal (hot water or nickel acetate) --> Rinse --> Dry --> Inspect --> Pack/Ship
```

### Applicable Specifications
- **MIL-A-8625F, Type II, Class 1 (undyed) or Class 2 (dyed)**
- **ASTM B580** -- Standard Specification for Anodic Oxide Coatings on Aluminum
- **AMS 2471** -- Anodic Treatment of Aluminum Alloys, Sulfuric Acid Process, Undyed
- **AMS 2472** -- Anodic Treatment of Aluminum Alloys, Sulfuric Acid Process, Dyed
- **AAMA 611** -- Voluntary Specification for Anodized Architectural Aluminum (architectural)
- **Qualanod** -- European quality label for architectural anodizing

---

## 1.2 Cleaning Stage

### Cleaner Type
Non-etch alkaline soak cleaner formulated for aluminum. Must NOT contain free caustic (NaOH) or strong alkali that would etch the aluminum surface. Typically a blend of sodium metasilicate, sodium carbonate, surfactants, and chelating agents. Mildly alkaline (pH 9--11).

### Parameters

| Parameter | Value |
|---|---|
| **Type** | Non-etch alkaline soak cleaner |
| **Concentration** | 4--8 oz/gal (30--60 g/L) |
| **Temperature** | 140--160 deg F (60--71 deg C) |
| **Time** | 3--10 min (rack); 2--5 min (barrel) |
| **pH** | 9--11 |
| **Agitation** | Air or mechanical; enhances cleaning |

### What "Clean" Means
The surface must be free of:
- Oils, greases, and drawing compounds
- Fingerprints and handling soils
- Adhesive residues and marking inks
- Buffing compounds and polishing residues

A water-break-free surface is the standard test: rinse water should sheet uniformly across the entire part with no beading or dewetting.

### Common Cleaning Problems
- **Residual oil** --> causes uneven etch and anodize "fish eyes" or bare spots
- **Silicate residue** from cleaner --> can inhibit etch and cause streaking
- **Etching during cleaning** --> if cleaner is too alkaline or temperature too high, surface damage occurs before the intentional etch step
- **Smut from cleaner** --> some alkaline cleaners generate a light smut on high-copper or high-silicon alloys even at low pH; must be addressed in desmut

---

## 1.3 Rinse (Pre-Etch)

### Purpose
Remove all alkaline cleaner residue before caustic etch. Prevents contamination of etch tank.

### Parameters

| Parameter | Value |
|---|---|
| **Type** | Flowing ambient water rinse (city or DI) |
| **Temperature** | Ambient (60--85 deg F / 15--30 deg C) |
| **Time** | 30--60 sec immersion; or spray rinse |
| **Conductivity target** | < 50 uS/cm for critical work; < 200 uS/cm for commercial |
| **Flow** | Counter-flow dual rinse preferred for water conservation |

### Key Points
- Drag-out of alkaline cleaner raises etch bath pH and depletes free caustic -- rinse thoroughly
- Inadequate rinsing causes staining and uneven etch patterns

---

## 1.4 Etch Stage

### Chemistry
Caustic (alkaline) etch using sodium hydroxide (NaOH). Dissolves a thin layer of aluminum to produce a uniform matte (satin) texture, remove minor surface defects (scratches, die lines, tool marks), and ensure uniform oxide growth in the anodize tank.

### Parameters

| Parameter | Value |
|---|---|
| **Chemical** | Sodium hydroxide (NaOH) -- caustic soda |
| **Concentration** | 4--8 oz/gal (30--60 g/L) free NaOH; total NaOH may be 50--100 g/L as Al dissolves |
| **Temperature** | 130--160 deg F (55--71 deg C) |
| **Time** | 1--5 min (cosmetic etch: 2--5 min; dimensional etch: 30--90 sec) |
| **Dissolved aluminum** | Control at 25--50 g/L for stable etch rate; >60 g/L = sluggish etch |
| **Etch rate** | ~0.001 in/surface/min at 140 deg F and 6 oz/gal NaOH |

### Role of Etch
1. **Texture**: Produces uniform matte/satin finish by leveling micro-roughness
2. **Defect removal**: Removes scratches, die lines, handling marks
3. **Alloy homogenization**: Dissolves surface-segregated alloying elements
4. **Oxide removal**: Strips native oxide for fresh aluminum surface

### Smut Formation
When aluminum dissolves in caustic, insoluble alloying elements (Cu, Fe, Si, Mn, Zn) remain on the surface as a dark residue called "smut." The smut MUST be removed in the desmut step or it will cause non-uniform anodizing.

- **High-Cu alloys (2024, 2014)**: Heavy dark copper-rich smut
- **High-Si alloys (cast, 4xxx)**: Gray/black silicon-rich smut
- **6061, 6063**: Light gray smut -- easily removed
- **7075**: Moderate smut (zinc + copper residues)

### Etch Alternatives
- **Non-etch (bright) path**: Skip caustic etch entirely; use chemical polish (bright dip) instead -- see Cluster 6
- **Acid etch**: Some shops use acid etch (fluoride-bearing) as an alternative to caustic for certain alloys; produces a finer matte texture

---

## 1.5 Deoxidize / Desmut Stage

### Purpose
Remove the dark smut left by caustic etching. Also dissolves any remaining native oxide and prepares a chemically clean, smut-free aluminum surface for anodizing.

### Chemistry Options

| Desmut Type | Composition | Concentration | Temp | Time |
|---|---|---|---|---|
| **Nitric acid** (standard) | HNO3 | 25--50% v/v (specific gravity 1.15--1.32) | Ambient (60--85 deg F) | 15--60 sec |
| **Ferric sulfate + sulfuric** | Fe2(SO4)3 + H2SO4 | 3--6 oz/gal ferric sulfate + 10--15% H2SO4 | 80--100 deg F | 2--10 min |
| **Nitric + HF** (high-Cu/Si alloys) | HNO3 + HF | 50% HNO3 + 1--3% HF (48%) | Ambient | 15--60 sec |
| **Proprietary chromic-free** | Varies (peroxide, persulfate, ferric-based) | Per vendor TDS | Per TDS | Per TDS |

### Alloy-Specific Considerations

| Alloy | Smut Character | Recommended Desmut |
|---|---|---|
| **6061 / 6063** | Light gray; easy | Straight nitric acid (50%) works fine |
| **2024** | Heavy dark copper smut | Nitric + HF (1--3%) or ferric sulfate; straight nitric struggles |
| **7075** | Moderate copper/zinc smut | Nitric + HF or ferric sulfate preferred |
| **Cast (A356, 380)** | Heavy silicon smut | Nitric + HF essential; may need extended time |
| **5052** | Light smut | Straight nitric acid adequate |

### Why Desmut Is Critical
- Residual smut under the anodic oxide causes:
  - Non-uniform coating thickness
  - Color variation after dyeing
  - Poor corrosion resistance (smut acts as discontinuity)
  - Adhesion failure of the oxide
- A properly desmutted surface is bright, clean, and uniformly reflective (or uniformly matte if etched)

---

## 1.6 Rinse (Pre-Anodize)

### Purpose
Remove all desmut acid from the part surface before entering the anodize tank. Acid drag-in to the anodize tank is less problematic than alkaline drag-in (since the anodize bath is acid), but excessive drag-in raises dissolved aluminum and sulfate levels.

### Parameters

| Parameter | Value |
|---|---|
| **Type** | Flowing ambient water rinse |
| **Temperature** | Ambient |
| **Time** | 30--60 sec |
| **Note** | DI water rinse preferred for critical/aerospace work to avoid chloride contamination from city water |

---

## 1.7 Anodize Main Tank

### Electrolyte and Parameters

| Parameter | Value |
|---|---|
| **Electrolyte** | Sulfuric acid (H2SO4) |
| **Concentration** | 15--20% w/v (165--225 g/L; 22--30 oz/gal) |
| **Specific gravity** | 1.10--1.14 |
| **Temperature** | 68--72 deg F (20--22 deg C) -- critical control parameter |
| **Current density** | 12--18 ASF (1.3--2.0 A/dm2) |
| **Voltage** | 15--21 V typical |
| **Time** | 20--60 min depending on desired thickness |
| **Dissolved aluminum** | Maintain below 20 g/L; >25 g/L degrades coating quality |
| **Cathode material** | Lead (Pb), lead-tin alloy, or aluminum (6063) |
| **Cathode-to-anode ratio** | 1:1 to 2:1 |
| **Agitation** | Air agitation required; uniform solution flow across parts |

### Film Formation Mechanism
1. At the anode (part): 2Al + 3H2O --> Al2O3 + 6H+ + 6e-
2. Simultaneously, H2SO4 dissolves the oxide at the pore bases, creating the characteristic porous columnar structure
3. Growth rate: ~0.7 mil/hr at 18 ASF, 70 deg F, 18% H2SO4
4. Film grows ~50% inward (into aluminum) and ~50% outward (above original surface)

### Film Thickness vs. Time
- 0.2 mil (5 um): ~15--20 min at 15 ASF
- 0.4 mil (10 um): ~25--35 min at 15 ASF
- 0.7 mil (18 um): ~40--50 min at 15 ASF
- 1.0 mil (25 um): ~55--70 min at 15 ASF

*Note: These are approximations. Actual growth rate depends on alloy, temperature, acid concentration, and dissolved aluminum.*

### Temperature Control Criticality
Temperature is THE most critical variable in sulfuric acid anodizing:
- **Too high (>75 deg F)**: Acid dissolution rate exceeds oxide formation rate --> soft, powdery, porous coating with poor wear and corrosion resistance
- **Too low (<65 deg F)**: Coating becomes harder and more brittle; approaches Type III behavior; may crack
- **Ideal (68--72 deg F)**: Balanced dissolution and formation --> uniform porous structure ideal for dye absorption and sealing

### Common Defects

| Defect | Cause | Solution |
|---|---|---|
| **Burning** (dissolved/powdery oxide at edges) | CD too high; temperature too high; poor contact | Reduce CD; verify temperature; check racking |
| **Powdering** (chalky white oxide) | Temperature too high; excessive time | Reduce temperature; reduce time |
| **Soft/thin coat** | Temperature too high; acid too dilute; time too short | Lower temperature; increase acid; increase time |
| **Uneven thickness** | Poor current distribution; racking errors; shielding | Improve racking; add thieves; check contacts |
| **Color variation after dye** | Uneven oxide thickness; alloy variation; poor desmut | Improve pre-treatment; verify alloy uniformity |
| **Bare spots** | Oil/soil contamination; inadequate cleaning | Improve cleaning; check water-break test |
| **Crazing/cracking** | Oxide too thick for substrate; thermal shock | Reduce thickness; avoid rapid temperature changes |

---

## 1.8 Seal / Post Treatment

### Dyeing (Optional -- Before Sealing)

| Parameter | Value |
|---|---|
| **Dye type** | Organic dyes (most common) or inorganic (metal salt) dyes |
| **Concentration** | 0.5--10 g/L depending on vendor and color depth |
| **Temperature** | 120--140 deg F (49--60 deg C) for organic dyes |
| **pH** | 5.5--6.0 (buffered with 2 g/L sodium acetate + acetic acid) |
| **Time** | 10--30 min depending on color depth; black = longest |
| **Agitation** | Mild; avoid turbulence that causes uneven absorption |

**Critical rule**: Parts must be dyed BEFORE sealing. The pores must be open to absorb dye. Once sealed, dye cannot penetrate.

### Sealing Methods

| Seal Method | Chemistry | Temperature | Time | Salt Spray (ASTM B117) | Notes |
|---|---|---|---|---|---|
| **Hot DI water** | Deionized water; pH 5.5--6.5 | 200--212 deg F (93--100 deg C) | 2--3 min/um thickness (min 15 min) | 336--750 hr (Type II, 0.7 mil) | Most common; pores hydrate to boehmite (AlOOH) |
| **Nickel acetate** (mid-temp) | 5--8 g/L Ni(CH3COO)2; pH 5.5--6.0 | 180--200 deg F (82--93 deg C) | 10--20 min | 750--1500+ hr | Superior corrosion resistance; aerospace standard |
| **Sodium dichromate** | 5--8 g/L Na2Cr2O7; pH 5.0--6.0 | 190--210 deg F (88--99 deg C) | 15--20 min | 1000--1500+ hr | Best corrosion resistance; contains Cr6+ -- restricted |
| **Cold seal (Ni-F)** | Nickel fluoride solution | 75--85 deg F (24--29 deg C) | 5--15 min | 336--750 hr | Energy savings; faster throughput |
| **PTFE impregnation** | PTFE dispersion | Per vendor | Per vendor | N/A (lubricity focus) | Used on hard coat for lubricity; not a corrosion seal |

### Effect on Properties
- **Unsealed**: Porous; absorbs stains; poor corrosion resistance; acceptable only as paint base
- **Hot water sealed**: Good corrosion resistance; locked-in dye; slight reduction in hardness
- **Nickel acetate sealed**: Excellent corrosion resistance; preferred for aerospace and military
- **Dichromate sealed**: Best corrosion resistance; yellows clear coatings slightly; Cr6+ regulatory concern

---

# Cluster 2 -- Hardcoat Anodizing (Type III)

*The engineering finish. Maximum hardness and wear resistance on aluminum.*

## 2.1 Process Flow Poster Data

### What It Is
Type III hardcoat anodizing uses the same fundamental electrochemistry as Type II (sulfuric acid electrolyte, aluminum as anode), but operates at near-freezing temperatures, lower acid concentration, and much higher current density/voltage. The result is a dense, hard, wear-resistant oxide 1.0--4.0 mil thick.

### What It Produces
- Dense aluminum oxide coating 1.0--4.0 mil (25--100 um); default 2.0 mil per MIL-A-8625 if unspecified
- Hardness: 500--700 HV (Vickers); approaches hard chrome territory
- Color: Natural dark bronze to near-black (thicker = darker); limited dyeability
- Excellent abrasion resistance, wear resistance, and dielectric strength

### Best/Worst Alloys

| Rating | Alloy | Notes |
|---|---|---|
| Excellent | 6061, 6063 | Best alloys for hardcoat; uniform, predictable growth |
| Good | 5052, 5005 | Slightly softer coating but good uniformity |
| Fair | 7075 | Can be hardcoated but requires careful ramp control; zinc/copper affect density |
| Difficult | 2024 | High copper causes burning, soft spots, and non-uniform growth; requires low CD and slow ramp |
| Difficult | Cast alloys | Silicon disrupts oxide growth; very difficult to achieve spec thickness |

### Full Process Sequence

```
Receiving/Racking --> Soak Clean (alkaline, non-etch) --> Rinse --> Caustic Etch (light -- 30-90 sec) -->
Rinse --> Desmut/Deoxidize --> Rinse --> Hardcoat Anodize (H2SO4, near-freezing) --> Rinse -->
[Dye (limited -- dark colors only)] --> Seal (hot water, NiAc, or PTFE) --> Rinse --> Dry --> Inspect
```

### Applicable Specifications
- **MIL-A-8625F, Type III, Class 1 (undyed) or Class 2 (dyed)**
- **AMS 2469** -- Anodic Treatment, Hard Coat
- **ASTM B580** -- Standard Specification for Anodic Oxide Coatings on Aluminum
- **MIL-A-8625F minimum hardness**: Rockwell C 60 minimum on 2xxx; 65 minimum on 7xxx; 70 minimum on other alloys (per specification)

---

## 2.2 Cleaning Stage

Same as Type II -- non-etch alkaline soak cleaner. See Cluster 1, Section 1.2.

**Hardcoat-specific note**: Cleanliness is even more critical for hardcoat. Any contamination nucleates burning at the defect site under the high current densities used. Ultrasonic cleaning may be specified for critical parts.

---

## 2.3 Etch Stage

### Parameters (Light Etch)

| Parameter | Value |
|---|---|
| **Chemical** | NaOH |
| **Concentration** | 4--6 oz/gal (30--45 g/L) |
| **Temperature** | 130--150 deg F (55--66 deg C) |
| **Time** | 30--90 sec (SHORTER than Type II) |

**Why shorter?** Hardcoat requires tighter dimensional control. Excessive material removal in etch affects final dimensions. Some hardcoat specs prohibit caustic etch entirely and require acid etch or no etch (clean only).

**Dimensional note**: Hardcoat builds ~50% outward. For a 2.0 mil total coating, the part grows ~1.0 mil per surface above the original dimension. Etch removes aluminum; anodize adds oxide. Net dimensional change must be calculated.

---

## 2.4 Desmut Stage

Same chemistry options as Type II (see Cluster 1, Section 1.5). For high-copper alloys commonly hardcoated (2024, 7075), the HNO3 + HF desmut is strongly preferred.

---

## 2.5 Anodize Main Tank

### Electrolyte and Parameters

| Parameter | Value |
|---|---|
| **Electrolyte** | Sulfuric acid (H2SO4) -- LOWER concentration than Type II |
| **Concentration** | 10--12% w/v (110--135 g/L; 15--18 oz/gal) |
| **Temperature** | 28--36 deg F (-2 to +2 deg C) -- NEAR FREEZING |
| **Current density** | 24--36 ASF (2.6--3.9 A/dm2) |
| **Voltage** | 40--75+ V; can exceed 100 V on some alloys |
| **Time** | 60--120 min for 2.0 mil; varies with alloy and thickness |
| **Dissolved aluminum** | Maintain below 15 g/L |
| **Cathode material** | Lead or aluminum |
| **Agitation** | Vigorous air agitation required for heat removal |

### Mixed Acid Variant (Alumilite 225/226)

| Parameter | Value |
|---|---|
| **Electrolyte** | Sulfuric acid + oxalic acid |
| **H2SO4 concentration** | 12% (132 g/L) |
| **Oxalic acid** | 1% (40--45 g/L) |
| **Temperature** | 28--36 deg F (-2 to +2 deg C) |
| **Notes** | Oxalic acid addition improves throwing power, reduces burning tendency, and produces a harder, more crack-resistant coating. Originally developed by Alcoa. Some variants use up to 3% oxalic acid. |

### Current/Voltage Ramp
Hardcoat anodizing requires a controlled current ramp to prevent burning at process start:
1. Start at ~6--12 ASF
2. Ramp to full current density (24--36 ASF) over 5--15 min
3. Hold at full CD for remainder of cycle
4. Voltage rises as oxide grows (increasing resistance); typical final voltage 50--80 V

**Some shops use voltage control** instead of current control: start at low voltage, ramp to operating voltage, and let current find its level. Both methods work; current control is more common for production.

### Temperature Control Criticality
**This is the single most important variable in hardcoat anodizing.**

- Temperature must be maintained within +/- 2 deg F of setpoint
- Refrigeration system (chiller) is MANDATORY -- typical 5--20 ton capacity depending on tank size
- The anodizing reaction generates significant heat (exothermic at the oxide/electrolyte interface)
- If temperature rises above 40 deg F: oxide softens, becomes porous, hardness drops, coating may dissolve (burn)
- Titanium heat exchangers or lead-lined cooling coils typically used (stainless steel corrodes in H2SO4)

### Film Thickness vs. Time
- 1.0 mil (25 um): ~30--45 min at 30 ASF
- 2.0 mil (50 um): ~60--90 min at 30 ASF
- 3.0 mil (75 um): ~90--135 min at 30 ASF
- 4.0 mil (100 um): ~120--180 min at 30 ASF

*Growth rate slows as coating thickens due to increasing electrical resistance.*

### Common Defects

| Defect | Cause | Solution |
|---|---|---|
| **Burning** (white or dissolved areas, especially edges/corners) | CD too high; temperature too high; poor contact; sharp geometry | Reduce CD; verify chiller; improve racking; radius sharp edges |
| **Cracking / crazing** | Oxide too thick for substrate; thermal stress; alloy CTE mismatch | Reduce thickness; slow post-process cooling; verify alloy |
| **Powdery / soft coating** | Temperature too high; acid concentration too high | Lower temperature; lower acid; check chiller capacity |
| **Non-uniform thickness** | Poor current distribution; inadequate agitation | Improve racking; add conforming cathodes; increase agitation |
| **Delamination** | Poor adhesion (contamination, smut, inadequate pre-treatment) | Improve cleaning/desmut; verify surface condition |

---

## 2.6 Seal / Post Treatment

### Sealing Options

| Method | Temperature | Time | Application |
|---|---|---|---|
| **Hot DI water** | 200--212 deg F | 2--3 min/um (min 30 min for thick coats) | Standard; closes pores |
| **Nickel acetate** | 180--200 deg F | 15--30 min | Aerospace; superior corrosion resistance |
| **PTFE impregnation** | Per vendor | Per vendor | Sliding surfaces; adds lubricity; reduces COF to 0.1--0.15 |
| **No seal** (as-anodized) | N/A | N/A | Some wear applications benefit from open pores that retain lubricant |

### Dyeing (Limited)
Type III hardcoat has a dense pore structure that limits dye absorption. Only dark colors (black, dark blue, dark green) are achievable. Light and bright colors are not practical. Most hardcoat is left in its natural dark bronze-to-black color.

---

# Cluster 3 -- Chromic Acid Anodizing (Type I)

*The aerospace original. Thin, fatigue-friendly, being phased out due to Cr(VI).*

## 3.1 Process Flow Poster Data

### What It Is
Type I chromic acid anodizing uses chromic acid (CrO3) as the electrolyte instead of sulfuric acid. It produces a thin, relatively soft oxide that has minimal effect on fatigue life and excellent paint adhesion properties. The thin, somewhat translucent coating also allows visual inspection of the substrate for flaws.

### What It Produces
- Thin aluminum oxide coating 0.03--0.10 mil (0.8--2.5 um)
- Moderate hardness (less than Type II)
- Color: Gray to dark gray (natural); limited dye absorption
- Excellent fatigue retention (thin coating = minimal stress concentration)
- Excellent paint adhesion base

### Best/Worst Alloys

| Rating | Alloy | Notes |
|---|---|---|
| Good | 6061, 5052, 1100 | Standard Type I substrates |
| Good | 2024 | Type I is actually PREFERRED for 2024 -- chromic acid is less aggressive to copper-containing alloys than sulfuric acid |
| Good | 7075 | Type I works well; thin coating minimizes alloy sensitivity issues |
| Not recommended | High-Si cast alloys | Poor results in any anodize process |

**Key point**: Type I is often the PREFERRED process for high-copper alloys (2xxx) where sulfuric acid anodizing produces poor results.

### Full Process Sequence

```
Receiving/Racking --> Soak Clean (alkaline) --> Rinse --> Caustic Etch (light, 30--60 sec) --> Rinse -->
Desmut (NON-chromic desmut for environmental preference; or chromic/nitric) --> Rinse -->
Chromic Acid Anodize (CrO3, voltage ramp cycle) --> Rinse --> [Seal] --> Rinse --> Dry --> Inspect
```

### Applicable Specifications
- **MIL-A-8625F, Type I (40V process) or Type IB (22V low-voltage process)**
- **AMS 2470** -- Anodic Treatment of Aluminum Alloys, Chromic Acid Process
- **BAC 5019** (Boeing)
- **Note**: Type IB is the low-voltage variant (max 22V) used for assemblies with recesses/blind holes where Type I's 40V can cause excessive dissolution

---

## 3.2 Cleaning Stage

Same as Type II -- non-etch alkaline soak cleaner. See Cluster 1, Section 1.2.

**Type I-specific note**: Chlorides must be absent from cleaning chemicals. Chloride contamination of chromic acid baths causes pitting and poor oxide quality. Maximum chloride in chromic acid bath: 0.02% (200 ppm).

---

## 3.3 Etch Stage

### Parameters (Very Light Etch)

| Parameter | Value |
|---|---|
| **Chemical** | NaOH (may be omitted entirely for some specs) |
| **Concentration** | 3--6 oz/gal (22--45 g/L) |
| **Temperature** | 130--150 deg F (55--66 deg C) |
| **Time** | 30--60 sec (very short) |

**Why very short / sometimes omitted?** Type I is used for fatigue-critical parts where material removal must be minimized. Some specs require no etch -- clean only.

---

## 3.4 Desmut Stage

Standard nitric acid desmut. See Cluster 1, Section 1.5.

**Avoid chromic acid desmut** if the goal is to minimize Cr(VI) usage. Nitric acid or ferric sulfate-based desmuts are preferred.

---

## 3.5 Anodize Main Tank

### Electrolyte and Parameters

| Parameter | Value |
|---|---|
| **Electrolyte** | Chromic acid (CrO3) |
| **Concentration** | 3--10% w/v (30--100 g/L); typical 5% (50 g/L) |
| **Temperature** | 90--100 deg F (32--38 deg C) |
| **Voltage (Type I -- 40V cycle)** | Ramp 0 to 40V over 10 min; hold 40V for 20--35 min; de-energize |
| **Voltage (Type IB -- low voltage)** | Max 22V; same ramp pattern |
| **Current density** | 5--10 ASF (voltage-controlled; CD is a result, not the control variable) |
| **Oxide thickness** | 0.03--0.10 mil (0.8--2.5 um) |
| **Dissolved aluminum** | Max 20 g/L |
| **Chloride** | Max 200 ppm (0.02%) -- critical contaminant |
| **Sulfate** | Max 500 ppm (0.05%) -- from drag-in; inhibits coating |

### Voltage Ramp Cycle (Type I, 40V Process)
This is the distinctive operating feature of chromic acid anodizing:

| Time (min) | Voltage |
|---|---|
| 0--5 | Ramp 0 to 40V |
| 5--10 | Hold at 40V |
| (total cycle) | 20--35 min at 40V hold |

*Some specifications use a step-ramp: 0V --> 18V (5 min hold) --> 22V (5 min hold) --> 40V (20 min hold)*

### Film Formation
- The chromic acid electrolyte is much less aggressive than sulfuric acid
- Oxide dissolution rate is lower --> thinner but denser barrier layer
- Pore structure is less developed than Type II --> limited dye absorption
- The oxide is integral and provides excellent paint adhesion

### Common Defects

| Defect | Cause | Solution |
|---|---|---|
| **Pitting** | Chloride contamination | Test bath for Cl-; maintain <200 ppm |
| **Thin/no coating** | Sulfate contamination; low CrO3 | Analyze bath; maintain CrO3 concentration |
| **Uneven color** | Poor racking; alloy variation | Improve racking; verify alloy certification |
| **Excessive dissolution** | Voltage too high; time too long | Verify voltage cycle; reduce time |

---

## 3.6 Seal / Post Treatment

### Sealing Methods

| Method | Temperature | Time | Notes |
|---|---|---|---|
| **Hot DI water** | 200--212 deg F | 15 min minimum | Standard |
| **Dichromate** | 190--210 deg F | 15--20 min | Maximum corrosion resistance; adds more Cr6+ |
| **Nickel acetate** | 180--200 deg F | 15--20 min | Alternative without additional Cr6+ |

### Corrosion Resistance
- Sealed Type I coating: 168--336 hr ASTM B117 salt spray (despite thin coating, chromic acid residue in oxide provides self-healing corrosion inhibition)
- Primed and painted over Type I: the primary application -- paint adhesion is the key performance metric, not stand-alone corrosion resistance

---

## 3.7 Environmental and Regulatory

### Hexavalent Chromium Status
**Chromic acid anodizing is under severe regulatory pressure worldwide:**

| Regulation | Status |
|---|---|
| **EU REACH** | CrO3 listed as Substance of Very High Concern (SVHC); Authorization required; sunset date passed |
| **RoHS** | Cr(VI) restricted to <1000 ppm in finished products |
| **OSHA PEL** | 5 ug/m3 Cr(VI) as 8-hr TWA (29 CFR 1910.1026) |
| **OSHA Action Level** | 2.5 ug/m3 Cr(VI) as 8-hr TWA |
| **EPA** | Cr(VI) discharge limits: <0.1 mg/L in wastewater |
| **California Prop 65** | Listed carcinogen |

### Waste Treatment
- Cr(VI) must be chemically reduced to Cr(III) before discharge
- Typical reductant: sodium bisulfite (NaHSO3) or ferrous sulfate (FeSO4) at pH <3
- After reduction: raise pH to 8--9 with NaOH to precipitate Cr(OH)3
- Sludge is hazardous waste (D007 chromium)

### Why It Is Being Replaced
- BSAA (Type IC) is the primary replacement -- see Cluster 4
- PAA is used for adhesive bonding applications -- see Cluster 5
- Type IIB (thin sulfuric acid) replaces some Type I applications

---

# Cluster 4 -- Boric-Sulfuric Acid Anodizing (BSAA)

*The chromate-free replacement for Type I. Rapidly gaining aerospace adoption.*

## 4.1 Process Flow Poster Data

### What It Is
BSAA uses a mixture of sulfuric acid and boric acid as the electrolyte, producing a thin oxide coating functionally equivalent to chromic acid anodize (Type I) without any hexavalent chromium. It was developed as a direct drop-in replacement for Type I in aerospace applications.

### What It Produces
- Thin aluminum oxide coating, similar to Type I
- Coating weight: 200--700 mg/ft2 per MIL-A-8625F Type IC
- Good fatigue retention (thin coating)
- Excellent paint adhesion base
- No Cr(VI) in the process -- full REACH/RoHS compliance

### Best/Worst Alloys
Same compatibility as Type I. Works well on 2xxx and 7xxx alloys where sulfuric acid processes are problematic.

### Full Process Sequence

```
Receiving/Racking --> Soak Clean (alkaline) --> Rinse --> Caustic Etch (light, 30--60 sec) --> Rinse -->
Desmut (nitric acid or ferric sulfate) --> Rinse --> BSAA Anodize (H2SO4 + H3BO3) --> Rinse -->
Seal (hot water or nickel acetate) --> Rinse --> Dry --> Inspect
```

### Applicable Specifications
- **MIL-A-8625F, Type IC, Class 1 or Class 2**
- **Boeing BAC 5632** -- the original BSAA specification (Boeing developed the process)
- **NADCAP-approved process**

---

## 4.2--4.4 Cleaning, Etch, Desmut

Same as Type I / Type II pre-treatment. See Clusters 1 and 3. No special pre-treatment requirements unique to BSAA.

---

## 4.5 Anodize Main Tank

### Electrolyte and Parameters

| Parameter | Value |
|---|---|
| **Electrolyte** | Sulfuric acid (H2SO4) + boric acid (H3BO3) |
| **H2SO4 concentration** | 3--5% w/v (30--50 g/L); some sources cite 60--100 g/L |
| **H3BO3 concentration** | 0.5--1.0% w/v (5--10 g/L); some sources cite 0.1--10.7 g/L |
| **Temperature** | 70--90 deg F (21--32 deg C) |
| **Voltage** | Ramp from ~5V to 15V |
| **Current density** | Max ~10 ASF average (voltage-controlled, similar to Type I) |
| **Time** | 20--30 min typical |
| **Coating weight** | 200--700 mg/ft2 |

### Role of Boric Acid
- Boric acid acts as a buffering agent in the electrolyte
- Reduces the aggressiveness of sulfuric acid dissolution
- Allows production of a thin, dense oxide similar to chromic acid but without Cr(VI)
- The boric acid does NOT contribute to the oxide -- it modifies the dissolution/formation balance

### Key Advantages Over Type I (Chromic)
1. **No hexavalent chromium** -- REACH/RoHS/OSHA compliant
2. **No hazardous waste** from Cr(VI) sludge
3. **Lower energy cost** -- operates at lower voltage than Type I
4. **Equivalent paint adhesion** to Type I
5. **Equivalent fatigue retention** to Type I
6. **NADCAP accepted** as Type I replacement

### Limitations
- Corrosion resistance of unsealed BSAA may be slightly lower than Type I (chromic acid provides self-healing inhibition in the oxide; BSAA does not)
- Process control is still evolving; less established operating history than Type I (decades of data)
- Dissolved aluminum must be monitored closely -- lower acid concentration = less tolerance

---

## 4.6 Seal / Post Treatment

Same sealing methods as Type I/II (hot water, nickel acetate). Dichromate seal would defeat the purpose of going chromate-free.

| Method | Temperature | Time | Notes |
|---|---|---|---|
| **Hot DI water** | 200--212 deg F | 15 min minimum | Standard for BSAA |
| **Nickel acetate** | 180--200 deg F | 15--20 min | Preferred for aerospace to maximize corrosion resistance |
| **Trivalent Cr seal** | Per vendor | Per vendor | Some shops use Cr(III) seal for self-healing corrosion inhibition without Cr(VI) |

---

# Cluster 5 -- Phosphoric Acid Anodizing (PAA)

*The adhesive bonding specialist. Structural aerospace joining.*

## 5.1 Process Flow Poster Data

### What It Is
Phosphoric acid anodizing (PAA) produces a thin, highly porous oxide with elongated "whisker-like" pore structures specifically designed for adhesive bonding. The whisker morphology allows structural adhesives to flow into the oxide and mechanically interlock, creating the strongest possible aluminum-to-adhesive bond. PAA is NOT used for corrosion protection or wear resistance -- it is a surface preparation for bonding.

### What It Produces
- Ultra-thin porous oxide with characteristic "whisker" or "finger-like" pore morphology
- Oxide thickness: typically 0.01--0.04 mil (0.3--1.0 um) -- thinner than Type I
- Open, columnar pore structure optimized for adhesive penetration
- Surface highly resistant to hydration (more stable than chromic acid oxide in humid environments)

### Best/Worst Alloys
Used primarily on aerospace structural alloys: 2024, 7075, 7475, 6061. Works on all aluminum alloys but is specified almost exclusively for structural bonding applications.

### Full Process Sequence

```
Receiving/Racking --> Alkaline Clean --> Rinse --> [Chromic Acid Etch or FPL Etch (Forest Products Lab)] --> Rinse -->
PAA Anodize (H3PO4) --> Rinse --> [Prime (BR 127 or equivalent)] --> Bond
```

**Note**: PAA is almost always followed immediately by primer application (within hours), NOT sealing. The open pore structure is the desired end state for adhesive bonding.

### Applicable Specifications
- **Boeing BAC 5555** -- the definitive PAA specification (Boeing developed the process)
- **ASTM D3933** -- Standard Guide for Preparation of Aluminum Surfaces for Structural Adhesive Bonding (Phosphoric Acid Anodizing)
- **MIL-A-8625F does NOT explicitly cover PAA** -- it is governed by Boeing/prime contractor specs

---

## 5.2--5.4 Cleaning, Etch, Desmut

### Pre-Treatment for PAA
PAA pre-treatment is typically the FPL etch (Forest Products Laboratory etch) or a chromic-sulfuric acid etch:

**FPL Etch (Chromic-Sulfuric):**

| Parameter | Value |
|---|---|
| **Chemistry** | Na2Cr2O7 (30 g/L) + H2SO4 (300 g/L) |
| **Temperature** | 150--160 deg F (66--71 deg C) |
| **Time** | 10--12 min |

**Non-chromate alternative**: Alkaline etch + acid desmut (same as Type II pre-treatment) is increasingly used to avoid Cr(VI) in the pre-treatment chain.

**P2 etch (Optimized FPL)**: Modified FPL with tighter control on dissolved aluminum and ferric sulfate addition.

---

## 5.5 Anodize Main Tank

### Electrolyte and Parameters

| Parameter | Value |
|---|---|
| **Electrolyte** | Phosphoric acid (H3PO4) |
| **Concentration** | 10--15% w/v (100--150 g/L); BAC 5555 specifies ~12% |
| **Temperature** | 70--100 deg F (21--38 deg C); some specs cite 80 deg F nominal |
| **Voltage** | 15--25 V |
| **Current density** | 5--8 ASF |
| **Time** | 20--25 min |

### Film Formation Mechanism
- Phosphoric acid is more aggressive than sulfuric acid at dissolving the oxide
- This creates a wider, more open pore structure with characteristic elongated "whiskers" at the pore mouths
- The whiskers provide enormous surface area for adhesive mechanical interlocking
- The phosphate ion partially incorporates into the oxide, making it more hydration-resistant than sulfuric acid or chromic acid oxides

### Why PAA for Bonding
1. **Whisker morphology**: Provides mechanical interlocking with adhesive at the nanoscale
2. **Hydration resistance**: PAA oxide is more stable in humid environments than other anodize types -- critical for long-term bond durability
3. **Open porosity**: Adhesive flows INTO the oxide structure and cures in place
4. **Consistent bond strength**: PAA-prepared bonds show the highest and most consistent peel and lap-shear strengths of any aluminum surface preparation

### Common Defects

| Defect | Cause | Solution |
|---|---|---|
| **Low bond strength** | Contamination before priming; excessive time between PAA and primer | Reduce transfer time; improve cleanliness |
| **Hydration of oxide** | Delay between anodize and primer application | Prime within 2--4 hours of anodize; some specs require <1 hour |
| **Over-dissolution** | Acid too concentrated or temperature too high | Reduce concentration; lower temperature |

---

## 5.6 Post Treatment

### No Traditional Seal
PAA is NOT sealed in the traditional sense. The open pore structure is the desired end state.

**Instead, the post-treatment is**:
1. Rinse thoroughly (DI water)
2. Dry
3. Apply adhesive primer (BR 127 or equivalent) within the time window specified (typically 2--4 hours; some specs allow up to 72 hours with controlled humidity storage)
4. Bond with structural adhesive (FM 73, FM 300, etc.)

---

# Cluster 6 -- Bright Anodizing

*The mirror finish. Chemical polishing before anodize.*

## 6.1 Process Flow Poster Data

### What It Is
Bright anodizing is not a different anodize chemistry -- it is a Type II sulfuric acid anodize performed on a chemically polished (bright dipped) surface. The "bright dip" step replaces the caustic etch in the standard process sequence, producing a mirror-like specular surface instead of a matte finish. The subsequent anodize is standard Type II.

### What It Produces
- Highly reflective, mirror-like aluminum surface
- Same oxide properties as Type II (0.2--1.0 mil, 300--400 HV)
- Can be dyed to produce brilliant, transparent colors over a reflective base
- Used for decorative trim, reflectors, cosmetic hardware, automotive bright trim

### Best/Worst Alloys

| Rating | Alloy | Notes |
|---|---|---|
| Excellent | 1100 | Purest Al = best reflectivity |
| Excellent | 5657 | Specifically developed for bright anodizing (bright trim alloy) |
| Very Good | 5252 | Good bright finish capability |
| Good | 6463 | Architectural bright trim alloy |
| Fair | 6061 | Can be bright dipped but less specular than dedicated bright alloys |
| Poor | 2024, 7075 | Copper/zinc cause pitting and uneven polishing in bright dip |
| Poor | Cast alloys | Silicon particles cause rough, non-specular finish |

### Full Process Sequence

```
Receiving/Racking --> [Mechanical Pre-Polish (optional)] --> Soak Clean (alkaline, non-etch) --> Rinse -->
BRIGHT DIP (H3PO4 + HNO3, ~200 deg F) --> Rinse --> [Desmut (if needed)] --> Rinse -->
Anodize (standard Type II H2SO4) --> Rinse --> [Dye] --> Seal --> Dry --> Inspect
```

**Key difference**: The caustic etch is REPLACED by the bright dip. No caustic etch is used.

### Applicable Specifications
- **MIL-A-8625F, Type II, Class 1 or Class 2** (the anodize itself is standard Type II)
- **ASTM B580**
- Some automotive specs reference proprietary bright anodize requirements

---

## 6.2 Cleaning Stage

Same as Type II -- see Cluster 1, Section 1.2. Cleanliness is especially critical for bright anodize because any residual soil creates visible defects on the highly reflective surface.

**Additional requirement**: Mechanical pre-polish (buffing, polishing) is often performed BEFORE chemical processing to maximize initial surface reflectivity. The bright dip chemically polishes the surface; it does not remove deep scratches or tool marks.

---

## 6.3 Bright Dip Stage (Replaces Caustic Etch)

### Chemistry

| Parameter | Value |
|---|---|
| **Chemistry** | Phosphoric acid (H3PO4) + nitric acid (HNO3) |
| **H3PO4** | ~85% of bath volume (using 85% reagent grade H3PO4) |
| **HNO3** | ~5% of bath volume (using 70% reagent grade HNO3) |
| **Typical ratio** | 95 parts 85% H3PO4 : 5 parts 70% HNO3 by volume |
| **Temperature** | 190--210 deg F (88--99 deg C) -- near boiling |
| **Time** | 30--120 sec (very short; time-critical) |
| **Specific gravity** | Monitor; increases as aluminum dissolves |
| **Dissolved aluminum limit** | ~40--50 g/L maximum; above this, polishing action degrades |
| **Copper limit** | Monitor on Cu-bearing alloys; copper enrichment on surface causes staining |

### Mechanism
1. At operating temperature, the viscous H3PO4/HNO3 solution dissolves aluminum preferentially at microscopic peaks (convex surfaces dissolve faster than concave valleys)
2. A viscous boundary layer of reaction products forms at the metal-solution interface
3. This boundary layer is thinner at peaks and thicker in valleys, causing preferential dissolution at peaks
4. Result: micro-leveling that produces a specular (mirror) finish

### Safety -- CRITICAL

| Hazard | Details |
|---|---|
| **NOx fumes** | Brown nitrogen oxide gas (NO2) evolves vigorously at operating temperature; EXTREMELY toxic and corrosive |
| **Ventilation** | Garage-style exhaust hood required; double-stage fume scrubber; automated part handling preferred |
| **Temperature** | Near-boiling acid mix -- severe burn hazard |
| **PPE** | Full face shield, acid-resistant suit/apron, long chemical-resistant gloves (butyl rubber), respiratory protection if scrubber is inadequate |
| **Tank construction** | Double-walled tank; polypropylene or PVDF lining; no stainless steel (HNO3 attacks it) |
| **Automation** | Many shops automate bright dip to minimize operator exposure |

---

## 6.4 Desmut (If Needed)

On most bright dip alloys (1xxx, 5xxx), desmut is minimal or unnecessary because the bright dip itself removes smut-forming elements. On alloys with copper or silicon, a brief nitric acid desmut (30--60 sec) may follow the bright dip.

---

## 6.5 Anodize Main Tank

**Standard Type II sulfuric acid anodize.** See Cluster 1, Section 1.7. No modifications to the anodize chemistry.

**Bright anodize-specific notes**:
- Temperature control is especially critical -- any softening of the oxide clouds the bright finish
- Coating thickness is usually kept thinner (0.2--0.5 mil) for maximum transparency/clarity
- Clear anodize (no dye) over bright dip = "bright clear anodize" -- the classic mirror finish
- Dyed over bright dip = brilliant transparent colors (jewel-like appearance)

---

## 6.6 Seal / Post Treatment

Standard Type II sealing. See Cluster 1, Section 1.8.

**Bright-specific note**: Hot water seal can slightly cloud the bright finish (boehmite formation scatters light). Nickel acetate or cold seal may produce a slightly clearer result. Trade-off: corrosion resistance vs. optical clarity.

---

# Cluster 7 -- Integral Color Anodizing

*Color FROM the oxide itself. No dye required.*

## 7.1 Process Flow Poster Data

### What It Is
Integral color anodizing produces colored aluminum oxide coatings where the color is an inherent property of the oxide itself -- NOT from an applied dye. The color develops during anodizing due to the incorporation of organic acid decomposition products into the growing oxide film. Colors range from pale champagne/gold through bronze, brown, gray, to near-black, depending on oxide thickness and electrolyte composition.

### What It Produces
- Colored aluminum oxide: champagne, gold, light bronze, medium bronze, dark bronze, gray, black
- Coating thickness: typically 0.5--2.0 mil (12--50 um)
- Hardness: typically harder than standard Type II due to organic acid addition and higher voltage
- Exceptional light-fastness (color does not fade in UV) -- organic dyes fade; integral color does not
- Used primarily in architectural applications (building facades, curtain walls, window frames)

### Best/Worst Alloys

| Rating | Alloy | Notes |
|---|---|---|
| Excellent | 6063 | Standard architectural alloy; produces uniform color |
| Very Good | 6061, 5005, 5052 | Good integral color response |
| Poor | 2024, 7075 | High Cu/Zn causes uneven color; not used for integral color |
| Poor | Cast alloys | Silicon causes dark, blotchy, non-uniform color |

### Full Process Sequence

```
Receiving/Racking --> Soak Clean (alkaline) --> Rinse --> Caustic Etch (standard) --> Rinse -->
Desmut --> Rinse --> Integral Color Anodize (mixed acid electrolyte) --> Rinse --> Seal --> Dry --> Inspect
```

**Note**: No dye step. The color is produced IN the anodize tank.

### Applicable Specifications
- **AAMA 611** -- Voluntary Specification for Anodized Architectural Aluminum (includes integral color)
- Some integral color processes have been classified under **MIL-A-8625F Type IC** (non-chromic acid anodizing using organic acid electrolytes)
- **Qualanod** specifications for European architectural applications

---

## 7.2--7.4 Cleaning, Etch, Desmut

Same as Type II -- see Cluster 1, Sections 1.2--1.5. Standard alkaline clean, caustic etch, nitric acid desmut.

**Integral color-specific note**: Etch uniformity is CRITICAL because any variation in surface texture translates directly to color variation. The matte texture from caustic etch must be perfectly even.

---

## 7.5 Anodize Main Tank

### Electrolyte Options

**Option A: Oxalic Acid Process (Original)**

| Parameter | Value |
|---|---|
| **Electrolyte** | Oxalic acid (HOOC-COOH) or oxalic + sulfuric acid mix |
| **Oxalic acid** | 30--50 g/L (as sole electrolyte) or 10--40 g/L (in mix) |
| **H2SO4 (if mixed)** | 50--165 g/L |
| **Temperature** | 68--85 deg F (20--29 deg C) |
| **Current density** | 10--20 ASF |
| **Voltage** | 40--80 V (higher than Type II) |
| **Time** | 30--90 min depending on color depth |
| **Colors produced** | Pale yellow to gold to bronze to dark brown/black |

**Option B: Sulfosalicylic Acid Process (Modern)**

| Parameter | Value |
|---|---|
| **Electrolyte** | Sulfosalicylic acid (5-SSA) + sulfuric acid |
| **Sulfosalicylic acid** | 40--80 g/L |
| **H2SO4** | 10--30 g/L |
| **Temperature** | 68--80 deg F (20--27 deg C) |
| **Current density** | 15--30 ASF |
| **Voltage** | 50--100 V (high voltage required) |
| **Time** | 30--90 min |
| **Colors produced** | Champagne, light bronze, medium bronze, dark bronze, gray, black |

**Option C: Mixed Organic Acid (Proprietary)**
Various proprietary processes use combinations of:
- Sulfosalicylic acid
- Sulfophthalic acid
- Maleic acid
- Tartaric acid
Mixed with sulfuric acid at vendor-specified ratios.

### Color Control
Color is controlled by:
1. **Oxide thickness** -- thicker = darker (primary control variable)
2. **Current density** -- higher CD = more organic acid incorporation = different hue
3. **Acid concentration** -- affects dissolution rate and thus organic incorporation
4. **Temperature** -- higher temperature = lighter color (more dissolution)
5. **Alloy** -- different alloys produce slightly different hues at the same thickness

### Color Matching Challenge
Integral color anodizing is the most difficult anodizing process to control for color consistency. Batch-to-batch matching requires:
- Tight alloy lot control (same heat, same extrusion run)
- Precise temperature control (+/- 1 deg F)
- Precise current density control (+/- 0.5 ASF)
- Consistent etch depth

### Key Advantage: Light-Fastness
Integral color does NOT fade in UV exposure. Organic dyes (Type II Class 2) can fade over years of outdoor exposure. This is why integral color was historically preferred for architectural facades in direct sunlight. However, two-step electrolytic coloring (Cluster 8) has largely replaced integral color for architecture due to lower cost and easier color control.

---

## 7.6 Seal / Post Treatment

### Sealing

| Method | Temperature | Time | Notes |
|---|---|---|---|
| **Hot DI water** | 200--212 deg F | 2--3 min/um thickness | Standard; no color shift |
| **Nickel acetate** | 180--200 deg F | 15--20 min | Can slightly shift color; test first |
| **Steam seal** | 212 deg F | Varies | Used in some high-volume architectural lines |

### No Dyeing
Integral color is not dyed. The color is inherent in the oxide. Sealing is the final chemical step.

---

# Cluster 8 -- Two-Step (Electrolytic) Color Anodizing

*Metal in the pores. The modern architectural standard.*

## 8.1 Process Flow Poster Data

### What It Is
Two-step electrolytic coloring is a two-stage process:
1. **Step 1**: Standard Type II sulfuric acid anodize (creates the porous oxide)
2. **Step 2**: Electrolytic deposition of metal (typically tin) into the pores using AC current

The metal deposits at the bottom of the pores (near the barrier layer), producing color by light interference and absorption. The result is a UV-stable, fade-resistant colored finish that has largely replaced both organic dyes and integral color anodizing for architectural applications.

### What It Produces
- Standard Type II oxide with metal (Sn, Ni, Co, or Cu) deposited in pores
- Colors: champagne, light bronze, medium bronze, dark bronze, black (limited palette, but UV-stable)
- The color is produced by metallic particles inside the oxide -- not a dye, not an integral oxide color
- Exceptional light-fastness and weathering resistance
- The dominant architectural anodizing process worldwide since the 1980s

### Best/Worst Alloys
Same as Type II. 6063 is the standard architectural alloy. See Cluster 1.

### Full Process Sequence

```
Receiving/Racking --> Soak Clean --> Rinse --> Caustic Etch --> Rinse --> Desmut --> Rinse -->
STEP 1: Sulfuric Acid Anodize (standard Type II) --> Rinse -->
STEP 2: Electrolytic Color (AC, tin sulfate bath) --> Rinse --> Seal --> Dry --> Inspect
```

### Applicable Specifications
- **AAMA 611** -- Voluntary Specification for Anodized Architectural Aluminum
- **Qualanod** (European architectural quality label)
- **ASTM B580**
- Two-step coloring is not separately classified in MIL-A-8625F -- the base anodize is Type II

---

## 8.2--8.6 Cleaning Through Anodize

Steps 1 through 6 (clean, rinse, etch, desmut, rinse, anodize) are identical to standard Type II sulfuric acid anodizing. See Cluster 1, Sections 1.2--1.7.

**Two-step-specific anodize notes**:
- Oxide thickness for electrolytic coloring is typically on the higher end: 0.5--1.0 mil (12--25 um) for architectural work
- Thicker oxide = deeper pores = more metal deposition = darker color
- The anodize conditions must be consistent to produce uniform pore depth for uniform coloring

---

## 8.7 Electrolytic Coloring Tank (Step 2)

### Bath Composition

| Parameter | Value |
|---|---|
| **Primary chemistry** | Stannous sulfate (SnSO4) -- tin-based (most common in North America) |
| **SnSO4 concentration** | 15--20 g/L (with stainless steel or graphite electrodes) |
| **SnSO4 concentration** | ~12 g/L (with tin counter-electrodes that replenish tin) |
| **Organic additives** | Required; ~1 lb organic per 3 lb stannous sulfate |
| **Sulfuric acid** | 10--20 g/L (provides conductivity) |
| **Temperature** | 65--75 deg F (18--24 deg C) |
| **Power supply** | AC (alternating current) -- 60 Hz single phase |
| **Voltage** | 10--20 VAC (typically 18--20V; ~1V lower than anodizing voltage) |
| **Peak current** | 10 ASF |
| **Average current** | 5 ASF |
| **Counter-electrode** | 316 stainless steel, tin, or graphite |

### Alternative Metal Systems

| Metal Salt | Color Range | Notes |
|---|---|---|
| **Stannous sulfate (Sn)** | Champagne to black | Most common; best color range |
| **Nickel sulfate (Ni)** | Bronze tones | Less common; used in some European processes |
| **Cobalt sulfate (Co)** | Blue-bronze | Specialty; limited use |
| **Copper sulfate (Cu)** | Reddish-bronze | Specialty; limited use |

### Coloring Times by Shade

| Color | Approximate Time |
|---|---|
| **Light champagne** | 30 sec -- 1 min |
| **Medium bronze** | 2--5 min |
| **Dark bronze** | 5--8 min |
| **Black** | ~10 min |

### How It Works
1. AC current drives tin ions into the pores during the cathodic half-cycle
2. During the anodic half-cycle, partial dissolution/redistribution occurs
3. Net result: metallic tin particles accumulate at the pore bottoms (near the barrier layer)
4. Color is produced by a combination of:
   - **Light absorption** by metallic particles
   - **Interference effects** from the pore depth and particle size/spacing
5. Deeper pores (thicker oxide) = more tin deposited = darker color
6. Time at voltage controls the amount of tin deposited

### Color Uniformity
- More uniform and reproducible than integral color anodizing
- Color is primarily controlled by time in the coloring bath (easy to control)
- Requires uniform oxide thickness from Step 1 (consistent anodize is the prerequisite)
- Parts must be racked to ensure even current distribution in the coloring bath

---

## 8.8 Seal / Post Treatment

Standard sealing methods -- see Cluster 1, Section 1.8.

**Two-step-specific notes**:
- Hot water seal is the standard for architectural two-step colored anodize
- Nickel acetate seal provides additional corrosion protection for coastal/industrial environments
- Sealing closes the pores over the deposited metal, locking it in permanently
- The metal is at the BOTTOM of the pores; the dye (if also used -- rare in two-step) is above the metal

### Color + Metal Combinations
Some architectural finishes combine two-step electrolytic coloring with organic dyeing:
1. Anodize (Type II)
2. Electrolytic color (tin -- produces bronze base)
3. Organic dye (adds tint over the metallic base)
4. Seal

This is uncommon but used for specialty colors not achievable with metal alone.

---

# Cross-Cluster Reference: Safety and Regulatory

## Hexavalent Chromium (Type I and Legacy Processes)

| Parameter | Limit / Standard |
|---|---|
| **OSHA PEL** | 5 ug/m3 Cr(VI) as 8-hr TWA |
| **OSHA Action Level** | 2.5 ug/m3 as 8-hr TWA |
| **EU REACH** | CrO3 = SVHC; authorization required for use |
| **RoHS** | Cr(VI) < 1000 ppm in finished product |
| **EPA discharge** | < 0.1 mg/L Cr(VI) in wastewater |
| **Cr(VI) reduction** | NaHSO3 or FeSO4 at pH <3; then precipitate Cr(OH)3 at pH 8--9 |
| **Sludge classification** | D007 hazardous waste (chromium characteristic) |

## Acid Mist Control (All Anodizing)

| Acid | Mist Concern | Control |
|---|---|---|
| **Sulfuric acid** | Moderate mist at operating temperature; heavy mist at high CD | Tank-side exhaust; foam blankets; PFOS-free suppressants |
| **Chromic acid** | Cr(VI) mist is the PRIMARY health hazard | Dedicated enclosure; HEPA scrubber; continuous air monitoring |
| **Phosphoric/nitric (bright dip)** | Heavy NOx fumes at 200+ deg F | Garage-style hood; double-stage scrubber; automation preferred |
| **Phosphoric acid (PAA)** | Light mist | Standard ventilation |
| **Boric-sulfuric** | Low mist (low acid concentration) | Standard ventilation |

## Aluminum Etch Waste

| Waste Stream | Characteristics | Treatment |
|---|---|---|
| **Spent caustic etch** | pH 13--14; 20--60 g/L dissolved aluminum | Acidify to pH 6--8; aluminum precipitates as Al(OH)3; dewater sludge |
| **Spent acid (desmut, anodize)** | pH <1; dissolved aluminum; fluorides (if HF used) | Neutralize with NaOH to pH 7--9; precipitate metals; fluoride removal may require CaCl2 addition |
| **Rinse water** | Low metal content; pH variable | pH adjust; may discharge to POTW with permit |

## PPE Requirements (All Anodizing Operations)

| Process | Minimum PPE |
|---|---|
| **Alkaline cleaning** | Safety glasses, nitrile gloves, apron |
| **Caustic etch** | Face shield, butyl/nitrile gloves, acid/alkali-resistant apron, arm protection |
| **Acid desmut** | Face shield, nitrile gloves, acid-resistant apron |
| **Sulfuric acid anodize** | Face shield, acid-resistant gloves, apron |
| **Chromic acid anodize** | Full face shield, Cr(VI)-rated respirator (if PEL exceeded), butyl gloves, full acid suit, continuous Cr(VI) monitoring |
| **Bright dip** | Full face shield, butyl rubber gloves, full acid suit, NOx respiratory protection, automated handling preferred |
| **Phosphoric acid anodize** | Face shield, acid-resistant gloves, apron |

---

# Cross-Cluster Reference: Alloy Compatibility Master Table

| Alloy Series | Type II (Sulfuric) | Type III (Hardcoat) | Type I (Chromic) | BSAA (Type IC) | PAA | Bright Dip | Integral Color | Two-Step |
|---|---|---|---|---|---|---|---|---|
| **1xxx** (1100) | Excellent | Good | Good | Good | Good | Excellent | Good | Excellent |
| **2xxx** (2024) | Poor | Difficult | Good (preferred) | Good | Good | Poor | Poor | Poor |
| **5xxx** (5052) | Very Good | Good | Good | Good | Good | Good | Very Good | Very Good |
| **6xxx** (6061) | Very Good | Excellent | Good | Good | Good | Good | Excellent (6063) | Excellent (6063) |
| **7xxx** (7075) | Fair | Fair | Good | Good | Good | Poor | Poor | Fair |
| **Cast** (A356) | Variable | Difficult | Not recommended | Variable | Possible | Poor | Poor | Variable |

---

# Cross-Cluster Reference: Sealing Methods Master Table

| Seal Method | Chemistry | Temperature | Time | Salt Spray Hours | Best For |
|---|---|---|---|---|---|
| **Hot DI water** | Pure water; pH 5.5--6.5 | 200--212 deg F (93--100 deg C) | 2--3 min/um (min 15 min) | 336--750 hr | Standard; all types |
| **Nickel acetate** (mid-temp) | 5--8 g/L Ni(CH3COO)2; pH 5.5--6.0 | 180--200 deg F (82--93 deg C) | 10--20 min | 750--1500+ hr | Aerospace; military |
| **Sodium dichromate** | 5--8 g/L Na2Cr2O7; pH 5.0--6.0 | 190--210 deg F (88--99 deg C) | 15--20 min | 1000--1500+ hr | Maximum corrosion resistance; legacy |
| **Cold seal (Ni-F)** | Nickel fluoride solution | 75--85 deg F (24--29 deg C) | 5--15 min | 336--750 hr | Energy savings; high throughput |
| **Trivalent Cr seal** | Cr(III) solution | Per vendor | Per vendor | Up to 3000+ hr reported | Cr(VI)-free alternative to dichromate |
| **PTFE impregnation** | PTFE dispersion | Per vendor | Per vendor | N/A | Hardcoat lubricity; COF 0.10--0.15 |
| **No seal** | N/A | N/A | N/A | N/A | PAA (bonding); some hardcoat wear applications |

---

# Specification Quick Reference

| Specification | Covers |
|---|---|
| **MIL-A-8625F** | All military anodizing: Type I, IB, IC, II, IIB, III |
| **AMS 2469** | Hard coat anodize |
| **AMS 2470** | Chromic acid anodize |
| **AMS 2471** | Sulfuric acid anodize, undyed |
| **AMS 2472** | Sulfuric acid anodize, dyed |
| **ASTM B580** | Standard specification for anodic oxide coatings |
| **ASTM B117** | Salt spray (fog) test procedure |
| **ASTM D3933** | PAA for structural adhesive bonding |
| **ASTM B921** | Metal finishing with anodizing |
| **Boeing BAC 5555** | Phosphoric acid anodizing (PAA) |
| **Boeing BAC 5632** | Boric-sulfuric acid anodizing (BSAA) |
| **AAMA 611** | Architectural anodizing (includes integral color and two-step) |
| **Qualanod** | European architectural anodizing quality mark |

---

# MIL-A-8625F Type and Class Summary

| Type | Process | Electrolyte |
|---|---|---|
| **I** | Chromic acid anodize (40V) | CrO3 |
| **IB** | Chromic acid anodize, low voltage (22V) | CrO3 |
| **IC** | Non-chromic acid anodize (BSAA, organic acid) | H2SO4 + H3BO3, or organic acids |
| **II** | Sulfuric acid anodize | H2SO4 |
| **IIB** | Thin sulfuric acid anodize | H2SO4 (thin film) |
| **III** | Hard anodic coating | H2SO4 (low concentration, near-freezing) |

| Class | Description |
|---|---|
| **1** | Non-dyed (clear or natural color) |
| **2** | Dyed |

---

*Watson Research Brief v1 authored 2026-04-26. Sources: MIL-A-8625F; Boeing BAC 5555/BAC 5632; Aluminum Anodizers Council (anodizing.org); Products Finishing (pfonline.com); finishing.com; OSHA 29 CFR 1910.1026; ASTM B580/B117/D3933; domain expertise. Gemini quota exhausted during research -- all data sourced from web search, web content extraction, existing Watson Poster #9 research brief (vault), and domain expertise. All operating parameters are specification-typical values suitable for educational poster content -- production shops must verify against their specific product TDS and customer specifications.*
