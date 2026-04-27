---
title: Painting & Organic Coating Clusters — Watson Research Brief
author: Watson (Chemistry Researcher)
date: 2026-04-26
version: v1
status: RESEARCH COMPLETE
purpose: Comprehensive technical reference for Alaina (Construction Workups) and Elara (Generation Prompts)
poster_count_estimate: 72 (8 clusters x 9 posters each)
gemini_status: QUOTA EXHAUSTED — written from Watson domain expertise; flag for Gemini verification when quota resets
---

# Painting & Organic Coating Clusters — Watson Research Brief

> **Note to Alaina & Elara:** This brief covers 8 industrial painting/coating processes, each broken into 9 poster topics. Every section includes the numerical parameters, standards, and failure modes needed to build accurate Construction Workups. Where I flag uncertainty, verify before finalizing poster content.

---

# TABLE OF CONTENTS

- [Cluster 1: Powder Coating](#cluster-1-powder-coating)
- [Cluster 2: Liquid Spray Painting](#cluster-2-liquid-spray-painting)
- [Cluster 3: E-Coating (Electrophoretic Deposition)](#cluster-3-e-coating-electrophoretic-deposition)
- [Cluster 4: Dip Coating](#cluster-4-dip-coating)
- [Cluster 5: Flow Coating](#cluster-5-flow-coating)
- [Cluster 6: Coil Coating](#cluster-6-coil-coating)
- [Cluster 7: Industrial Priming Systems](#cluster-7-industrial-priming-systems)
- [Cluster 8: Protective Coatings (Epoxy / Urethane)](#cluster-8-protective-coatings-epoxy-urethane)
- [Cross-Cluster Standards Reference](#cross-cluster-standards-reference)
- [Cross-Cluster Safety Reference](#cross-cluster-safety-reference)
- [Cross-Cluster Defect Glossary](#cross-cluster-defect-glossary)

---

# CLUSTER 1: POWDER COATING

## 1.1 — Process Flow (Summary Poster)

### Process Sequence
1. Receiving / racking parts on grounded hooks or fixtures
2. Pretreatment (multi-stage wash: clean, rinse, phosphate/conversion, rinse, seal rinse)
3. Dry-off oven (250-300 deg F / 121-149 deg C, 10-15 min) — moisture must be fully removed
4. Cool to ambient (or near-ambient) before powder application
5. Powder application (electrostatic spray gun or fluidized bed)
6. Cure oven (350-400 deg F / 177-204 deg C, 10-20 min at metal temperature)
7. Cool down
8. Inspection (DFT, adhesion, visual)
9. Unrack, pack, ship

### Film-Forming Mechanism
- **Thermoset powders:** Particles melt, flow, gel, and cross-link irreversibly during cure. The cross-linking reaction is between the resin backbone (e.g., carboxyl-functional polyester) and a hardener (e.g., TGIC, HAA, or blocked isocyanate). Once cured, the film cannot be remelted.
- **Thermoplastic powders:** Particles melt, flow, and solidify on cooling. No chemical cross-linking occurs. The film can be remelted. Applied primarily via fluidized bed for thick coatings (8-25+ mils).

### Key Chemistry Families

| Chemistry | Cross-linker | Exterior Durability | Chemical Resistance | Typical Use |
|-----------|-------------|---------------------|--------------------:|-------------|
| Epoxy | Dicyandiamide (DICY) or phenolic | Poor (chalks/yellows in UV) | Excellent | Interior functional: pipe, rebar, electrical |
| Polyester-TGIC | Triglycidyl isocyanurate | Excellent | Good | Architectural, outdoor furniture, automotive trim |
| Polyester-HAA | Hydroxyalkylamide (Primid) | Excellent | Good | TGIC-free alternative (European preference) |
| Hybrid (epoxy-polyester) | Epoxy resin is the cross-linker for polyester | Moderate (indoor/mild outdoor) | Good | General industrial, office furniture, shelving |
| Polyurethane | Blocked isocyanate (caprolactam or IPDI) | Excellent | Very good | Automotive wheels, high-appearance outdoor |
| Acrylic | GMA-functional acrylic + diacid | Excellent | Good | Automotive clearcoat (high gloss, DOI) |

### Thermoplastic Powders

| Material | Melt Point | Typical DFT | Key Use |
|----------|-----------|-------------|---------|
| Nylon 11 (PA11) | 365 deg F / 185 deg C | 8-20 mils | Chemical/abrasion resistance; dishwasher racks |
| Nylon 12 (PA12) | 350 deg F / 177 deg C | 8-20 mils | Similar to PA11, lower moisture absorption |
| Polyethylene (PE) | 230-275 deg F / 110-135 deg C | 10-30 mils | Wire goods, tool handles, playground equipment |
| Polypropylene (PP) | 320 deg F / 160 deg C | 10-25 mils | Chemical tanks, lab equipment |
| PVC (Plastisol) | 350 deg F / 177 deg C | 10-40 mils | Fencing, hangers, tool grips |

### VOC Advantage
- Powder coatings contain essentially **zero VOC** (no solvents). Transfer efficiency 60-70% for electrostatic spray (overspray is reclaimed and reused). Waste is minimal. This is the single largest regulatory advantage of powder vs. liquid paint.

---

## 1.2 — Surface Preparation

### Substrate Requirements
- Powder coating can be applied to any electrically conductive substrate: steel, aluminum, zinc die-cast, brass, copper.
- Non-conductive substrates (MDF, plastics) require special conductive primers or pre-heating techniques.
- **Surface cleanliness is paramount** — powder magnifies surface defects because the film is typically 2-4 mils thick and cannot "fill" imperfections the way a thick liquid primer might.

### Incoming Material Condition
- Mill scale, rust, weld spatter, laser oxide, drawing compounds, machining oils must all be removed.
- For steel: mechanical prep to SSPC-SP6 (Commercial Blast) minimum; SSPC-SP10 (Near-White Blast) for high-performance.
- For aluminum: alkaline etch or non-etch clean, followed by chromate or non-chrome conversion coating.
- **Outgassing risk:** Cast aluminum, hot-rolled steel, and galvanized steel trap gases in the substrate. These gases escape during cure and create pinholes/craters ("outgassing"). Mitigation: pre-bake substrate at cure temperature for 10-20 min before powder application, or use outgassing-resistant powder formulations.

### Blast Profile (Steel)
- Target profile: 1.0-2.5 mils (25-63 microns) per ASTM D4417
- Media: aluminum oxide (aggressive), steel grit (consistent profile), garnet
- Blast-to-coat time window: 4 hours maximum in humid environments (flash rust risk)

---

## 1.3 — Cleaning

### Multi-Stage Washer (Spray Tunnel)
Typical 5-stage spray washer for powder coating:

| Stage | Chemistry | Temperature | Time | Purpose |
|-------|-----------|------------|------|---------|
| 1 — Alkaline Clean | pH 10-12, 2-5% concentration | 120-150 deg F (49-66 deg C) | 60-120 sec | Remove oils, soils, drawing compounds |
| 2 — Fresh Water Rinse | DI or city water | Ambient | 30-60 sec | Remove cleaner residuals |
| 3 — Conversion Coating | Iron phosphate or zirconium | 100-140 deg F (38-60 deg C) | 60-120 sec | Promote adhesion, corrosion resistance |
| 4 — Fresh Water Rinse | DI or RO water | Ambient | 30-60 sec | Remove conversion coating residuals |
| 5 — Seal Rinse (optional) | Non-chrome seal (Zr/Ti based) or DI final rinse | Ambient | 15-30 sec | Enhance corrosion resistance |

### Cleaner Chemistry
- **Alkaline cleaners:** Sodium hydroxide, sodium metasilicate, surfactants, chelating agents (EDTA, GLDA, citrate). Free alkalinity control by titration.
- **Acidic cleaners** (for aluminum): Phosphoric acid-based, pH 2-4; avoid strong alkaline on Al (etching/smut).
- **Conductivity monitoring:** Rinse water conductivity should be below 200 microsiemens/cm; below 50 for final DI rinse.

### Critical Control Points
- **Oil breakthrough:** Alkaline cleaner oil-loading capacity is finite. Monitor by water-break test (ASTM F22) — a sheet of unbroken water film on the surface confirms cleanliness.
- **Silicate residues:** Sodium silicate in cleaners can leave insoluble residues that cause adhesion failure. Use low-silicate or silicate-free formulations for powder coat pretreatment.

---

## 1.4 — Rinse / Dry

### Rinse Quality
- **Between cleaning and conversion coating:** City water acceptable; conductivity < 500 microsiemens/cm.
- **After conversion coating (final rinse):** DI water preferred; conductivity < 50 microsiemens/cm. High TDS in final rinse deposits salts on the surface that cause osmotic blistering under the powder film.
- **Counterflow rinse design:** Fresh water enters the last rinse tank and overflows backward to conserve water.

### Dry-Off Oven
- **Temperature:** 250-300 deg F (121-149 deg C)
- **Time:** 10-15 min at metal temperature (heavier parts need longer soak)
- **Purpose:** Remove all moisture. Any residual moisture causes blistering, adhesion loss, or outgassing during powder cure.
- **Air knife (optional):** Compressed air blow-off before oven entry removes standing water from recesses, reducing dry time and preventing water spotting.
- **Critical:** Parts must cool to below 90 deg F (32 deg C) before entering the powder booth. Hot parts attract powder unevenly and can cause thick edges/thin centers. Exception: "hot flocking" technique for thermoplastic powders intentionally uses preheated parts.

---

## 1.5 — Pretreatment

### Iron Phosphate (Most Common for Powder Coating)
- **Chemistry:** Acidic phosphate solution (pH 3.5-5.5) containing phosphoric acid, accelerators (hydroxylamine, nitrite, or molybdate), and surfactants.
- **Coating weight:** 25-75 mg/ft2 (270-810 mg/m2) — measured by gravimetric strip (ASTM B137 adapted) or XRF.
- **Crystal structure:** Amorphous (non-crystalline) iron phosphate, unlike the crystalline structure of zinc phosphate.
- **Color indicator:** Iridescent blue-to-gold film on steel. Heavier coatings appear darker blue/purple.
- **Salt spray performance:** Iron phosphate + powder coat typically achieves 500-750 hours B117 on cold-rolled steel.

### Zinc Phosphate (Higher Performance)
- **Coating weight:** 150-500 mg/ft2 (1,600-5,400 mg/m2)
- **Crystal structure:** Crystalline hopeite [Zn3(PO4)2 . 4H2O] and phosphophyllite [Zn2Fe(PO4)2 . 4H2O]
- **Performance:** 750-1,500+ hours B117 salt spray with powder coat.
- **Complexity:** Requires surface conditioning rinse (titanium phosphate colloidal, e.g., Henkel Fixodine), higher operating temperatures, more stages, and sludge management.
- **Cost:** 3-5x the chemical and waste treatment cost of iron phosphate.
- **When to specify:** Automotive, aerospace, severe exterior exposure, extended warranty requirements.

### Zirconium / Nanoceramic Conversion Coatings
- **Chemistry:** Fluorozirconic acid (H2ZrF6) or fluorotitanic acid at pH 3.5-5.0, ambient to 110 deg F.
- **Coating weight:** 5-30 mg/ft2 (very thin — nanoscale oxide film).
- **Advantages:** Chrome-free, low sludge, low temperature operation, effective on multi-metal lines (steel + aluminum + galvanized in one washer).
- **Performance:** Comparable to iron phosphate (500-750 hr B117) with powder coat; approaches zinc phosphate with optimized seal rinses.
- **Growing adoption:** Replacing iron phosphate in many shops due to lower waste treatment burden and multi-metal capability.

### Chromate Conversion (Aluminum Substrates)
- **Hexavalent chromate (MIL-DTL-5541 Type I):** Still required by many aerospace specs. Coating weight 40-150 mg/ft2. Being phased out under RoHS/REACH.
- **Trivalent chromate (MIL-DTL-5541 Type II):** Chrome-III process. Lower coating weight. Gaining aerospace approval.
- **Non-chrome alternatives:** Ti/Zr-based (see nanoceramic above); gaining traction but not yet universally accepted for aerospace.

---

## 1.6 — Application Stage

### Electrostatic Spray (Primary Method)

| Parameter | Typical Range | Notes |
|-----------|--------------|-------|
| Gun voltage | 60-100 kV | Higher voltage = better wrap; risk of back-ionization above 80 kV |
| Gun current (microamps) | 10-80 uA | Lower current for recoat/touch-up |
| Powder flow rate | 100-400 g/min | Adjust for line speed and target DFT |
| Gun-to-part distance | 6-12 inches (150-300 mm) | Closer = thicker but risk of back-ionization |
| Particle size (D50) | 30-45 microns | Finer for thin films; coarser for fluidized bed |
| Air velocity in booth | 60-100 fpm (0.3-0.5 m/s) | Enough to contain overspray, not enough to strip powder from parts |
| Transfer efficiency | 60-70% first-pass | Overspray reclaimed, total material utilization 95-98% |
| Reclaim system | Cyclone + cartridge filter | Cartridge filters for color change flexibility; cyclone for long-run colors |

### Charging Methods
- **Corona charging:** High-voltage electrode at gun tip ionizes air; free ions charge powder particles. Most common method. Can cause back-ionization (orange peel, pinholes) on thick films.
- **Tribo charging:** Powder particles gain charge by friction against PTFE gun barrel. No free ions = no back-ionization. Better penetration into Faraday cage areas. Lower charge density, slower build rate. Requires specific powder formulations designed for tribo.

### Faraday Cage Effect
- Deep recesses, inside corners, and box sections are electrostatically shielded — the electric field lines wrap around the edges rather than penetrating inside.
- **Mitigation:** Reduce voltage, reduce gun-to-part distance for recesses, use tribo guns, use smaller-diameter gun nozzles, or apply manual touch-up to recesses.

### Fluidized Bed Application
- Parts are preheated to 400-500 deg F (204-260 deg C) and dipped into a bed of fluidized powder.
- Powder melts on contact with the hot metal surface.
- Builds 8-25+ mils in a single dip. Primarily used for thermoplastic powders (nylon, PE, PVC).
- **Electrostatic fluidized bed:** Combines fluidization with a charging grid at the bottom of the bed. Parts do not need preheating. Practical for flat parts (panels, sheet metal) at 2-6 mil DFT.

### DFT Targets

| Application | DFT Range (mils) | DFT Range (microns) |
|-------------|-------------------|---------------------|
| Decorative interior (furniture, shelving) | 1.5-3.0 | 38-76 |
| General industrial | 2.0-4.0 | 51-102 |
| Architectural exterior | 2.5-4.0 | 64-102 |
| Automotive (primer + topcoat) | 3.0-5.0 | 76-127 |
| Functional/protective (rebar, pipe) | 7-14 | 178-356 |
| Fluidized bed (thermoplastic) | 8-25+ | 200-635+ |

---

## 1.7 — Flash / Leveling

### Not Applicable in Conventional Sense
- Powder coating has no solvent, so there is no "flash" period as in liquid paint.
- However, the **gel-flow-cure** sequence in the oven is the equivalent:
  1. **Melt/gel phase (first 2-5 min):** Powder particles soften, melt, and begin to flow together into a continuous film.
  2. **Flow/leveling phase (next 3-8 min):** Molten coating flows and levels. Viscosity is at minimum. This is when orange peel is determined — longer flow time = smoother finish.
  3. **Cross-link/cure phase (remaining time):** Viscosity increases rapidly as cross-linking proceeds. Film hardens irreversibly.
- **Poster angle for this slot:** Focus on the gel-flow-cure stages as a visual timeline diagram. Show temperature ramp vs. viscosity curve. Highlight that insufficient flow time causes orange peel, and excessive time/temperature causes overbake (yellowing, embrittlement).

### Factors Affecting Leveling
- Powder particle size distribution (finer = smoother)
- Cure schedule (faster ramp = less flow time)
- Powder formulation (flow additives, e.g., benzoin for degassing, acrylate flow agents)
- Film thickness (thicker films flow and level better)

---

## 1.8 — Cure Stage

### Cure Parameters

| Chemistry | Cure Temperature (metal temp) | Cure Time at Temp | Notes |
|-----------|------------------------------|-------------------|-------|
| Epoxy | 350-400 deg F (177-204 deg C) | 10-20 min | Standard cure |
| Hybrid (epoxy-polyester) | 350-375 deg F (177-191 deg C) | 10-15 min | |
| Polyester-TGIC | 375-400 deg F (191-204 deg C) | 10-15 min | |
| Polyester-HAA | 375-400 deg F (191-204 deg C) | 10-15 min | Emits water during cure (condensation reaction) |
| Polyurethane | 350-400 deg F (177-204 deg C) | 15-25 min | Blocked isocyanate unblocks at ~320 deg F |
| Acrylic | 325-375 deg F (163-191 deg C) | 15-20 min | Lower cure temp possible |
| Low-temp cure formulations | 250-300 deg F (121-149 deg C) | 15-30 min | For heat-sensitive substrates (MDF, plastics) |

### Critical Distinction: Oven Temperature vs. Metal Temperature
- **The cure window is always defined by METAL temperature, not oven air temperature.** A large steel part may require 30+ minutes of oven time to reach 375 deg F metal temperature, even though the oven air is at 400 deg F.
- **Oven profiling:** Use thermocouple data loggers (e.g., Datapaq, ECD) to map actual metal temperature vs. time through the oven. The "cure window" is the integral of time at or above the minimum cure temperature.

### Undercure vs. Overcure
- **Undercure:** Film remains soft, poor chemical resistance, poor adhesion, low hardness. Test by MEK rub (ASTM D4752) — undercured film dissolves in < 50 double rubs.
- **Overcure:** Film yellows (especially epoxy), becomes brittle, loses flexibility, impact resistance drops. Overcure also wastes energy.
- **MEK rub test:** Apply MEK-soaked cloth, 50 double rubs with 2 lb pressure. Fully cured thermoset shows no softening, no color transfer. Standard pass: 50+ double rubs with no breakthrough.

### Oven Types
- **Convection (most common):** Gas-fired or electric, with recirculating fans. Even heat distribution critical.
- **Infrared (IR):** Rapid heat-up; good for thin, uniform parts. Poor penetration into recesses or heavy parts.
- **IR + convection combination:** IR zone for fast gel/melt, followed by convection zone for full cure.

---

## 1.9 — Inspection & Handling

### Film Thickness
- **Measurement:** Magnetic gauge (steel substrate) or eddy current gauge (aluminum substrate) per ASTM D7091.
- **Frequency:** Per quality plan — typically 3-5 readings per part, minimum of 5 parts per rack or batch.
- **Specification:** Per customer requirement; general industrial tolerance +/- 0.5 mil from target.

### Adhesion
- **ASTM D3359 Method B (Cross-Cut):** Score a lattice pattern (6 or 11 cuts), apply tape, pull at 180 deg. Rate 0B (complete removal) to 5B (no removal). Pass = 4B or 5B.
- **ASTM D3359 Method A (X-Cut):** Score an X, apply tape, pull. Less quantitative but faster.

### Hardness
- **ASTM D3363 Pencil Hardness:** Push calibrated pencils (6B to 9H) across the film. Report the hardest pencil that does NOT cut through. Typical thermoset powder: F to 3H.
- **Buchholz indentation (ISO 2815):** More reproducible than pencil hardness for QC.

### Flexibility
- **ASTM D522 Mandrel Bend:** Bend coated panel over cylindrical mandrel (1/8" to 1" diameter). Report smallest mandrel diameter with no cracking. Typical polyester powder: 1/8" mandrel pass.
- **ASTM D2794 Impact Resistance:** Drop a weighted tup onto coated panel. Report inch-pounds (direct and reverse). Typical: 80-160 in-lb direct impact.

### Chemical Resistance / MEK Rub
- **ASTM D4752 MEK Double Rub:** Standard cure verification test. 50+ double rubs = fully cured.
- **Chemical spot test:** Apply reagent drops (10% NaOH, 10% H2SO4, MEK, xylene) to the film for specified time. Evaluate staining, softening, blistering.

### Salt Spray
- **ASTM B117:** Scribed panels exposed to 5% NaCl fog at 95 deg F. Evaluate creepage from scribe per ASTM D1654.
- Typical performance:
  - Iron phosphate + polyester powder: 500-750 hours
  - Zinc phosphate + polyester powder: 1,000-1,500 hours
  - Iron phosphate + epoxy powder (interior): 1,000+ hours

### Handling
- Parts must cool to below 120 deg F (49 deg C) before handling — fingerprints embed in warm powder film.
- Use clean cotton or nitrile gloves. Silicone-contaminated gloves cause fish-eye defects on adjacent uncured parts.
- Packaging: Avoid contact between coated surfaces. Use foam dividers, kraft paper interleaving.

---

# CLUSTER 2: LIQUID SPRAY PAINTING

## 2.1 — Process Flow (Summary Poster)

### Process Sequence
1. Receiving / racking / masking
2. Surface preparation (blast, sand, degrease)
3. Cleaning (alkaline wash or solvent wipe)
4. Rinse / dry
5. Pretreatment (phosphate, chromate, or conversion coating)
6. Primer application (spray)
7. Flash / dry (ambient or force)
8. Topcoat application (basecoat + clearcoat for multi-coat, or single-stage topcoat)
9. Flash between coats
10. Cure (air dry, force dry, or bake)
11. Inspection (DFT, adhesion, visual, gloss)
12. Unrack / pack / ship

### Film-Forming Mechanisms

| System | Mechanism | Example |
|--------|-----------|---------|
| Lacquer | Solvent evaporation only; no chemical reaction; film redissolves in original solvent | Nitrocellulose lacquer, acrylic lacquer |
| Oxidative dry | Solvent evaporation + oxygen-induced cross-linking of unsaturated fatty acids | Alkyd enamels, linseed oil paints |
| Moisture cure | Isocyanate reacts with atmospheric moisture | Moisture-cure polyurethane |
| 2K chemical cure | Component A (polyol/epoxy) + Component B (isocyanate/amine) react when mixed | 2K urethane, 2K epoxy |
| Waterborne coalescence | Water evaporates, latex particles deform and coalesce into continuous film; optional cross-linking | Acrylic latex, water-reducible alkyd |
| High-solids | Solvent evaporation + cross-linking (same as 2K but with less solvent) | High-solids epoxy, high-solids urethane |
| UV cure | Photoinitiator absorbs UV light, generates free radicals, initiates polymerization | UV-cure acrylate (wood, plastic) |

---

## 2.2 — Surface Preparation

### Steel
- **SSPC-SP1 Solvent Cleaning:** Remove visible oil, grease, soil.
- **SSPC-SP2 Hand Tool Cleaning** / **SSPC-SP3 Power Tool Cleaning:** Remove loose mill scale, rust, old paint.
- **SSPC-SP6 Commercial Blast:** Remove all mill scale, rust, old coatings except shadows/streaks.
- **SSPC-SP10 Near-White Blast:** 95% of surface free of all visible residues. High-performance coatings.
- **SSPC-SP5 White Metal Blast:** 100% removal. Immersion service (tank lining).
- **Profile:** 1.5-3.0 mils (38-76 microns) for most liquid primers.

### Aluminum
- Alkaline etch or non-etch clean + chromate conversion per MIL-DTL-5541 (aerospace), or non-chrome conversion.
- Scuff sand with 180-320 grit Scotch-Brite for mechanical adhesion.
- Anodize (sulfuric or chromic) as pretreatment for paint adhesion on aluminum aerospace parts.

### Plastic
- Solvent wipe (IPA) + adhesion promoter (chlorinated polyolefin for PP/PE, or flame/plasma treatment).
- Static dissipation treatment for electrostatic spray on plastics.

---

## 2.3 — Cleaning

### Methods
- **Solvent wipe:** Acetone, MEK, IPA, or proprietary blends. Two-rag method (wet rag dissolves contamination, dry rag removes it before evaporation).
- **Alkaline spray wash:** Same multi-stage system as powder coating (see Cluster 1.3).
- **Vapor degreasing:** Trichloroethylene or nPB vapor (declining use due to EPA regulation).
- **Aqueous parts washer:** Heated alkaline solution with agitation.

### Verification
- **Water break test (ASTM F22):** Unbroken water film = clean surface.
- **UV inspection lamp:** Fluorescent oils/compounds glow under 365 nm UV.
- **Contact angle measurement:** Research/aerospace QC. < 5 deg = excellent cleanliness.

---

## 2.4 — Rinse / Dry

### Same principles as Cluster 1.4
- DI rinse after conversion coating.
- Air blow-off for recesses.
- Force dry or air dry to remove all moisture.
- **Key difference from powder:** Some liquid primers are moisture-tolerant (e.g., wash primers/etch primers can be applied to damp surfaces). Powder coating absolutely cannot.

### Tack Cloth
- After sanding between coats, wipe with tack cloth to remove dust before spray.
- Use low-tack (silicone-free) tack cloths to avoid fish-eye contamination.

---

## 2.5 — Pretreatment

### Iron Phosphate
- Standard for general industrial liquid spray painting on steel.
- Same parameters as Cluster 1.5 (coating weight 25-75 mg/ft2).
- Paired with alkyd or acrylic primer, provides 250-500 hours B117.

### Zinc Phosphate
- Automotive and high-performance.
- Coating weight 150-500 mg/ft2.
- With epoxy primer: 750-1,500 hours B117.

### Wash Primer (Vinyl Butyral Etch Primer)
- **DOD-P-15328** (military spec) / TT-P-1757
- Two-component: polyvinyl butyral resin + phosphoric acid catalyst.
- Applied at 0.3-0.5 mil DFT.
- Etches bare metal + deposits thin conversion layer + provides primer adhesion simultaneously.
- Excellent for field touch-up where multi-stage washer is unavailable.
- Must be topcoated — not a standalone primer.

### Chromate Conversion (Aluminum)
- MIL-DTL-5541 Type I (hex chrome) or Type II (tri-chrome).
- Required by many aerospace prime specs before painting.
- Coating weight: 40-150 mg/ft2.

### Self-Etching Primers
- Acid-functional primers (phosphoric acid component) that combine adhesion promotion with priming in one coat.
- DFT: 0.5-1.0 mil.
- Common in automotive refinish and aerospace touch-up.

---

## 2.6 — Application Stage

### Spray Methods Comparison

| Method | Atomizing Pressure | Fluid Delivery | Transfer Efficiency | Finish Quality | Best For |
|--------|-------------------|----------------|--------------------:|---------------|----------|
| Conventional Air Spray | 30-60 psi at cap | 8-15 psi fluid pressure, siphon or pressure pot | 25-45% | Excellent atomization, finest finish | High-quality topcoats, small parts |
| HVLP (High Volume Low Pressure) | Max 10 psi at air cap | Gravity cup or pressure pot | 65%+ (EPA minimum for HVLP) | Very good | General industrial, regulatory compliance |
| Airless | N/A | 1,500-3,000 psi fluid pressure | 50-70% | Good (coarser atomization) | Large surface areas, high production |
| Air-Assisted Airless | 5-30 psi air assist | 500-1,500 psi fluid pressure | 60-75% | Very good (finer than pure airless) | Heavy industrial, shipyard, structural steel |
| Electrostatic (rotary bell) | Turbine atomizer, 20,000-60,000 RPM | Metered pump | 85-95% | Excellent | Automotive OEM, highest efficiency |

### Application Parameters

| Parameter | Primer | Basecoat (Color) | Clearcoat |
|-----------|--------|-------------------|-----------|
| Target DFT (mils) | 0.8-2.0 | 0.5-1.5 | 1.5-2.5 |
| Number of coats | 1-2 | 2-3 (metallic may need 3+) | 2 |
| Flash between coats | 5-15 min | 3-10 min | 5-15 min |
| Gun distance (inches) | 8-12 | 6-10 | 8-12 |
| Pattern overlap | 50% | 50-75% | 50% |
| Spray booth air velocity | 75-125 fpm crossdraft; 50-75 fpm downdraft | Same | Same |

### Wet Film Thickness Measurement
- **ASTM D4414 Wet Film Gauge:** Notched gauge pressed into wet paint. Read the highest notch that is wetted. Used to predict DFT based on volume solids: DFT = WFT x % Volume Solids / 100.

### Viscosity Control
- **Zahn cup (ASTM D4212):** #2 cup for light coatings (12-20 sec), #4 cup for heavier (15-25 sec).
- **Ford cup (ASTM D1200):** #4 Ford cup: 15-30 sec for spray viscosity.
- Viscosity is temperature-sensitive: calibrate to 77 deg F (25 deg C).

---

## 2.7 — Flash / Leveling

### Flash Time
- **Definition:** Time between coats (or after final coat before entering oven) to allow solvent evaporation and initial film formation.
- **Ambient flash:** 5-15 minutes typical, depending on solvent blend, temperature, humidity.
- **Force flash:** 140-180 deg F (60-82 deg C), 5-10 min — accelerates solvent release, prevents solvent pop in bake.
- **Waterborne flash:** Requires controlled humidity and airflow. Waterborne basecoats need 70-80 deg F, 50-70% RH, and directional airflow for proper water evaporation. Too fast = skin over = solvent pop. Too slow = sag.

### Leveling
- Solvent blend is formulated to provide the right evaporation rate for leveling. "Tail solvents" (slow evaporators like butyl cellosolve, PM acetate) keep the film fluid long enough to level.
- **Orange peel** results from too-fast solvent evaporation, too-low atomization pressure, too-far gun distance, or spray applied too dry.

### Intercoat Adhesion Window
- Most coatings have a maximum recoat window — if you wait too long, the primer surface becomes too hard for the topcoat to bite into.
- Typical windows: Alkyd 24-72 hr; 2K epoxy 4-24 hr (critical — epoxy becomes too hard); 2K urethane 1-24 hr.
- **If window is exceeded:** Scuff sand with 320-400 grit before recoating.

---

## 2.8 — Cure Stage

### Cure Methods

| Method | Temperature | Time | Systems |
|--------|------------|------|---------|
| Air dry (ambient) | 65-85 deg F (18-29 deg C) | 1-7 days to full cure | Alkyds, latex, moisture-cure PU |
| Force dry | 140-180 deg F (60-82 deg C) | 30-60 min | Alkyds, modified acrylics |
| Bake (low temp) | 200-250 deg F (93-121 deg C) | 20-30 min | Modified alkyds, polyesters |
| Bake (high temp) | 250-350 deg F (121-177 deg C) | 15-30 min | Thermoset acrylics, baking enamels |
| 2K chemical cure | Ambient to 140 deg F | Pot life dependent (15 min - 8 hr) | 2K epoxy, 2K urethane |
| UV cure | Ambient (UV lamp exposure) | 1-10 sec under lamp | UV acrylate (wood, plastic, printing) |

### Pot Life (2K Systems)
- **2K Epoxy:** 30 min - 4 hours, depending on hardener reactivity and temperature.
- **2K Urethane:** 15 min - 8 hours (aliphatic isocyanate longer; aromatic shorter).
- Mixed material must be used within pot life or discarded — cross-linking in the container causes gelling.

---

## 2.9 — Inspection & Handling

### DFT Measurement
- **ASTM D7091:** Magnetic and eddy current gauges. Same as powder coating.
- **Tooke Gauge (ASTM D4138):** Destructive — cuts a V-groove through the film. Measures individual coat thicknesses in multi-coat systems. Essential for automotive refinish and multi-coat industrial systems.

### Gloss
- **ASTM D523:** 60-degree glossmeter. Report in Gloss Units (GU).
  - High gloss: > 80 GU
  - Semi-gloss: 30-80 GU
  - Satin: 15-30 GU
  - Flat/matte: < 15 GU

### Color
- **ASTM D2244 (Delta E):** Spectrophotometer measurement. Delta E < 1.0 = imperceptible difference. Most industrial specs require Delta E < 3.0.

### Adhesion, Hardness, Flexibility
- Same tests as powder coating: D3359 (adhesion), D3363 (pencil hardness), D522 (mandrel bend), D2794 (impact).

### VOC Compliance
- **EPA 40 CFR Part 63, Subpart HHHHHH (6H):** NESHAP for paint stripping and miscellaneous surface coating at area sources.
- **EPA 40 CFR Part 63, Subpart MMMM:** NESHAP for surface coating of miscellaneous metal parts and products (major sources).
- **Typical VOC limits:** 2.0-4.2 lb/gal (less water) depending on coating category and state/local rules.
- **SCAQMD Rule 1107 (Southern California):** Strictest in the US; drives industry toward waterborne and high-solids.

---

# CLUSTER 3: E-COATING (ELECTROPHORETIC DEPOSITION)

## 3.1 — Process Flow (Summary Poster)

### Process Sequence (Automotive Body-in-White Standard)
1. Spot weld body assembly
2. Alkaline spray clean (2 stages)
3. Rinse
4. Surface conditioning (colloidal titanium phosphate seed crystals)
5. Zinc phosphate immersion (2-3 min)
6. Rinse (2 stages)
7. Non-chrome seal rinse (post-rinse)
8. DI water rinse
9. **E-coat immersion tank** (cathodic electrodeposition, 2-3 min, 200-400 V DC)
10. UF permeate rinse (2-3 stages)
11. DI rinse
12. E-coat bake oven (350-375 deg F, 20-30 min at metal temp)
13. Cool
14. Inspect
15. To topcoat line (primer surfacer, basecoat, clearcoat)

### Why E-Coat Matters
- E-coat is the **standard first-coat primer for virtually every automobile made worldwide**. It is the foundation of automotive corrosion protection.
- **Throwing power** is the key advantage: electrodeposition drives coating into every recess, box section, weld seam, and interior cavity of a car body — areas that spray painting cannot reach.
- Annual global e-coat volume exceeds 500 million square meters of coated surface.

---

## 3.2 — Surface Preparation

### Automotive Standard
- Body-in-white arrives from welding with stamping oils, metal fines, weld flux residues.
- **No abrasive blasting** — car bodies are thin-gauge steel (0.6-1.2 mm); blasting would deform panels.
- All preparation is chemical (spray and immersion).

### Multi-Metal Considerations
- Modern automotive bodies contain cold-rolled steel, galvanized steel (electrogalvanized and hot-dip), aluminum panels, and sometimes magnesium.
- The pretreatment system must handle all substrates simultaneously.
- Zinc phosphate chemistry is tuned for multi-metal: nickel/manganese-modified bath for uniform crystal structure on steel and galvanized.

---

## 3.3 — Cleaning

### Two-Stage Alkaline Clean

| Stage | Type | Chemistry | Temperature | Time |
|-------|------|-----------|------------|------|
| 1 — Pre-clean | Spray | Alkaline, pH 10-12, 1-3% | 120-140 deg F (49-60 deg C) | 60-90 sec |
| 2 — Main clean | Immersion | Alkaline, pH 10-12, 2-5% | 130-150 deg F (54-66 deg C) | 120-180 sec |

- **Critical:** Cleaner must be low-foaming for spray stages, and must not leave silicate residues that interfere with phosphating.
- **Oil loading:** Monitor by titration (free alkalinity, total alkalinity) and oil content analysis. Dump and recharge when oil loading exceeds 5-8 g/L.
- **Body drainage:** Car bodies must be designed with drain holes and entry points to allow cleaning solutions to flood all cavities. "Dip-drain-dip" sequencing is critical.

---

## 3.4 — Rinse / Dry

### Rinse Stages (Pre-E-Coat)
- **After cleaning:** 2 spray rinse stages, counterflow, conductivity monitored.
- **After zinc phosphate:** 2 immersion rinse stages + 1 non-chrome seal rinse + 1 DI final rinse.
- **DI water quality:** Conductivity < 20 microsiemens/cm for final rinse before e-coat.
- **No dry-off oven before e-coat** — the body enters the e-coat tank wet (unlike powder coating where parts must be bone dry). The wet surface is electrochemically active and the e-coat process is aqueous.

### Post-E-Coat Rinse (UF Permeate System)
This is unique to e-coat and is a **critical poster topic**:
- When the body exits the e-coat tank, it drags out 10-30% of its wet weight in e-coat paint.
- This dragout is rinsed off in 2-3 stages of **ultrafiltration (UF) permeate** — water that has been extracted from the e-coat tank through semipermeable UF membranes.
- The UF permeate contains water + solvent + small-molecule solutes, but **no resin or pigment** (these are too large to pass through the UF membrane).
- The rinse dragout (now diluted e-coat) flows **back to the e-coat tank**, recovering > 95% of the dragged-out paint.
- This closed-loop recovery makes e-coat extremely material-efficient (> 99% paint utilization) and minimizes wastewater.

### UF System Parameters

| Parameter | Typical Range |
|-----------|--------------|
| UF membrane pore size | 50,000-100,000 molecular weight cutoff (MWCO) |
| Permeate flow rate | 5-20 gal/min per 100 sq ft membrane area |
| Permeate conductivity | 500-2,000 microsiemens/cm |
| Permeate pH | Close to bath pH (5.8-6.2 for cathodic) |
| Membrane material | Polysulfone or PVDF (tubular or hollow fiber) |
| Membrane cleaning | Periodic flush with permeate + cleaning solution |

---

## 3.5 — Pretreatment (Zinc Phosphate for E-Coat)

### Full Automotive Zinc Phosphate Line

| Stage | Process | Chemistry | Temperature | Time | Key Parameter |
|-------|---------|-----------|------------|------|---------------|
| 1 | Pre-clean | Alkaline spray | 120-140 deg F | 60-90 sec | Free alkalinity 3-8 points |
| 2 | Main clean | Alkaline immersion | 130-150 deg F | 120-180 sec | Total alkalinity 15-25 points |
| 3 | Rinse | City water spray | Ambient | 30-60 sec | |
| 4 | Rinse | City water immersion | Ambient | 60 sec | |
| 5 | Surface conditioning | Colloidal TiPO4 | Ambient-100 deg F | 30-60 sec | Concentration 0.5-2.0 g/L; refines crystal size |
| 6 | Zinc phosphate | Immersion | 95-115 deg F (35-46 deg C) | 120-180 sec | Total acid 18-25 points; free acid 0.6-1.0 points; accelerator (NO2 or H2O2) |
| 7 | Rinse | City water immersion | Ambient | 60 sec | |
| 8 | Rinse | City water spray | Ambient | 30 sec | |
| 9 | Post-rinse / Seal rinse | Non-chrome seal (Zr-based) | Ambient | 30-60 sec | Seals open porosity in phosphate crystal matrix |
| 10 | DI rinse | DI immersion | Ambient | 60 sec | Conductivity < 20 uS/cm |

### Zinc Phosphate Crystal Quality
- **Target coating weight:** 150-400 mg/ft2 (1,600-4,300 mg/m2) for automotive.
- **Crystal size:** Fine, uniform microcrystalline. Surface conditioning with colloidal TiPO4 (Henkel Fixodine or equivalent) provides nucleation sites for small, dense crystals.
- **Crystal composition:** Mixture of hopeite [Zn3(PO4)2 . 4H2O] and phosphophyllite [Zn2Fe(PO4)2 . 4H2O]. Higher phosphophyllite ratio = better paint adhesion and corrosion resistance.
- **Sludge:** Zinc phosphate baths generate iron phosphate sludge (from dissolved iron substrate). Must be removed by settling, filtration, or centrifuge. Sludge ratio: 10-20 g sludge per m2 coated surface.

---

## 3.6 — Application Stage (E-Coat Tank)

### Cathodic Electrodeposition — How It Works
1. Car body (cathode) is immersed in the e-coat bath containing waterborne paint emulsion.
2. DC voltage (200-400 V) is applied between the body (cathode) and anodes (stainless steel or carbon) positioned along the tank walls and bottom.
3. Positively charged resin micelles (cationic epoxy-amine resin + pigment) migrate toward the cathodic body surface.
4. At the cathode surface, water electrolysis generates OH- ions: 2H2O + 2e- -> H2 + 2OH-
5. Local pH rise at the cathode surface causes the cationic resin to become insoluble (neutralization of the amine groups), and it deposits as a dense, adherent film.
6. The deposited film is electrically insulating — once it reaches sufficient thickness, current can no longer flow through that area, and deposition stops. This is the **self-limiting mechanism** that gives e-coat its uniform thickness and excellent throwing power.

### Bath Parameters

| Parameter | Cathodic Epoxy E-Coat | Anodic Acrylic E-Coat |
|-----------|----------------------|----------------------|
| Solids content | 18-22% (by weight) | 8-14% |
| pH | 5.8-6.2 | 7.5-8.5 |
| Conductivity | 1,000-1,800 uS/cm | 800-1,500 uS/cm |
| Temperature | 85-95 deg F (29-35 deg C) | 80-90 deg F (27-32 deg C) |
| Voltage | 200-400 V DC | 50-250 V DC |
| Immersion time | 120-180 sec | 90-120 sec |
| Film build (wet) | 0.8-1.5 mils | 0.5-1.0 mils |
| DFT (cured) | 0.6-1.2 mils (15-30 microns) | 0.4-0.8 mils |
| P/B ratio (pigment/binder) | 0.15-0.25 | 0.10-0.20 |
| MEQ (milliequiv acid/100g solids) | 30-45 | N/A (base-neutralized) |
| Throwing power | Excellent (8-12 inches into box sections) | Moderate |

### Anode Management
- Anodes are enclosed in **anode boxes** (dialysis membranes) that allow organic acid anions to pass out of the bath, preventing acid buildup.
- Anode box effluent (anolyte) is bled off and replaced with DI water to control bath pH and conductivity.
- Anode material: 316 stainless steel (cathodic e-coat); carbon/graphite (anodic e-coat, because anodic bath dissolves stainless).

### Cathodic vs. Anodic — Why Cathodic Dominates
- **Cathodic:** Body is cathode. Metal does not dissolve during deposition. Superior corrosion protection. Used for > 95% of automotive e-coat worldwide.
- **Anodic:** Body is anode. Metal dissolution can contaminate bath and reduce corrosion performance. Simpler chemistry. Used for non-critical applications (small appliances, general industrial).

---

## 3.7 — Flash / Leveling

### Post-Rinse Drain / Flash
- After UF rinse stages, the body passes through an air blow-off zone and a brief flash/drain zone before entering the bake oven.
- **Flash zone temperature:** Ambient to 120 deg F, 3-5 min.
- The e-coat film at this stage is a wet, gel-like deposit. It does not flow or level like liquid paint — the film is already deposited in its final location by the electric field.
- **No leveling concerns in the conventional sense.** The electrodeposition process inherently produces a smooth, uniform film. Orange peel is not an issue for e-coat.

### Poster Angle
- Focus on the **UF rinse recovery system** as the "flash/leveling equivalent" for e-coat. The multi-stage counterflow rinse with UF permeate is the unique process step that distinguishes e-coat from all other coating methods.

---

## 3.8 — Cure Stage

### Bake Parameters

| Parameter | Cathodic Epoxy E-Coat |
|-----------|----------------------|
| Oven temperature | 350-375 deg F (177-191 deg C) oven air |
| Metal temperature at cure | 340-360 deg F (171-182 deg C) |
| Time at metal temp | 20-30 min |
| Total oven time (including ramp) | 30-45 min for car bodies |

### Cure Chemistry
- The deposited film contains blocked isocyanate cross-linkers (typically caprolactam-blocked MDI or IPDI).
- During bake, the blocking agent volatilizes (unblocks) at ~300 deg F, freeing the isocyanate groups to react with hydroxyl groups on the epoxy resin backbone.
- This cross-linking reaction produces a tough, solvent-resistant thermoset film.
- **Blocking agent emission:** Caprolactam or other blocking agents are released as vapor during bake. These must be captured by an afterburner (thermal or catalytic oxidizer) in the oven exhaust. This is the primary VOC/air emission source from e-coat operations.

### Undercure Detection
- MEK double rub test: minimum 100 double rubs for fully cured cathodic e-coat.
- Undercured e-coat shows solvent sensitivity, poor adhesion of subsequent topcoat layers, and reduced salt spray performance.

---

## 3.9 — Inspection & Handling

### Film Thickness
- **Target DFT:** 0.6-1.2 mils (15-30 microns). Automotive spec is typically 0.7-1.0 mil.
- Measured per ASTM D7091 on flat surfaces. Destructive cross-section (optical microscopy) for cavity interiors.
- **Throwing power measurement:** Measure DFT at various distances inside a standardized test box (e.g., 2" x 4" x 12" deep). Ratio of interior DFT to exterior DFT is the throwing power index.

### Salt Spray
- **Cathodic e-coat over zinc phosphate on CRS:** 500-1,000+ hours B117 (as a standalone primer, no topcoat).
- **Full automotive system (e-coat + primer surfacer + basecoat + clearcoat):** 1,500-4,000+ hours B117 depending on substrate and pretreatment.
- **Cyclic corrosion testing (SAE J2334, GMW14872):** More representative of real-world automotive corrosion than B117. Specified by most OEMs.

### Adhesion
- ASTM D3359 Method B: 5B required.
- Wet adhesion test: Soak coated panel in DI water at 104 deg F (40 deg C) for 240 hr, then crosshatch tape pull within 30 min of removal. Must maintain 4B-5B.

### Bath Monitoring
- **Daily:** pH, conductivity, temperature, solids (by weight), P/B ratio (by ash test or centrifuge).
- **Weekly:** MEQ (milliequivalents of acid per 100 g solids — by titration), solvent content (by GC or distillation), rupture voltage test (measures film insulation quality).
- **UF membrane performance:** Permeate flow rate, conductivity, pressure differential. Declining flow rate indicates membrane fouling.

---

# CLUSTER 4: DIP COATING

## 4.1 — Process Flow (Summary Poster)

### Process Sequence
1. Surface preparation (clean, degrease, blast as needed)
2. Preheat (optional, for thermoplastic dip coatings)
3. Immerse part into coating tank
4. Withdraw at controlled speed
5. Drain / drip (gravity removes excess)
6. Cure (air dry, oven bake, or cool for thermoplastic)
7. Inspect

### Applications
- Wire and cable insulation (PVC plastisol)
- Tool handles (rubber, PVC, polyethylene)
- Dishwasher racks (nylon 11, vinyl)
- Container lining (epoxy phenolic for food cans)
- Medical devices (silicone, parylene — specialized)
- Rubber coatings on metal parts (plasti-dip type)

### Film-Forming Mechanisms
- **Plastisol dip:** PVC particles suspended in plasticizer. Heat fuses particles into a continuous film. No solvent evaporation. Cure: 350-400 deg F (177-204 deg C), 10-20 min.
- **Hot-dip thermoplastic:** Preheated part dipped into fluidized bed or liquid melt. Film builds by thermal transfer. Thickness controlled by part temperature and dip time.
- **Solution/dispersion dip:** Part immersed in liquid coating (solvent-borne or waterborne). Film controlled by withdrawal speed, viscosity, and drainage.
- **Electrocoat dip:** See Cluster 3 (e-coat is a specialized dip process with electrophoretic deposition).

---

## 4.2 — Surface Preparation

### Steel Parts
- Alkaline clean + phosphate conversion (iron or zinc phosphate).
- Abrasive blast for heavy-duty applications (SSPC-SP6 minimum).
- Primer coat (optional) for multi-coat dip systems.

### Wire and Cable
- Wire is continuously drawn through cleaning stages (alkaline spray, rinse) before entering the dip/extrusion coating head.
- Copper wire: surface must be free of drawing lubricant residues.

### Tool Handles / Consumer Products
- Degrease + mechanical roughening (80-120 grit blast) for maximum adhesion.
- Adhesion promoter (primer) for PVC on steel, PE on steel.

---

## 4.3 — Cleaning

- Same general principles as other processes.
- **For continuous wire/cable lines:** In-line alkaline spray cleaning with ultrasonic assist.
- **For batch dip:** Alkaline soak clean (120-160 deg F, 5-15 min), rinse, dry.
- Cleanliness is less critical for thick dip coatings (8-40 mils) than for thin spray coatings (1-3 mils), but adhesion still requires a clean surface.

---

## 4.4 — Rinse / Dry

- Parts must be **completely dry** before dip coating — moisture trapped under the coating causes blistering during cure.
- Oven dry: 200-250 deg F (93-121 deg C), 10-15 min.
- For hot-dip thermoplastic: Parts are preheated to 400-500 deg F (204-260 deg C), which inherently eliminates moisture.

---

## 4.5 — Pretreatment

### Iron Phosphate (Steel Parts)
- Standard for general dip coating applications.
- Coating weight 25-75 mg/ft2.
- Provides adhesion and under-film corrosion resistance.

### Primer (Adhesion Promoter)
- Many dip coating systems require a liquid primer before the dip coat:
  - **PVC on steel:** Phenolic-based or polyester primer.
  - **Nylon on steel:** Epoxy primer.
  - **Polyethylene on steel:** Chlorinated polyolefin primer or flame treatment.
- Primer DFT: 0.3-1.0 mil, baked or air-dried before dipping.

---

## 4.6 — Application Stage

### Dip Process Parameters

| Parameter | Plastisol (PVC) | Hot-Dip (Nylon/PE) | Solution Dip |
|-----------|-----------------|---------------------|-------------|
| Bath temperature | Ambient to 120 deg F | N/A (fluidized bed at ambient) | Ambient to 100 deg F |
| Part preheat | None (plastisol gels on cold part too) or 200-300 deg F for thicker builds | 400-600 deg F (204-316 deg C) | None |
| Immersion time | 2-30 sec (controls thickness) | 2-10 sec (controls thickness) | 1-10 sec |
| Withdrawal speed | 2-12 inches/sec | Rapid | 1-6 inches/sec (slower = thinner film) |
| Film build per dip | 5-40 mils (depends on time and viscosity) | 8-25 mils | 0.5-3 mils per dip |
| Multiple dips | Yes (for very thick coatings) | Rarely needed | Common (build thickness gradually) |

### Film Thickness Control
- **Withdrawal speed** is the primary control for solution/dispersion dip. The Landau-Levich equation governs: film thickness is proportional to (withdrawal speed)^(2/3) x (viscosity)^(2/3) / (surface tension)^(1/6).
- **Dip time and part temperature** are the primary controls for hot-dip thermoplastic.
- **Viscosity management:** For plastisol, viscosity is controlled by PVC particle size, plasticizer type and ratio, and diluent additions. For solutions, viscosity is controlled by solids content and solvent additions.

### Drip / Drainage
- After withdrawal, excess coating drains by gravity. The part is rotated or inverted to prevent thick "drip edges" at the bottom.
- **Drip time:** 10-60 sec before entering cure oven.
- Continuous wire/cable lines use air knives or die strippers to control film thickness at line speeds of 100-1,000+ ft/min.

---

## 4.7 — Flash / Leveling

### Drain Zone
- Parts hang in ambient air (or heated tunnel) to allow drainage and initial solvent evaporation.
- **Plastisol:** No solvent, so flash is just drainage/drip control.
- **Solution dip:** Solvent flash 5-15 min before bake to prevent solvent entrapment and blistering.

### Leveling Challenges
- Thick dip coatings are prone to drips, runs, and uneven thickness (thick at bottom, thin at top).
- **Rotation:** Some systems rotate parts during drain/gel phase to equalize thickness.
- **Viscosity adjustment:** Higher viscosity = less drainage = more uniform but thicker. Trade-off.

---

## 4.8 — Cure Stage

### Cure Parameters by Coating Type

| Coating | Cure Temperature | Cure Time | Mechanism |
|---------|-----------------|-----------|-----------|
| PVC Plastisol | 350-400 deg F (177-204 deg C) | 10-20 min at metal temp | Fusion (PVC particles solvate into plasticizer, forming continuous gel) |
| Nylon 11/12 | Melt on hot part, cool to solidify | Cooling time varies | Thermoplastic solidification |
| Polyethylene | Melt on hot part, cool to solidify | Cooling time varies | Thermoplastic solidification |
| Epoxy solution dip | 300-400 deg F (149-204 deg C) | 15-30 min | Thermoset cross-linking |
| Rubber (latex dip) | 250-350 deg F (121-177 deg C) | 15-30 min | Vulcanization (sulfur cross-linking) |
| Silicone | 300-400 deg F (149-204 deg C) | 10-30 min | Condensation or addition cure |

### PVC Plastisol Fusion
- **Gel point:** ~250 deg F (121 deg C) — PVC particles begin to absorb plasticizer, material gels.
- **Fusion point:** ~350 deg F (177 deg C) — complete solvation, continuous homogeneous film. Below fusion = weak, porous film.
- **Over-fusion:** Above 420 deg F (216 deg C) = thermal degradation, HCl gas evolution, discoloration. PVC decomposition releases toxic hydrogen chloride.

---

## 4.9 — Inspection & Handling

### Film Thickness
- Magnetic/eddy current gauge per ASTM D7091 for thin films.
- For thick coatings (> 10 mils): micrometer measurement (cut cross-section) or ultrasonic thickness gauge.

### Adhesion
- ASTM D3359 for thin films.
- For thick dip coatings: manual peel test, knife adhesion test (score and attempt to peel by hand).

### Flexibility
- **ASTM D522 Mandrel Bend** for thin films.
- For thick plastisol/thermoplastic: cold-temperature flexibility test (bend at -20 deg F / -29 deg C — critical for dishwasher racks and outdoor applications).

### Hardness
- **Shore A durometer** for soft/flexible coatings (plastisol, rubber).
- **Shore D durometer** for hard thermoplastics (nylon).
- ASTM D2240.

### Defects Specific to Dip Coating
- Drip marks / curtaining (thick edge at bottom)
- Blistering (trapped moisture or air)
- Pinholes (outgassing from substrate)
- Thin spots (air pockets where coating did not wet)
- Bridging (coating spans across holes or slots instead of coating the edges)

---

# CLUSTER 5: FLOW COATING

## 5.1 — Process Flow (Summary Poster)

### Process Sequence
1. Surface preparation
2. Cleaning
3. Rack / hang parts
4. Flow coating application (liquid coating poured/flowed over the part)
5. Drain / drip
6. Cure (air dry, force dry, or bake)
7. Inspect

### What Is Flow Coating?
- Flow coating applies liquid paint by **pouring or flowing** it over the workpiece by gravity. Excess coating drains off and is collected for recirculation.
- Used for large, flat, or irregularly shaped parts where spray booths would be impractical or wasteful.
- Common in: architectural panels, large structural steel fabrications, transformer tanks, agricultural equipment, cabinet and furniture interiors.

### Advantages
- **High transfer efficiency** (90-95%) — nearly all coating that doesn't adhere drains back to the reservoir.
- **Simple equipment** — pump, nozzles/weirs, drain pan, recirculation tank. No compressed air, no spray booth.
- **Coverage of interior surfaces** — coating flows into recesses, channels, and interior cavities.

### Limitations
- Limited film thickness control compared to spray.
- Prone to runs, sags, and uneven thickness on complex geometries.
- Not suitable for high-appearance/high-gloss topcoats (automotive, aerospace).
- Limited to low-to-medium viscosity coatings.

---

## 5.2 — Surface Preparation

- Same as liquid spray painting (Cluster 2.2).
- Typically used on steel — SSPC-SP6 or SP10 blast, or mechanical prep.
- For flow-coated primers on structural steel: minimum SSPC-SP6 with 1.5-3.0 mil profile.

---

## 5.3 — Cleaning

- Solvent wipe or alkaline wash.
- For continuous flow coat lines: multi-stage spray washer (same as powder coat or liquid spray pretreatment).
- Cleanliness standard: water break free.

---

## 5.4 — Rinse / Dry

- Standard rinse and dry protocols.
- Parts must be completely dry — trapped water in recesses will blister under the coating.

---

## 5.5 — Pretreatment

- Iron phosphate for general industrial.
- Zinc phosphate for high-performance.
- Same specifications as liquid spray painting (Cluster 2.5).

---

## 5.6 — Application Stage

### Flow Coating Methods

| Method | Description | Typical Use |
|--------|-------------|-------------|
| Curtain flow | Coating poured from a weir or slot die in a continuous curtain; part passes through the curtain on a conveyor | Flat panels, coil-like applications (not true coil coating) |
| Flood/flow | Nozzles flood coating over the part from above; coating flows down by gravity | Large 3D parts (tanks, enclosures, frames) |
| Dip-drain (hybrid) | Part immersed briefly, withdrawn, and excess drains | Overlap with dip coating (Cluster 4) |

### Application Parameters

| Parameter | Typical Range |
|-----------|--------------|
| Coating viscosity | 20-40 sec (Zahn #2 cup) for curtain; 15-30 sec for flood |
| Flow rate | 1-5 gal/min per nozzle |
| Drain time | 30-120 sec |
| DFT per coat | 0.5-2.0 mils (primer); 1.0-3.0 mils (topcoat) |
| Recirculation tank volume | 50-500 gal depending on line size |
| Film build uniformity | +/- 30-50% (less precise than spray) |

### Coating Recirculation
- Excess coating drains into a collection pan and returns to the reservoir.
- **Solvent replenishment:** Recirculated coating gradually increases in viscosity due to solvent evaporation. Regular viscosity checks and solvent additions are required.
- **Contamination control:** Recirculated coating accumulates dirt, substrate particles, and cured skin. Strain/filter continuously (60-100 mesh screen minimum).
- **Pot life (2K systems):** Flow coating with 2K coatings requires careful pot life management — the entire recirculation volume has a limited working life.

---

## 5.7 — Flash / Leveling

### Drain Zone
- Gravity drainage is the leveling mechanism.
- Parts are hung at specific angles to direct drainage and minimize thick buildup at the bottom.
- **Rotation or tumbling** can be used for small parts.
- Flash: 5-15 min ambient, or 5-10 min in heated tunnel (120-160 deg F) before oven.

---

## 5.8 — Cure Stage

### Same as Liquid Spray Painting
- Air dry, force dry, or bake depending on coating chemistry.
- See Cluster 2.8 cure table.
- **Most flow-coated products** are alkyd or modified alkyd (air dry or force dry) or baking enamel (250-350 deg F).

---

## 5.9 — Inspection & Handling

### Film Thickness
- ASTM D7091 on accessible surfaces.
- Due to flow-coat thickness variability, measure at multiple locations (top, middle, bottom of part).
- Specify minimum DFT rather than target, with maximum for sag/run areas.

### Defects Specific to Flow Coating
- **Curtaining / sagging:** Excessive coating buildup at bottom edges. Control by viscosity, drain time, and part orientation.
- **Holidays / missed areas:** Areas shielded from flow — inner corners or horizontal surfaces facing up.
- **Skinning in recirculation tank:** Surface film forms on stagnant coating. Keep tank agitated or covered.

---

# CLUSTER 6: COIL COATING

## 6.1 — Process Flow (Summary Poster)

### Process Sequence (Continuous Coil Line)
1. Uncoiler (payoff reel)
2. Accumulator (allows continuous operation during coil changes)
3. Alkaline cleaning (spray + brush scrub)
4. Rinse
5. Chemical pretreatment (chromate or non-chrome conversion coating)
6. Rinse
7. Dry / preheat
8. **Prime coat application** (reverse roll coater — bottom side) + top prime (roll coater — top side)
9. Prime oven (PMT 400-450 deg F, 20-40 sec)
10. Quench (water)
11. **Finish coat application** (reverse roll coater)
12. Finish oven (PMT 430-480 deg F, 30-60 sec)
13. Quench (water)
14. Recoiler (takeup reel)

### What Is Coil Coating?
- Coil coating (also called "pre-painting" or "prepaint") is a continuous, high-speed process for applying organic coatings to flat metal coil (steel or aluminum) before it is fabricated into finished products.
- **Line speeds:** 200-700 ft/min (60-210 m/min). A coil coating line can coat 50,000-100,000+ sq ft per hour.
- **Products made from pre-painted coil:** Building panels (roofing, siding, wall panels), appliance housings (refrigerators, washers, HVAC), gutters and downspouts, garage doors, beverage cans (exterior decoration), automotive trim.
- The coating is applied **before** fabrication (stamping, roll-forming, bending) — this requires excellent adhesion and flexibility to survive forming without cracking.

---

## 6.2 — Surface Preparation

### Coil Surface Condition
- Hot-dip galvanized (HDG) steel: Zinc surface, mill oil present.
- Galvalume (55% Al-Zn): Similar to HDG but different chemistry.
- Cold-rolled steel (CRS): Bare steel, drawing oil present.
- Aluminum: 3000-series or 5000-series alloy coil, mill oil present.

### In-Line Cleaning
- **Alkaline spray + brush scrub:** Heated alkaline solution (130-150 deg F) sprayed onto the coil surface while rotating nylon brush scrubbers physically remove oil and debris.
- **Cleaning is done at line speed** — the entire cleaning section is only 20-40 ft long, so contact time is seconds, not minutes. High pressure and mechanical action compensate for short contact time.

---

## 6.3 — Cleaning

### Coil Cleaning Details

| Parameter | Typical Range |
|-----------|--------------|
| Cleaner type | Low-foam alkaline, pH 10-12 |
| Concentration | 1-3% by volume |
| Temperature | 130-160 deg F (54-71 deg C) |
| Spray pressure | 15-30 psi |
| Brush scrubbers | 2-4 stages, nylon bristle, counter-rotating |
| Rinse | DI water spray, 2 stages |
| Cleanliness verification | Water break test on strip samples; surface carbon analysis (< 2 mg/m2) |

- **Oil removal target:** < 5 mg/m2 residual oil. Coil coating is a very thin film system (0.2-1.0 mil primer), so even trace oil causes adhesion failure.

---

## 6.4 — Rinse / Dry

### Rinse
- DI water spray rinse, 2 stages, counterflow.
- Conductivity target: < 30 microsiemens/cm final rinse.

### Dry / Preheat
- **IR pre-heater or convection dryer** immediately after rinse.
- Dries the strip and preheats to ~100-120 deg F to improve conversion coating reactivity.
- Must be completely dry before conversion coating — water droplets cause uneven treatment.

---

## 6.5 — Pretreatment

### Conversion Coating for Coil

| Type | Chemistry | Application Method | Coating Weight | Notes |
|------|-----------|-------------------|---------------|-------|
| Chromate rinse (CrVI) | Chromic acid + silica sol | Roll apply or spray | 10-30 mg/ft2 Cr | Traditional; best performance; declining due to RoHS/REACH |
| Chrome-free (Ti/Zr) | Fluorotitanic/fluorozirconic acid | Roll apply or spray | 5-15 mg/ft2 | Growing standard; REACH compliant |
| Dry-in-place (no rinse) | Proprietary chrome-free polymers | Roll apply | Very thin (< 5 mg/ft2 metal) | Simplest; no rinse water waste |
| Phosphate (iron or zinc) | Phosphoric acid based | Spray | 25-75 mg/ft2 (iron) | Less common for coil; used for heavy-gauge |

- **Chrome-free conversion is now the industry standard** for new coil coating lines. European REACH regulation has accelerated the transition. Legacy lines may still run hexavalent chromate where permitted.

---

## 6.6 — Application Stage

### Reverse Roll Coater (Primary Method)

The reverse roll coater is the heart of a coil coating line:

1. **Pickup roll** rotates in a coating reservoir, picking up a metered film of liquid coating.
2. **Applicator roll** receives coating from the pickup roll and transfers it to the coil strip.
3. The applicator roll rotates **in the opposite direction** to the strip travel (reverse roll application).
4. This shearing action produces an extremely smooth, uniform film.

### Roll Coater Parameters

| Parameter | Primer Coat | Finish (Topcoat) |
|-----------|-------------|-------------------|
| Target DFT | 0.15-0.30 mil (4-8 microns) | 0.60-1.0 mil (15-25 microns) |
| Wet film thickness | 0.3-0.6 mil | 1.0-2.0 mil |
| Roll speed ratio (applicator/strip) | 1.05-1.25:1 | 1.05-1.25:1 |
| Roll pressure (nip) | 20-100 pli (pounds per linear inch) | 20-100 pli |
| Coating viscosity | 40-80 sec (Zahn #2) | 30-60 sec (Zahn #2) |
| Line speed | 200-700 ft/min | 200-700 ft/min |

### Coating Types for Coil

| Chemistry | Typical DFT | Flexibility | Weathering | Use |
|-----------|-------------|-------------|-----------|-----|
| Polyester | 0.7-1.0 mil | Good (T-bend 0-2T) | Good (15-25 yr) | Building panels, general |
| Silicone-modified polyester (SMP) | 0.7-1.0 mil | Good | Very good (25-30 yr) | Premium architectural |
| Polyvinylidene fluoride (PVDF/Kynar 500) | 0.8-1.2 mil | Very good | Excellent (30-40 yr) | Premium architectural, color retention |
| Polyurethane | 0.7-1.0 mil | Excellent | Very good | Appliance, automotive trim |
| Epoxy primer (back coat) | 0.15-0.25 mil | Good | Poor (interior only) | Back-side protection, adhesion |
| Plastisol (PVC) | 4-8 mils | Excellent | Moderate | Heavy-gauge roofing, rain goods |

### T-Bend Flexibility Test
- **ASTM D4145:** Coated coil is bent 180 degrees over itself. "0T" = bent flat on itself with no mandrel (tightest bend). "1T" = one thickness of metal in the bend. "2T" = two thicknesses.
- The result is reported as the smallest T-bend with no cracking. Premium coatings achieve 0T to 1T.

---

## 6.7 — Flash / Leveling

### Not Applicable in Conventional Sense
- Coil coating has no flash time between application and cure — the coated strip travels directly from the roll coater into the oven at line speed.
- **Leveling occurs on the roll coater itself** — the reverse roll action produces a smooth film. Additional leveling happens in the first few seconds of oven entry as the coating heats and viscosity drops.
- **Poster angle:** Focus on the roll coater mechanics as the "leveling" step. The roll speed ratio, nip pressure, and coating viscosity together determine the film smoothness and uniformity.

---

## 6.8 — Cure Stage

### Coil Coating Oven Parameters

| Parameter | Primer Oven | Finish Oven |
|-----------|-------------|-------------|
| Peak Metal Temperature (PMT) | 400-450 deg F (204-232 deg C) | 430-480 deg F (221-249 deg C) |
| Oven length | 80-150 ft | 100-200 ft |
| Residence time in oven | 15-40 sec | 20-60 sec |
| Oven type | Convection (gas-fired) | Convection (gas-fired) |
| Afterburner | Thermal or catalytic oxidizer on exhaust | Same |

### Critical Points
- **PMT is the specification parameter** — always defined by peak metal temperature, not oven air temperature.
- **Short cure times:** Because the strip is thin (0.015-0.060 inch gauge), it heats rapidly. The entire cure cycle is 20-60 seconds — compared to 10-20 minutes for powder coating and 20-30 minutes for e-coat.
- **PMT measurement:** In-line non-contact IR pyrometer continuously monitors PMT. Thermocouple data loggers (attached to test strips) are used for periodic oven profiling.
- **Water quench:** Immediately after the oven, the strip passes through a water quench to rapidly cool. This locks in film properties and prevents overcure. Quench water temperature: ambient to 100 deg F.

### VOC/Emissions
- Coil coating ovens generate significant solvent emissions (the coatings are typically solvent-borne, 50-70% volume solids).
- **EPA 40 CFR Part 63, Subpart SSSS:** NESHAP for Surface Coating of Metal Coil.
- Afterburners (thermal oxidizers at 1,400-1,600 deg F or catalytic oxidizers at 600-800 deg F) achieve > 95% VOC destruction.
- **Enclosure efficiency:** The oven itself acts as an emission enclosure. Total system VOC capture and destruction efficiency must meet > 95% (or site-specific permit limits).

---

## 6.9 — Inspection & Handling

### In-Line Quality Control
Coil coating lines run at high speed — quality control must be rapid and often automated.

| Test | Method | Frequency | Target |
|------|--------|-----------|--------|
| DFT | In-line beta-backscatter or X-ray fluorescence | Continuous | Per spec (0.7-1.0 mil typical) |
| Gloss | In-line glossmeter | Continuous or per coil | 60 deg gloss per ASTM D523 |
| Color | In-line spectrophotometer or per-coil handheld | Per coil minimum | Delta E < 1.0 (CIE L*a*b*) |
| T-bend flexibility | ASTM D4145 | Per coil | 0T to 2T (spec dependent) |
| Pencil hardness | ASTM D3363 | Per coil | F to 2H typical |
| Adhesion | ASTM D3359 cross-hatch | Per coil | 5B |
| MEK double rub | ASTM D4752 | Per coil | 100+ double rubs (indicates full cure) |
| Reverse impact | ASTM D2794 | Per coil | 40-80 in-lb (spec dependent) |
| Salt spray (panel test) | ASTM B117 | Per lot / qualification | 500-3,000 hr depending on system |
| Humidity resistance | ASTM D2247 | Per lot | 1,000-2,000 hr |
| UV accelerated weathering | ASTM G154 (QUV) or ASTM G155 (xenon arc) | Qualification | 2,000-10,000 hr to spec'd retention |

### Handling
- Coated coil is rewound with paper interleaving to prevent scratching.
- Storage: Indoor, dry, temperature-controlled. Avoid condensation (coil sweating).
- Forming: Fabricator must use forming tools designed for pre-painted coil (polished rolls, Teflon-coated dies) to avoid scratching the coating.

---

# CLUSTER 7: INDUSTRIAL PRIMING SYSTEMS

## 7.1 — Process Flow (Summary Poster)

### What This Cluster Covers
- **Zinc-rich primers** (inorganic and organic) — galvanic protection of steel
- **Epoxy primers** — barrier protection, chemical resistance
- **Aerospace primers** — chromated epoxy, non-chrome epoxy, high-performance systems
- These are all **primer-only** systems — they are typically topcoated with an intermediate and/or finish coat.

### Zinc-Rich Primer: The Key Concept
- A zinc-rich primer provides **cathodic (galvanic) protection** to steel — the same principle as hot-dip galvanizing, but applied as a paint film.
- The zinc particles in the dried film are in electrical contact with each other and with the steel substrate. When the coating is damaged (scratched, cut), the zinc corrodes preferentially (sacrificially) to protect the exposed steel.
- **Minimum zinc loading:** For effective galvanic protection, the dry film must contain a high percentage of zinc dust:
  - Inorganic zinc (IOZ): 75-85% zinc by weight in the dry film (per SSPC-PS 12.01)
  - Organic zinc (OZ): 65-80% zinc by weight in the dry film

---

## 7.2 — Surface Preparation

### For Zinc-Rich Primers (Most Demanding)
- **SSPC-SP10 Near-White Blast** minimum. Many specs require **SSPC-SP5 White Metal Blast**.
- Profile: 1.5-3.0 mils (38-76 microns) per ASTM D4417 Method C (replica tape).
- **Surface preparation is the single most critical factor** for zinc-rich primer performance. The zinc particles must be in direct metallic contact with the steel for galvanic protection to work. Any residual mill scale, rust, or contamination breaks the electrical circuit.
- **Soluble salt limits:** Chloride < 3 micrograms/cm2, sulfate < 10 micrograms/cm2 per SSPC-SP12 / ISO 8502. Conductometric testing per SSPC Guide 15.

### For Epoxy Primers (General Industrial)
- SSPC-SP6 Commercial Blast minimum for new steel.
- SSPC-SP3 Power Tool Cleaning for maintenance/repair.
- Profile: 1.5-2.5 mils.

### For Aerospace Primers
- Aluminum: Chromate conversion (MIL-DTL-5541) or anodize (MIL-PRF-8625 Type I chromic acid anodize or Type IIB thin sulfuric anodize).
- Steel: Cadmium plate (declining) or zinc-nickel plate + chromate conversion.
- Surface cleanliness to MIL-PRF-680 (solvent clean) + alkaline clean + conversion coating.

---

## 7.3 — Cleaning

- Solvent cleaning per SSPC-SP1 before blasting.
- After blast: compressed air blow-down (oil-free air per ASTM D4285 blotter test) or vacuum.
- No chemical cleaning after blast — direct to prime.

---

## 7.4 — Rinse / Dry

- Not applicable in the conventional sense — zinc-rich and epoxy primers are applied directly to blast-cleaned dry steel.
- For aerospace: rinse and dry after conversion coating per process spec.
- **Blast-to-prime time:** Apply primer within 4-8 hours of blasting (or before flash rust appears, whichever is shorter). In humid environments (> 80% RH), this window may be as short as 1-2 hours.

---

## 7.5 — Pretreatment

### For Zinc-Rich Primers on Steel
- **No chemical pretreatment** — the blasted steel profile IS the pretreatment. Zinc-rich primer is applied directly to the bare, profiled steel surface.
- Adding a phosphate conversion coating under a zinc-rich primer is counterproductive — it insulates the zinc from the steel and defeats the galvanic mechanism.

### For Epoxy Primers on Steel
- Optional iron phosphate or wash primer for additional adhesion.
- Many industrial epoxy primers perform adequately on blast-cleaned steel without conversion coating.

### For Aerospace Primers on Aluminum
- Chromate conversion coating (MIL-DTL-5541) or anodize (MIL-PRF-8625) is mandatory — this is the pretreatment.
- Non-chrome alternatives: Ti/Zr sol-gel (Boegel AC-131, approved on some Boeing specs), trivalent chromium process (TCP per MIL-DTL-5541 Type II).

---

## 7.6 — Application Stage

### Zinc-Rich Primer Application

| Parameter | Inorganic Zinc (IOZ) | Organic Zinc (OZ) |
|-----------|----------------------|--------------------|
| Binder | Ethyl silicate (solvent-borne) or alkali silicate (waterborne) | Epoxy, polyurethane, or moisture-cure urethane |
| Zinc content (dry film) | 75-85% by weight | 65-80% by weight |
| ASTM zinc dust spec | ASTM D520 Type II (fine spherical) or D521 | ASTM D520 Type II |
| Target DFT | 2.5-4.0 mils (64-102 microns) | 2.0-3.5 mils (51-89 microns) |
| Number of coats | 1-2 | 1-2 |
| Application method | Airless spray (most common), air spray, brush (touch-up only) | Airless spray, air spray, brush, roll |
| Mixing | Continuous agitation essential — zinc settles rapidly | Continuous agitation essential |
| Pot life | 4-8 hours (ethyl silicate + zinc slurry) | 15 min - 8 hours (2K epoxy-zinc); unlimited (1K moisture-cure) |
| Spray pressure (airless) | 2,500-3,500 psi | 2,000-3,000 psi |
| Tip size | 0.017-0.023 inch | 0.017-0.021 inch |

### Epoxy Primer Application

| Parameter | Range |
|-----------|-------|
| Target DFT | 1.0-3.0 mils (per coat) |
| Coats | 1-2 |
| Pot life (2K) | 30 min - 8 hours |
| Application | Airless, air spray, HVLP, brush, roll |
| Volume solids | 50-80% (high-solids epoxy) |

### Aerospace Primer Application

| Primer Type | DFT | Key Spec |
|-------------|-----|----------|
| Chromated epoxy (BMS 10-11, MIL-PRF-23377) | 0.6-1.0 mil | Contains strontium chromate pigment for corrosion inhibition |
| Non-chrome epoxy (BMS 10-72, MIL-PRF-85582) | 0.6-1.0 mil | Rare earth or other non-chrome inhibitors |
| Epoxy primer for composites | 0.3-0.8 mil | Low-density, flexible formulation |
| Wash primer (MIL-DTL-15328) | 0.3-0.5 mil | Vinyl butyral + phosphoric acid; for spot repair |

---

## 7.7 — Flash / Leveling

### Inorganic Zinc Primer Curing Behavior
- IOZ primers cure by a unique mechanism: hydrolysis and condensation of ethyl silicate binder in the presence of atmospheric moisture.
- **Moisture is required for cure** — in dry environments (< 30% RH), IOZ primers may not cure properly. Mist coating with water accelerates cure.
- The film does not "level" like a liquid paint — the high zinc loading produces a rough, matte, porous film by design.
- **Mud cracking:** If applied too thick (> 5 mils), IOZ primer develops cracks resembling dried mud. This is a critical defect — it means the film was applied too thick for the shrinkage forces during cure.

### Organic Zinc Primer
- Cures by the binder mechanism (epoxy cure, moisture-cure PU, etc.).
- Better leveling than IOZ but still rough/matte due to high zinc loading.

### Flash Time
- IOZ: 30-60 min between coats at 50% RH; allow full cure (typically 24 hr) before topcoating with epoxy intermediate.
- OZ: Per binder type (epoxy pot life, moisture-cure overnight).

---

## 7.8 — Cure Stage

### Cure Parameters

| Primer Type | Cure Mechanism | Conditions | Full Cure Time |
|-------------|---------------|------------|----------------|
| Inorganic zinc (ethyl silicate) | Hydrolysis + condensation of silicate binder | Ambient temp, 40-80% RH | 24-72 hr (moisture-dependent) |
| Inorganic zinc (alkali silicate, waterborne) | Water evaporation + silicate hardening | Ambient temp | 24-48 hr |
| Organic zinc (2K epoxy) | Amine-epoxy cross-linking | Ambient to 120 deg F | 7-14 days full cure; recoat 4-24 hr |
| Organic zinc (moisture-cure PU) | Isocyanate + atmospheric moisture | Ambient, > 30% RH | 24-72 hr |
| Epoxy primer (2K) | Amine-epoxy cross-linking | Ambient to 120 deg F | 7-14 days full cure; recoat 4-24 hr |
| Chromated epoxy (aerospace) | Amine cross-linking (often heat-accelerated) | 77 deg F air dry or 250 deg F force cure, 1 hr | 7 days air dry; 1 hr force cure |

### Topcoating Over Zinc-Rich Primer
- **Mist coat / tie coat:** Before applying a full topcoat over IOZ primer, apply a thin "mist coat" of the intermediate (usually epoxy) to seal the porous zinc surface. If a full-thickness coat is applied directly, solvent from the topcoat can penetrate the porous IOZ and cause bubbling/pinholing (solvent entrapment).
- **Topcoat recoat window for IOZ:** Wait minimum 24 hours (full cure) before topcoating. If more than 30 days have elapsed, the zinc surface may develop white zinc corrosion products — these must be sweep-blasted (SSPC-SP7) before topcoating.

---

## 7.9 — Inspection & Handling

### Film Thickness
- ASTM D7091 magnetic gauge. For IOZ on steel, use a gauge calibrated for rough surfaces (some gauges read high on rough IOZ surfaces).
- DFT range enforcement is critical — too thin = insufficient galvanic protection; too thick = mud cracking.

### Zinc Loading Verification
- **SSPC-PA 2:** Procedure for Determining Conformance to Dry Coating Thickness Requirements.
- Verify zinc content by manufacturer COA or in rare cases by XRF analysis.

### Salt Spray Performance

| System | B117 Hours (Typical) |
|--------|---------------------|
| IOZ primer alone (3 mil DFT) | 1,500-3,000+ hr |
| OZ primer alone (3 mil DFT) | 500-1,500 hr |
| IOZ + epoxy intermediate + polyurethane topcoat (6-10 mil total) | 5,000-10,000+ hr |
| Epoxy primer alone (3 mil DFT) | 500-1,500 hr |

### Key Standards for This Cluster
- **SSPC-PS 12.01:** Guide for Selecting Zinc-Rich Primers (IOZ and OZ)
- **ASTM D520:** Specification for Zinc Dust (Type I irregular, Type II spherical)
- **ASTM D521:** Chemical Analysis of Zinc Dust (Metallic Zinc Content)
- **SSPC-Paint 20:** Zinc-Rich Primers (Type I inorganic, Type II organic)
- **ISO 12944:** Corrosion protection of steel structures by protective paint systems (Corrosivity categories C1-C5, CX)
- **MIL-PRF-23377:** Primer, Epoxy Chemical and Solvent Resistant (aerospace)
- **MIL-PRF-85582:** Primer, Non-Chromate Epoxy (aerospace)

---

# CLUSTER 8: PROTECTIVE COATINGS (EPOXY / URETHANE)

## 8.1 — Process Flow (Summary Poster)

### What This Cluster Covers
- High-build protective coating systems for severe service:
  - Marine (ship hulls, offshore platforms, splash zone)
  - Tank lining (chemical storage, water tanks, fuel tanks)
  - Concrete floor coatings (warehouse, manufacturing, food processing)
  - Pipeline coatings (external and internal)
  - Bridge and infrastructure
- These are typically **multi-coat systems** totaling 6-20+ mils DFT.

### Typical System Architecture

| Coat | Material | DFT | Purpose |
|------|----------|-----|---------|
| Primer | Zinc-rich (steel) or epoxy | 2-4 mils | Corrosion protection / adhesion |
| Intermediate / build coat | High-build epoxy | 4-8 mils per coat | Barrier protection, chemical resistance |
| Topcoat / finish | Aliphatic polyurethane | 2-3 mils | UV resistance, color, gloss retention, weathering |

### Why Two-Component (2K)?
- Epoxy and urethane protective coatings are **two-component reactive systems:**
  - **Epoxy:** Component A (epoxy resin, typically bisphenol A diglycidyl ether) + Component B (amine or polyamide hardener).
  - **Urethane:** Component A (acrylic or polyester polyol resin) + Component B (aliphatic isocyanate hardener, typically HDI trimer or IPDI).
- The two components are mixed immediately before application. Cross-linking begins on mixing, producing a chemically resistant thermoset film that cannot be achieved with single-component coatings.

---

## 8.2 — Surface Preparation

### Steel
- **SSPC-SP10 Near-White Blast** for new construction.
- **SSPC-SP5 White Metal Blast** for immersion service (tank lining, marine below-waterline).
- Profile: 2.0-4.0 mils (51-102 microns) for high-build systems.
- Soluble salt testing: Chloride < 3 ug/cm2, sulfate < 10 ug/cm2 (SSPC Guide 15).

### Concrete
- **ICRI CSP 2-5 (Concrete Surface Profile):** Ranges from light shot blast to heavy scarification.
- Moisture testing: Calcium chloride test (ASTM F1869) < 3 lb/1,000 ft2/24 hr; or RH probe (ASTM F2170) < 75% RH.
- pH: Surface pH 7-10 (test with pH paper or phenolphthalein).
- **No curing compounds or sealers** on the concrete surface — these prevent adhesion. If present, must be removed by grinding or blasting.

### Previously Coated Surfaces (Maintenance)
- SSPC-SP11 Power Tool Cleaning to Bare Metal for spot repairs.
- Feather edges of existing coating with sander.
- Adhesion test existing coating (D3359) — if < 3B, remove entirely.

---

## 8.3 — Cleaning

### Steel
- SSPC-SP1 Solvent Cleaning before abrasive blasting.
- After blast: compressed air blow-down or vacuum. Verify oil-free air (ASTM D4285 blotter test).
- **Salt removal:** If chloride/sulfate levels are elevated (coastal or marine environments), water wash or pressurized fresh water rinse before blasting. Test after blasting with Bresle patch (ISO 8502-6) or conductometric method.

### Concrete
- Degrease with alkaline cleaner or solvent.
- Power wash to remove laitance and surface contaminants.
- Acid etch (10-15% muriatic acid solution) if mechanical prep is not available — rinse thoroughly and neutralize.

---

## 8.4 — Rinse / Dry

### Steel
- If water washing was used for salt removal, allow full drying before blasting.
- After blast: no rinse. Apply primer before flash rust.
- Dew point monitoring: Surface temperature must be minimum 5 deg F (3 deg C) above dew point at all times during application and cure. Measured by sling psychrometer + surface thermometer per ASTM E337.

### Concrete
- After water wash or acid etch, allow minimum 24 hours drying.
- Moisture testing before coating application (see 8.2).

---

## 8.5 — Pretreatment

### Steel
- Zinc-rich primer serves as both pretreatment and primer for the most demanding applications (see Cluster 7).
- For less demanding: epoxy primer directly on blast-cleaned steel.
- No conversion coating required — the blast profile provides mechanical adhesion.

### Concrete
- **No chemical conversion coating.** The mechanical profile from blast or grind is the adhesion mechanism.
- Some manufacturers offer epoxy penetrating sealers as "primers" for porous concrete.

---

## 8.6 — Application Stage

### Epoxy Application Parameters

| Parameter | Standard Build | High-Build | Tank Lining |
|-----------|---------------|-----------|-------------|
| Target DFT per coat (mils) | 3-5 | 5-10 | 4-8 |
| Total system DFT (mils) | 6-12 | 10-20 | 12-20+ |
| Number of coats | 2-3 | 2-3 | 3-4 |
| Mix ratio (A:B by volume) | 1:1 to 4:1 (formulation dependent) | Same | Same |
| Pot life at 77 deg F | 30 min - 4 hours | 20 min - 2 hours | 30 min - 2 hours |
| Induction time | 15-30 min (polyamide-cured); none (amine-adduct) | Varies | Per TDS |
| Application method | Airless spray (primary), brush, roll | Airless spray | Airless spray |
| Spray pressure (airless) | 2,000-3,000 psi | 2,500-3,500 psi | 2,500-3,500 psi |
| Tip size | 0.017-0.025 inch | 0.021-0.031 inch | 0.019-0.025 inch |
| Volume solids | 60-80% (standard); 80-100% (solventless) | 85-100% | 90-100% (solventless for tank lining) |

### Polyurethane Topcoat Application

| Parameter | Range |
|-----------|-------|
| Target DFT per coat | 2.0-3.0 mils |
| Coats | 1-2 |
| Mix ratio (A:B) | Varies by product (2:1 to 5:1 typical) |
| Pot life at 77 deg F | 1-4 hours (aliphatic); 30 min - 2 hours (aromatic) |
| Application | Airless, HVLP, conventional air spray |
| Volume solids | 50-75% |

### Aliphatic vs. Aromatic Isocyanate
- **Aliphatic (HDI, IPDI):** UV-stable, non-yellowing, excellent gloss retention. Used for exterior topcoats. More expensive. Slower cure.
- **Aromatic (MDI, TDI):** Yellow/chalk on UV exposure. Used for interior or under-topcoat applications. Less expensive. Faster cure.

### Solventless / 100% Solids Epoxy
- Zero VOC. Used for tank lining and concrete floor coatings.
- Higher viscosity — requires heated spray equipment (plural-component proportioning systems with heated hoses).
- **Application temperature:** Material heated to 100-140 deg F to reduce viscosity for spray application.
- **Pot life is very short** (minutes, not hours) — plural-component systems mix at the spray gun or in a static mixer immediately before application.

---

## 8.7 — Flash / Leveling

### Recoat Windows (Critical for Multi-Coat Systems)

| System | Minimum Recoat (77 deg F) | Maximum Recoat (77 deg F) | Exceeding Max Recoat |
|--------|--------------------------|---------------------------|---------------------|
| Epoxy over epoxy | 6-16 hours | 3-7 days | Scuff sand 80-120 grit |
| Urethane over epoxy | 6-16 hours | 3-7 days | Scuff sand 180-320 grit |
| Epoxy over IOZ | 24 hours | 30 days | Sweep blast (SSPC-SP7) |
| Urethane over urethane | 4-12 hours | 1-3 days | Scuff sand 320 grit |

- **Amine blush (epoxy):** In cool/humid conditions (< 50 deg F, > 80% RH), amine hardener reacts with CO2 and moisture at the film surface, forming a waxy amine carbamate ("blush"). This must be removed by water wash or solvent wipe before recoating — otherwise it causes intercoat adhesion failure.

### Flash Time Between Coats
- 4-24 hours between coats for ambient-cure epoxy (temperature and humidity dependent).
- 2-8 hours between urethane coats.
- **Stripe coating:** Before each full coat, apply a stripe coat (brush-applied) to all edges, welds, bolts, and hard-to-reach areas to ensure adequate DFT. Stripe coat first, flash, then full spray coat.

---

## 8.8 — Cure Stage

### Cure Parameters

| System | Ambient Cure | Force Cure | Full Chemical Cure |
|--------|-------------|-----------|-------------------|
| Amine-cured epoxy | 50-100 deg F (10-38 deg C), > 40% RH | 140-180 deg F, 1-4 hours | 7-14 days ambient |
| Polyamide-cured epoxy | 50-100 deg F, > 40% RH | 140-180 deg F, 1-4 hours | 7-14 days ambient |
| Aliphatic urethane | 50-100 deg F | 140-160 deg F, 1-2 hours | 5-7 days ambient |
| Solventless epoxy (tank lining) | 60-100 deg F | 150-200 deg F, 2-4 hours | 7-14 days ambient; 4-7 days for immersion service |

### Immersion Service Cure
- Tank linings and immersion coatings require **full cure before filling with chemical.**
- Minimum 7 days ambient cure at 77 deg F, or accelerated by force cure.
- Solventless epoxy for potable water tanks: must meet **NSF/ANSI 61** (Drinking Water System Components — Health Effects).
- Cure verification: solvent rub test (MEK or MIBK, 50-100 double rubs), Shore D hardness (> 75D for most tank lining epoxies).

### Temperature Effects on Cure
- **Below 50 deg F (10 deg C):** Most amine-cured epoxies cure extremely slowly or not at all. Use cycloaliphatic amine hardeners designed for low-temp cure (some cure down to 35 deg F / 2 deg C).
- **Above 90 deg F (32 deg C):** Pot life is dramatically shortened. Reduce batch sizes.
- **Rule of thumb:** Pot life halves for every 18 deg F (10 deg C) increase in temperature.

---

## 8.9 — Inspection & Handling

### Film Thickness
- **SSPC-PA 2:** Procedure for Determining Conformance to DFT Requirements. Defines spot measurement, area measurement, and statistical acceptance criteria.
- Measure with ASTM D7091 gauge on steel; ASTM D4138 Tooke gauge for multi-coat system individual layer measurement.
- **High-build epoxy:** Typical tolerance +/- 20% from target DFT.

### Holiday Detection (Pinhole/Void Detection)
- **Low-voltage wet sponge (ASTM D5162):** 67.5 V DC, wet sponge electrode passed over the coating. Beeps when a holiday (pinhole) is found. For coatings < 20 mils.
- **High-voltage spark test (NACE SP0188 / ASTM D4787):** Voltage calculated at 100 V per mil of DFT (for coatings > 20 mils). Arc/spark indicates a holiday. Critical for tank lining and pipeline coatings.

### Adhesion
- **ASTM D4541 Pull-Off Adhesion (Elcometer):** Glue a dolly to the coating, pull with a hydraulic tester. Report in psi. Typical requirement: > 200 psi for industrial epoxy; > 300 psi for immersion.
- ASTM D3359 crosshatch for thin films.

### Salt Spray and Corrosion Testing

| System | B117 Hours (Typical) |
|--------|---------------------|
| Epoxy primer + epoxy intermediate (6-8 mils total) | 2,000-4,000 hr |
| IOZ + epoxy + urethane (10-14 mils total) | 5,000-10,000+ hr |
| Solventless epoxy tank lining (12-20 mils) | 5,000-10,000+ hr |
| High-build epoxy for concrete (10-15 mils) | N/A (not typically salt spray tested; chemical resistance tested instead) |

### Chemical Resistance Testing
- **ASTM D3912 / ASTM C868:** Immersion in specified chemicals at specified temperature for specified duration. Evaluate softening, blistering, disbondment, weight change.
- Novolac epoxy formulations provide highest chemical resistance (concentrated acids, solvents, caustics up to 200 deg F).
- Standard bisphenol A epoxy: Good general chemical resistance; limited to 150 deg F continuous immersion.
- **Amine-cured** > **polyamide-cured** for chemical resistance (polyamide is more flexible but less chemically resistant).

### Safety for 2K Systems

| Hazard | Details |
|--------|---------|
| Isocyanate exposure (urethane) | TLV-TWA: 0.005 ppm (HDI monomer); respiratory sensitizer; supplied-air respirator required for spray application |
| Epoxy resin (BPA diglycidyl ether) | Skin sensitizer; contact dermatitis; gloves mandatory |
| Amine hardeners | Skin/eye corrosive; vapor irritant; strong sensitizers |
| Solvent exposure | MEK, xylene, MAK — see PEL/TLV for each; LEL monitoring for confined space |
| Confined space (tank lining) | OSHA 29 CFR 1910.146; continuous air monitoring; supplied air; attendant required |

---

# CROSS-CLUSTER STANDARDS REFERENCE

## Film Properties Testing

| Standard | Test | Applicable Clusters |
|----------|------|---------------------|
| ASTM D7091 | DFT by magnetic/eddy current gauge | All |
| ASTM D4138 | DFT by Tooke gauge (destructive) | 2, 7, 8 (multi-coat) |
| ASTM D4414 | Wet film thickness gauge | 2, 5, 7, 8 |
| ASTM D3359 | Adhesion (crosshatch tape pull) | All |
| ASTM D4541 | Pull-off adhesion (dolly pull) | 7, 8 |
| ASTM D3363 | Pencil hardness | All |
| ASTM D2240 | Shore durometer hardness | 4 (soft coatings) |
| ASTM D522 | Mandrel bend flexibility | 1, 2, 4 |
| ASTM D2794 | Impact resistance | 1, 2, 6 |
| ASTM D4145 | T-bend flexibility (coil) | 6 |
| ASTM D4752 | MEK double rub (cure test) | 1, 3, 6, 8 |
| ASTM D523 | Gloss (60 deg) | 2, 6, 8 |
| ASTM D2244 | Color (Delta E) | 2, 6 |
| ASTM B117 | Salt spray (neutral fog) | All (corrosion test) |
| ASTM D1654 | Evaluation of painted specimens after salt spray | All |
| ASTM G154 | UV accelerated weathering (QUV fluorescent) | 2, 6, 7, 8 |
| ASTM G155 | UV weathering (xenon arc) | 2, 6 |
| ASTM D2247 | Humidity resistance | 6 |
| ASTM D5162 | Holiday detection (low voltage, wet sponge) | 8 |
| ASTM D4787 | Holiday detection (high voltage, spark) | 8 |

## Surface Preparation Standards

| Standard | Description |
|----------|------------|
| SSPC-SP1 | Solvent cleaning |
| SSPC-SP2 | Hand tool cleaning |
| SSPC-SP3 | Power tool cleaning |
| SSPC-SP5 | White metal blast (Sa 3) |
| SSPC-SP6 | Commercial blast (Sa 2) |
| SSPC-SP7 | Brush-off blast (Sa 1) |
| SSPC-SP10 | Near-white blast (Sa 2.5) |
| SSPC-SP11 | Power tool cleaning to bare metal |
| SSPC-SP12 | Surface prep of steel and coated steel with high/ultra-high-pressure water jetting |
| SSPC-PA 2 | DFT measurement procedure |
| SSPC-PS 12.01 | Guide for zinc-rich primers |
| ASTM D4417 | Blast profile measurement (Methods A, B, C) |
| ASTM D4285 | Indicating oil/water in compressed air (blotter test) |

## Pretreatment Standards

| Standard | Description |
|----------|------------|
| MIL-DTL-5541 | Chemical conversion coatings on aluminum (Type I hex Cr, Type II tri Cr) |
| MIL-PRF-8625 | Anodic coatings on aluminum |
| TT-C-490 | Chemical conversion coatings (federal spec, older) |

## Regulatory

| Regulation | Scope |
|-----------|-------|
| EPA 40 CFR 63 Subpart HHHHHH (6H) | NESHAP: paint stripping and surface coating of miscellaneous parts (area sources) |
| EPA 40 CFR 63 Subpart MMMM | NESHAP: surface coating of miscellaneous metal parts (major sources) |
| EPA 40 CFR 63 Subpart SSSS | NESHAP: surface coating of metal coil |
| SCAQMD Rule 1107 | VOC limits for metal parts coatings (Southern California — strictest in US) |
| RoHS Directive 2011/65/EU | Restriction of hazardous substances (Cr6+, Cd, Pb, Hg, etc.) |
| REACH (EC 1907/2006) | Registration/evaluation of chemicals (chromate restriction, isocyanate restriction) |
| OSHA 29 CFR 1910.146 | Confined space entry (tank lining) |
| OSHA 29 CFR 1910.1043 | Occupational exposure to cotton dust (N/A) — reference: 29 CFR 1910.1000 Table Z-1 for PEL values |
| NSF/ANSI 61 | Drinking water system components (potable water tank linings) |

---

# CROSS-CLUSTER SAFETY REFERENCE

## Hazard Summary by Process

| Process | Primary Hazards |
|---------|----------------|
| Powder coating | Dust explosion (combustible dust cloud); grounding failure (electrostatic); oven burns |
| Liquid spray | Solvent vapors (LEL/UEL monitoring); spray mist inhalation; fire |
| E-coat | Electrical (200-400 V DC in wet environment); chemical handling (acids, bases) |
| Dip coating | Chemical immersion burns; PVC degradation → HCl gas; hot-dip burn hazard |
| Flow coating | Solvent vapors; skin contact; slippery floors from dripped coating |
| Coil coating | High-speed moving machinery; thermal oxidizer operation; solvent vapors |
| Priming systems | Zinc dust inhalation; solvent vapors; ethyl silicate fumes; isocyanate (PU primers) |
| Protective coatings | Isocyanate exposure (critical — respiratory sensitizer); epoxy/amine dermatitis; confined space |

## Isocyanate Hazard (2K Urethane — Clusters 2, 7, 8)
- **OSHA PEL:** 0.02 ppm (as NCO) ceiling
- **ACGIH TLV-TWA:** 0.005 ppm HDI monomer
- **Health effects:** Respiratory sensitization (occupational asthma), skin sensitization, eye irritation
- **PPE (spray application):** Supplied-air respirator (SAR) or self-contained breathing apparatus (SCBA); full protective clothing; chemical-resistant gloves; hood
- **Air monitoring:** Real-time isocyanate monitors (colorimetric tape, e.g., MDA Scientific) or personal sampling with OSHA Method 42/47
- **EU regulation:** REACH Restriction (August 2023) — isocyanate training mandatory for all workers handling diisocyanates

## Combustible Dust Hazard (Powder Coating — Cluster 1)
- **NFPA 652:** Standard on the Fundamentals of Combustible Dust
- **NFPA 33:** Standard for Spray Application Using Flammable or Combustible Materials
- **Kst value for typical powder coating:** 150-200 bar-m/s (St1 class — moderate explosion severity)
- **MEC (Minimum Explosible Concentration):** ~30-60 g/m3 for organic powder coatings
- **MIE (Minimum Ignition Energy):** 1-10 mJ — very low; static discharge can ignite
- **Controls:** Grounding of all equipment and parts; explosion venting or suppression on collectors; good housekeeping (no accumulation > 1/32 inch depth); no open flames/sparks in powder areas

## Solvent Flash Points (Liquid Paint — Clusters 2, 5, 7, 8)

| Solvent | Flash Point (closed cup) | LEL (% by volume) |
|---------|------------------------|-------------------|
| Acetone | -4 deg F (-20 deg C) | 2.5% |
| MEK (methyl ethyl ketone) | 16 deg F (-9 deg C) | 1.8% |
| Toluene | 40 deg F (4 deg C) | 1.2% |
| Xylene | 81 deg F (27 deg C) | 1.0% |
| Mineral spirits | 104-113 deg F (40-45 deg C) | 0.7% |
| n-Butyl acetate | 72 deg F (22 deg C) | 1.7% |
| PM acetate (1-methoxy-2-propyl acetate) | 108 deg F (42 deg C) | 1.4% |
| MAK (methyl n-amyl ketone) | 102 deg F (39 deg C) | 1.1% |
| Butyl cellosolve (2-butoxyethanol) | 143 deg F (62 deg C) | 1.1% |
| Water (waterborne coatings) | N/A (nonflammable carrier) | N/A |

---

# CROSS-CLUSTER DEFECT GLOSSARY

## Common Coating Defects Across All Processes

| Defect | Description | Root Cause(s) | Affected Clusters |
|--------|-------------|---------------|-------------------|
| Orange peel | Textured surface resembling orange skin | Improper atomization, too-fast solvent evaporation, gun too far, powder too coarse | 1, 2, 5 |
| Fish eye / cratering | Small circular voids/craters with raised edges | Silicone contamination, oil contamination, incompatible coatings | 1, 2, 3, 5, 6 |
| Sagging / running | Coating slides downward, leaving thick drips at bottom | Too thick per coat, low viscosity, substrate too smooth, slow solvent | 2, 4, 5, 7, 8 |
| Solvent pop / boiling | Small craters or bubbles in cured film | Solvent trapped beneath skin; insufficient flash time; too-fast oven ramp | 2, 7, 8 |
| Blistering | Bubbles (osmotic or adhesion-related) under the film | Moisture, soluble salts, poor adhesion, solvent entrapment | All |
| Outgassing / pinholes | Small holes in cured film | Substrate gases escaping during cure (castings, galvanized, porous metal) | 1, 4 |
| Undercure | Film soft, poor hardness, poor chemical resistance | Insufficient time/temperature; wrong mix ratio; expired hardener | 1, 2, 3, 6, 7, 8 |
| Mud cracking | Network of cracks in thick primer | Excessive DFT on IOZ primer; shrinkage exceeds cohesive strength | 7 |
| Dry spray | Rough, sandy texture; powdery appearance | Gun too far, too-high air pressure, too-low fluid flow | 2, 7, 8 |
| Poor adhesion | Coating peels or flakes from substrate | Contamination, inadequate pretreatment, recoat window exceeded, amine blush | All |
| Amine blush | Waxy/greasy surface on epoxy | Amine + CO2 + moisture reaction at low temp / high humidity | 7, 8 |
| Back-ionization | Pinholes/craters in thick powder | Excessive voltage causing reverse ionization at film surface | 1 |
| Color drift / metamerism | Color appears different under different light sources | Pigment selection, non-matching formulations | 2, 6 |
| Chalking | Powdery surface degradation from UV exposure | UV breakdown of binder (epoxy, aromatic urethane) | 2, 7, 8 |
| Delamination (intercoat) | Layers separate from each other | Recoat window exceeded, contamination between coats, incompatible coatings | 2, 7, 8 |
| Bridging (dip coat) | Coating spans across holes/slots instead of coating edges | Surface tension, viscosity too high, withdrawal too fast | 4 |
| Edge pull-back | Coating thins at sharp edges during cure | Surface tension pulls coating away from edges as it flows | 1, 3, 6 |

---

# RESEARCH METHODOLOGY AND CONFIDENCE

## Sources
- **Primary:** Watson domain expertise in industrial coatings, surface preparation, and corrosion protection. This knowledge base draws from training data encompassing SSPC, NACE (now AMPP), ASTM, Products Finishing, Journal of Protective Coatings & Linings, coatings manufacturer technical data sheets (PPG, Sherwin-Williams, International/AkzoNobel, Hempel, Axalta, Jotun), and coating inspector training curriculum (NACE CIP Level 1-3 / SSPC QP standards).
- **Gemini:** QUOTA EXHAUSTED at time of writing (10+ hour reset). All data in this brief is from domain expertise. Recommend spot-verification of specific numerical ranges when Gemini quota resets, particularly:
  - E-coat UF membrane specifications
  - Current EPA NESHAP citation numbers (40 CFR 63 subpart letters)
  - ISO 12944 corrosivity categories (C1-CX designations were updated in 2017 revision)
  - Coil coating line speed ranges (these vary widely by source)

## Confidence Levels
- **HIGH confidence** (> 95%): Application parameters, DFT targets, cure temperatures, ASTM/SSPC standard numbers, safety data (flash points, LEL values), defect descriptions, zinc-rich primer chemistry, e-coat electrochemistry, pretreatment chemistry.
- **MODERATE confidence** (80-95%): Salt spray performance ranges (these are highly formulation-dependent), specific EPA subpart letter designations, coil coating PMT ranges, exact UF membrane pore size specifications. These should be verified against current sources.
- **Flagged for verification:** The EPA 40 CFR 63 subpart designations (HHHHHH, MMMM, SSSS) — I am confident in the subpart letters but the regulatory landscape changes. Verify current applicability before poster publication.

## Poster Count
- 8 clusters x 9 posters = **72 total posters**.
- Each section above maps directly to one poster topic within its cluster.
- The cross-cluster references (Standards, Safety, Defects) can serve as supplementary posters or as shared reference content across the series.

---

*Watson — Chemistry Research*
*A Brite Company Technical Services*
*Research Brief v1 — 2026-04-26*
*Gemini verification pending quota reset*
