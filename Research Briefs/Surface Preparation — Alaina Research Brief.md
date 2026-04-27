---
created: 2026-04-03T00:00:00
version: v2
poster: "#1 — Surface Preparation: The Foundation of Every Flawless Finish"
tags:
  - SurfacePreparation
  - PosterResearch
  - ResearchBrief
---

# Surface Preparation — Alaina Research Brief

**Poster**: #1 — Surface Preparation: The Foundation of Every Flawless Finish
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-03 (v1); 2026-04-04 (v2)
**Version**: v2 — expanded chemistry, ASTM B322 soil classification, cleaning mechanism detail, additional visual concepts
**Source documents**: Products Finishing (*Preparation for Electroplating*; *Better Electrocleaning*; *Electrolytic Cleaning*; *Reverse Current Cleaning*); NMFRC (*Surface Preparation of Metals Prior to Plating*); PAVCO (*Electrolytic Cleaning*; *How to Integrate Electrolytic Cleaning*); ASTM B322-99(2020)e1 (*Standard Guide for Cleaning Metals Prior to Electroplating*); ASTM B571; ASTM B850; AMS 2759/9; 1993 Metal Finishing Guidebook; Drew's Quick Reference Metal Finishing Notes (vault); domain expertise

> [!NOTE]
> v2 upgrades: Added ASTM B322 soil classification system, expanded saponification/emulsification chemistry, refined electrocleaning gas-volume mechanism, added rinse ratio science, added 2 new visual concepts (#11, #12). All v1 content retained and refined. This is the shop-floor-ready edition.

---

## Why This Poster Matters

Surface preparation is the single highest-impact variable in plating quality. An estimated **80% or more of all plating defects** (blistering, peeling, skip plating, pitting) trace back to inadequate cleaning or activation — not to the plating bath itself. Every plating process, every substrate, every shop shares this reality.

This poster has the broadest possible audience: every plater, every line, every metal. It is the one poster that applies universally.

---

## What You Are Cleaning Off — The ASTM B322 Soil Classification

ASTM B322-99(2020)e1, *Standard Guide for Cleaning Metals Prior to Electroplating*, classifies surface contaminants ("soils") into categories that determine which cleaning method is required. Understanding what you are removing is just as important as understanding the cleaning process itself.

### Soil Types

| Soil Category | Examples | Removal Method |
|---|---|---|
| **Organic — Saponifiable** | Animal fats, vegetable oils, fatty acids, tallow-based drawing compounds | Alkaline cleaning (saponification converts these to water-soluble soaps) |
| **Organic — Non-saponifiable (mineral)** | Petroleum oils, mineral greases, cutting fluids, waxes, silicone lubricants | Surfactant emulsification; solvent precleaning if heavy |
| **Organic — Solid films** | Buffing and polishing compounds, carbonized oil, lacquer, paint, adhesive residues | Aggressive soak cleaning; may require solvent precleaning or abrasive blasting |
| **Inorganic — Oxides and scale** | Rust (Fe2O3/FeOOH), mill scale, heat treat oxide, aluminum oxide (Al2O3) | Acid pickling or alkaline etching (aluminum) |
| **Inorganic — Metallic smuts** | Copper smut on aluminum after etching; metallic deposits from cathodic cleaning in dirty solution | Desmut (acid dip — often HNO3 or HNO3/HF); anodic electrocleaning |
| **Inorganic — Salts and fingerprints** | Chloride and sulfate residues; skin oils containing NaCl | Alkaline cleaning followed by adequate rinsing |

### The Two Cleaning Mechanisms — Saponification vs. Emulsification

**Saponification** is a chemical reaction: alkaline builders (NaOH, KOH) react with animal/vegetable fats (triglycerides) to form water-soluble soap (sodium salts of fatty acids) and glycerol. The contaminant is chemically converted into a soluble product and rinsed away.

```
Triglyceride (fat) + 3 NaOH -> Glycerol + 3 Sodium fatty acid salts (soap)
```

**Emulsification** is a physical process: surfactants in the cleaner orient themselves at the oil-water interface — their hydrophobic tails penetrate the oil, and their hydrophilic heads face the water. This breaks the oil into microscopic droplets suspended in water (an emulsion) that can be rinsed away. Mineral oils and petroleum-based lubricants cannot be saponified and must be removed by emulsification.

**For the poster:** This saponification vs. emulsification distinction is a powerful teaching concept. Most operators know that cleaners "remove oil" but do not understand that two fundamentally different mechanisms are at work — one chemical, one physical — and that both are required because real-world soils are mixtures.

---

## The Universal Pre-Treatment Sequence

The standard pre-plating sequence used in the vast majority of rack and barrel plating lines:

```
SOAK CLEAN → Rinse → ELECTROLYTIC CLEAN → Rinse → ACID ACTIVATE → Rinse → PLATE
```

**Extended sequence** (for heavily soiled or hard-to-clean substrates, or multi-layer plating):

```
SOAK CLEAN → Rinse → ELECTRO CLEAN → Rinse → ACID DIP → Rinse → 2nd ELECTRO CLEAN → Rinse → 2nd ACID DIP → Rinse → STRIKE → Rinse → PLATE
```

**Aluminum-specific sequence** (alkaline etch line):

```
SOAK CLEAN → Rinse → CAUSTIC ETCH → Rinse → DESMUT → Rinse → PLATE or ANODIZE
```

### Step-by-Step Breakdown

#### Step 1: Soak Clean (Alkaline Immersion Clean)

**What it does**: Removes the bulk of organic soils — oils, greases, cutting fluids, drawing compounds, shop dirt, and fingerprints — by chemical action alone (no electricity).

**How it works**: Alkaline cleaners contain a combination of:
- **Builders** (NaOH or KOH, 2–6 oz/gal) — saponify animal and vegetable fats, provide alkalinity
- **Surfactants** (wetting agents) — lower surface tension, emulsify mineral oils that alkalinity alone cannot saponify
- **Chelating agents** (EDTA, gluconate, MGDA, citrate) — sequester hard-water minerals (Ca²⁺, Mg²⁺) that would otherwise deposit on the part and interfere with subsequent steps
- **Silicates** (sodium metasilicate) — provide detergency, inhibit etching of aluminum and zinc substrates

**Typical operating parameters**:

| Parameter | Range |
|---|---|
| Concentration | 4–8 oz/gal (30–60 g/L) |
| Temperature | 140–180 deg F (60–82 deg C) |
| Immersion time | 3–10 minutes |
| pH | 10–13 |
| Agitation | Air or mechanical preferred |

**Key point for poster**: Soak cleaning does the heavy lifting. If the soak cleaner fails to remove the bulk of the soil, every subsequent step is compromised. "You cannot electroclean off what the soak cleaner left behind."

---

#### Step 2: Rinse (after Soak Clean)

**What it does**: Removes alkaline cleaner residue from the part surface before the next step.

**Why it matters**: Alkaline drag-out into the electrocleaner is acceptable (both are alkaline). Alkaline drag-out into an acid tank causes neutralization, contamination, and wasted chemistry. Every rinse in the sequence prevents cross-contamination.

**Best practice**: Counterflow (cascade) rinsing; minimum two rinse tanks after the soak cleaner; water temperature 70–120 deg F.

---

#### Step 3: Electrolytic Clean (Electrocleaning)

**What it does**: Removes the final traces of soil by combining alkaline chemistry with vigorous gas evolution at the part surface. The gas bubbles provide a mechanical "scrubbing" action that soak cleaning alone cannot match.

**How it works**: The part is immersed in an alkaline electrolyte and connected to a DC power supply. Gas evolution at the part surface physically lifts residual contaminants off the metal.

**Two modes — and the order matters**:

| Mode | Part is the... | Gas evolved at part | Primary benefit | Primary risk |
|---|---|---|---|---|
| **Cathodic** (Direct) | Cathode (negative) | Hydrogen (H₂) | 2x the gas volume of anodic; more aggressive scrubbing | Hydrogen embrittlement on high-strength steels; can deposit metallic smuts from contaminated solution |
| **Anodic** (Reverse) | Anode (positive) | Oxygen (O₂) | Dissolves a microscopic layer of base metal — removes metallic smuts and activates the surface; no H₂ embrittlement risk | Less gas volume; slight metal dissolution (usually beneficial) |

**Why cathodic produces 2x the gas — the stoichiometry:**

Water electrolysis produces hydrogen at the cathode and oxygen at the anode:

```
Cathode: 2 H₂O + 2e- -> H₂ + 2 OH-
Anode:   2 H₂O -> O₂ + 4 H⁺ + 4e-
```

For every mole of O₂ produced at the anode, two moles of H₂ are produced at the cathode. Since the gas bubbles are the primary mechanical scrubbing agent, cathodic cleaning generates twice the scrubbing intensity per amp applied. This is a direct consequence of water's 2:1 hydrogen-to-oxygen molecular composition.

**However**, cathodic cleaning carries two risks that anodic does not:
1. **Hydrogen embrittlement** — atomic hydrogen absorbs into the steel lattice, causing delayed brittle fracture in high-strength steels
2. **Metallic smut deposition** — dissolved metal ions (Cu, Zn, Fe) in a dirty electrocleaner will plate out cathodically onto the part surface, creating an adherent metallic smut that interferes with plating adhesion

**Industry standard practice**: **Anodic (reverse) cleaning as the final electrocleaning step** before plating. This ensures a smut-free, activated surface with no hydrogen embrittlement risk. Many lines run cathodic first (for maximum soil removal) then switch to anodic (for final activation). The sequence is sometimes abbreviated as "C-A" (cathodic then anodic).

**Typical operating parameters**:

| Parameter | Range |
|---|---|
| Concentration | 4–8 oz/gal (30–60 g/L) |
| Temperature | 140–180 deg F (60–82 deg C) |
| Current density | 15–50 ASF (1.5–5.0 ASD) |
| Voltage | 4–6 V typical |
| Time | 30–120 seconds (30–45 sec common) |

**Critical detail from Drew's Quick Reference**: Electrocleaning generates oxygen (anodic) or hydrogen (cathodic) at the part surface, promoting a scrubbing action in the pores. Etching can occur when voltage is too high, caustic is too low, chloride contamination is present (>10 g/L is too high), or immersion time is too long. Chloride contamination causes initial corrosion embedded in the substrate prior to plating — when plated over, this causes premature salt spray failure.

---

#### Step 4: Rinse (after Electrocleaner)

Same principle as Step 2. Clean water removes alkaline electrocleaner residue before the acid step. Inadequate rinsing drags alkaline solution into the acid, neutralizing the acid and reducing its effectiveness.

---

#### Step 5: Acid Activation (Acid Dip)

**What it does**: Removes the thin oxide film that forms on metal surfaces even during the brief transfer from the electrocleaner through the rinse. Also neutralizes any residual alkaline film. Leaves the base metal surface chemically "active" — bare, clean metal atoms ready to accept the plating deposit.

**How it works**: A brief immersion in dilute mineral acid dissolves surface oxides through simple acid-base chemistry. The most common acids used:

| Acid | Typical Concentration | Best For |
|---|---|---|
| Hydrochloric acid (HCl, muriatic) | 10–50% v/v | Steel, copper, brass — most universal |
| Sulfuric acid (H₂SO₄) | 5–25% v/v | Steel, zinc die-cast; also used for aluminum desmut |
| Phosphoric acid (H₃PO₄) | 5–10% v/v | Specialty use; less aggressive on zinc substrates |
| Hydrofluoric acid (HF) — blends | 0.5–5% v/v | Stainless steel, titanium, high-alloy steels (activates passive films) |

**Typical operating parameters**:

| Parameter | Range |
|---|---|
| Concentration | 10–50% v/v (process-dependent) |
| Temperature | Room temperature (65–85 deg F / 18–30 deg C) |
| Immersion time | 15–60 seconds (brief!) |
| Agitation | Gentle or none |

**Key point for poster**: The acid dip is a brief, aggressive step. Too long and it etches the substrate; too short and oxide remains. "Seconds count in the acid dip."

---

#### Step 6: Rinse (after Acid Dip) — then PLATE

Final rinse before plating. This rinse must be extremely clean — any acid drag-into the plating bath can alter pH, introduce chlorides (from HCl dips), or contaminate the chemistry. Many shops use a dedicated "drag-in" rinse immediately before the plating tank to minimize contamination.

---

## Substrate-Specific Variations

### Steel and Iron Alloys (Most Common)

Standard sequence: Soak Clean → Rinse → Electro Clean → Rinse → Acid Dip (HCl or H₂SO₄) → Rinse → Plate

Special consideration: **Hydrogen embrittlement** — high-strength steels (>1000 MPa UTS / >39 HRC) are susceptible to hydrogen absorbed during cathodic electrocleaning and acid pickling. Minimize cathodic exposure; use anodic final cleaning; bake within 4 hours of plating per ASTM B850 / AMS 2759/9.

### Aluminum

Standard sequence: Soak Clean → Rinse → **Caustic Etch** (NaOH/KOH, 4–8 oz/gal, 120–160 deg F, 30 sec–5 min) → Rinse → **Desmut** (HNO₃ or HNO₃/HF blend, room temp, 15–60 sec) → Rinse → Plate or Anodize

Special consideration: Aluminum forms an extremely tenacious oxide layer (Al₂O₃) that must be chemically removed by alkaline etching. After etching, alloying elements (copper, silicon, manganese) remain on the surface as a dark "smut" that the desmut step removes.

A Brite products for this sequence: **Brite-Kleen ALE-680** (liquid caustic etch), **Brite-Kleen ALE-650** (solid/flake caustic etch), **Brite-Kleen APT-DEOX NC-620** (desmut).

### Copper and Brass

Standard sequence: Soak Clean → Rinse → Electro Clean → Rinse → Acid Dip (HCl or H₂SO₄ 5–10%) → Rinse → Plate

Special consideration: Copper alloys tarnish rapidly. Minimize transfer time between acid dip and plating. Some shops add a bright dip (dilute HNO₃ + H₂SO₄) for a mirror-bright surface before plating.

### Zinc Die-Cast

Standard sequence: Soak Clean → Rinse → **Anodic** Electro Clean (cathodic can deposit smuts) → Rinse → Acid Dip (H₂SO₄ 0.25–0.50%, room temp, 25–45 sec) → Rinse → Cyanide Copper Strike → Plate

Special consideration: Zinc die-cast is porous and traps buffing compounds and oils in pores. Extended soak cleaning and thorough rinsing are essential. Acid dip must be very mild — zinc dissolves aggressively in strong acid. All traces of acid must be rinsed from porous areas or the parts will blister after plating.

Drew's Quick Reference note: "For die cast parts: flash with acid chloride zinc (1-3 um), re-condition surface in post electro rinse."

### Stainless Steel

Standard sequence: Soak Clean → Rinse → Electro Clean → Rinse → **Wood's Nickel Strike** (NiCl₂, high HCl, <1.0 pH, 50–250 ASF, 30 sec–5 min) → Rinse → Plate

Special consideration: The chromium-rich passive oxide layer on stainless steel resists normal acid activation. A Wood's nickel strike is required — it simultaneously activates the surface and deposits a thin (0.05–0.5 um) adherent nickel layer as a base for subsequent plating.

---

## Common Failure Modes from Poor Surface Preparation

This section gives Alaina the "problems" content for the poster — the visual warning layer.

| Failure Mode | Root Cause | Visible Symptom |
|---|---|---|
| **Blistering / Peeling** | Residual oil, oxide, or smut between substrate and deposit | Bubbles or lifted areas in the plating; often appears after baking or heat cycling |
| **Skip Plating (bare spots)** | Surface not fully activated; passive oxide remains; water break present | Unplated areas, often in recesses or low-current-density zones |
| **Pitting** | Hydrogen gas trapped on surface during plating; caused by residual organic contamination that prevents gas release | Small holes in the deposit surface |
| **Poor Adhesion (general)** | Any contamination layer between base metal and deposit | Deposit flakes or peels under tape test, bend test, or thermal shock |
| **Roughness / Nodules** | Particulate contamination carried from cleaning tanks; metallic smuts from cathodic cleaning in dirty solution | Bumps, grit, or sandpaper texture on the plated surface |
| **Staining / Discoloration** | Inadequate rinsing; alkaline or acid drag-out into subsequent tanks | Streaks, halos, or color variation on the plated or passivated surface |
| **Premature Corrosion Failure** | Chloride contamination from electrocleaner etching embedded in substrate before plating | Salt spray failure at the substrate-deposit interface, not at the surface |

---

## The Water Break Test — The Universal Go/No-Go Check

**What it is**: After the final cleaning step (acid dip), rinse the part and hold it vertically. If water sheets off the surface in a continuous, unbroken film, the surface is clean ("water-break-free"). If water beads up or pulls away from any area, organic contamination remains at that spot.

**Why it matters**: This is the simplest, cheapest, and most universally used quality check in any plating shop. It requires no instruments, no chemicals, and no training beyond "does the water sheet or bead?"

**Poster callout**: "If the water beads, don't plate."

---

## Rinse Water Quality

Rinse water quality directly impacts plating results:

| Parameter | Target |
|---|---|
| Total dissolved solids (TDS) | < 500 ppm for general rinsing; < 50 ppm for final rinse before critical plating |
| Chlorides | < 25 ppm in rinse water before chloride-sensitive baths (chrome, EN) |
| Conductivity | < 50 uS/cm for DI water final rinse |
| pH | 5.0–8.0 (neutral range) |

### The Rinse Ratio Concept

The **dilution ratio** of a rinse is defined as:

```
Dilution Ratio = Volume of clean water flowing through rinse / Volume of dragout carried in by parts
```

A single rinse tank typically achieves a dilution ratio of 500:1 to 1000:1. A counterflow (cascade) system of two tanks in series achieves the *square* of the single-tank ratio — so two 500:1 tanks in series produce an effective 250,000:1 dilution. This is why counterflow rinsing is dramatically more effective than single-tank rinsing and uses far less water.

**Rule of thumb:** Two counterflow rinses after each process tank is the minimum standard. Three may be required before chromium, EN, or other contamination-sensitive baths.

---

## Visual / Diagram Opportunities for Poster Design

### 1. The Process Flow Diagram (HERO visual)

A horizontal left-to-right flow showing each tank in sequence: Soak Clean → Rinse → Electro Clean → Rinse → Acid Dip → Rinse → Plate. Each tank drawn as a simple rectangle or vessel with its contents labeled and color-coded. Arrows connect the tanks. This is the central visual element — the poster's backbone.

**Color coding suggestion** (using locked palette):
- Alkaline steps (soak clean, electrocleaner): Teal `#2EC4B6`
- Rinse steps: light/neutral tone
- Acid steps (acid dip): Amber `#E8A020`
- Plating tank: Emerald `#27AE60`

### 2. The Water Break Test Close-Up

A split illustration or two-panel visual:
- Left panel: "CLEAN" — water sheeting uniformly off a vertical part (Emerald accent)
- Right panel: "CONTAMINATED" — water beading/breaking on the surface (Coral accent)
- Caption: "If the water beads, don't plate."

### 3. The Failure Mode Gallery

A 2x3 or 3x3 grid of small icons or illustrations showing common defects caused by poor prep: blistering, peeling, skip plating, pitting, roughness, staining. Each with a 2–3 word label and a one-line root cause. Use Coral `#E05C5C` as the accent for this section.

### 4. Anodic vs. Cathodic Electrocleaning Diagram

Two simple circuit diagrams side by side:
- Left: Part connected to positive terminal (anodic) — O₂ bubbles shown — "Activates surface"
- Right: Part connected to negative terminal (cathodic) — H₂ bubbles shown (2x volume) — "Maximum scrubbing"
- Callout: "Always finish anodic."

### 5. Substrate Decision Tree

A simple branching diagram:
- Steel/Iron → Standard sequence
- Aluminum → Caustic Etch + Desmut
- Zinc Die-Cast → Mild acid + Copper Strike
- Stainless Steel → Wood's Nickel Strike
- Copper/Brass → Standard sequence + Bright Dip (optional)

### 6. The Contamination Barrier Concept

A cross-section showing three layers:
- Bottom: Base metal (substrate)
- Middle: Thin contamination layer (oil film, oxide, smut) — shown in Coral
- Top: Plating deposit
- Arrow pointing to the contamination layer: "This is where adhesion fails."
- A second version with no contamination layer and a clean bond line shown in Emerald.

### 7. Time-Temperature-Concentration Callout Box

A small data panel for each step showing the three critical variables:
- Soak Clean: 140–180 deg F / 4–8 oz/gal / 3–10 min
- Electro Clean: 140–180 deg F / 4–8 oz/gal / 30–120 sec / 15–50 ASF
- Acid Dip: Room temp / 10–50% v/v / 15–60 sec

### 8. The 80% Rule Callout

A bold, prominent callout number:
- "80% of plating defects trace back to surface preparation."
- This is the poster's thesis statement — it should be impossible to miss.

### 9. The Rinse Cascade Diagram

A simple illustration showing counterflow rinsing — water flows from the cleanest rinse to the dirtiest, with the part moving in the opposite direction. This is a simple but powerful concept that many operators don't understand.

### 10. The "Enemies of Adhesion" Icon Row

A row of simple icons representing the contaminants that cause adhesion failure:
- Oil droplet (cutting fluid, fingerprints)
- Rust/oxide crystal
- Smut particles
- Buffing compound residue
- Hard water scale
Each with a one-word label beneath.

### 11. Saponification vs. Emulsification Split Panel

Two-panel illustration showing the two cleaning mechanisms side by side:
- Left: **Saponification** — NaOH molecule reacting with a fat molecule, converting it into soluble soap + glycerol. Chemical arrows. Label: "Animal/vegetable fats — chemically converted."
- Right: **Emulsification** — surfactant molecules surrounding a mineral oil droplet, hydrophobic tails in oil, hydrophilic heads in water. Label: "Mineral oils — physically suspended."
- Footer: "Real-world soils are mixtures. Both mechanisms are required."

### 12. Soil Classification Quick Reference Strip

A horizontal bar divided into colored segments matching the ASTM B322 soil categories:
- Organic saponifiable (e.g., tallow) -> Alkaline clean
- Organic non-saponifiable (e.g., cutting fluid) -> Surfactant + emulsification
- Organic solid (e.g., buffing compound) -> Solvent preclean + aggressive soak
- Inorganic oxide (e.g., rust, scale) -> Acid pickle
- Inorganic smut (e.g., copper on aluminum) -> Desmut acid
- Inorganic salt (e.g., fingerprints) -> Alkaline clean + rinse
This gives operators a quick-reference "what am I dealing with and how do I clean it" strip.

---

## Key Data Points for Callouts

These are the numbers and facts Alaina should feature prominently on the poster:

**The thesis**:
- `80%+` of plating defects originate in surface preparation

**Soak clean parameters**:
- Temperature: `140–180 deg F`
- Concentration: `4–8 oz/gal`
- Time: `3–10 minutes`

**Electrocleaner parameters**:
- Current density: `15–50 ASF`
- Time: `30–120 seconds`
- Cathodic produces `2x the gas volume` of anodic

**Acid dip parameters**:
- Time: `15–60 seconds`
- Temperature: `Room temperature`

**Water break test**:
- "If the water beads, don't plate."

**Chloride contamination threshold**:
- `> 10 g/L chlorides` in electrocleaner causes embedded substrate corrosion

**Hydrogen embrittlement threshold**:
- Steels above `39 HRC / 1000 MPa` — minimize cathodic exposure; bake within 4 hours

**Rinse efficiency**:
- Single rinse dilution ratio: `500:1 to 1000:1`
- Two-stage counterflow: `250,000:1` effective dilution
- Minimum: `2 counterflow rinses` after each process tank

**Gas stoichiometry**:
- Cathodic cleaning produces `2x the gas volume` of anodic (H₂ vs. O₂, stoichiometric 2:1 ratio)

**Governing standards**:
- `ASTM B322` — Standard Guide for Cleaning Metals Prior to Electroplating
- `ASTM B850` — Post-coating hydrogen embrittlement relief
- `AMS 2759/9` — Hydrogen embrittlement relief for steel parts

---

## Collaboration Flags

- **Drew**: Confirm that the rack zinc pre-treatment sequence shown (Soak → EC → Acid → Plate) matches the most common line layout he sees in customer shops. Confirm whether electrolytic cleaning order (cathodic first → anodic final) is the standard recommendation he gives to customers.
- **Tyler**: No direct validation needed for this poster — surface preparation is upstream of Tyler's titration domain. However, if Tyler encounters any disagreement with the chloride threshold (10 g/L) or electrocleaner parameters from A Brite product TDS data, flag it.
- **Alaina**: The "80% of defects" statistic is widely cited in industry literature but is an approximation, not a formally measured value. It is safe to use as a poster callout — it reflects genuine industry consensus. Consider whether to cite it as "80%+" or "most" depending on the visual weight desired.

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-04-04 (v1: 2026-04-03). Sources: Products Finishing (pfonline.com — "Better Electrocleaning," "Electrolytic Cleaning," "Reverse Current Cleaning"); NMFRC Surface Preparation of Metals Prior to Plating; PAVCO ("Electrolytic Cleaning," "How to Integrate Electrolytic Cleaning"); ASTM B322-99(2020)e1; ASTM B571; ASTM B850; AMS 2759/9; 1993 Metal Finishing Guidebook and Directory (vault); Drew's Quick Reference Metal Finishing Notes (vault); Finishing and Coating ("Electrocleaning's Basic Operating Dynamics"); domain expertise. Alaina should flag any data points requiring additional verification before final poster production.*
