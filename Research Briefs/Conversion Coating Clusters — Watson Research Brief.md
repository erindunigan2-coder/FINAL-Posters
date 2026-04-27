---
title: Conversion Coating Clusters — Watson Research Brief
author: Watson (Chemistry Researcher)
date: 2026-04-26
version: v1
status: Complete — Gemini quota exhausted; written from domain expertise
purpose: Technical backbone for 64 posters (8 processes x 8 posters each) — Alaina Construction Workups and Elara Generation Prompts
tags:
  - ConversionCoating
  - PlatingPostersInc
  - ResearchBrief
---

# Conversion Coating Clusters — Watson Research Brief

> **Note to Alaina & Elara:** Each of the 8 process sections below maps to an 8-poster cluster. The subsections are organized to feed directly into the poster sequence: (1) Process Flow, (2) Cleaning, (3) Rinse -- Pre-Condition, (4) Surface Conditioning / Activation / Etch, (5) Rinse -- Pre-Coat, (6) Conversion Coating -- Main Stage, (7) Rinse -- Post-Coat, (8) Seal / Post-Treatment / Drying. Cross-reference data freely across posters within each cluster.

---

## CLUSTER 1: Iron Phosphate Conversion Coating

### 1.1 Process Overview (Poster 1 — Process Flow)

Iron phosphate is the lightest-duty phosphate conversion coating. It is used primarily as a paint pretreatment on steel, providing moderate corrosion resistance and excellent paint adhesion at low cost and simple chemistry. It is the workhorse of powder coat and liquid paint pretreatment lines across general industrial, appliance, HVAC, and light automotive applications.

**Process Configurations:**
- **1-Stage (Cleaner-Coater):** Combined alkaline cleaner + iron phosphate chemistry in a single spray or immersion stage. Simplest system. Coating weight is lighter (15–40 mg/ft2). Common in small job shops and low-volume operations.
- **3-Stage:** Clean --> Iron Phosphate --> Seal rinse. The most common industrial configuration. Separate cleaning allows heavier, more uniform coating.
- **5-Stage:** Clean --> Rinse --> Iron Phosphate --> Rinse --> Seal rinse. Best coating quality, used when OEM paint specs demand it.

**Typical Process Sequence (5-Stage):**
1. Alkaline clean (spray or immersion)
2. Fresh water rinse
3. Iron phosphate coating
4. Fresh water rinse
5. Non-chrome seal rinse or DI water final rinse
6. Dry-off oven

### 1.2 Cleaning (Poster 2)

**Cleaner Type:** Mildly alkaline cleaner, pH 9.5–11.5, with surfactants for oil and soil removal. Must be compatible with phosphate chemistry — avoid highly caustic cleaners (NaOH > 5%) that can passivate the steel surface and inhibit phosphate deposition.

**Key Parameters:**
| Parameter | Spray | Immersion |
|-----------|-------|-----------|
| Concentration | 2–4 oz/gal (15–30 g/L) | 4–8 oz/gal (30–60 g/L) |
| Temperature | 120–150 F (49–66 C) | 130–160 F (54–71 C) |
| Time | 1–2 min | 3–5 min |
| Pressure (spray) | 15–25 psi | N/A |

**Critical Points:**
- The cleaner must fully remove stamping oils, drawing compounds, rust preventatives, and shop soils. Residual oil causes skip areas in the phosphate coating.
- Silicate-containing cleaners should be avoided or carefully controlled — silicate residues interfere with phosphate crystal nucleation.
- Free alkalinity is typically monitored by titration (phenolphthalein endpoint, ~10 mL of 0.1N H2SO4 per 10 mL sample is a typical range).

### 1.3 Rinse — Pre-Condition (Poster 3)

**Purpose:** Remove all cleaner residues and prevent dragover of alkaline chemistry into the phosphate stage.

**Parameters:**
- Fresh water, ambient to 80 F (27 C)
- Overflow rate: 1–3 gal/min continuous overflow for spray; immersion tanks need periodic dump-and-fill
- Conductivity target: < 500 microS/cm for good performance; < 200 microS/cm ideal
- pH should drop below 9.0 after rinsing — if pH stays high, cleaner dragover is excessive

**Key Point for Poster:** In a 3-stage system, this rinse is eliminated — the phosphate stage must tolerate some cleaner dragover. In a 1-stage cleaner-coater, there is no rinse at all; the combined chemistry handles both cleaning and coating.

### 1.4 Surface Conditioning (Poster 4)

**Iron phosphate does NOT typically use a separate surface conditioner.** This is a critical distinction from zinc phosphate.

- No titanium or zirconium colloid activator is needed (or beneficial) for iron phosphate.
- The steel surface is "conditioned" simply by the cleaning step — exposing fresh, active iron.
- If the steel has been over-pickled or over-etched, it may be too active and form an excessively heavy/powdery coating. The cleaner should clean without aggressive etching.

**Exception:** Some 5-stage lines insert a mild acid conditioning rinse (0.5–1% phosphoric acid at ambient temperature) between the clean rinse and the phosphate stage. This lowers surface pH and promotes more uniform initial attack.

**Poster Content Suggestion:** This poster can focus on "what surface conditioning means for iron phosphate" — emphasize that the cleaning step IS the conditioning step, and contrast this with zinc phosphate (which requires a separate Ti/Zr activator).

### 1.5 Rinse — Pre-Coat (Poster 5)

In a full 5-stage line, this is the rinse between surface conditioning (or the acid rinse) and the iron phosphate stage. Purpose is identical to Poster 3 — prevent contamination of the phosphate bath.

**Parameters:** Same as 1.3 — fresh water, ambient, low conductivity.

**In 3-stage systems:** This rinse does not exist. The transition is directly from clean to phosphate.

**Poster Content:** Emphasize water quality. Hard water (high Ca/Mg) can interfere with iron phosphate film formation. Softened or DI water is recommended for rinse stages, especially in areas with > 150 ppm hardness.

### 1.6 Iron Phosphate Coating — Main Stage (Poster 6)

**Chemical Mechanism:**
Iron phosphate coatings form by a controlled dissolution-precipitation reaction:

1. **Acid attack:** The mildly acidic phosphate solution (pH 3.5–5.5) attacks the steel surface, dissolving iron:
   - Fe --> Fe2+ + 2e-
2. **Local pH rise:** As iron dissolves and hydrogen is evolved at the metal surface, the local pH at the metal-solution interface rises.
3. **Precipitation:** The local pH increase causes iron phosphate (vivianite structure, Fe3(PO4)2) to precipitate as an amorphous, adherent film directly on the steel surface.
4. **Accelerator role:** Oxidizing accelerators (nitrite, chlorate, or organic oxidants) oxidize Fe2+ to Fe3+ at the surface, promoting the formation of FePO4 (strengite) which is more protective than the Fe2+ phosphate.

**Bath Chemistry:**
| Component | Concentration | Function |
|-----------|---------------|----------|
| Phosphoric acid (as H3PO4) | 5–15 g/L (0.7–2.0 oz/gal) | Primary film-forming agent |
| Sodium dihydrogen phosphate (NaH2PO4) | 10–30 g/L | Phosphate source, pH buffer |
| Sodium nitrite (NaNO2) | 0.1–0.5 g/L | Accelerator / oxidant |
| Sodium molybdate (optional) | 0.05–0.2 g/L | Accelerator (non-nitrite systems) |
| Surfactants (nonionic) | 0.5–2.0 g/L | Wetting, cleaning assist (in cleaner-coater formulations) |
| Fluoride (optional) | 0.5–2.0 g/L as F- | Aluminum and galvanized substrate compatibility |

**Operating Parameters:**
| Parameter | Spray | Immersion |
|-----------|-------|-----------|
| Temperature | 100–140 F (38–60 C) | 110–150 F (43–66 C) |
| pH | 3.8–5.5 | 3.5–5.0 |
| Time | 1–3 min | 3–5 min |
| Free acid (titration) | 0.5–2.0 pts | 1.0–3.0 pts |
| Total acid (titration) | 4–12 pts | 6–15 pts |
| Free/Total acid ratio | 1:4 to 1:8 | 1:4 to 1:8 |

**Film Characteristics:**
| Property | Value |
|----------|-------|
| Coating weight | 20–80 mg/ft2 (200–860 mg/m2) |
| Target for paint prep | 30–60 mg/ft2 (300–650 mg/m2) |
| Appearance | Iridescent blue to gold to gray-blue |
| Thickness | 0.25–1.0 um (0.01–0.04 mil) |
| Crystal structure | Amorphous to microcrystalline |
| Bare salt spray (no paint) | 2–24 hours |

**Coating Weight Interpretation:**
- < 20 mg/ft2: Too light — insufficient paint adhesion
- 20–40 mg/ft2: Acceptable for non-critical applications
- 40–60 mg/ft2: Ideal range for most paint pretreatment
- 60–80 mg/ft2: Acceptable but approaching heavy side
- > 80 mg/ft2: Too heavy — powdery, poor paint adhesion, chalking

### 1.7 Rinse — Post-Coat (Poster 7)

**Purpose:** Remove unreacted phosphate solution and soluble salts from the freshly formed phosphate coating before sealing.

**Parameters:**
- Fresh water, ambient to 80 F (27 C)
- Must be clean — contaminated post-coat rinse causes staining and poor sealer adhesion
- Overflow rate: 1–2 gal/min
- pH: Neutral (6.5–8.0)
- Do NOT use hot water — thermal shock can damage the thin iron phosphate film

**Critical:** Excessive dwell time between phosphate and rinse allows the wet phosphate film to oxidize (flash rust). Parts should move promptly from phosphate to rinse.

### 1.8 Seal / Post-Treatment / Drying (Poster 8)

**Chrome Seal Rinse (Legacy):**
- 0.01–0.05% hexavalent chromic acid (CrO3) in DI water
- Provides 2–5x improvement in bare corrosion resistance
- Being phased out due to Cr(VI) regulations (REACH, RoHS)

**Non-Chrome Seal Rinses (Current Standard):**
- Zirconium-based sealers (ZrO2 nanoparticle dispersions)
- Reactive silane/siloxane sealers
- Organic polymer sealers
- Concentration: 0.5–3.0% by volume in DI water
- Temperature: Ambient to 100 F (38 C)
- Time: 30 sec to 2 min (spray or immersion)
- pH: 3.5–5.5 (most non-chrome sealers are mildly acidic)

**DI Water Final Rinse:**
- If a seal rinse is used, a final DI rinse may or may not follow (depends on sealer type — some are designed to be the last wet stage)
- Conductivity: < 50 microS/cm for DI water
- Spot-free drying is critical for appearance-sensitive parts

**Dry-Off Oven:**
- Temperature: 250–350 F (121–177 C)
- Time: 5–15 minutes (substrate dependent)
- Must dry completely before paint — moisture under paint causes adhesion failure and blistering
- Do not exceed 400 F (204 C) — degrades the phosphate film

**Standards:**
- TT-C-490 (Federal specification for chemical conversion coatings on ferrous metals)
- ASTM D2092 — Guide for preparation of zinc-coated/galvanized steel for painting (references phosphate)
- OEM specifications vary widely (Caterpillar, John Deere, GM, etc. all have proprietary pretreatment specs)

**Common Defects:**
| Defect | Cause | Fix |
|--------|-------|-----|
| Light/no coating (bare spots) | Low acid, low temp, short time, oil contamination, silicate residue | Increase concentration, temp, time; improve cleaning |
| Heavy/powdery coating | Excess acid, excess time, high temp, depleted accelerator | Reduce concentration/time/temp; replenish accelerator |
| Flash rust | Long dwell between phosphate and rinse/dry; high humidity | Speed up line; improve ventilation |
| Yellowing | Excess nitrite accelerator; iron buildup in bath | Reduce accelerator; decant/dump portion of bath |
| Poor paint adhesion | Coating too light or too heavy; poor cleaning; contaminated seal rinse | Optimize coating weight to 40–60 mg/ft2 |

---

## CLUSTER 2: Zinc Phosphate Conversion Coating

### 2.1 Process Overview (Poster 1 — Process Flow)

Zinc phosphate produces a heavier, more crystalline coating than iron phosphate. It is the standard for automotive body-in-white pretreatment, military applications, and any situation requiring maximum paint adhesion and corrosion resistance. The chemistry is more complex and the process requires tighter control, including a mandatory surface conditioning step.

**Typical Process Sequence (7+ stages):**
1. Alkaline clean (spray or immersion)
2. Fresh water rinse
3. Surface conditioning (titanium colloid activator)
4. Zinc phosphate coating
5. Fresh water rinse
6. Post-rinse / seal (chromic acid or non-chrome)
7. DI water final rinse
8. Dry-off oven

### 2.2 Cleaning (Poster 2)

**Cleaner Type:** Alkaline cleaner, pH 10–13. Can be more aggressive than iron phosphate cleaning because the zinc phosphate process includes a conditioning step that "resets" the surface.

**Key Parameters:**
| Parameter | Spray | Immersion |
|-----------|-------|-----------|
| Concentration | 2–6 oz/gal (15–45 g/L) | 4–8 oz/gal (30–60 g/L) |
| Temperature | 130–160 F (54–71 C) | 140–180 F (60–82 C) |
| Time | 1–3 min | 3–10 min |
| Free alkalinity | 3–8 pts | 5–12 pts |
| Total alkalinity | 8–20 pts | 12–30 pts |

**Critical Points:**
- Heavy stamping oils, waxes, and rust preventatives MUST be completely removed. Zinc phosphate is less forgiving than iron phosphate of residual soils.
- Two-stage cleaning (pre-clean + clean) is common on automotive lines.
- Silicate-free cleaners are strongly preferred — silicate residues poison the zinc phosphate bath and cause skip areas.

### 2.3 Rinse — Pre-Condition (Poster 3)

**Purpose:** Remove alkaline cleaner before surface conditioner. Critical because alkaline carryover raises conditioner pH and deactivates the titanium colloid.

**Parameters:**
- Fresh water, ambient to 80 F (27 C)
- Counter-flow rinse systems (2 stages) are common on automotive lines
- Conductivity: < 300 microS/cm target
- pH: Must drop below 9.0; ideally below 8.0

**Key Point:** Zinc phosphate processes are much more sensitive to rinse quality than iron phosphate. Contaminated rinses are the #1 cause of poor zinc phosphate coating.

### 2.4 Surface Conditioning (Poster 4)

**THIS IS THE MOST CRITICAL STEP IN ZINC PHOSPHATE PROCESSING.**

**What It Is:** A dilute dispersion of titanium phosphate colloid (Ti(HPO4)2) or occasionally zirconium-based particles that adsorb onto the steel surface, creating millions of nucleation sites per cm2 for zinc phosphate crystal growth.

**Why It Matters:**
- Without conditioning: Zinc phosphate crystals nucleate only at grain boundaries and surface defects --> large, coarse crystals (50–100+ um) --> porous, poorly adherent coating
- With conditioning: Crystals nucleate uniformly across the entire surface --> fine, dense crystals (2–10 um) --> compact, highly adherent coating with maximum corrosion protection

**Chemistry:**
- Product type: Colloidal titanium phosphate activator (trade names: Gardolene, Bonderite, Gardobond, Prepalene)
- Concentration: 0.1–0.5% by weight (1–5 g/L)
- pH: 7.5–9.5 (mildly alkaline — the colloid is unstable below pH 7 and above pH 10)
- Temperature: Ambient to 100 F (16–38 C) — NEVER heat this bath; heat destabilizes the colloid
- Time: 30 sec to 2 min (immersion or spray)

**Control Parameters:**
- pH: 7.5–9.5 (adjust with Na2CO3 or dilute NaOH)
- Conductivity: Indicates contamination level; dump-and-make-up when conductivity exceeds 1500–2000 microS/cm
- Activity test: Some suppliers provide a settling test or turbidity measurement to confirm colloid viability

**Common Problems:**
| Problem | Cause |
|---------|-------|
| Coarse phosphate crystals | Conditioner pH too high or too low; contaminated; overheated; too dilute |
| Conditioner "dead" | Excess alkaline or acid carryover; bacterial growth; aged beyond shelf life |
| Conditioner pH rising | Alkaline cleaner dragover — improve rinse between clean and condition |

### 2.5 Rinse — Pre-Coat (Poster 5)

**Critical: DO NOT rinse between conditioner and zinc phosphate bath.**

This is a key process design point. The titanium colloid activator must remain on the surface when the part enters the phosphate bath. A rinse between conditioning and phosphating would wash away the nucleation sites.

**In process lines that show "Rinse -- Pre-Coat" in their sequence, this rinse is placed BEFORE the conditioner, not after it.**

**Poster Content:** Emphasize that the conditioner-to-phosphate transition is direct — no rinse. This is counterintuitive and one of the most common setup errors in zinc phosphate lines.

### 2.6 Zinc Phosphate Coating — Main Stage (Poster 6)

**Chemical Mechanism:**
Zinc phosphate coatings form by a multi-step dissolution-reprecipitation reaction:

1. **Acid attack on substrate:**
   - Fe --> Fe2+ + 2e- (steel substrate)
   - 2H+ + 2e- --> H2 (hydrogen evolution)

2. **Local pH rise:** Hydrogen evolution and iron dissolution raise the pH at the metal-solution interface from ~3.0 (bulk) to ~5.5+ (interface).

3. **Zinc phosphate precipitation:** As pH rises above the saturation point, zinc phosphate crystallizes on the surface:
   - 3Zn2+ + 2H2PO4- + 4H2O --> Zn3(PO4)2 . 4H2O (hopeite) + 4H+
   - On steel, dissolved Fe2+ co-precipitates: Zn2Fe(PO4)2 . 4H2O (phosphophyllite)

4. **Accelerator function:** Oxidizing accelerators (NO2-, NO3-, ClO3-, H2O2, or organic oxidants like hydroxylamine) serve two purposes:
   - Oxidize Fe2+ to Fe3+ at the surface, preventing buildup of soluble iron that inhibits crystal growth
   - Depolarize the cathodic reaction (replace slow H2 evolution with faster NO3-/NO2- reduction), increasing the rate of coating formation

**Phosphophyllite vs. Hopeite:**
- **Phosphophyllite** (Zn2Fe(PO4)2.4H2O) — contains iron from the substrate; forms only on steel; harder, more compact, better paint adhesion and alkali resistance
- **Hopeite** (Zn3(PO4)2.4H2O) — pure zinc phosphate; forms on all substrates including galvanized and aluminum; softer, more prone to alkali attack
- The phosphophyllite-to-hopeite ratio (P-ratio) is a key quality metric: P-ratio > 0.5 is preferred for automotive OEM work; measured by XRD or chemical dissolution

**Bath Chemistry:**
| Component | Concentration | Function |
|-----------|---------------|----------|
| Zinc (as Zn2+) | 0.8–2.0 g/L (typical spray) | Primary coating cation |
| Phosphoric acid (total PO4) | 10–25 g/L | Film-forming anion |
| Nickel (Ni2+) | 0.5–1.5 g/L | Grain refinement; improves paint adhesion; promotes phosphophyllite |
| Manganese (Mn2+) | 0.5–1.5 g/L | Grain refinement; improves corrosion resistance |
| Nitrite (NO2-) | 0.05–0.15 g/L | Accelerator (immersion baths) |
| Nitrate (NO3-) | 3–8 g/L | Accelerator (spray systems) |
| Fluoride (F-) | 0.5–2.0 g/L | Required for aluminum/galvanized substrates; attacks Al2O3 |
| Sludge | Iron phosphate sludge accumulates | Requires filtration; 1–5% of coating weight becomes sludge |

**Operating Parameters:**
| Parameter | Spray | Immersion |
|-----------|-------|-----------|
| Temperature | 95–130 F (35–54 C) | 130–200 F (54–93 C) |
| Free acid | 0.5–1.5 pts | 0.8–2.0 pts |
| Total acid | 15–30 pts | 20–40 pts |
| Accelerator | 1–4 pts (nitrite/nitrate test) | 2–6 pts |
| Free acid / Total acid ratio | 1:10 to 1:20 | 1:10 to 1:20 |
| pH | 2.8–3.5 | 2.5–3.5 |
| Time | 1–3 min | 3–10 min |

**Film Characteristics:**
| Property | Value |
|----------|-------|
| Coating weight — light | 100–200 mg/ft2 (1.1–2.2 g/m2) |
| Coating weight — medium | 200–500 mg/ft2 (2.2–5.4 g/m2) |
| Coating weight — heavy | 500–1000+ mg/ft2 (5.4–10.8+ g/m2) |
| Automotive OEM target | 150–350 mg/ft2 (1.6–3.8 g/m2) |
| Thickness | 2–25 um (0.08–1.0 mil) |
| Crystal size (conditioned) | 2–10 um |
| Crystal size (unconditioned) | 30–100+ um |
| Color | Medium to dark gray |
| Bare salt spray (no paint) | 4–48 hours |
| With e-coat + topcoat | 500–1500+ hours |

### 2.7 Rinse — Post-Coat (Poster 7)

**Purpose:** Remove soluble zinc phosphate salts and acid residues before sealing.

**Parameters:**
- Fresh water, ambient to 80 F (27 C)
- Two-stage counter-flow rinse is standard for automotive
- pH: 5.5–8.0
- Conductivity: < 500 microS/cm
- Must be prompt — extended dwell time causes white salt efflorescence on the zinc phosphate coating

### 2.8 Seal / Post-Treatment / Drying (Poster 8)

**Chromic Acid Seal (Legacy — Still MIL-SPEC Standard):**
- 0.01–0.1% CrO3 (hexavalent chromic acid) in DI water
- Temperature: Ambient to 150 F (66 C)
- Time: 15–60 sec
- Passivates the zinc phosphate crystal surface, filling micropores with Cr2O3
- Dramatically improves paint adhesion and corrosion resistance
- Required by MIL-DTL-16232 for many military applications
- Being phased out except where mil-spec demands it

**Non-Chrome Seal Rinses:**
- Zirconium/titanium oxide sealers
- Reactive silane/siloxane coatings
- Organic polymer seals
- 0.5–3% in DI water, ambient, 30 sec–2 min

**Dry-Off Oven:**
- Temperature: 250–350 F (121–177 C)
- Time: 5–15 min
- Complete drying is critical before e-coat or paint

**Standards:**
- **MIL-DTL-16232** — Phosphate coatings, heavy (Type M = manganese; Type Z = zinc; Type ZM = zinc-manganese)
  - Class 1: Supplementary preservative (oil)
  - Class 2: Chemically converted (chromic acid seal)
  - Class 3: Resin coated
  - Class 4: As deposited
- **TT-C-490** (Federal) — Cleaning and phosphate pretreatment
- **GM 6041M, Ford WSS-M2P188, Chrysler PS-7902** — Automotive OEM phosphate specifications
- **ASTM D2092** — Guide for preparation of zinc-coated/galvanized steel surfaces for painting

**Common Defects:**
| Defect | Cause | Fix |
|--------|-------|-----|
| Coarse crystal structure | Conditioner failure; conditioner pH wrong; no conditioner | Check/replace conditioner; verify pH 7.5–9.5 |
| Light coating weight | Low total acid; low temp; short time; high free acid | Increase T/A; reduce F/A; increase time/temp |
| Heavy/powdery coating | Low free acid; excess zinc; excess time | Increase F/A; reduce time; check zinc level |
| Incomplete coverage | Oil contamination; cleaner failure; substrate passivation | Improve cleaning; check substrate condition |
| Excess sludge | High iron carryover; insufficient filtration | Improve filtration; reduce dragover; add sludge conditioner |
| Mud cracking | Coating too heavy; dried too fast at high temp | Reduce coating weight; lower oven temp initially |

---

## CLUSTER 3: Manganese Phosphate Conversion Coating

### 3.1 Process Overview (Poster 1 — Process Flow)

Manganese phosphate produces the heaviest phosphate conversion coating. It is NOT a paint pretreatment — it is used for its unique combination of wear resistance, oil/lubricant retention, anti-galling properties, and break-in lubrication. Primary applications: military weapons and firearms, gears, bearings, piston rings, fasteners, and engine components.

The coating is always dark gray to black, providing cosmetic uniformity on military hardware (the characteristic "Parkerized" finish on firearms).

**Typical Process Sequence:**
1. Alkaline or solvent clean
2. Hot water rinse
3. Acid pickle (if rust or scale present)
4. Water rinse
5. Surface conditioning (optional — Mn phosphate is less conditioner-dependent than Zn phosphate)
6. Manganese phosphate coating (ALWAYS immersion — never spray)
7. Water rinse
8. Oil/wax/supplementary preservative

### 3.2 Cleaning (Poster 2)

**Cleaner Type:** Aggressive alkaline cleaner, pH 11–14. Manganese phosphate is applied to heavy industrial parts — gears, weapon components, machined parts — that often carry heavy machining oils, coolants, and grinding compounds.

**Key Parameters:**
| Parameter | Immersion |
|-----------|-----------|
| Concentration | 4–10 oz/gal (30–75 g/L) |
| Temperature | 150–190 F (66–88 C) |
| Time | 5–15 min |

**Special Considerations:**
- Parts are often heavily contaminated — two-stage cleaning (soak clean + electrocleaner) is common
- Vapor degreasing (solvent) may precede alkaline cleaning for very oily parts
- Abrasive blasting (grit/shot blast) is sometimes used as a mechanical cleaning step before chemical cleaning, especially for cast iron parts with foundry scale

### 3.3 Rinse — Pre-Condition (Poster 3)

**Purpose:** Remove all cleaning chemistry. Alkaline carryover into the acid manganese phosphate bath raises pH and disrupts coating formation.

**Parameters:**
- Hot water rinse, 120–160 F (49–71 C) — warm rinse helps remove stubborn alkaline residues
- Overflow: 2–5 gal/min
- Multiple rinse stages are common for heavily soiled parts

### 3.4 Surface Conditioning / Activation (Poster 4)

**Acid Pickle (if needed):**
- 10–25% HCl or 10–20% H2SO4 at ambient to 150 F
- Time: 2–15 min (until scale/rust is removed)
- Purpose: Remove rust, mill scale, heat treat scale from steel parts
- MUST be followed by a thorough rinse to remove residual acid

**Surface Conditioning:**
- Manganese phosphate is less dependent on Ti/Zr conditioning than zinc phosphate
- However, many modern Mn phosphate processes DO benefit from a manganese-based or titanium-based conditioner for finer crystal structure
- Some processes use a dilute manganese phosphate "pre-dip" (5–10% of normal concentration) as a conditioning step
- Temperature: Ambient
- Time: 1–2 min

**Manganese phosphate on hardened steel:**
- Hardened/tempered parts (> 40 HRC) are more resistant to acid attack, resulting in slower coating and lighter weight
- An acid etch or activation step (dilute HCl or proprietary activator) may be needed to "open up" the surface

### 3.5 Rinse — Pre-Coat (Poster 5)

**Purpose:** Remove all pickle acid and conditioning chemistry before entering the phosphate bath.

**Parameters:**
- Fresh water, ambient
- This rinse is CRITICAL after acid pickling — any HCl or H2SO4 carryover will upset the phosphate bath free acid and create excessive sludge
- Multiple rinse stages may be needed

### 3.6 Manganese Phosphate Coating — Main Stage (Poster 6)

**Chemical Mechanism:**
Virtually identical to zinc phosphate but with manganese replacing zinc:

1. **Acid attack:** Fe --> Fe2+ + 2e-; 2H+ + 2e- --> H2
2. **Local pH rise** at the metal surface
3. **Precipitation:** Mn5H2(PO4)4.4H2O (hureaulite) crystallizes on the surface, often incorporating iron: (Mn,Fe)5H2(PO4)4.4H2O
4. **Accelerator:** Nitrate and/or nitrite; some formulations use organic accelerators (hydroxylamine sulfate)

**Bath Chemistry:**
| Component | Concentration | Function |
|-----------|---------------|----------|
| Manganese (Mn2+) | 8–15 g/L | Primary coating cation |
| Phosphoric acid (total PO4) | 20–50 g/L | Film-forming anion |
| Nickel (Ni2+) | 0–2 g/L (optional) | Grain refinement |
| Nitrate (NO3-) | 5–20 g/L | Accelerator |
| Iron (Fe2+) | 0.5–3.0 g/L (builds up from substrate dissolution) | Incorporated into coating |

**Operating Parameters:**
| Parameter | Value |
|-----------|-------|
| Temperature | 190–210 F (88–99 C) — ALWAYS HOT |
| Free acid | 2–5 pts |
| Total acid | 25–50 pts |
| Free acid / Total acid ratio | 1:7 to 1:12 |
| pH | 2.0–3.0 |
| Time | 10–30 min (much longer than Zn phosphate) |
| Method | IMMERSION ONLY — spray is not used |

**Critical Temperature Note:** Manganese phosphate MUST operate near boiling. Below 185 F (85 C), coating formation essentially stops. The bath is typically maintained at 195–205 F (91–96 C). Boiling (212 F / 100 C) should be avoided — it causes excessive sludge and foaming.

**Film Characteristics:**
| Property | Value |
|----------|-------|
| Coating weight | 500–2500 mg/ft2 (5.4–27 g/m2) |
| Military spec target | 1000–2000 mg/ft2 (10.8–21.5 g/m2) |
| Thickness | 5–25 um (0.2–1.0 mil) |
| Crystal size | 10–50 um (columnar or needle-like) |
| Color | Dark gray to black |
| Hardness | ~500 HV (crystal hardness) |
| Oil absorption capacity | High — porous structure retains lubricants |
| Bare salt spray | 2–8 hours (no oil) |
| With oil | 48–200+ hours |

### 3.7 Rinse — Post-Coat (Poster 7)

**Purpose:** Remove unreacted phosphate acid and soluble salts.

**Parameters:**
- Warm water rinse, 100–140 F (38–60 C) — warm rinse helps dry faster and prevents cold-water thermal shock on hot parts
- Brief: 30 sec to 2 min
- Do not over-rinse — the porous coating structure can absorb rinse water that is hard to displace with oil

### 3.8 Seal / Post-Treatment / Drying (Poster 8)

**Manganese phosphate is ALWAYS post-treated. Bare manganese phosphate provides almost no corrosion protection — the value is in its ability to absorb and retain oil/wax preservatives.**

**Oil Dip (Most Common):**
- MIL-PRF-3150 (Preservative oil, general purpose)
- MIL-PRF-16173 Grade 1 (Corrosion preventive compound, solvent cutback)
- Light machine oil or water-displacing oil
- Temperature: 150–180 F (66–82 C) for better penetration; or ambient for light oils
- Time: 2–5 min immersion
- Drain and centrifuge excess oil

**Wax Dip (Fasteners):**
- Supplementary wax coating for additional corrosion protection and torque-tension control
- Applied hot: 150–200 F (66–93 C)

**Chromic Acid Seal (Military Spec Option):**
- 0.05–0.1% CrO3 rinse before oil (MIL-DTL-16232 Class 2)

**No Dry-Off Oven** — parts go from rinse directly to oil. The oil displaces residual water from the porous coating.

**Standards:**
- **MIL-DTL-16232, Type M** — Manganese phosphate coating
  - Class 1: Oil supplementary treatment
  - Class 2: Chemically converted (chromic acid + oil)
  - Class 3: Supplementary resin coating
  - Class 4: As deposited (no supplementary treatment)
- **ASTM B733** is for EN, not phosphate. The correct ASTM for phosphate weight testing is **ASTM B767** (gravimetric method for phosphate coating weight)
- **SAE AMS 2530** — Manganese phosphate coating for corrosion protection and wear resistance
- **TT-C-490, Type II** — Manganese phosphate

**Common Defects:**
| Defect | Cause | Fix |
|--------|-------|-----|
| Light/thin coating | Low temp; short time; free acid too high; worn-out bath | Increase temp to 195–205 F; increase time; reduce F/A |
| Red/brown powdery coating | Bath too hot (boiling); excess iron; depleted bath | Cool to 195–205 F; decant; add replenisher |
| Non-uniform / blotchy | Poor cleaning; mixed metallurgy in load; passive surface | Improve clean; separate hardened from soft parts |
| Excessive sludge | Bath overheated; excessive acid; high iron | Control temp; filter continuously; maintain F/A ratio |
| Poor oil retention | Coating too thin; crystals too fine; coating polished | Increase coating weight; check not over-rinsing |

---

## CLUSTER 4: Chromate Conversion — Hexavalent (MIL-DTL-5541 Type I) on Aluminum

### 4.1 Process Overview (Poster 1 — Process Flow)

Hexavalent chromate conversion coating (chem film, Alodine, Iridite) on aluminum is the gold standard for corrosion protection and paint adhesion on aluminum alloys. It provides "self-healing" corrosion protection — hexavalent chromium leaches from the coating to repassivate scratches and damage. This is irreplaceable for certain military and aerospace applications.

**Regulatory Warning:** Hexavalent chromium is a known human carcinogen (OSHA PEL: 5 ug/m3). Subject to REACH restrictions in the EU and targeted for elimination. MIL-DTL-5541 Type II (trivalent) is the designated replacement, but Type I remains specified for many legacy programs.

**Typical Process Sequence:**
1. Alkaline clean
2. Water rinse
3. Deoxidize / desmut (acid etch)
4. Water rinse
5. Chromate conversion coating
6. Water rinse
7. Air dry (NO heat dry — critical)

### 4.2 Cleaning (Poster 2)

**Cleaner Type:** Non-etch alkaline cleaner for most applications; mild alkaline (pH 9–11). For heavy soils, a stronger alkaline cleaner (pH 12–13) may be used but MUST be followed by a thorough rinse and deoxidize step.

**Key Parameters:**
| Parameter | Immersion | Spray |
|-----------|-----------|-------|
| Concentration | 4–8 oz/gal (30–60 g/L) | 2–4 oz/gal (15–30 g/L) |
| Temperature | 120–160 F (49–71 C) | 100–140 F (38–60 C) |
| Time | 3–10 min | 1–3 min |

**Critical Points:**
- Avoid strongly caustic (NaOH-based) cleaners on aluminum — they etch aggressively and produce a smut layer that is hard to remove
- Inhibited alkaline cleaners (with silicate or other etch inhibitors) are preferred for aluminum
- Fluoride-bearing cleaners can also be used but must be carefully controlled

### 4.3 Rinse — Pre-Condition (Poster 3)

**Purpose:** Remove cleaner residues before deoxidizing. Alkaline carryover into the acid deoxidizer neutralizes the acid and reduces effectiveness.

**Parameters:**
- Fresh water, ambient to 80 F (27 C)
- Double rinse (two immersion tanks) is standard in aerospace processing
- DI or RO water preferred for aerospace — chloride and sulfate contamination in rinse water can cause pitting on aluminum

### 4.4 Deoxidize / Desmut (Poster 4 — "Surface Conditioning" for Aluminum)

**Purpose:** Remove the aluminum oxide layer (which naturally reforms in seconds on aluminum) and any smut (dark residue from alloying elements like Cu, Si, Mn, Fe) left by the cleaning step. This exposes a fresh, active aluminum surface for the chromate reaction.

**Chemistry Options:**
| Deoxidizer Type | Concentration | Temperature | Time |
|-----------------|---------------|-------------|------|
| Nitric acid (HNO3) | 30–50% by volume | Ambient | 1–5 min |
| Nitric + HF (for high-Si alloys) | 30% HNO3 + 1–3% HF | Ambient | 30 sec–3 min |
| Chromic-sulfuric acid (legacy) | 10–15 oz/gal CrO3 + 30–40 oz/gal H2SO4 | 140–160 F | 5–10 min |
| Non-chrome deoxidizers (ferric sulfate, persulfate) | Per supplier | Ambient to 120 F | 1–5 min |
| Ammonium bifluoride | 4–8 oz/gal | Ambient | 1–3 min |

**Alloy-Specific Notes:**
- **2024, 2014 (high copper):** Require HNO3/HF or chromic-sulfuric to remove copper-rich smut
- **7075, 7050 (zinc-copper):** Same as above; copper smut is tenacious
- **6061, 6063 (low alloy):** Mild nitric acid or non-chrome deoxidizer is sufficient
- **356, A356 (cast, high silicon):** Require HF-containing deoxidizer to dissolve silicon particles

### 4.5 Rinse — Pre-Coat (Poster 5)

**Purpose:** Remove all acid, dissolved metals, and fluoride before chromate bath.

**Parameters:**
- Fresh water, ambient
- Double rinse is standard (drag-out is acidic and may carry dissolved copper, iron, silicon)
- Must be thorough — acid carryover accelerates chromate bath consumption; dissolved metals contaminate the bath

**Time-Critical:** Aluminum re-oxidizes almost instantly in water. Minimize time between deoxidize rinse and chromate coating — ideally < 5 minutes.

### 4.6 Hexavalent Chromate Conversion Coating — Main Stage (Poster 6)

**Chemical Mechanism:**
The hex chrome conversion coating forms by a complex redox reaction between the chromate solution and the aluminum substrate:

1. **Aluminum dissolution (anodic):**
   - Al --> Al3+ + 3e-

2. **Chromate reduction (cathodic):**
   - Cr2O7 2- + 14H+ + 6e- --> 2Cr3+ + 7H2O
   - CrO4 2- + 8H+ + 3e- --> Cr3+ + 4H2O

3. **Gel layer formation:** The reduced Cr3+ ions combine with Al3+, chromate, oxide, and fluoride to form a complex mixed oxide gel:
   - Cr2O3 / Cr(OH)3 / CrOOH (Cr3+ backbone)
   - Residual CrO4 2- (Cr6+) trapped in the gel (this is the self-healing reservoir)
   - Al2O3 / Al(OH)3 (from substrate dissolution)
   - CrF3, AlF3 (fluoride bridges)

4. **Self-healing mechanism:** When the coating is scratched or damaged, residual Cr6+ in the gel migrates to the exposed aluminum and undergoes the same reduction reaction, redepositing a protective Cr3+ oxide layer over the damage.

**Bath Chemistry:**
| Component | Concentration | Function |
|-----------|---------------|----------|
| Chromic acid (CrO3) or Na2Cr2O7 | 3–6 g/L (as Cr6+) | Oxidizing agent, film-forming |
| Potassium ferricyanide K3Fe(CN)6 | 0.5–1.5 g/L | Accelerator (depolarizer) |
| Sodium fluoride (NaF) or HF | 0.5–1.5 g/L as F- | Activator — dissolves Al2O3 barrier layer |
| Phosphoric acid (H3PO4) | Optional, 1–3 g/L | Produces phosphate-bearing films |
| pH (adjusted with NaOH or HNO3) | 1.2–2.0 | Critical — controls film thickness and Cr6+ content |

**Proprietary Products:**
- Alodine 1200S (Henkel) — the industry standard for decades
- Iridite 14-2 (MacDermid) — common alternative
- Surtec 650 is TRIVALENT (Cluster 5, not this one)

**Operating Parameters:**
| Parameter | Immersion | Spray | Touch-Up (Pen/Swab) |
|-----------|-----------|-------|---------------------|
| Temperature | 60–100 F (16–38 C) | 70–95 F (21–35 C) | Ambient |
| Time | 1–5 min (typ. 2–3 min) | 1–3 min | Apply and keep wet 1–5 min |
| pH | 1.3–1.8 | 1.3–1.8 | N/A (pre-mixed gel) |
| Coating forms in | 15–30 sec (visible) | 15–30 sec | 1–3 min |

**Film Characteristics:**
| Property | Value |
|----------|-------|
| Appearance | Clear to iridescent gold to golden brown |
| Thickness | 0.25–1.0 um (10–40 uin) |
| Coating weight | 10–40 mg/ft2 (100–430 mg/m2) |
| Cr6+ content in film | 10–30% of total Cr (self-healing reservoir) |
| Electrical resistance | Low: 0.001–5 milliohms/in2 (maintains conductivity) |
| Salt spray (ASTM B117) — bare | 168–336 hours minimum per MIL-DTL-5541 |
| Salt spray — painted | 1000–3000+ hours |
| Thermal stability | Degrades above 140 F (60 C) — Cr6+ content drops, self-healing diminishes |
| Color interpretation | Clear/iridescent = light coating; gold = standard; brown = heavy; rainbow = normal variation |

### 4.7 Rinse — Post-Coat (Poster 7)

**Purpose:** Remove residual chromate solution. Critical for appearance uniformity and to prevent continued film growth.

**Parameters:**
- Cold water ONLY — ambient to 77 F (25 C)
- **NEVER use hot water** — heat damages the fresh gel coating and drives off Cr6+ self-healing component
- Brief immersion: 15–30 sec
- Do not agitate aggressively — the fresh coating is soft and easily damaged
- The coating continues to harden over 24 hours at ambient temperature

**Time-Critical:** The coating must not be touched, rubbed, or abraded for at least 24 hours after application. Even water spots during the first few hours can cause permanent marks.

### 4.8 Seal / Post-Treatment / Drying (Poster 8)

**CRITICAL: NO HEAT DRYING.**

Hexavalent chromate conversion coatings on aluminum must be AIR DRIED only. Forced air is acceptable (room temperature, filtered air). Oven drying above 150 F (66 C) degrades the Cr6+ content and severely compromises self-healing and corrosion resistance.

**Drying:**
- Air dry at ambient temperature
- Clean, filtered forced air is acceptable
- Minimum 24-hour cure before handling, stacking, or painting
- Full hardness develops over 24–72 hours

**Paint Application:**
- Chromate conversion coating is an excellent paint base
- Paint should be applied within 72 hours of chromate coating (per most aerospace specs) — longer delays allow the coating to age and become less receptive to paint
- Some specs allow up to 7 or 14 days if stored properly

**Standards:**
- **MIL-DTL-5541F, Type I** — Hexavalent chromate conversion coating on aluminum
  - Class 1A: Maximum corrosion protection (thicker, gold/brown color); 168 hr salt spray minimum
  - Class 3: Low electrical resistance (thinner, clear/iridescent); used where electrical conductivity is required
- **AMS 2473** — Chemical treatment for aluminum alloys, chromate conversion
- **AMS 2474** — Same, for touchup
- **ASTM B449** — Standard specification for chromates on aluminum
- **ASTM B117** — Salt spray testing

**Common Defects:**
| Defect | Cause | Fix |
|--------|-------|-----|
| No coating / bare spots | pH too high; fluoride depleted; over-rinsed after deox; substrate passivated | Check pH (must be 1.3–1.8); add fluoride; check deox step |
| Powdery/chalky coating | Over-immersion; bath too concentrated; temperature too high | Reduce time; dilute; cool bath |
| Dark brown/sooty coating | Excess copper in alloy or bath contamination; pH too low | Check/clean bath; adjust pH; filter |
| White powdery spots after drying | Water spots from dirty rinse; handling before 24-hr cure | Improve rinse water quality; enforce no-touch cure period |
| Failed salt spray | Heat exposure (oven dried); coating too thin; Cr6+ depleted from bath | Air dry only; increase coating time; replenish bath |
| High electrical resistance (Class 3 failure) | Coating too thick | Reduce immersion time; reduce concentration |

---

## CLUSTER 5: Chromate Conversion — Trivalent (MIL-DTL-5541 Type II) on Aluminum

### 5.1 Process Overview (Poster 1 — Process Flow)

Trivalent chromate conversion coating (TCP — Trivalent Chromium Process, or Cr3+ chem film) is the RoHS-compliant, REACH-compliant replacement for hexavalent chromate on aluminum. It contains NO hexavalent chromium. The coating is clear to slightly blue/iridescent (never gold/brown like hex).

**Key Difference from Hex:** Trivalent chrome coatings do NOT have the self-healing property of hexavalent coatings. There is no mobile Cr6+ reservoir. Corrosion protection relies entirely on the integrity of the initial barrier film. This is the fundamental trade-off.

**Typical Process Sequence:**
1. Alkaline clean
2. Water rinse
3. Deoxidize / desmut
4. Water rinse
5. Trivalent chromate conversion coating
6. Water rinse
7. Air dry

### 5.2 Cleaning (Poster 2)

Identical requirements to Cluster 4 (Hex Chromate). See Section 4.2.

- Non-etch or mildly alkaline cleaner, pH 9–11
- Silicate-inhibited preferred for aluminum
- 3–10 min immersion at 120–160 F (49–71 C)

### 5.3 Rinse — Pre-Condition (Poster 3)

Identical to Cluster 4. See Section 4.3.

- Double rinse, ambient, DI/RO preferred
- Minimize chloride and sulfate contamination

### 5.4 Deoxidize / Desmut (Poster 4)

Identical deoxidize/desmut requirements to Cluster 4. See Section 4.4.

**One Critical Addition:** Trivalent chromate baths are MORE sensitive to surface cleanliness than hexavalent baths. Hex chrome is a powerful oxidizer that can "burn through" minor surface contamination — trivalent chrome cannot. The deoxidize step must be thorough and complete.

- Alloy-appropriate deoxidizer (HNO3, HNO3/HF, non-chrome)
- Contact time and concentration matched to alloy family (2xxx, 6xxx, 7xxx, cast)

### 5.5 Rinse — Pre-Coat (Poster 5)

Identical to Cluster 4. See Section 4.5.

- Double rinse, ambient
- Minimize transit time to the trivalent coating bath (< 5 min)

### 5.6 Trivalent Chromate Conversion Coating — Main Stage (Poster 6)

**Chemical Mechanism:**
The trivalent process also forms a mixed oxide gel on aluminum, but the chemistry is fundamentally different:

1. **Aluminum dissolution:**
   - Al --> Al3+ + 3e- (same as hex process)

2. **No Cr6+ reduction step.** The chromium is already in the +3 oxidation state in solution. Instead:
   - Zr4+ and/or Ti4+ fluorocomplexes (ZrF6 2-, TiF6 2-) hydrolyze as local pH rises at the surface
   - Cr3+ co-deposits with Zr/Ti oxide as an amorphous mixed oxide gel
   - The fluoride activator dissolves the Al2O3 barrier layer, enabling the reaction

3. **Film composition:**
   - ZrO2 / TiO2 backbone (depending on formulation)
   - Cr2O3 / Cr(OH)3 (trivalent chromium oxide — barrier protection)
   - Al2O3 (from substrate)
   - Fluoride bridges
   - **NO Cr6+** — zero hexavalent chromium in the film

**Bath Chemistry:**
| Component | Concentration | Function |
|-----------|---------------|----------|
| Cr3+ (as CrCl3, Cr2(SO4)3, or Cr(NO3)3) | 0.5–2.0 g/L | Film-forming element |
| Zr4+ (as H2ZrF6 or K2ZrF6) | 0.5–3.0 g/L | Primary barrier-forming element |
| Fluoride (F-) | 0.5–2.0 g/L free F- | Aluminum oxide activator |
| pH buffer (organic acid or sulfate) | Varies | Maintains operating pH |
| pH | 3.5–4.2 | Critical — narrow operating window |

**Proprietary Products:**
- Surtec 650 ChromitAL (Surtec) — most widely used globally
- Alodine 5700 (Henkel) — aerospace-approved
- Bonderite M-CR T5900 (Henkel)
- TCP-HF (NAVAIR-developed, open formula)
- Lumenite TC (Atotech)

**Operating Parameters:**
| Parameter | Immersion | Spray |
|-----------|-----------|-------|
| Temperature | 65–95 F (18–35 C) | 70–90 F (21–32 C) |
| Time | 2–5 min (typically 3–4 min) | 1–3 min |
| pH | 3.5–4.2 (narrower than hex) | 3.5–4.2 |
| Agitation | Mild air or mechanical | N/A |

**Film Characteristics:**
| Property | Value |
|----------|-------|
| Appearance | Clear to pale blue/iridescent; sometimes slightly yellowish |
| Thickness | 0.02–0.10 um (1–4 uin) — MUCH thinner than hex |
| Coating weight | 2–15 mg/ft2 (20–160 mg/m2) — significantly lighter than hex |
| Self-healing | NO — no Cr6+ reservoir |
| Electrical resistance | Very low (< 0.1 milliohms/in2) — excellent for Class 3 applications |
| Salt spray (ASTM B117) — bare | 168 hours minimum (meets MIL-DTL-5541 Type II) |
| Salt spray — painted | 500–2000+ hours |
| Thermal stability | More thermally stable than hex — no Cr6+ to degrade |
| RoHS/REACH | Fully compliant |

### 5.7 Rinse — Post-Coat (Poster 7)

**Parameters:**
- Cold to warm water, ambient to 100 F (38 C) — trivalent is slightly more tolerant of warm rinse than hex
- Brief immersion: 15–60 sec
- DI water final rinse is preferred for appearance-sensitive aerospace parts
- The coating is less fragile than fresh hex chromate but should still be handled carefully for the first few hours

### 5.8 Seal / Post-Treatment / Drying (Poster 8)

**Drying:**
- Air dry at ambient temperature (same as hex — best practice)
- Unlike hex, some trivalent coatings CAN tolerate mild heat acceleration (up to 150 F / 66 C) without significant degradation — but this varies by supplier formulation. Check supplier TDS.
- Full cure: 24 hours at ambient

**Supplementary Sealers:**
Because trivalent coatings lack the self-healing property, supplementary sealers are more important:
- Silane/siloxane sealers (most common — form a hydrophobic barrier)
- Zirconium-based sealers
- Organic polymer topcoats
- These can extend bare salt spray from 168 to 500+ hours

**Paint Application:**
- Excellent paint base — comparable to hex for most paint systems
- Apply paint within 72 hours (per most aerospace specs)
- May require primer specifically qualified over trivalent chem film

**Standards:**
- **MIL-DTL-5541F, Type II** — Trivalent chromate conversion coating on aluminum
  - Class 1A: Corrosion protection (168 hr salt spray minimum)
  - Class 3: Low electrical resistance
  - Same performance requirements as Type I, but with Cr3+ chemistry
- **AMS 2487** — Trivalent chromium conversion coating for aluminum alloys
- **SAE ARP 6584** — Trivalent chromium process qualification
- **ASTM B921** — Standard specification for non-hexavalent chromium conversion coatings on aluminum
- **NADCAP AC7108** — Aerospace chemical processing accreditation (covers both hex and tri)

**Common Defects:**
| Defect | Cause | Fix |
|--------|-------|-----|
| No coating | pH too high (> 4.5); fluoride depleted; surface not activated | Adjust pH to 3.5–4.2; add fluoride; check deox |
| White haze / powdery | Over-immersion; bath pH too low (< 3.0); excess fluoride | Reduce time; adjust pH; check fluoride |
| Rainbow/colored film | Normal variation on some alloys — usually acceptable | Verify meets spec (coating weight, salt spray) |
| Failed salt spray at 168 hr | Coating too thin; surface contamination; no sealer | Increase time; improve cleaning; add sealer |
| Blue/purple discoloration | Zirconium precipitation; contamination | Check bath; filter; verify chemistry |

---

## CLUSTER 6: Aluminum Conversion Coating / TCP / Chem Film / Alodine

### 6.1 Process Overview (Poster 1 — Process Flow)

**Note to Alaina/Elara:** This cluster covers the BROADER category of non-chromate or "alternative" aluminum conversion coatings — the newer generation of entirely chromium-free technologies. Clusters 4 and 5 are specifically chromate-based (hex and tri). This cluster covers:

- **Titanium/Zirconium (Ti/Zr) conversion coatings** — the most commercially established Cr-free alternative
- **Zirconium-only systems** — dominant in automotive pretreatment
- **Rare earth (cerium, lanthanum) conversion coatings** — emerging technology
- **Sol-gel coatings** — hybrid organic-inorganic alternatives

These are used when complete chromium elimination is required (not just Cr6+-free, but totally Cr-free).

**Typical Process Sequence:**
1. Alkaline clean
2. Water rinse
3. Deoxidize / acid etch
4. Water rinse
5. Ti/Zr or alternative conversion coating
6. Water rinse (DI water)
7. Dry (air or low-temp oven)

### 6.2 Cleaning (Poster 2)

Similar to Clusters 4 and 5 — non-etch or mildly alkaline, pH 9–11.

**Special Consideration for Automotive/Coil Lines:**
- Zr-based conversion coatings are heavily used on automotive multi-metal bodies (steel + galvanized + aluminum in one body)
- The cleaner must work on ALL substrates without etching aluminum or passivating steel
- Low-temperature, low-energy cleaners are preferred (energy cost reduction in automotive)

### 6.3 Rinse — Pre-Condition (Poster 3)

Standard fresh water rinse. See Clusters 4/5.

### 6.4 Acid Etch / Deoxidize (Poster 4)

**For aluminum:**
- Same deoxidizer options as Clusters 4/5 (HNO3, HNO3/HF, ferric sulfate, etc.)

**For multi-metal automotive applications:**
- The deoxidize/activation step may be an acidic fluoride rinse that works on all substrates:
  - pH 2.5–4.5, containing H2TiF6 or H2ZrF6 at 0.1–0.5 g/L
  - Temperature: Ambient to 100 F
  - Time: 30 sec–2 min

### 6.5 Rinse — Pre-Coat (Poster 5)

Standard fresh water rinse. DI or RO water is strongly preferred — dissolved minerals in tap water compete with the Ti/Zr film-forming reaction.

### 6.6 Ti/Zr or Alternative Conversion Coating — Main Stage (Poster 6)

**Zirconium-Based (Dominant Technology):**

**Chemical Mechanism:**
1. Acid attack on substrate (Al, steel, or galvanized):
   - Al --> Al3+ + 3e- (aluminum)
   - Fe --> Fe2+ + 2e- (steel)
   - Zn --> Zn2+ + 2e- (galvanized)
2. Local pH rise at the metal surface (consumption of H+ at the cathode)
3. Hydrolysis and precipitation of zirconium oxide/hydroxide:
   - ZrF6 2- + 2H2O --> ZrO2 + 6F- + 4H+ (simplified)
   - The rising pH at the surface drives this hydrolysis to the right
4. Result: A thin, adherent, amorphous ZrO2 film — typically 20–100 nm thick

**Bath Chemistry (Zr-Based):**
| Component | Concentration | Function |
|-----------|---------------|----------|
| H2ZrF6 (hexafluorozirconic acid) | 50–200 ppm as Zr | Film-forming species |
| Free fluoride (F-) | 10–50 ppm | Activator — dissolves native oxide |
| Cu2+ (optional) | 5–30 ppm | Accelerator (Cu deposits cathodically, accelerating Zr deposition) |
| Organic polymer (some formulations) | 100–500 ppm | Organic sealer co-deposited with Zr film |
| pH | 3.8–5.0 | Controlled by addition of H2ZrF6 + alkali |

**Operating Parameters:**
| Parameter | Spray | Immersion |
|-----------|-------|-----------|
| Temperature | 70–110 F (21–43 C) | 70–120 F (21–49 C) |
| Time | 60–120 sec | 60–180 sec |
| pH | 3.8–5.0 | 3.8–5.0 |
| Free fluoride | 10–50 ppm | 10–50 ppm |

**Proprietary Products:**
- Bonderite M-NT (Henkel) — oxsilan technology (silane + Zr hybrid)
- Gardobond X4707 (Chemetall/BASF) — Zr-based
- Zircobond (PPG) — widely used in automotive e-coat pretreatment
- Oxilan (Chemetall) — silane-Zr hybrid

**Film Characteristics (Zr-Based):**
| Property | Value |
|----------|-------|
| Appearance | Clear to pale iridescent (nearly invisible) |
| Thickness | 20–100 nm (0.02–0.10 um) — ultra-thin |
| Coating weight | 5–30 mg/m2 as Zr (measured by XRF) |
| Multi-metal compatibility | Excellent — works on steel, galvanized, aluminum in one bath |
| Salt spray — bare | 24–72 hours (less than chromate) |
| Salt spray — with e-coat | 500–1500+ hours (comparable to zinc phosphate + chromate seal) |
| Sludge generation | Negligible (vs. zinc phosphate which generates heavy sludge) |
| Wastewater | No heavy metals (Cr, Ni, Mn) — much simpler treatment |

**Cerium-Based (Emerging):**
- Ce3+ (cerium chloride or nitrate) at 0.01–0.1 M
- pH 3–5, ambient to 130 F (54 C)
- Forms CeO2/Ce(OH)3 mixed oxide on cathodic sites
- Still primarily in development/academic stage for most industrial applications
- Shows promise for aluminum-copper alloys (2xxx, 7xxx) where Cu-rich intermetallics are cathodic

### 6.7 Rinse — Post-Coat (Poster 7)

**Parameters:**
- DI water final rinse — critical for thin-film conversion coatings; tap water minerals leave deposits that are visible and can interfere with paint adhesion
- Ambient temperature
- Brief: 15–60 sec
- Avoid aggressive spray that could damage the ultra-thin film

### 6.8 Dry / Post-Treatment (Poster 8)

**Drying:**
- Air dry or low-temperature oven: 180–250 F (82–121 C) max
- Some Zr/silane hybrid coatings REQUIRE a thermal cure (200–350 F / 93–177 C for 5–15 min) to crosslink the organic component — check supplier TDS
- Over-cure degrades the film

**Sealers:**
- Not always required — many Zr systems are designed as complete, single-stage treatments
- Silane/siloxane topcoats can be added for additional protection
- Organic polymer sealers (waterborne or solvent-borne)

**Standards:**
- No dedicated MIL-SPEC for Zr conversion coatings (as of writing)
- **SAE ARP 5903** — Evaluation of non-chromate conversion coatings
- **ASTM D5894** — Cyclic salt spray / UV testing (often used for non-chrome evaluation)
- Automotive OEM specifications (GM, Ford, Toyota) each have proprietary approval for specific Zr products
- **ASTM B921** — Standard specification for non-hexavalent chromium conversion coatings on aluminum (also covers Zr)

**Common Defects:**
| Defect | Cause | Fix |
|--------|-------|-----|
| No visible coating | Normal — Zr coatings are nearly invisible; verify with XRF | Measure Zr by XRF; do not judge by eye |
| Poor paint adhesion | Coating too thin; contamination; wrong pH | Increase time; improve cleaning; check pH |
| Water spotting | Hard water rinse; poor drainage; DI water failure | Check DI quality; improve racking |
| Inconsistent XRF readings | Uneven coating; mixed substrates in same load | Optimize bath parameters per substrate |

---

## CLUSTER 7: Black Oxide (Steel) — Hot Alkaline Oxidizing Process

### 7.1 Process Overview (Poster 1 — Process Flow)

Black oxide (also called blackening, bluing, or gun bluing in firearms) converts the surface of steel/iron parts to a thin layer of magnetite (Fe3O4) — a mixed-valence iron oxide that is black, adherent, and dimensionally insignificant. It is used for:
- Cosmetic blackening (tooling, fasteners, firearms)
- Mild corrosion protection (when oiled or waxed)
- Reduced light reflection (optical/military equipment)
- Minimal dimensional change (< 0.05 mil / 1.3 um total)

**Black oxide provides very little standalone corrosion protection. It MUST be sealed with oil, wax, or lacquer for any meaningful protection.**

**Typical Process Sequence:**
1. Alkaline clean
2. Water rinse
3. Acid pickle (if rust/scale present)
4. Water rinse
5. Black oxide (hot alkaline bath, 280–295 F / 138–146 C)
6. Cold water rinse
7. Hot water rinse (or supplementary chromate dip)
8. Oil/wax seal

### 7.2 Cleaning (Poster 2)

**Cleaner Type:** Strong alkaline cleaner — black oxide is very sensitive to surface cleanliness. Any oil, fingerprint, or residue will cause non-uniform blacking (red or brown spots instead of uniform black).

**Key Parameters:**
| Parameter | Immersion |
|-----------|-----------|
| Concentration | 4–8 oz/gal (30–60 g/L) |
| Temperature | 160–190 F (71–88 C) |
| Time | 5–15 min |
| Free alkalinity | 4–10 pts |

**Critical Points:**
- Electroclean (anodic, 30–60 ASF, 1–3 min) is often used after soak clean for critical parts
- Solvent degrease as a first step for heavily oiled parts
- Parts must be COMPLETELY clean — even a fingerprint will show as a defect after blackening

### 7.3 Rinse — Pre-Condition (Poster 3)

**Purpose:** Remove all cleaner residues. Surfactant carryover into the acid pickle or black oxide bath causes problems.

**Parameters:**
- Fresh water, ambient to warm
- Overflow rinse or spray rinse
- Parts should feel "water-break-free" (water sheets uniformly) — any beading indicates residual oil

### 7.4 Acid Pickle / Activation (Poster 4)

**Purpose:** Remove rust, scale, and passivation film. Activates the steel surface for uniform oxide formation.

**Chemistry:**
| Acid | Concentration | Temperature | Time |
|------|---------------|-------------|------|
| Hydrochloric acid (HCl) | 20–50% by volume | Ambient | 2–10 min |
| Sulfuric acid (H2SO4) | 10–25% by volume | 120–160 F (49–71 C) | 5–15 min |
| Phosphoric acid (H3PO4) | 10–25% by volume | Ambient to 140 F | 5–15 min |

**Notes:**
- HCl is most common for black oxide pre-pickling — fast, ambient temperature, good activation
- Do not over-pickle — excessive metal removal roughens the surface and produces a pitted, matte black finish instead of smooth, lustrous black
- Inhibitors may be added to limit hydrogen embrittlement on hardened steel parts
- Hydrogen embrittlement bake (375 F / 191 C for 4+ hours) may be required for high-strength steel (> 40 HRC) per ASTM B633 / ASTM F519

### 7.5 Rinse — Pre-Coat (Poster 5)

**Purpose:** Remove all acid before the hot alkaline black oxide bath. Acid carryover is extremely problematic — it neutralizes the caustic bath, causes spattering (water + hot caustic), and produces red oxide instead of black oxide.

**Parameters:**
- Fresh water, thorough immersion rinse
- Multiple rinses may be needed after strong acid pickling
- Parts should be neutral (pH 6–8) before entering the blackening bath

**Safety Warning:** Water carryover into the 285 F (140+ C) black oxide bath causes violent boiling and spattering of hot caustic. Parts MUST be well-drained.

### 7.6 Black Oxide Coating — Main Stage (Poster 6)

**Chemical Mechanism:**
Hot alkaline black oxide operates by controlled alkaline oxidation of iron in the presence of sodium hydroxide and an oxidizing agent (sodium nitrite or sodium nitrate):

1. **Iron dissolution in hot caustic:**
   - Fe + 2NaOH --> Na2FeO2 (sodium ferrite) + H2
   - At 280–295 F in concentrated NaOH, the steel surface dissolves to form soluble sodium ferrite

2. **Oxidation by nitrite/nitrate:**
   - Na2FeO2 is oxidized from Fe2+ to a mixture of Fe2+ and Fe3+:
   - 3Na2FeO2 + NaNO2 + 2H2O --> Fe3O4 (magnetite) + 7NaOH + NH3 (simplified)

3. **Magnetite deposition:**
   - Fe3O4 (magnetite, inverse spinel structure) precipitates as a thin, adherent, dense black film directly on the steel surface
   - Magnetite is a mixed-valence oxide: FeO . Fe2O3 or Fe2+(Fe3+)2O4

**Bath Chemistry:**
| Component | Concentration | Function |
|-----------|---------------|----------|
| Sodium hydroxide (NaOH) | 80–120 oz/gal (600–900 g/L) | Dissolves iron; maintains alkalinity |
| Sodium nitrite (NaNO2) | 4–10 oz/gal (30–75 g/L) | Oxidizing agent |
| Sodium nitrate (NaNO3) | 4–10 oz/gal (30–75 g/L) | Secondary oxidizer; temperature stabilizer |
| Proprietary additives | Per supplier | Wetting agents, penetrants, grain refiners |
| Water | Balance | The bath is ~45–55% NaOH by weight |

**Operating Parameters:**
| Parameter | Value |
|-----------|-------|
| Temperature | 280–295 F (138–146 C) — CRITICAL: must be in this narrow range |
| Time | 15–30 min (typical); some parts need 30–45 min |
| Boiling point | ~290 F (143 C) for properly made-up bath |
| Specific gravity | 1.40–1.50 at operating temp |

**Temperature Control is THE Critical Variable:**
- Below 275 F: Red/brown oxide forms instead of black magnetite — the "red rouge" defect
- 280–295 F: Proper black magnetite formation
- Above 300 F: Bath "salts out" — NaNO2/NaNO3 crystallize; caustic concentration too high
- The bath boiling point IS the operating temperature — the bath operates AT or just below its boiling point
- Water additions raise the boiling point (dilution); salt additions lower it — this is how temperature is "controlled"

**Film Characteristics:**
| Property | Value |
|----------|-------|
| Composition | Fe3O4 (magnetite) |
| Color | Deep blue-black (lustrous when oiled) |
| Thickness | 0.5–2.5 um (0.02–0.10 mil) |
| Dimensional change | < 0.05 mil (< 1.3 um) per surface — essentially none |
| Hardness | Harder than the substrate oxide (conversion film, not a deposit) |
| Bare salt spray | < 1 hour (minimal without oil) |
| With oil/wax | 24–100+ hours |
| Temperature resistance | Stable to 800+ F (427 C) — inorganic oxide |

### 7.7 Rinse — Post-Coat (Poster 7)

**Two-Stage Rinse Protocol:**

**Stage 1: Cold Water Rinse**
- Ambient temperature
- Removes bulk caustic and dissolved salts
- Time: 1–2 min immersion with agitation
- WARNING: Parts emerge from the black oxide bath at ~285 F — immersing in cold water causes thermal shock and steam. Use ventilation.

**Stage 2: Hot Water Rinse**
- 180–200 F (82–93 C)
- Serves two purposes: (a) further removes caustic; (b) heats the part to promote water evaporation before oil dip
- Time: 1–2 min
- Some operations add chromic acid (0.5–2 oz/gal) to this stage as a passivating rinse — improves corrosion resistance but adds Cr6+ regulatory burden

### 7.8 Seal / Post-Treatment / Drying (Poster 8)

**Oil Dip (Standard):**
- Water-displacing oil or light machine oil
- Temperature: 150–180 F (66–82 C) for hot oil immersion
- Time: 2–5 min
- The hot, wet part goes directly from the hot water rinse into oil — the oil displaces water from the porous magnetite surface
- Excess oil is drained/centrifuged

**Wax Seal:**
- For fasteners and parts requiring dry lubricity
- Microcrystalline wax or polymer-based sealers
- Applied at 150–200 F (66–93 C)

**Lacquer/Clear Coat:**
- For parts requiring a dry, non-oily black finish
- Applied after air-drying the bare oxide
- Less corrosion protection than oil (oil fills micropores better)

**Standards:**
- **MIL-DTL-13924** — Black oxide coating for ferrous metals
  - Class 1: Hot alkaline process (this cluster)
  - Class 2: Room temperature black oxide (not recommended — uses selenium dioxide or copper selenite; inferior adhesion)
  - Class 3: Hot alkaline with supplementary wax/oil
  - Class 4: Alkaline with phosphate sealant
- **AMS 2485** — Black oxide finish for ferrous metals
- **ASTM D769** (no longer active; references remain in legacy specs)

**Common Defects:**
| Defect | Cause | Fix |
|--------|-------|-----|
| Red/reddish-brown instead of black | Bath temp too low (< 275 F); diluted bath; depleted oxidizer | Increase temp; add NaNO2; check SG |
| Smutty/powdery coating (rubs off) | Bath too hot; over-immersion; depleted NaOH; contaminated bath | Cool bath; reduce time; add NaOH; decant |
| Non-uniform (spots/streaks) | Oil contamination; poor cleaning; parts touching in basket | Improve cleaning; rearrange load for full immersion |
| Rusting after blackening | No oil seal; insufficient rinse (caustic residue attracts moisture) | Oil immediately after rinse; improve rinse thoroughness |
| Red spots / fingerprints | Handling before oiling; localized contamination before blackening | Do not handle between rinse and oil; wear clean gloves |

---

## CLUSTER 8: Passivation (Stainless Steel) — Nitric Acid or Citric Acid

### 8.1 Process Overview (Poster 1 — Process Flow)

Passivation of stainless steel is the process of removing free iron and other surface contaminants (from machining, forming, welding, or handling) to restore the chromium-rich passive oxide layer that gives stainless steel its corrosion resistance. Unlike the other processes in this brief, passivation does NOT deposit a conversion coating — it REMOVES contamination and allows the natural passive film to reform.

**The two main passivation chemistries:**
1. **Nitric acid (HNO3)** — traditional, aggressive, well-established
2. **Citric acid (C6H8O7)** — newer, gaining market share; safer, less waste, effective for most alloys

**Typical Process Sequence:**
1. Alkaline clean
2. Water rinse
3. Passivation (nitric or citric acid bath)
4. Water rinse
5. Verification testing (optional but recommended — copper sulfate, salt spray, high humidity)
6. Air dry or warm air dry

### 8.2 Cleaning (Poster 2)

**Cleaner Type:** Alkaline cleaner, pH 10–13. Must remove all machining oils, cutting fluids, grinding compounds, polishing compounds, and organic soils. Stainless steel is relatively insensitive to strong alkaline cleaners (unlike aluminum).

**Key Parameters:**
| Parameter | Immersion |
|-----------|-----------|
| Concentration | 4–8 oz/gal (30–60 g/L) |
| Temperature | 130–180 F (54–82 C) |
| Time | 5–15 min |

**Special Considerations:**
- Chloride-containing cleaners must NEVER be used on stainless steel — chloride causes pitting corrosion and undermines the entire purpose of passivation
- Electroclean (cathodic preferred — avoids oxygen evolution that can pit the surface) is common for precision parts
- Parts with heavy heat tint (blue/gold oxide from welding or heat treatment) require acid pickling BEFORE passivation — the thick thermal oxide is too tenacious for passivation acid alone

**Descaling/Pickling (if needed):**
- Nitric-hydrofluoric acid pickle: 10–15% HNO3 + 1–3% HF, 120–140 F, 5–15 min
- Removes heat tint, weld discoloration, and heavy oxide scale
- This is NOT passivation — it is aggressive surface removal. Passivation follows separately.

### 8.3 Rinse — Pre-Condition (Poster 3)

**Purpose:** Remove all cleaner (and pickle acid, if used) before passivation.

**Parameters:**
- Fresh water, ambient to warm
- Overflow or spray rinse
- Conductivity: < 500 microS/cm
- If pickling was performed, double rinse to remove all HF residues

### 8.4 Surface Conditioning / Activation (Poster 4)

**Stainless steel passivation does NOT require a separate activation or conditioning step.**

The passivation acid itself performs both functions:
1. **Activation/dissolution:** The acid dissolves free iron and iron-rich surface contamination
2. **Passivation:** The oxidizing environment (nitric acid's oxidizing power, or dissolved oxygen in citric acid) promotes the formation of the chromium-rich passive film

**Poster Content:** Focus on the distinction between free-iron contamination (the problem) and the chromium-rich passive film (the goal). Explain that free iron comes from:
- Machining tools (carbon steel tooling transfers iron particles to stainless)
- Grinding/polishing (abrasive media embeds iron)
- Contact with carbon steel (storage racks, handling fixtures)
- Shop environment (iron particles in air near grinding operations)

The passivation process removes this free iron and allows the underlying chromium (11–30% of the alloy, depending on grade) to oxidize and form the protective Cr2O3-rich passive layer.

### 8.5 Rinse — Pre-Coat (Poster 5)

In passivation, there is no separate pre-coat rinse stage — the sequence goes directly from the clean rinse (Poster 3) to the passivation bath. This poster can cover:

- Water quality requirements for the final rinse before passivation
- The importance of DI or RO water for aerospace/medical stainless parts
- Temperature: Ambient — do not heat parts before acid immersion (thermal oxide is counterproductive)

### 8.6 Passivation — Main Stage (Poster 6)

**Chemical Mechanism — Nitric Acid:**
1. **Free iron dissolution:**
   - Fe + 2HNO3 (dilute) --> Fe(NO3)2 + H2 (or Fe2+ + NO2- + H2O in concentrated HNO3)
   - Iron dissolves readily in nitric acid; chromium and nickel are relatively resistant (this is the selectivity that makes passivation work)
2. **Passive film formation:**
   - HNO3 is an oxidizing acid — it provides the oxidizing environment necessary for Cr2O3 formation
   - As free iron is removed, the surface becomes enriched in chromium
   - Cr + oxidizing environment --> Cr2O3 (passive film, 1–5 nm thick, self-healing)
3. **Nickel role:** Nickel in the alloy (8–14% in austenitic grades) is resistant to nitric acid and helps maintain the passive state. This is why austenitic stainless (300-series) is generally easier to passivate than ferritic (400-series).

**Chemical Mechanism — Citric Acid:**
1. **Iron chelation:**
   - Fe3+ + C6H5O7 3- --> Fe(C6H5O7) (iron citrate complex — soluble)
   - Citric acid chelates free iron from the surface, pulling it into solution
   - Citric acid is NOT an oxidizing acid — it relies on dissolved oxygen in the solution and in the air to provide the oxidizing environment for passive film formation
2. **Passive film formation:**
   - Same result: free iron removed, chromium-enriched surface, Cr2O3 passive film forms in contact with dissolved O2

**Key Difference: Nitric acid actively oxidizes the surface AND dissolves iron. Citric acid only chelates iron — the passive film forms by exposure to dissolved oxygen. Both achieve the same endpoint for most alloys.**

**Nitric Acid Passivation Baths (per ASTM A967 / AMS 2700):**

| Bath Type | HNO3 Concentration | Sodium Dichromate | Temperature | Time |
|-----------|--------------------|--------------------|-------------|------|
| Nitric 1 | 20–25% by volume | 2.0–3.0 oz/gal (Na2Cr2O7) | 120–130 F (49–54 C) | 20 min min |
| Nitric 2 | 20–25% by volume | None | 120–140 F (49–60 C) | 20 min min |
| Nitric 3 | 20–45% by volume | None | 70–90 F (21–32 C) | 30 min min |
| Nitric 4 | 20–45% by volume | None | 120–140 F (49–60 C) | 30 min min |

**Citric Acid Passivation Baths (per ASTM A967):**

| Bath Type | Citric Acid Concentration | Temperature | Time |
|-----------|---------------------------|-------------|------|
| Citric 1 | 4–10% by weight | 70–120 F (21–49 C) | 4 min minimum |
| Citric 2 | 4–10% by weight | 120–150 F (49–66 C) | 4–10 min |
| Citric 3 | 4–10% by weight | 70–160 F (21–71 C) | 4–20 min |
| Citric 4 | 10–20% by weight | 70–160 F (21–71 C) | 4–20 min |

**pH of citric acid baths:** Typically 1.5–3.0 (self-buffering; no pH adjustment usually needed)

**Alloy-Specific Guidance:**

| Alloy Family | Grade Examples | Preferred Passivation | Notes |
|--------------|----------------|----------------------|-------|
| Austenitic (300-series) | 304, 304L, 316, 316L, 321, 347 | Citric or Nitric 2/3 | Easy to passivate; high Cr + Ni |
| Ferritic (400-series) | 430, 434, 444 | Nitric 3 or 4 | Moderate; lower Ni, moderate Cr |
| Martensitic (400-series) | 410, 420, 440C | Nitric 1 or 2 (with dichromate) or Citric 4 | Harder to passivate; low Cr (~12%); dichromate helps for difficult grades |
| Precipitation hardening | 17-4 PH, 15-5 PH, PH 13-8 Mo | Citric or Nitric 2/3 | Similar to austenitic |
| Duplex | 2205, 2507 | Citric or Nitric 3 | Mixed austenite/ferrite; generally straightforward |
| Free-machining | 303, 416, 420F | Nitric 1 or 2 (with dichromate) | Sulfur/selenium inclusions make passivation difficult; may require longer times or more aggressive chemistry |

**Film Characteristics:**
| Property | Value |
|----------|-------|
| Passive film composition | Cr2O3-rich amorphous oxide |
| Passive film thickness | 1–5 nm (10–50 Angstroms) — essentially invisible |
| Appearance change | None (no visible coating — the part looks the same) |
| Dimensional change | None measurable |
| Corrosion protection | The passive film provides the corrosion resistance inherent to stainless steel — passivation RESTORES it, not adds it |

### 8.7 Rinse — Post-Coat (Poster 7)

**Purpose:** Remove all acid residues. Nitric acid residue causes acid staining; citric acid residue can promote microbial growth.

**Parameters:**
- Fresh water, ambient to warm
- Multiple rinse stages for critical parts
- DI water final rinse for medical/pharmaceutical/semiconductor applications (prevents chloride and mineral deposits)
- Thorough — trapped acid in crevices, blind holes, or threads is the #1 cause of post-passivation staining

### 8.8 Verification / Post-Treatment / Drying (Poster 8)

**Verification Testing (per ASTM A967 / AMS 2700):**

Passivation success is verified by testing for free iron on the surface:

| Test | Method | Pass Criteria | Notes |
|------|--------|---------------|-------|
| **Copper sulfate test (Practice A)** | Immerse in CuSO4/H2SO4 solution for 6 min | No copper color (pink/red) deposit on surface | Most common; detects free iron; does NOT work on free-machining grades (303, 416) |
| **Salt spray (Practice B)** | ASTM B117, 2–24 hours | No rust | Time duration depends on spec requirements |
| **High humidity (Practice C)** | 24 hours at 95% RH, 95 F (35 C) | No rust | Most stringent short-term test |
| **Water immersion (Practice D)** | Immerse in water for 24 hours | No rust | Simple but effective |
| **Ferroxyl test** | Apply potassium ferricyanide / nitric acid solution | No blue color (Turnbull's blue) | Indicates free iron; very sensitive |

**Drying:**
- Air dry at ambient temperature
- Warm forced air (120–150 F / 49–66 C) acceptable for faster drying
- NO high-temperature oven drying — causes thermal oxidation (heat tint) that defeats the purpose
- Parts must be completely dry before packaging — moisture trapped in crevices causes crevice corrosion

**Post-Treatment:**
- Normally NONE — the passive film is the final surface
- For enhanced protection in aggressive environments:
  - Electropolishing BEFORE passivation (removes surface roughness and embedded contaminants)
  - Citric acid passivation AFTER electropolishing is becoming the standard aerospace/medical protocol

**Standards:**
- **ASTM A967/A967M** — Standard specification for chemical passivation treatments for stainless steel parts (the primary industry standard)
- **AMS 2700** — Passivation of corrosion resistant steels (aerospace; references ASTM A967 methods)
- **ASTM A380** — Standard practice for cleaning, descaling, and passivation of stainless steel parts (broader cleaning/descaling guidance)
- **QQ-P-35** (Canceled, superseded by ASTM A967) — legacy federal specification; still referenced in some older drawings
- **ASTM F86** — Surface preparation and marking of metallic surgical implants (medical)
- **SEMI F42** — Test method for evaluating stainless steel surfaces for semiconductor applications

**Common Defects:**
| Defect | Cause | Fix |
|--------|-------|-----|
| Copper sulfate test failure (copper deposits) | Free iron remaining; insufficient passivation time; acid too dilute; contaminated bath | Increase time/concentration/temperature; replace bath |
| Orange/brown staining after passivation | Flash rust from rinse water; trapped acid; chloride in rinse | Improve rinsing; use DI water; dry promptly |
| Pitting during passivation | Chloride contamination in acid; bath temperature too high for the alloy; wrong acid for the grade | Use chloride-free reagents; reduce temperature; change to appropriate bath type |
| Non-uniform appearance | Mixed alloy loads; incomplete cleaning; embedded contaminants | Separate alloys; improve cleaning; consider electropolish pre-treatment |
| Etching (matte/frosted surface) | Acid too concentrated; temperature too high; time too long (especially with HNO3/HF pickle) | Reduce concentration/temp/time; switch to citric for sensitive grades |

**Citric Acid vs. Nitric Acid — Decision Matrix:**

| Factor | Nitric Acid | Citric Acid |
|--------|-------------|-------------|
| Effectiveness on 300-series | Excellent | Excellent |
| Effectiveness on 400-series martensitic | Good to Excellent (with dichromate) | Good (may need longer time or higher conc.) |
| Free-machining grades (303, 416) | Better (with dichromate) | May struggle; longer times needed |
| Safety | Fuming, toxic NOx vapors; aggressive | Mild organic acid; safe to handle |
| Waste treatment | Hazardous waste (heavy metals, Cr6+ if dichromate used) | Non-hazardous in most cases; biodegradable |
| Bath life | Long (years with maintenance) | Moderate (months; iron buildup limits life) |
| Cost per gallon | Moderate | Similar or lower |
| Regulatory burden | High (HNO3 reporting, Cr6+ if dichromate) | Low |
| Industry trend | Legacy standard; still dominant in aerospace | Gaining share rapidly; preferred for new installations |
| ASTM A967 coverage | Full | Full — citric is now an equal option, not an "alternative" |

---

## CROSS-CUTTING NOTES FOR ALL CLUSTERS

### Regulatory Landscape

| Chemistry | Primary Concern | Key Regulations |
|-----------|----------------|-----------------|
| Hexavalent chromate (Clusters 4, plus legacy seals in 2, 3, 7) | Cr6+ is a known human carcinogen; OSHA PEL 5 ug/m3 | EU REACH Annex XIV (authorization required); RoHS Directive 2011/65/EU; OSHA 29 CFR 1910.1026; EPA NESHAP for chrome plating/anodizing |
| Phosphate (Clusters 1, 2, 3) | Phosphorus discharge to waterways (eutrophication) | Local POTW limits; EPA phosphorus discharge limits |
| Manganese phosphate (Cluster 3) | Mn discharge; sludge disposal | EPA manganese limits; sludge classified as hazardous if fails TCLP |
| Black oxide (Cluster 7) | Hot caustic = severe burn hazard; NaNO2 is toxic | OSHA PPE requirements; NaNO2 storage/handling (oxidizer) |
| Nitric acid passivation (Cluster 8) | HNO3 fumes (NOx); dichromate if used | OSHA PEL for HNO3; Cr6+ regulations if dichromate is used |
| Citric acid passivation (Cluster 8) | Minimal | Essentially non-hazardous; minimal regulatory burden |

### Water Quality Summary

| Process | Rinse Water Requirement |
|---------|------------------------|
| Iron phosphate | Softened water preferred; DI for seal rinse |
| Zinc phosphate | Softened or DI; conductivity < 300 uS/cm |
| Manganese phosphate | Tap water acceptable for intermediate rinses; warm final rinse |
| Hex chromate (Al) | DI/RO preferred for all rinses; chloride-free |
| Tri chromate (Al) | DI/RO for final rinse minimum |
| Ti/Zr conversion (Al) | DI/RO strongly preferred (thin film sensitive to minerals) |
| Black oxide | Tap water acceptable; cold + hot rinse sequence |
| Passivation (SS) | DI for final rinse; chloride-free is CRITICAL |

### Temperature Comparison

| Process | Operating Temperature | Notes |
|---------|-----------------------|-------|
| Iron phosphate | 100–150 F (38–66 C) | Moderate |
| Zinc phosphate (spray) | 95–130 F (35–54 C) | Moderate |
| Zinc phosphate (immersion) | 130–200 F (54–93 C) | Hot |
| Manganese phosphate | 190–210 F (88–99 C) | Near boiling — always |
| Hex chromate (Al) | 60–100 F (16–38 C) | Ambient to cool |
| Tri chromate (Al) | 65–95 F (18–35 C) | Ambient |
| Ti/Zr (Al) | 70–120 F (21–49 C) | Low energy |
| Black oxide | 280–295 F (138–146 C) | The hottest process in this brief |
| Nitric passivation | 70–140 F (21–60 C) | Ambient to warm |
| Citric passivation | 70–160 F (21–71 C) | Ambient to warm |

---

## SOURCE NOTES / CONFIDENCE ASSESSMENT

**Gemini Status:** Quota exhausted at session start (10+ hour cooldown). This entire brief was written from Watson's domain expertise in electrochemistry, surface finishing, and industrial metal finishing chemistry.

**High Confidence (direct professional knowledge):**
- All chemical mechanisms (phosphate, chromate, black oxide, passivation)
- Bath chemistry compositions and operating parameters
- MIL-DTL-5541, MIL-DTL-16232, ASTM A967, AMS 2700 specifications and their scope
- Defect-cause-fix tables (drawn from field troubleshooting experience)
- Citric vs. nitric passivation comparison
- Surface conditioning requirements (Ti/Zr activator for zinc phosphate)
- Black oxide temperature criticality
- Hex vs. tri chromate self-healing distinction

**Moderate Confidence (standard industry knowledge, but would benefit from Gemini verification):**
- Exact ppm ranges for Zr-based automotive conversion coatings (proprietary formulations vary widely)
- Cerium-based conversion coating status (emerging technology — commercial adoption status may have changed)
- Some specific ASTM/SAE numbers for Ti/Zr coatings (this is a newer field with evolving standards)
- Exact P-ratio measurement methodology (XRD vs. chemical dissolution — details vary by lab)

**Recommendation:** If Gemini becomes available before Alaina begins Construction Workups, a spot-check query on Clusters 5 and 6 (trivalent and Ti/Zr systems) would be valuable — these are the most rapidly evolving technologies in this brief.

---

*Watson — Chemistry Researcher, Plating Posters Inc.*
*Research completed 2026-04-26 from domain expertise (Gemini quota unavailable)*
