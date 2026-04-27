---
title: "Electroplating Clusters — Watson Research Brief"
date: 2026-04-26T00:00:00
author: Watson (chemistry-researcher)
scope: Comprehensive technical data for 14 electroplating process clusters (112 posters)
status: Complete
version: v1.0
tags:
  - PosterResearch
  - Series2
  - ElectroplatingClusters
  - WatsonBrief
---

# Electroplating Clusters — Watson Research Brief

**Watson — Chemistry Research Division**
**Plating Posters Inc — Series 2 Cluster Research**
**2026-04-26 (v1.0)**

---

## Purpose

This document provides the technical foundation for 14 electroplating process clusters (112 total posters, 8 per cluster). Each cluster covers: Process Flow, Cleaning, Rinse Pre-Activation, Activation, Rinse Pre-Plate, Main Tank, Rinse Post-Plate, and Post Treatment.

Zinc Alkaline (Cluster EP-01) is covered separately in its own brief and is excluded here.

**Research methodology:** Web-verified data from Products Finishing (pfonline.com), Nickel Institute (nickelinstitute.org), NMFRC, ASTM standards, ASM Handbook Vol. 5, SubsTech, finishing.com forums, ResearchGate publications, and patent literature. Supplemented by Watson domain expertise in electroplating chemistry. Gemini CLI was rate-limited at time of writing; all data verified via WebSearch.

**Confidence flag convention:**
- [VERIFIED] = confirmed by 2+ published sources
- [DOMAIN] = Watson domain expertise, consistent with industry practice but not multi-source verified in this session
- [FLAG] = data point requires Drew or Tyler review

---

# CLUSTER 1: ZINC PLATING (ACID / CHLORIDE)

## 1.1 Process Flow Poster Data

**What is this process?** Acid chloride zinc plating deposits a sacrificial zinc coating on steel and iron substrates from an acidic (pH ~5) chloride electrolyte. It provides galvanic corrosion protection — zinc corrodes preferentially to steel. Used extensively in automotive fasteners, stampings, brackets, clips, wire goods, and general hardware.

**Substrates:** Low-carbon steel, medium-carbon steel, cast iron, spring steel (with HE bake), powdered metal (with seal). Not recommended for high-strength steel >39 HRC without careful HE management.

**Full process sequence:**
1. Receiving / Racking or Barreling
2. Alkaline soak clean (remove oils, greases, drawing compounds)
3. Rinse (overflow)
4. Electrocleaning (anodic preferred)
5. Rinse (overflow)
6. Acid activation (HCl dip)
7. Rinse (overflow)
8. Acid chloride zinc plate
9. Rinse (drag-out recovery + overflow)
10. Nitric acid bright dip (optional, 0.5-1% v/v HNO3)
11. Rinse
12. Chromate conversion coating (trivalent or hexavalent)
13. Rinse
14. Hot water rinse / dry (140-160 deg F / 60-71 deg C)
15. Final inspection (thickness, adhesion, salt spray if required)

**Quality checkpoints:**
- Post-clean: water-break-free surface
- Post-activation: uniform matte gray appearance, no smut
- Post-plate: uniform color, no burning, no blistering, thickness per ASTM B633
- Post-chromate: uniform color, no bare spots, adhesion per bend test
- Final: salt spray hours per service condition class

## 1.2 Cleaning Stage

**Preferred method:** Alkaline soak clean followed by anodic electrocleaning. [VERIFIED]

**Alkaline soak cleaner:**
- Type: Mildly alkaline, silicated or non-silicated cleaner; neutral or low-caustic preferred for zinc to avoid substrate attack
- Concentration: 4-8 oz/gal (30-60 g/L) [VERIFIED]
- Temperature: 140-180 deg F (60-82 deg C); typical center 160 deg F (71 deg C)
- Time: 3-5 minutes soak, 1-3 minutes electroclean

**Electrocleaning preference:** Anodic (part is anode) preferred for final electroclean stage. Anodic electrocleaning produces oxygen at the part surface, scrubbing oils away. Cathodic cleaning produces more gas volume (hydrogen) for better scrubbing but risks hydrogen absorption and can plate out metallic contaminants onto the surface. Many shops use cathodic first (heavy soil removal) then anodic (final clean). [VERIFIED]

- Current density: 30-80 ASF (3.2-8.6 A/dm2)
- Voltage: 6-9 V typical

**Common cleaning failures for this process:**
- Residual drawing compounds causing skip plating or poor adhesion
- Silicate film from over-concentration of silicated cleaners — causes blister defects
- Inadequate rinsing leaving alkaline film that raises bath pH
- Over-cleaning of spring steel causing hydrogen pickup before plating even begins

## 1.3 Rinse Stages

**Pre-activation rinse:** Single overflow rinse is minimum; double counterflow preferred for production. Purpose: remove all alkaline cleaner residue before acid dip. Dragout of alkaline cleaner into acid activation wastes acid and creates precipitates.

**Pre-plate rinse:** Single overflow rinse after acid activation. Critical to prevent dragging acid and dissolved iron into the zinc bath. Iron contamination >50 ppm in the zinc bath causes dark, dull deposits and reduced chromate receptivity. [DOMAIN]

**DI water requirements:** Not required for acid chloride zinc; municipal water with conductivity <500 microS/cm is acceptable. DI water is reserved for final rinse before chromate if hexavalent chromates are used.

**Dragout considerations:** Barrel plating generates heavy dragout. A drag-out recovery tank before the overflow rinse recovers zinc and reduces waste treatment load. [VERIFIED]

## 1.4 Activation Stage

**Chemical:** Hydrochloric acid (muriatic acid), 10-50% v/v (typically 25-30% v/v or ~3-5 N). Some shops use 10% HCl for light activation. [VERIFIED]

**Temperature:** Ambient (room temperature, 65-85 deg F / 18-29 deg C). Do not heat.

**Time:** 15-60 seconds for clean steel. 1-3 minutes for scaled or heat-treated parts.

**What it does:** Removes surface oxides (mill scale, rust, heat treat scale) and provides a micro-etch that promotes adhesion. Dissolves the thin iron oxide/hydroxide passive layer. [VERIFIED]

**Over-activation risk:** Excessive time or concentration causes pitting, excessive base metal dissolution, and hydrogen absorption. On high-strength steel, over-activation in HCl is a significant HE risk factor. Time must be minimized. [VERIFIED]

**Under-activation risk:** Residual oxide causes skip plating, poor adhesion, or blistering during chromate.

**Unique requirement:** For cast iron substrates, a brief anodic etch (30-60 sec, 30-50 ASF in 10% H2SO4) may be needed to remove graphite smut before HCl activation. [DOMAIN]

## 1.5 Main Tank (Plating Bath)

### Bath Chemistry [VERIFIED]

There are three sub-types of acid chloride zinc:

**Type A — Ammonium chloride / Potassium chloride (mixed)**

| Component | Concentration | Purpose |
|---|---|---|
| Zinc chloride | 8-12 oz/gal (60-90 g/L) as ZnCl2 | Zinc ion source (~30-45 g/L Zn metal) |
| Potassium chloride | 15-25 oz/gal (112-187 g/L) | Conductivity |
| Ammonium chloride | 2-6 oz/gal (15-45 g/L) | Buffering, conductivity |
| Boric acid | 3-4 oz/gal (22-30 g/L) | pH buffer (in all-KCl systems) |
| Brighteners (carrier + primary + secondary) | Per supplier TDS | Grain refinement, leveling, brightness |
| Wetting agent | 0.1-0.5% v/v | Reduce pitting |

**Type B — All-potassium chloride (ammonium-free)**

| Component | Concentration |
|---|---|
| Zinc chloride | 8-12 oz/gal (60-90 g/L) |
| Potassium chloride | 25-35 oz/gal (187-262 g/L) |
| Boric acid | 3-4 oz/gal (22-30 g/L) |
| Brighteners | Per supplier TDS |

**Type C — Low-ammonium (hybrid)**
Same as Type A but with ammonium chloride limited to 1-3 oz/gal (7-22 g/L) — reduces wastewater ammonium issues while retaining buffering.

### Operating Parameters [VERIFIED]

| Parameter | Value |
|---|---|
| Temperature | 70-95 deg F (21-35 deg C); center point 80 deg F (27 deg C) |
| pH | 4.8-5.6; optimal 5.0-5.4 for best LCD brightness |
| Cathode current density (rack) | 10-40 ASF (1.1-4.3 A/dm2); typical 20-30 ASF |
| Cathode current density (barrel) | 5-15 ASF (0.5-1.6 A/dm2) |
| Voltage | 3-9 V (depends on load and rack/barrel) |
| Agitation | Air agitation (oil-free) preferred; solution movement; barrel rotation |
| Anode material | Special high-grade (SHG) zinc, 99.99% purity; ball anodes in Ti baskets for barrel |
| Anode:cathode ratio | 1:1 to 2:1 |
| Filtration | Continuous, 5-10 micron; carbon filtration periodic |

### Efficiency and Plating Rate [VERIFIED]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 90-98% (typically 95%) |
| Anode efficiency | ~100% (soluble anodes) |
| Plating rate at 20 ASF | ~0.3 mil/hr (7.6 microns/hr) approximate |

**Note:** Because anode efficiency exceeds cathode efficiency, zinc metal builds up in solution over time. The zinc:chloride ratio must be monitored. Excess zinc causes haze and roughness. [VERIFIED per Columbia Chemical reference]

### pH Control [VERIFIED]
- pH too low (<4.8): brightener oil-out, increased anode dissolution, zinc metal buildup
- pH too high (>5.6): hydroxide precipitates, roughness, poor HCD coverage
- Adjust down: HCl (small additions, well-diluted)
- Adjust up: KOH or NH4OH (depending on bath type)

### Analytical Methods [DOMAIN]
- Zinc metal: EDTA titration at pH 10, Eriochrome Black T indicator; or AA spectrophotometry
- Total chloride: Mohr titration (silver nitrate, potassium chromate indicator)
- pH: calibrated pH meter
- Boric acid: mannitol titration with NaOH
- Ammonium: formaldehyde method or ISE
- Hull cell: 267 mL, 2A, 10 min at bath temperature

### Common Defects [VERIFIED]

| Defect | Cause | Corrective Action |
|---|---|---|
| Burning at HCD | Low zinc metal, high CD, low chloride | Increase Zn, reduce CD, add KCl |
| Dull/hazy deposit | High zinc metal, low brightener, high pH | Reduce Zn, add brightener, adjust pH |
| Pitting | Low wetting agent, organic contamination, inadequate agitation | Add wetter, carbon treat, increase agitation |
| Skip plating | Poor cleaning, low zinc, passive substrate | Improve cleaning, check activation |
| Dark LCD | Iron contamination >50 ppm, low brightener | Treat iron (raise pH to 6.5, filter, re-adjust), add brightener |
| Roughness | Particulates, high zinc, anode sludge | Filter, reduce Zn, bag anodes, maintain baskets |
| Blistering/peeling | Poor adhesion from inadequate cleaning or activation | Review pre-treatment, check for silicate residue |

### Hull Cell Interpretation [DOMAIN]
- **Good panel:** Bright and level from 5-50 ASF, slight haze at extreme LCD
- **Low brightener:** Dull appearance across panel, especially mid-range
- **High zinc:** Spongy or dark deposit at HCD
- **Iron contamination:** Dark streaks or iridescent discoloration at LCD
- **Low wetting agent:** Pitting scattered across panel

## 1.6 Post Treatment

### Chromate Conversion Coatings [VERIFIED]

Per ASTM B633 service condition classifications:

| Type | Description | Salt Spray (hours to white rust) | Typical Chemistry |
|---|---|---|---|
| Clear/blue (Type II) | Thin clear-blue iridescent | 8-24 hr (uncoated clear) | Trivalent chromium + mineral acid |
| Yellow iridescent (Type III) | Yellow-gold iridescent | 72-96 hr | Hexavalent chromium (being phased out) |
| Olive drab (Type IV) | Heavy hex chrome | 96-200 hr | Hexavalent chromium, thick film |
| Trivalent clear | Clear, slight blue tint | 24-72 hr (with topcoat: 120-200 hr) | Trivalent chromium |
| Trivalent black | Black appearance | 48-96 hr | Trivalent chrome + silver/cobalt salt |
| Trivalent w/ topcoat (sealed) | Clear or black + organic seal | 120-500+ hr | Trivalent chrome + topcoat sealant |

**RoHS note:** Hexavalent chromium chromates are restricted under EU RoHS and REACH. Trivalent chromium passivates are the standard replacement. Most automotive OEMs now require trivalent-only. [VERIFIED]

### Hydrogen Embrittlement Baking [VERIFIED]

Per ASTM B850 / AMS 2759/9:
- Required for all steel parts with hardness >= 31 HRC (or tensile >= 1000 MPa)
- Temperature: 375-430 deg F (190-220 deg C); standard: 375 deg F (191 deg C)
- Time: Minimum 8 hours for 31-36 HRC; 12 hours for 37-39 HRC; 24 hours for >=40 HRC
- Must commence within 4 hours of plating completion (1 hour preferred for >39 HRC)
- Bake BEFORE chromate conversion coating (chromate will degrade at bake temperatures)

### Applicable Specifications

| Specification | Coverage |
|---|---|
| ASTM B633 | Electrodeposited coatings of zinc on iron and steel |
| ASTM B850 | Post-coating treatments to reduce HE risk |
| ASTM B849 | Pre-treatments to reduce HE risk |
| AMS 2402 | Zinc plating (aerospace) |
| SAE J2329 / J2334 | Automotive corrosion testing |

## 1.7 Safety and Regulatory

**Key chemical hazards:**
- Hydrochloric acid fumes (activation tank) — respiratory irritant
- Zinc chloride — skin/eye irritant; ingestion hazard
- Ammonium chloride — fume generation when heated
- Chromate solutions — hexavalent chromium is carcinogenic (Group 1, IARC); trivalent is low toxicity

**PPE:** Chemical splash goggles, face shield at chromate tanks, acid-resistant gloves (nitrile minimum), rubber apron, ventilation/fume extraction at all tanks. Hex chrome tanks require dedicated exhaust with mist eliminators.

**Wastewater:** Alkaline precipitation of zinc as Zn(OH)2 at pH 8.5-9.5 (optimal 9.0). Hex chrome waste must be reduced to Cr(III) with sodium metabisulfite at pH <3, then co-precipitated. Ammonium-bearing waste requires breakpoint chlorination or air stripping. [DOMAIN]

---

# CLUSTER 2: ZINC-NICKEL PLATING (ALKALINE AND ACID)

## 2.1 Process Flow Poster Data

**What is this process?** Zinc-nickel alloy plating co-deposits zinc and nickel (target 12-16% Ni by weight) to produce a coating with 5-10x the corrosion resistance of plain zinc. The alloy remains sacrificial to steel while the nickel content dramatically slows the corrosion rate of the coating itself. Dominant in automotive, aerospace, defense, and heavy truck applications.

**Substrates:** Steel (all grades), cast iron, high-strength steel (with HE bake), sintered metal. Zinc-nickel is specifically chosen when parts see severe corrosion environments — underhood, brake components, structural fasteners.

**Two bath types exist:**
- **Alkaline zinc-nickel** — dominant in industry; better alloy uniformity; preferred for rack and barrel
- **Acid zinc-nickel** — higher speed; narrower operating window; less common

**Full process sequence:**
1. Receiving / Racking or Barreling
2. Alkaline soak clean
3. Rinse
4. Electrocleaning (anodic)
5. Rinse
6. Acid activation (HCl or H2SO4)
7. Rinse
8. Zinc-nickel alloy plate
9. Rinse (multiple — drag-out + overflow)
10. Nitric acid dip (bright dip / de-smut, 0.5-1% HNO3, 10-30 sec)
11. Rinse
12. Trivalent passivation (clear, iridescent, or black)
13. Rinse
14. Topcoat/sealer (optional but common)
15. Hot air dry
16. HE bake (if applicable — bake BEFORE passivation)
17. Final inspection

## 2.2 Cleaning Stage

Same as acid chloride zinc (Section 1.2). Alkaline soak clean + anodic electrocleaning. Cleaning is even more critical for zinc-nickel because alloy ratio is sensitive to surface condition. Any residual oil or oxide causes nickel-rich areas (dark spots) or zinc-rich areas (poor corrosion resistance). [DOMAIN]

## 2.3 Rinse Stages

**Pre-activation:** Double counterflow rinse recommended. Any alkaline dragout into acid activation creates insoluble zinc hydroxide smut.

**Pre-plate:** Double counterflow rinse mandatory for zinc-nickel. Dragout of acid into the alkaline ZnNi bath will cause localized pH drop and alloy composition shift. For acid ZnNi, single rinse after acid dip is acceptable if acid activation and bath share compatible chemistry. [DOMAIN]

**Post-plate:** Triple rinse recommended — drag-out recovery + double counterflow. ZnNi baths are expensive; drag-out recovery is economically justified.

**DI water:** Not required for process rinses. DI recommended for final rinse before passivation to prevent water spot staining on appearance-critical parts.

## 2.4 Activation Stage

**Alkaline ZnNi process:**
- Chemical: 10-30% v/v HCl (hydrochloric acid) at room temperature
- Time: 15-45 seconds
- Purpose: oxide removal, micro-etch
- Alternative: 5-10% H2SO4 for heat-treated parts (less aggressive hydrogen pickup)

**Acid ZnNi process:**
- Chemical: 5-10% H2SO4 or 5-10% HCl
- Time: 15-30 seconds

**Critical note for high-strength steel:** Minimize acid contact time. Some aerospace specs (BAC 5748, Boeing) mandate H2SO4 activation instead of HCl to reduce hydrogen absorption. Pre-bake per ASTM B849 may be required before plating. [DOMAIN]

## 2.5 Main Tank (Plating Bath)

### Alkaline Zinc-Nickel Bath Chemistry [VERIFIED]

| Component | Concentration | Purpose |
|---|---|---|
| Zinc oxide (or zinc metal as ZnO) | 6-12 g/L as Zn metal (8-16 g/L as ZnO) | Zinc ion source |
| Nickel sulfate or nickel chloride | 1-3 g/L as Ni metal | Nickel ion source |
| Sodium hydroxide | 100-150 g/L | Conductivity, complexation |
| Amine complexing agent | Per supplier TDS (proprietary) | Stabilizes Ni in alkaline solution |
| Brightener / grain refiner | Per supplier TDS | Deposit quality |
| Zn:Ni ratio in bath | Typically 4:1 to 8:1 (metal basis) | Controls alloy composition |

### Acid Zinc-Nickel Bath Chemistry [DOMAIN]

| Component | Concentration | Purpose |
|---|---|---|
| Zinc chloride | 25-50 g/L as Zn metal | Zinc ion source |
| Nickel chloride | 25-40 g/L as Ni metal | Nickel ion source |
| Ammonium chloride or KCl | 100-200 g/L | Conductivity |
| Boric acid | 25-35 g/L | pH buffer |
| Brighteners | Per supplier TDS | Leveling, brightness |
| pH | 5.5-6.5 | |

### Operating Parameters

| Parameter | Alkaline ZnNi | Acid ZnNi |
|---|---|---|
| Temperature | 75-95 deg F (24-35 deg C) | 75-105 deg F (24-40 deg C) |
| pH | >13 (strongly alkaline) | 5.5-6.5 |
| Cathode CD (rack) | 10-40 ASF (1.1-4.3 A/dm2) | 10-50 ASF (1.1-5.4 A/dm2) |
| Cathode CD (barrel) | 5-15 ASF (0.5-1.6 A/dm2) | 5-20 ASF (0.5-2.2 A/dm2) |
| Voltage | 4-12 V | 3-8 V |
| Agitation | Mechanical or solution flow; air OK if oil-free | Air agitation preferred |
| Anode material | Zinc anodes (pure Zn, no Ni in anode) | Steel or Ni-plated steel anodes (insoluble) or Zn anodes |
| Anode:cathode ratio | 1:1 to 2:1 | 1:1 to 2:1 |
| Cathodic efficiency | 40-70% (alkaline) | 80-95% (acid) |

**Target alloy composition:** 12-16% Ni by weight (balance zinc). [VERIFIED per ASTM B841-18 Class 2]
- <10% Ni: Corrosion resistance drops significantly; may not meet spec
- >18% Ni: Coating becomes cathodic to steel (loses sacrificial protection)
- Alloy control is primarily via Zn:Ni metal ratio, temperature, and current density

**Plating rate (alkaline):** ~0.15-0.25 mil/hr at 20 ASF (3.8-6.4 microns/hr). Slower than plain zinc due to lower efficiency. [DOMAIN]

### Analytical Methods [DOMAIN]
- Zinc metal: EDTA titration at pH 10
- Nickel metal: EDTA titration with murexide or dimethylglyoxime colorimetric
- Sodium hydroxide: acid-base titration (HCl, phenolphthalein endpoint)
- Alloy composition (deposit): XRF (preferred for QC), or dissolve coating in HNO3 and analyze by AA
- Hull cell: 267 mL, 2A, 10 min (alkaline) or 1A, 10 min (acid)

### Common Defects

| Defect | Cause | Corrective Action |
|---|---|---|
| Low nickel in deposit (<10%) | Low bath Ni, high CD, low temperature | Add Ni replenisher, reduce CD, raise temp |
| High nickel in deposit (>18%) | High bath Ni, low CD, high temperature | Reduce Ni, plate at higher CD |
| Burning at HCD | Low Zn metal, high CD | Add Zn, reduce CD |
| Dark deposits | Organic contamination, metallic contamination (Cu, Fe) | Carbon treat, dummy plate, check cleaning |
| Blistering | Poor cleaning, insufficient activation | Review pre-treatment, extend electrocleaning |
| Uneven alloy distribution | Poor agitation, improper racking | Improve agitation, re-rack for uniform CD |
| Poor passivation acceptance | Over-bright deposit, Ni% out of range | Adjust brightener, correct alloy ratio |

## 2.6 Post Treatment

### Trivalent Passivation [VERIFIED]

Hexavalent chromates are almost universally prohibited for zinc-nickel in automotive and aerospace. Trivalent passivation is standard.

| Type | Salt Spray (white corrosion) | Salt Spray (red rust) | Notes |
|---|---|---|---|
| Trivalent clear | 120-200 hr | 500-1000 hr | Automotive standard |
| Trivalent iridescent | 200-400 hr | 720-1500 hr | Higher protection |
| Trivalent black | 96-200 hr | 500-1000 hr | Appearance applications |
| Trivalent + topcoat sealer | 400-1000 hr | 1000-2000+ hr | Premium automotive/aerospace |

### Hydrogen Embrittlement Baking
Same requirements as plain zinc per ASTM B850 / AMS 2759/9 (see Section 1.6). Bake BEFORE passivation. For aerospace, some specs require 23 +/- 1 hour bake at 375 deg F regardless of hardness level. [DOMAIN]

### Applicable Specifications

| Specification | Coverage |
|---|---|
| ASTM B841 | Electrodeposited zinc-nickel alloy coatings |
| ASTM B850 | HE relief |
| GM 6191M, Ford WSS-M21P38-A2 | Automotive OEM specs |
| Boeing BAC 5748 | Aerospace zinc-nickel |
| VW TL 233 / TL 244 | European automotive |
| AMS 2417 | Zinc-nickel plating (aerospace) |

## 2.7 Safety and Regulatory

**Key hazards:**
- Sodium hydroxide (alkaline bath): severe burn hazard, pH >13
- Nickel compounds: dermal sensitizer, IARC Group 2B carcinogen (inhalation)
- Hydrochloric acid: respiratory irritant
- Passivation chemicals: chromium(III) low toxicity but must be managed in waste

**PPE:** NaOH-resistant gloves (neoprene), face shield, rubber apron. Nickel baths require fume suppression and good ventilation. Respiratory protection if misting.

**Wastewater:** Zinc precipitates at pH 8.5-9.5. Nickel precipitates at pH 9.0-10.0 (higher than zinc). Two-stage hydroxide precipitation may be needed, or chelated nickel may require additional treatment. Nickel discharge limits are typically 1-3 mg/L depending on local pretreatment standards. [DOMAIN]

---

# CLUSTER 3: NICKEL PLATING (WATTS)

## 3.1 Process Flow Poster Data

**What is this process?** Watts nickel plating (named for Oliver P. Watts, 1916) is the most widely used nickel electroplating process worldwide. It deposits a bright, semi-bright, or matte nickel coating from a sulfate/chloride/boric acid electrolyte. Applications include decorative finishing (automotive trim, plumbing fixtures, consumer electronics), engineering coatings (wear resistance, buildup), and as an underplate for chrome.

**Substrates:** Steel, copper, brass, zinc die cast (after copper strike), aluminum (after zincate + copper or nickel strike), stainless steel (after Wood's nickel strike).

**Full process sequence (on steel):**
1. Receiving / Racking
2. Alkaline soak clean
3. Rinse
4. Anodic electrocleaning
5. Rinse
6. Acid activation (10-30% HCl, 15-30 sec)
7. Rinse
8. Nickel strike (Wood's strike for stainless steel or passivating alloys; sulfamate strike for direct plating on active steel)
9. Rinse (if using strike)
10. Watts nickel plate (semi-bright, then bright for decorative duplex)
11. Rinse
12. Chrome plate (if decorative nickel-chrome)
13. Rinse
14. Hot water rinse / dry
15. Inspection

## 3.2 Cleaning Stage

**Preferred method:** Alkaline soak clean + anodic electrocleaning. [VERIFIED]

Nickel is extremely sensitive to surface contamination. Even trace organic films cause pitting. Electrocleaning is mandatory, not optional.

- Soak cleaner: 4-8 oz/gal (30-60 g/L), 140-180 deg F (60-82 deg C), 3-5 min
- Electroclean: Anodic at 40-80 ASF (4.3-8.6 A/dm2), 1-2 min
- Cathodic step first is acceptable for heavy soils, but MUST finish anodic

**Common cleaning failures:**
- Organic residues cause pitting (the #1 defect in Watts nickel)
- Silicate residue from cleaners causes adhesion failure
- Smut from cathodic cleaning (metallic contamination deposited on part) carries into bath

## 3.3 Rinse Stages

**Pre-activation rinse:** Double counterflow preferred. Must completely remove alkaline cleaner. Any alkaline dragout into HCl causes iron chloride formation on surface.

**Pre-plate rinse:** Single overflow minimum after acid activation. If Wood's nickel strike is used, rinse between strike and Watts bath to prevent HCl dragout (lowers Watts bath pH rapidly).

**Post-plate rinse:** Double counterflow. Nickel drag-out is expensive and an environmental concern (Ni discharge limits are tight). Drag-out recovery tank saves money.

**DI water:** Recommended for final rinse before decorative chrome to prevent water spots on nickel surface.

## 3.4 Activation Stage

**For steel substrates:**
- 10-30% v/v HCl, room temperature, 15-30 seconds
- Alternative: 5-10% H2SO4 for sensitive substrates

**For stainless steel / Inconel / passivating alloys:**
- Wood's nickel strike is REQUIRED (see below)

**Wood's Nickel Strike** [VERIFIED]

| Component | Concentration |
|---|---|
| Nickel chloride (NiCl2.6H2O) | 240-340 g/L (32-45 oz/gal) |
| Hydrochloric acid (37%) | 75-125 mL/L (10-16 fl oz/gal) |
| pH | <1.0 |
| Temperature | Room temperature to 100 deg F (38 deg C) |
| Current density | Step 1: Anodic at 10-20 ASF for 1-2 min (etch); Step 2: Cathodic at 20-50 ASF for 2-4 min (strike) |

Purpose: The anodic step etches the passive oxide film. The cathodic step simultaneously deposits nickel while evolving hydrogen gas, preventing re-passivation. The resulting thin nickel layer (~0.1 mil) provides an adherent base for subsequent Watts nickel plating.

## 3.5 Main Tank (Plating Bath)

### Watts Bath Formulation [VERIFIED]

| Component | Low | Typical | High | Purpose |
|---|---|---|---|---|
| Nickel sulfate (NiSO4.6H2O) | 225 g/L (30 oz/gal) | 300 g/L (40 oz/gal) | 375 g/L (50 oz/gal) | Primary Ni ion source |
| Nickel chloride (NiCl2.6H2O) | 30 g/L (4 oz/gal) | 60 g/L (8 oz/gal) | 75 g/L (10 oz/gal) | Anode corrosion, conductivity |
| Boric acid (H3BO3) | 30 g/L (4 oz/gal) | 40 g/L (5.3 oz/gal) | 45 g/L (6 oz/gal) | Cathode film pH buffer |
| Total nickel metal | 60 g/L | 80 g/L | 100 g/L | |
| Brighteners (primary + secondary) | Per supplier TDS | | | Leveling, brightness |
| Wetting agent (anti-pit) | 0.05-0.3% v/v | | | Eliminate pitting |

### Operating Parameters [VERIFIED]

| Parameter | Range | Typical Center |
|---|---|---|
| Temperature | 110-160 deg F (43-71 deg C) | 135 deg F (57 deg C) for bright; 140 deg F (60 deg C) for semi-bright |
| pH | 3.0-4.5 | 3.8-4.2 for bright; 4.0-4.5 for semi-bright |
| Cathode CD (rack) | 20-80 ASF (2.2-8.6 A/dm2) | 40 ASF (4.3 A/dm2) |
| Cathode CD (barrel) | 5-25 ASF (0.5-2.7 A/dm2) | 10-15 ASF |
| Voltage | 4-8 V | 6 V typical |
| Agitation | Air agitation (oil-free, low-pressure) mandatory | |
| Filtration | Continuous, 5-10 micron; activated carbon canister | |
| Anode material | Electrolytic nickel (S-Rounds or R-Rounds) in Ti baskets with anode bags (polypropylene, 1-5 micron) | |
| Anode:cathode ratio | 1:1 to 2:1 | 1.5:1 preferred |

### Efficiency and Plating Rate [VERIFIED]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 93-97% |
| Plating rate at 40 ASF | ~0.9-1.0 mil/hr (23-25 microns/hr) |
| Bright Ni density | 8.5-8.9 g/cm3 (varies with sulfur content) |

### Anode Management [VERIFIED]
- S-Rounds (sulfur-depolarized): Standard for bright nickel; dissolve evenly; preferred
- R-Rounds (electrolytic, no sulfur): For semi-bright nickel (sulfur-free deposit required for duplex systems)
- Anode bags are MANDATORY: prevent particulate dissolution products from entering bath and causing roughness
- Anode passivation: Caused by low chloride, low temperature, or excessive anode CD. Symptoms: rising voltage, decreasing deposition rate. Corrective: increase NiCl2.

### pH Control [VERIFIED]
- pH too low (<3.5): Excessive hydrogen evolution, reduced efficiency, burning at HCD, poor leveling
- pH too high (>4.5): Hydroxide precipitation in cathode film, pitting, dark deposits, treeing
- Adjust down: Dilute H2SO4 (do NOT use HCl — already have chloride control separately)
- Adjust up: Nickel carbonate (preferred — raises pH without adding dilution water or foreign cation)
- Boric acid does NOT change bulk pH — it only buffers the cathode film

### Analytical Methods [DOMAIN]
- Nickel metal: EDTA titration at pH 10, murexide indicator (pink to purple endpoint); or AA
- Chloride: Mohr titration (AgNO3 / K2CrO4)
- Boric acid: Mannitol complexation + NaOH titration
- pH: Calibrated pH meter (check daily)
- Brightener (organic): Hull cell is primary method; some suppliers offer cyclic voltammetric stripping (CVS)
- Sulfur in deposit: XRF (for duplex nickel, must be <0.005% in semi-bright layer)
- Hull cell: 267 mL, 2A, 10 min at bath temperature; evaluate brightness range, pitting, burning

### Common Defects [VERIFIED]

| Defect | Cause | Corrective Action |
|---|---|---|
| Pitting | Low wetting agent, organic contamination, air agitation too vigorous, particles | Add anti-pit, carbon treat + H2O2 treatment, adjust air, filter |
| Burning at HCD | Low Ni metal, high CD, low temperature, high pH | Increase NiSO4, reduce CD, raise temp, lower pH |
| Dull deposits | Low brightener, low temperature, metallic contamination | Add brightener, raise temp, dummy plate at 5-10 ASF |
| Roughness | Particulates, anode dissolving products, no anode bags, poor filtration | Replace anode bags, filter continuously, maintain Ti baskets |
| Peeling/blistering | Inadequate cleaning, passive substrate, skip in pre-treatment | Review entire pre-treatment line; check for silicate contamination |
| Dark deposits | Cu/Zn/Fe contamination, high pH | Dummy plate; correct pH; analyze for metals by AA |
| Treeing/dendrites | Very high CD, very low Ni, organic breakdown products | Reduce CD, maintain chemistry, carbon treat |
| Haze/milky | Excess organic contamination, brightener imbalance | Carbon treatment, adjust brightener ratio |

### Metallic Contamination Thresholds [DOMAIN — Tyler verify recommended]

| Contaminant | Symptom Threshold | Effect |
|---|---|---|
| Copper | >10-20 ppm | Dark LCD deposits, discoloration |
| Iron | >25-50 ppm | Roughness, pitting, dark HCD |
| Zinc | >10-20 ppm | Dull deposits, poor ductility |
| Chromium (Cr6+) | >5 ppm | Severe: all current density burning, pitting |
| Lead | >1-5 ppm | Black streaks, treeing |

**Carbon treatment procedure:** [DOMAIN]
1. Raise pH to 5.0-5.5 with NiCO3
2. Add 3-5 g/L powdered activated carbon; mix 1-2 hours
3. Add body feed (diatomaceous earth or filter aid)
4. Filter through 1-5 micron filter media
5. Return to operating pH (3.8-4.2 with dilute H2SO4)
6. Re-add brightener and wetting agent (carbon removes organics)
7. Run Hull cell to confirm deposit quality before production

## 3.6 Post Treatment

**Decorative nickel-chrome:** Nickel plate is followed by decorative chromium (hex or trivalent). No intermediate treatment needed — transfer must be fast (<30 seconds rinse-to-chrome) to prevent nickel surface passivation.

**Stand-alone nickel:** May receive clear lacquer or wax topcoat for tarnish resistance. Nickel tarnishes in sulfur-bearing atmospheres.

**HE baking:** Nickel plating itself generates relatively low hydrogen compared to acid baths, but per ASTM B850, high-strength steel substrates still require baking (375 deg F, 8+ hours for >=31 HRC).

### Applicable Specifications

| Specification | Coverage |
|---|---|
| ASTM B689 | Electrodeposited nickel on metallic substrates |
| AMS 2403 | Nickel plating (aerospace) |
| AMS-QQ-N-290 | Nickel plating (federal) |
| ASTM B764 | Simultaneous thickness and composition of nickel coatings (STEP test) |
| ASTM B504 | Thickness by coulometric method |

## 3.7 Safety and Regulatory

**Key hazards:**
- Nickel salts: skin sensitizer (#1 industrial allergen); IARC Group 1 (nickel compounds, inhalation); Group 2B (metallic nickel)
- Sulfuric acid (pH adjustment): corrosive
- Brightener organics: low acute toxicity but can be irritants
- HCl fumes at acid activation

**PPE:** Nitrile gloves (minimum), neoprene for extended contact. Safety goggles. Respiratory protection if aerosolized. Local exhaust ventilation mandatory. Nickel-specific biological monitoring (urinary nickel) recommended for chronic exposure assessment.

**Wastewater:** Nickel hydroxide precipitation at pH 9.5-10.5. Nickel discharge limits are stringent: typically 0.5-3.4 mg/L depending on categorical standard (40 CFR 433). Chelated nickel from cleaners or dragout can pass through hydroxide precipitation — may require sulfide precipitation or ion exchange polishing. [DOMAIN]

---

# CLUSTER 4: NICKEL PLATING (SULFAMATE)

## 4.1 Process Flow Poster Data

**What is this process?** Nickel sulfamate plating deposits a low-stress, highly ductile, and highly pure nickel coating. It is the preferred process for engineering applications requiring dimensional accuracy, electroforming (building up free-standing nickel structures), and applications where deposit stress must be minimized (electronic components, aerospace hydraulic fittings, mold inserts).

**Substrates:** Steel, stainless steel (with Wood's strike), copper, brass, Invar, beryllium copper, mandrels for electroforming.

**Key distinction from Watts:** Sulfamate Ni produces deposits with significantly lower internal stress (can approach zero or slightly compressive with stress reducers), higher purity, and better fatigue life. Watts nickel deposits typically have 15-30 ksi tensile stress; sulfamate can achieve 0-5 ksi.

**Full process sequence:**
1. Receiving / Racking (or mandrel preparation for electroforming)
2. Alkaline soak clean
3. Rinse
4. Anodic electrocleaning
5. Rinse
6. Acid activation (HCl or H2SO4)
7. Rinse
8. Wood's nickel strike (for stainless, Invar, passivating alloys)
9. Rinse
10. Nickel sulfamate plate
11. Rinse
12. Hot water rinse / dry (or mandrel separation for electroforming)
13. Inspection (thickness, hardness, stress if specified)

## 4.2 Cleaning Stage

Same as Watts nickel (Section 3.2). Sulfamate baths are even MORE sensitive to organic contamination because they run without brighteners (for low-stress applications), so any organic film on the substrate transfers directly into the deposit.

## 4.3 Rinse Stages

Same as Watts nickel (Section 3.3). DI water rinse recommended before entering sulfamate bath to prevent introducing foreign anions (sulfate, chloride from rinse water).

## 4.4 Activation Stage

Same as Watts nickel (Section 3.4). Wood's strike for passivating alloys; HCl dip for steel.

## 4.5 Main Tank (Plating Bath)

### Sulfamate Bath Formulation [VERIFIED]

| Component | Low | Typical | High | Purpose |
|---|---|---|---|---|
| Nickel sulfamate [Ni(SO3NH2)2] | 300 g/L (40 oz/gal) | 450 g/L (60 oz/gal) | 650 g/L (87 oz/gal) | Ni ion source (high solubility allows high concentration) |
| Nickel chloride (NiCl2.6H2O) | 0 g/L (for zero-stress electroforming) | 5-15 g/L (0.7-2 oz/gal) | 30 g/L (4 oz/gal) | Anode corrosion; adds stress at higher levels |
| Boric acid (H3BO3) | 30 g/L (4 oz/gal) | 37 g/L (5 oz/gal) | 45 g/L (6 oz/gal) | Cathode film pH buffer |
| Nickel metal content | 60 g/L | 80-90 g/L | 110 g/L | |
| Stress reducer | Per supplier TDS | | | Optional; saccharin-based or proprietary |

**CRITICAL NOTE:** Nickel sulfamate hydrolyzes to nickel ammonium sulfate at temperatures above 160 deg F (71 deg C) or pH below 3.0. Hydrolysis is irreversible and increases stress. Temperature and pH must be carefully controlled. [VERIFIED]

### Operating Parameters [VERIFIED]

| Parameter | Low-Stress Electroforming | General Engineering |
|---|---|---|
| Temperature | 90-110 deg F (32-43 deg C) | 100-140 deg F (38-60 deg C) |
| pH | 3.8-4.2 | 3.5-4.5 |
| Cathode CD | 10-40 ASF (1.1-4.3 A/dm2) | 20-100 ASF (2.2-10.8 A/dm2) |
| Voltage | 4-12 V | 6-15 V (higher CD needs more voltage) |
| Agitation | Mechanical (cathode rod oscillation) or solution flow; air agitation AVOIDED (introduces CO2 and organics) | Air OK for engineering if quality permits |
| Filtration | Continuous, 1-5 micron; activated carbon | Same |
| Anode material | S-Rounds (sulfur-depolarized) in Ti baskets with bags; or electrolytic Ni | Same |
| Anode:cathode ratio | 1:1 to 2:1 | Same |
| Cathodic efficiency | 95-100% | 95-100% |

**Plating rate:** At 40 ASF: ~0.9-1.0 mil/hr. At 100 ASF (high-speed): ~2.2-2.5 mil/hr. [DOMAIN]

### Stress Control [VERIFIED]

| Factor | Effect on Stress |
|---|---|
| Higher chloride | Increases tensile stress |
| Higher temperature (>140 deg F) | Risk of hydrolysis; stress becomes erratic |
| Lower pH (<3.5) | Hydrolysis risk; tensile stress increases |
| Organic contamination | Increases tensile stress dramatically |
| Saccharin (stress reducer) | Shifts stress from tensile to compressive; 50-200 mg/L range |
| Higher current density | Slightly increases tensile stress |
| Metallic impurities (Cu, Fe, Zn) | Increase stress and embrittlement |

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| High tensile stress | Chloride too high, organic contamination, hydrolysis | Reduce NiCl2, carbon treat, check for hydrolysis products |
| Cracking | Extreme tensile stress + insufficient ductility | Stress reducer addition, purify bath |
| Pitting | Low wetting agent, particles, poor filtration | Add anti-pit agent (use sparingly — organics affect stress) |
| Rough deposits | Particulates, anode dissolution products | Filter continuously, anode bags, maintain Ti baskets |
| Peeling | Inadequate activation or strike on passivating alloy | Review Wood's strike procedure |
| Sulfamate hydrolysis | Temperature >160 deg F or pH <3.0 | Irreversible; bath must be partially or fully replaced |

## 4.6 Post Treatment

**Electroforming:** Mandrel is separated from deposit (chemical, mechanical, or thermal differential). Deposit may receive additional machining, grinding, or polishing.

**Engineering coatings:** May be used as-plated, or ground/lapped to final dimension.

**HE baking:** Required for high-strength steel per ASTM B850 (same as Watts).

### Applicable Specifications

| Specification | Coverage |
|---|---|
| AMS 2403 | Nickel plating (covers both Watts and sulfamate) |
| AMS-QQ-N-290 | Nickel plating, general |
| AMS 2424 | Nickel plating, low-stressed-deposit (specifically sulfamate) |
| ASTM B689 | Electrodeposited nickel |
| MIL-STD-1501 | Electroforming |

## 4.7 Safety and Regulatory

Same as Watts nickel (Section 3.7). Additional note: sulfamate solutions are somewhat less hazardous than Watts due to absence of sulfuric acid and lower chloride, but nickel exposure risks are identical. Hydrolysis products (ammonium sulfate) add ammonia to wastewater — may require attention in wastewater permitting. [DOMAIN]

---

# CLUSTER 5: NICKEL-COBALT PLATING

## 5.1 Process Flow Poster Data

**What is this process?** Nickel-cobalt alloy plating co-deposits nickel and cobalt to produce a coating with enhanced hardness (400-700 HV), superior wear resistance, and improved high-temperature performance compared to pure nickel. Used in aerospace turbine components, magnetic recording media, tooling and dies, and corrosion-resistant engineering coatings.

**Substrates:** Steel, stainless steel (with Wood's strike), copper alloys, Inconel, aerospace superalloys.

**Cobalt content range:** 10-50 wt% Co. Optimal corrosion resistance at ~10% Co. Maximum hardness at ~40-50% Co. [VERIFIED per ResearchGate sources]

**Full process sequence:**
1. Receiving / Racking
2. Alkaline soak clean
3. Rinse
4. Anodic electrocleaning
5. Rinse
6. Acid activation
7. Rinse
8. Wood's nickel strike (for passivating alloys)
9. Rinse
10. Nickel-cobalt plate
11. Rinse
12. Post-plate heat treatment (optional, for hardness increase)
13. Inspection

## 5.2 Cleaning Stage

Same as Watts nickel (Section 3.2). Stringent cleaning required. Organic contamination shifts alloy composition.

## 5.3 Rinse Stages

Same as Watts nickel (Section 3.3).

## 5.4 Activation Stage

Same as Watts nickel (Section 3.4). Wood's strike for passivating alloys.

## 5.5 Main Tank (Plating Bath)

### Bath Chemistry (Modified Watts Type) [VERIFIED]

| Component | Concentration | Purpose |
|---|---|---|
| Nickel sulfate (NiSO4.6H2O) | 200-300 g/L | Nickel ion source |
| Cobalt sulfate (CoSO4.7H2O) | 10-80 g/L (adjust for target alloy) | Cobalt ion source |
| Nickel chloride (NiCl2.6H2O) | 20-40 g/L | Anode dissolution, conductivity |
| Boric acid (H3BO3) | 30-40 g/L | pH buffer |
| Sodium dodecyl sulfate (SDS) | 0.01-0.1 g/L | Wetting agent, reduces porosity |

### Operating Parameters [VERIFIED]

| Parameter | Value |
|---|---|
| Temperature | 104-150 deg F (40-65 deg C); typical 122 deg F (50 deg C) |
| pH | 2.5-5.0; typical 3.5-4.5 |
| Cathode CD | 10-100 ASF (1-10 A/dm2); typical 20-50 ASF (2-5 A/dm2) |
| Voltage | 4-10 V |
| Agitation | Air or mechanical |
| Anode material | Electrolytic nickel; separate cobalt anodes or cobalt salt additions |
| Anode:cathode ratio | 1:1 to 2:1 |
| Cathodic efficiency | 85-95% |
| Plating rate at 30 ASF | ~0.7-0.9 mil/hr (~18-23 microns/hr) [DOMAIN] |

### Alloy Control [VERIFIED]

Cobalt content in the deposit is controlled by:
- Co:Ni ratio in solution (primary factor)
- Current density (higher CD tends to deposit more Co)
- pH (lower pH favors Co deposition)
- Temperature (higher temperature slightly reduces Co%)

The phenomenon of "anomalous co-deposition" (the less-noble metal deposits preferentially) does NOT apply to Ni-Co as strongly as it does to Zn-Ni. Ni-Co deposition is relatively normal (deposit composition roughly tracks solution composition). [DOMAIN]

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| Low cobalt in deposit | Low CoSO4, high pH, low CD | Add cobalt salt, adjust pH, increase CD |
| Brittleness | Co% too high (>50%), organic contamination | Reduce Co salt, carbon treat |
| Roughness | Particles, poor filtration | Filter, anode bags |
| Cracking | Excessive internal stress at high Co% | Heat treat post-plate; or reduce Co% |
| Pitting | Low wetting agent | Add SDS or proprietary anti-pit |

## 5.6 Post Treatment

**Heat treatment:** NiCo deposits can be heat treated at 600-800 deg F (315-427 deg C) for 1-4 hours to increase hardness from ~400 HV to 600-700 HV. [DOMAIN]

**No chromate needed** — the NiCo alloy is inherently corrosion-resistant.

### Applicable Specifications
- AMS 2403 (nickel plating, general)
- Customer/OEM-specific aerospace specifications
- No widely adopted ASTM specification specifically for NiCo alloy plating [FLAG — verify if newer ASTM or AMS covers NiCo specifically]

## 5.7 Safety and Regulatory

**Key hazards:**
- Nickel compounds: skin sensitizer, respiratory carcinogen (see Section 3.7)
- Cobalt compounds: skin sensitizer; IARC Group 2B (possibly carcinogenic); respiratory hazard
- Both nickel and cobalt require biological monitoring for chronic exposure
- Cobalt discharge limits in wastewater are stringent where established

**PPE:** Same as nickel plating plus attention to cobalt-specific exposure limits (OSHA PEL for cobalt: 0.1 mg/m3 TWA).

---

# CLUSTER 6: CHROME PLATING (DECORATIVE / TRIVALENT)

## 6.1 Process Flow Poster Data

**What is this process?** Decorative trivalent chromium plating deposits a thin (0.005-0.05 mil / 0.13-1.3 microns) chromium layer from a Cr(III) electrolyte. It provides the characteristic "chrome look" — bright, reflective, blue-white — with dramatically reduced toxicity compared to hexavalent chromium. Almost always applied over bright nickel (duplex or triple nickel systems for automotive). Trivalent chrome is now the standard for decorative applications due to RoHS, REACH, and OEM mandates.

**Substrates:** Bright nickel plated surfaces (steel, zinc die cast, ABS plastic after electroless Cu/Ni, copper alloys). The chrome is applied over nickel — it does not plate directly on bare steel in decorative applications.

**Two trivalent system types:**
- **Chloride-based:** Faster plating, matches hex chrome speed; graphite or mixed-metal-oxide (MMO) anodes
- **Sulfate-based:** Slower but wider operating window; lead or catalytic anodes; lower corrosion in some tests

**Full process sequence (decorative nickel-chrome on steel):**
1. Part is already bright nickel plated (see Cluster 3)
2. Post-nickel rinse
3. Chromium plate (trivalent)
4. Rinse (multiple)
5. DI water final rinse
6. Hot air dry
7. Inspection (appearance, adhesion, CASS test, thickness if required)

**Note:** Trivalent decorative chrome is typically self-limiting — the deposit reaches maximum thickness (0.3-0.8 microns typical) and then slows dramatically. This is a characteristic feature, not a defect.

## 6.2 Cleaning Stage

**Not applicable in the traditional sense.** The part arrives at the chrome tank already fully cleaned and nickel-plated. The key requirement is that the nickel surface must be ACTIVE — transfer from nickel rinse to chrome must occur within 30-60 seconds maximum. If the nickel surface passivates (air exposure, slow transfer), an activation dip in dilute acid (1-3% HCl or proprietary activator) may be needed. [DOMAIN]

## 6.3 Rinse Stages

**Pre-chrome rinse:** Quick rinse after nickel; DI or clean municipal water. Purpose: prevent nickel dragout into chrome bath (Ni contamination in chrome bath causes haze and adhesion loss).

**Post-chrome rinse:** Triple rinse minimum. Chrome baths have high dragout. First rinse is a static dragout tank for recovery. Second and third are flowing.

**DI water:** Required for final rinse to prevent water spots.

## 6.4 Activation Stage

**Pre-chrome activation (if needed):**
- 1-3% HCl, 5-15 seconds, room temperature
- Or proprietary activator per chrome supplier
- Only needed if transfer time from nickel exceeds ~60 seconds

## 6.5 Main Tank (Plating Bath)

### Trivalent Chromium Bath Chemistry [VERIFIED]

| Component | Chloride System | Sulfate System |
|---|---|---|
| Chromium (as Cr3+) | 5-20 g/L (typical 10-15 g/L) | 5-20 g/L (typical 10-15 g/L) |
| Chromium source | Chromium chloride (CrCl3.6H2O) | Chromium sulfate [Cr2(SO4)3] |
| Complexing agent | Glycine, formic acid, or proprietary | Glycine, formic acid, or proprietary |
| Conductivity salt | Potassium or ammonium chloride (100-200 g/L) | Sodium or potassium sulfate (50-150 g/L) |
| Buffer | Boric acid (30-45 g/L) | Boric acid (30-45 g/L) |
| Wetting agent | Proprietary | Proprietary |

### Operating Parameters [VERIFIED]

| Parameter | Chloride System | Sulfate System |
|---|---|---|
| Temperature | 85-115 deg F (29-46 deg C); typical 95-105 deg F (35-40 deg C) | 85-115 deg F (29-46 deg C) |
| pH | 2.7-3.8; typical 3.0-3.5 | 2.7-3.8; typical 3.0-3.5 |
| Cathode CD | 50-200 ASF (5.4-21.5 A/dm2); typical 75-125 ASF (8-13.5 A/dm2) | 50-150 ASF (5.4-16 A/dm2); typical 75-100 ASF |
| Voltage | 5-10 V | 6-12 V |
| Plating time | 2-8 minutes (self-limiting) | 3-10 minutes (slower) |
| Agitation | Cathode bar movement; solution flow; air sparging avoided (oxidation risk) | Same |
| Anode material | Graphite or MMO-coated titanium | Lead alloy (Pb-Sn) or catalytic |
| Anode:cathode ratio | 1:1 to 3:1 | 2:1 to 4:1 |
| Cathodic efficiency | 15-25% (chloride); up to 35% at low CD | 10-20% |

**Plating rate (chloride system):** 0.1-0.25 microns/min. Self-limits at ~0.3-0.8 microns. [VERIFIED]
**Plating rate (sulfate system):** 0.04-0.08 microns/min. [VERIFIED]

### Critical Bath Maintenance [DOMAIN]

| Issue | Threshold | Effect | Corrective |
|---|---|---|---|
| Cr(VI) formation (oxidation at anode) | Any detectable Cr6+ | Yellowing, haze, health hazard | Graphite/MMO anodes prevent this; sulfate systems use shielded anodes |
| Nickel contamination | >100 ppm | Haze, adhesion loss | Reduce dragout; partial bath dump |
| Iron contamination | >200 ppm | Darkening, roughness | Raise pH to 4.0, filter precipitate, re-adjust |
| Copper contamination | >20 ppm | Dark deposits, discoloration | Dummy plate at low CD |
| Trivalent chrome depletion | <5 g/L Cr3+ | Thin deposits, poor coverage | Add Cr replenisher per supplier |

### Color Limitations [DOMAIN]
Trivalent chrome produces a slightly darker, more "stainless steel" appearance compared to the blue-white brightness of hexavalent chrome. This is due to the thinner deposit and different crystal structure. Color matching between hex and tri processes requires careful specification — they are NOT identical in appearance.

## 6.6 Post Treatment

**Typically none.** Decorative trivalent chrome is the final layer. No chromate or seal is applied over chrome.

**Special:** Some OEMs require a clear anti-fingerprint topcoat on chrome-plated parts.

### Applicable Specifications
- ASTM B456 (electrodeposited coatings of nickel plus chromium)
- ASTM B368 (CASS test for decorative chromium)
- GM 4346M, Ford WSS-M1P85-A (automotive decorative chrome)
- No specific separate ASTM for trivalent vs. hexavalent — both fall under B456

## 6.7 Safety and Regulatory

**Key advantage of trivalent:** Cr(III) is not classified as carcinogenic. It is a mild irritant. No OSHA PEL concerns at the level of hex chrome.

Compare:
- Cr(VI) OSHA PEL: 5 micrograms/m3 (extremely low; practically impossible in open plating)
- Cr(III): No specific OSHA PEL; regulated as "nuisance particulate" at 15 mg/m3

**Regulatory:** Trivalent chrome is RoHS and REACH compliant. No special wastewater permit for Cr(III) in most jurisdictions — treat as a heavy metal (hydroxide precipitation at pH 8-9). [VERIFIED]

---

# CLUSTER 7: HARD CHROME PLATING (HEXAVALENT)

## 7.1 Process Flow Poster Data

**What is this process?** Hard chrome (industrial chrome, functional chrome) deposits thick chromium (typically 0.2-20 mils / 5-500 microns) from a hexavalent chromium (CrO3 + H2SO4) bath. It produces the hardest electroplated coating available (800-1000 HV), with exceptional wear resistance, low coefficient of friction, and excellent corrosion resistance when sufficiently thick. Used on hydraulic cylinders, piston rings, mold surfaces, printing rolls, gauges, aircraft landing gear, gun barrels, and industrial tooling.

**Substrates:** Steel (most common), stainless steel, cast iron, copper alloys, aluminum (with special pre-treatment). High-strength steel is common — HE baking is almost always required.

**Full process sequence:**
1. Receiving / Racking (specialized fixturing for uniform current distribution)
2. Vapor degreasing or alkaline soak clean
3. Rinse
4. Anodic etch (reverse current in chrome bath or separate H2SO4 etch)
5. Hard chrome plate
6. Rinse (triple: drag-out recovery + double counterflow)
7. HE bake (almost always required — most hard chrome substrates are high-strength)
8. Grind/hone to final dimension (if required)
9. Inspection (thickness, hardness, adhesion, crack pattern if specified)

**Note:** Hard chrome shops often skip separate electrocleaning and acid activation — the etch cycle (anodic in the chrome bath itself for 30-120 seconds) serves as both activation and cleaning.

## 7.2 Cleaning Stage

**Preferred method:** Vapor degreasing (for heavy oils/coolants) or alkaline soak clean. Electrocleaning is used in some shops but less universally than in nickel plating.

**Alkaline clean (if used):**
- 4-8 oz/gal (30-60 g/L), 140-180 deg F (60-82 deg C), 3-5 min
- Must be thoroughly rinsed to prevent chromate formation of sodium chromate in the bath

**Anodic etch in chrome bath:** [VERIFIED]
- Part is made anodic (reversed polarity) in the chrome bath for 30-120 seconds at 100-200 ASF
- This simultaneously cleans the surface, removes passive films, and heats the part to bath temperature
- Avoids the need for separate acid activation
- Standard practice in most hard chrome shops

## 7.3 Rinse Stages

**Pre-plate rinse:** If separate cleaning is used, rinse thoroughly. If anodic etch is done in the chrome bath, no pre-plate rinse is needed.

**Post-plate rinse:** CRITICAL. Chrome bath dragout contains hexavalent chromium — a regulated carcinogen.
- Static drag-out tank (recovery — return to bath)
- Double or triple counterflow rinse
- DI water final rinse recommended for precision parts

**Drag-out reduction:** Chrome baths have high surface tension. Drag-out is heavy. Wetting agents (fume suppressants, typically PFAS-free fluorosurfactants) reduce surface tension and dragout. [DOMAIN]

## 7.4 Activation Stage

**Anodic etch in chrome bath (standard method):**
- 100-200 ASF (10.8-21.5 A/dm2) anodic for 30-120 seconds
- Dissolves ~0.05-0.1 mil surface material
- Generates fresh, active surface

**Separate acid activation (alternative):**
- 20-50% HCl, 15-60 seconds, room temperature
- Used when anodic etch is not feasible (complex geometries)

**For stainless steel substrates:** Anodic etch in chrome is usually sufficient. Some specs require a Wood's nickel strike before chrome.

## 7.5 Main Tank (Plating Bath)

### Bath Chemistry [VERIFIED]

| Component | Conventional Bath | High-Concentration Bath |
|---|---|---|
| Chromic acid (CrO3) | 200-250 g/L (26-33 oz/gal) | 300-400 g/L (40-53 oz/gal) |
| Sulfuric acid (H2SO4) | 2.0-2.5 g/L | 3.0-4.0 g/L |
| CrO3:SO4 ratio (by weight) | 100:1 (standard "Sargent bath") | 75:1 to 100:1 |
| Trivalent chromium (Cr3+) | 1-3 g/L (must be present) | 2-5 g/L |
| Total chromium (as CrO3 equivalent) | Same as CrO3 concentration | Same |

**Mixed catalyst baths:** Some proprietary formulations use combinations of sulfate and fluoride (or fluorosilicate) catalysts for improved throwing power and efficiency. Fluoride catalyst concentration: 0.5-3 g/L as F. These are called "SRHS" (self-regulating high-speed) baths. [DOMAIN]

### Operating Parameters [VERIFIED]

| Parameter | Value |
|---|---|
| Temperature | 120-145 deg F (49-63 deg C); typical 130-135 deg F (54-57 deg C) |
| Cathode CD | 150-400 ASF (16-43 A/dm2); typical 200-300 ASF (22-32 A/dm2) |
| Voltage | 6-12 V (higher for complex geometries) |
| Agitation | Solution flow; mechanical; NO air agitation (blows Cr6+ mist) |
| Anode material | Lead alloy (Pb-6%Sn or Pb-7%Sn); or platinized titanium |
| Anode:cathode ratio | 2:1 to 3:1 (conforming anodes preferred for uniform thickness) |
| Filtration | Continuous, 10-25 micron; must handle lead particles |

### Efficiency and Plating Rate [VERIFIED]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 10-18% (very low — most current goes to hydrogen evolution and Cr3+ formation) |
| Plating rate at 200 ASF | ~1.0-1.5 mil/hr (25-38 microns/hr) for conventional; up to 2.0 mil/hr for SRHS |
| Plating rate at 300 ASF | ~1.5-2.2 mil/hr (38-56 microns/hr) |

### CrO3:SO4 Ratio Control [VERIFIED]
This ratio is THE critical control parameter in hard chrome.

- Ratio too high (>125:1, sulfate too low): Poor coverage, milky deposits, poor hardness
- Ratio too low (<75:1, sulfate too high): Poor throwing power, burning, pitting, reduced efficiency
- Optimal: 80:1 to 100:1 for most applications
- Sulfate addition: dilute H2SO4
- Sulfate removal: barium carbonate (BaCO3) — precipitates BaSO4

### Trivalent Chrome (Cr3+) Control [VERIFIED]
- Must be present at 1-3% of total CrO3 (typically 2-5 g/L)
- Too low: poor throwing power, burning
- Too high (>5% of CrO3): dramatically reduced efficiency, dull deposits, reduced hardness
- Reduce Cr3+: dilution, or electrolytic oxidation with high anode area
- Increase Cr3+: add sugar (sucrose) or proprietary reducer

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| Burning (brown/black at HCD) | Too high CD, too low temp, too high Cr3+, sulfate too high | Reduce CD, raise temp, reduce Cr3+, check ratio |
| Milky/hazy deposit | CrO3:SO4 ratio too high (low sulfate), low temperature | Add H2SO4, raise temp |
| Poor coverage at LCD | Low CrO3, poor ratio, high Cr3+, cold bath | Increase CrO3, correct ratio, reduce Cr3+, raise temp |
| Pitting | Contamination (Fe, Cu), gas pitting from poor current distribution | Remove contaminants, use conforming anodes, fume suppressant |
| Roughness | Particulates from lead anodes, bath contamination | Filter, maintain anodes, check for metallic contaminants |
| Poor adhesion / peeling | Inadequate etch, passive substrate, poor current reversal | Extend anodic etch time, check etch current |
| Excessive micro-cracking | Inherent in hard chrome; density depends on deposit thickness and bath type | Not a defect per se — micro-cracked chrome is often specified for oil retention |

### Contamination [DOMAIN]

| Contaminant | Threshold | Effect | Removal |
|---|---|---|---|
| Iron | >5-10 g/L | Reduced efficiency, dull deposits | Porous pot electrolysis or partial dump |
| Copper | >200 ppm | Dark spots, discoloration | Dummy plate; porous pot |
| Trivalent chrome (excess) | >5% of CrO3 | Severe efficiency loss | Dilute, or electrolyze with large anode area |
| Chloride | >200 ppm | Pitting, anode attack | Precipitate with silver (expensive) or dilute |
| Organic (oil, wetting agent excess) | Any significant | Cr3+ buildup, reduced efficiency | Oxidize by running bath at high temp with high anode area |

## 7.6 Post Treatment

### Hydrogen Embrittlement Baking [VERIFIED]
Hard chrome plating generates massive hydrogen. HE baking is almost always required:
- Temperature: 375 deg F (191 deg C) minimum, up to 430 deg F (220 deg C) for critical aerospace parts
- Time: 8-24 hours depending on hardness (see ASTM B850 schedule in Section 1.6)
- Must commence within 1-4 hours of plating
- Aerospace (AMS 2406, AMS 2460): typically 23 hours at 375 deg F

### Grinding/Honing
Hard chrome deposits are ground or honed to final dimension. Chrome is too hard (HV 800-1000) for conventional machining. Diamond or CBN grinding wheels are standard.

### Applicable Specifications

| Specification | Coverage |
|---|---|
| AMS 2406 | Hard chrome plating (aerospace) |
| AMS 2460 | Hard chrome, low hydrogen embrittlement |
| ASTM B177 | Engineering chromium plating |
| QQ-C-320 | Chrome plating (federal, superseded but still referenced) |
| MIL-STD-1501 | Chromium plating requirements |
| ASTM B850 | HE relief |

## 7.7 Safety and Regulatory

**THIS IS THE MOST HAZARDOUS COMMON PLATING PROCESS.** [VERIFIED]

**Hexavalent chromium (Cr6+):**
- IARC Group 1 carcinogen (confirmed human lung carcinogen via inhalation)
- OSHA PEL: 5 micrograms/m3 (8-hour TWA) — extremely stringent
- OSHA Action Level: 2.5 micrograms/m3
- EPA: listed hazardous waste (D007)
- EU REACH: Annex XIV (authorization required)
- RoHS: restricted substance

**Required controls:**
- Full enclosure or lip exhaust with mist eliminators (mesh pad, packed bed, or HEPA)
- Fume suppressants mandatory (PFAS-free required in many jurisdictions)
- Full face respirator with P100 cartridge or supplied air for maintenance operations
- Chemical-resistant full suits for tank maintenance
- Dedicated chrome room with contained drainage
- Biological monitoring: urinary chromium for exposed workers
- Medical surveillance program

**Wastewater:**
- Cr6+ must be reduced to Cr3+ before discharge
- Standard reduction: sodium metabisulfite (Na2S2O5) or ferrous sulfate at pH <3
- Then hydroxide precipitation at pH 8-9 as Cr(OH)3
- EPA discharge limit: 0.5 mg/L total Cr (daily max); 0.2 mg/L monthly average (40 CFR 433)

---

# CLUSTER 8: COPPER PLATING (ACID SULFATE)

## 8.1 Process Flow Poster Data

**What is this process?** Acid copper sulfate plating deposits copper from an acidic electrolyte (CuSO4 + H2SO4). It produces bright, highly leveled deposits with excellent throwing power (with modern brightener systems). Used for decorative plating (automotive, plumbing fixtures over Ni), printed circuit boards (PCB through-hole and via fill), electroforming, EMI/RFI shielding, and as a base layer for further plating.

**Substrates:** Steel (requires copper cyanide strike first — cannot plate acid Cu directly on steel), copper (including PCB substrates), brass, zinc die cast (after cyanide Cu strike), ABS plastic (after electroless Cu or Ni).

**CRITICAL:** Acid copper CANNOT be plated directly on steel or zinc. An immersion displacement reaction would occur, depositing loose, non-adherent copper. A cyanide copper strike (or alkaline non-cyanide copper strike) must be applied first. [VERIFIED]

**Full process sequence (on steel):**
1. Receiving / Racking
2. Alkaline soak clean
3. Rinse
4. Electrocleaning (anodic)
5. Rinse
6. Acid activation (HCl dip)
7. Rinse
8. Cyanide copper strike (or alkaline non-cyanide copper)
9. Rinse (drag-out + overflow)
10. Acid copper plate
11. Rinse (drag-out + overflow)
12. Next process (Ni plate, chrome, etc.) or anti-tarnish
13. Inspection

## 8.2 Cleaning Stage

Standard alkaline soak clean + anodic electrocleaning (see Section 1.2 or 3.2). The copper strike provides additional cleaning action (the cyanide copper bath itself is mildly cleaning), but thorough pre-cleaning is still essential.

## 8.3 Rinse Stages

**Pre-plate rinse (after strike):** Double counterflow. Must remove all cyanide residue from the strike bath before entering the acid copper. Cyanide contamination in acid copper causes gas evolution and poor deposits. In most process lines, there is an acid dip (5-10% H2SO4) between the strike rinse and the acid copper tank to neutralize any residual cyanide alkalinity and prevent immersion copper on the strike surface. [DOMAIN]

**Post-plate rinse:** Double counterflow. Copper dragout stains parts blue-green if not rinsed properly. Anti-tarnish dip (benzotriazole, BTA) may be used after rinse.

## 8.4 Activation Stage

**Before cyanide copper strike:**
- 10-30% HCl, 15-30 sec, room temperature (standard steel activation)

**Between strike and acid copper:**
- 5-10% H2SO4, 15-30 sec — neutralizes alkaline film and prevents immersion copper

## 8.5 Main Tank (Plating Bath)

### Bath Chemistry [VERIFIED]

| Component | Low (PCB/general) | Typical | High (high-throw decorative) |
|---|---|---|---|
| Copper sulfate (CuSO4.5H2O) | 150 g/L (20 oz/gal) | 200-225 g/L (27-30 oz/gal) | 250 g/L (33 oz/gal) |
| Copper metal (as Cu) | 38 g/L | 50-56 g/L | 63 g/L |
| Sulfuric acid (H2SO4) | 30 g/L (4 oz/gal) | 50-75 g/L (7-10 oz/gal) | 300 g/L (PCB high-throw formulations) |
| Chloride (as Cl-) | 30 mg/L (ppm) | 50-80 mg/L (ppm) | 150 mg/L (ppm) |
| Brightener system (suppressor + accelerator + leveler) | Per supplier TDS | | |

**Note on H2SO4 range:** High-acid/low-copper formulations (30-50 g/L Cu, 150-300 g/L H2SO4) are used for PCB plating where throwing power into through-holes is critical. Standard decorative uses higher copper and lower acid. [VERIFIED]

### Operating Parameters [VERIFIED]

| Parameter | Value |
|---|---|
| Temperature | 70-90 deg F (21-32 deg C); typical 75-80 deg F (24-27 deg C) for decorative; up to 110 deg F (43 deg C) for PCB high-speed |
| pH | Not meaningful (strongly acidic; pH ~0-1) |
| Cathode CD (rack) | 10-50 ASF (1.1-5.4 A/dm2); typical 20-30 ASF (2.2-3.2 A/dm2) |
| Cathode CD (barrel) | 5-15 ASF (0.5-1.6 A/dm2) |
| Cathode CD (PCB) | 15-30 ASF (1.6-3.2 A/dm2) standard; up to 40 ASF with pulse |
| Voltage | 1-6 V (acid copper has very high conductivity) |
| Agitation | Air agitation (oil-free) for rack/barrel; solution flow + cathode bar movement for PCB |
| Anode material | Phosphorized copper (0.04-0.06% P); or solid copper bars |
| Anode:cathode ratio | 1:1 to 2:1 |
| Filtration | Continuous, 5-10 micron; carbon core canister for organics |

### Efficiency and Plating Rate [VERIFIED]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 97-100% |
| Anode efficiency | ~100% with phosphorized anodes (P forms black film that prevents passivation) |
| Plating rate at 20 ASF | ~0.5 mil/hr (12.7 microns/hr) |
| Plating rate at 30 ASF | ~0.75 mil/hr (19 microns/hr) |

### Chloride Ion Control [VERIFIED]
- Chloride is essential for brightener system activity
- Too low (<30 ppm): Dull deposits, brightener system inactive, "skip" in LCD areas
- Too high (>150 ppm): Matte deposits, roughness, anode passivation (CuCl precipitates on anodes)
- Ideal range: 50-80 ppm (center 60 ppm)
- Add as NaCl or HCl (1 mL/L of HCl adds ~35 ppm Cl-)
- Remove excess: not easily removed; dilution is the standard approach

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| Dull deposits | Low brightener, low Cl-, low temperature, organic contamination | Add brightener, check Cl-, raise temp, carbon treat |
| Roughness | Particulates, anode sludge, high Cu metal | Filter, anode bags, reduce CuSO4 |
| Pitting | Low agitation, organic contamination, particles | Increase air, carbon treat, filter |
| Skip plating at LCD | Low Cl-, low acid, depleted brightener | Correct Cl-, add H2SO4, replenish brightener |
| Burned/dark HCD | Very high CD, low Cu metal, low acid | Reduce CD, add CuSO4, add H2SO4 |
| Immersion copper (non-adherent) | Plating on unstriked steel or zinc | MUST use copper strike first |
| Anode passivation | High Cl- (>200 ppm), low P content in anodes, heavy anode film | Reduce Cl-, replace anodes, clean anode bags |
| Treeing/nodules | Organic breakdown, high CD + depleted leveler | Carbon treat, add leveler, reduce CD |

### Hull Cell Interpretation [DOMAIN]
- 267 mL, 2A, 5-10 min at bath temperature
- **Good panel:** Bright and level 5-50 ASF, slight matte at extreme LCD
- **Low accelerator:** Dull mid-range, slight haze
- **Low suppressor:** Bright but rough, possible nodulation
- **Low leveler:** Bright but uneven thickness, treeing at HCD
- **Low chloride:** Entirely dull panel; brightener system non-functional

## 8.6 Post Treatment

**Anti-tarnish:** Benzotriazole (BTA) dip, 0.1-0.5 g/L, 15-30 sec, room temperature. Forms a protective organic film. Required if copper is the final finish or if parts will be stored before further plating. [DOMAIN]

**Chromate conversion (rarely used on copper):** Possible for corrosion protection but uncommon in decorative lines.

**HE baking:** Not typically required for acid copper — the process operates at near-100% efficiency with minimal hydrogen evolution. Exception: if the substrate is high-strength steel that was earlier acid-activated and cyanide-struck, the bake requirement comes from THOSE steps, not the acid copper itself.

### Applicable Specifications

| Specification | Coverage |
|---|---|
| ASTM B734 | Electrodeposited copper for engineering applications |
| AMS 2418 | Copper plating (aerospace) |
| IPC-6012 | Rigid PCB qualification (copper plating thickness requirements) |
| MIL-C-14550 | Copper plating (federal) |

## 8.7 Safety and Regulatory

**Key hazards:**
- Sulfuric acid: corrosive, severe burn hazard
- Copper sulfate: toxic by ingestion; skin and eye irritant
- Chloride (as HCl fumes): respiratory irritant at high concentrations
- Brightener organics: varies; generally low acute toxicity

**PPE:** Acid-resistant gloves (nitrile), splash goggles, face shield for bath maintenance, rubber apron.

**Wastewater:** Copper hydroxide precipitation at pH 8.5-9.5. Copper discharge limits are typically 0.5-3.38 mg/L (40 CFR 433). Chelated copper (from dragout of cyanide strike) can be very difficult to precipitate — require sulfide precipitation or ion exchange. [DOMAIN]

---

# CLUSTER 9: COPPER PLATING (ALKALINE NON-CYANIDE)

## 9.1 Process Flow Poster Data

**What is this process?** Alkaline non-cyanide copper plating is a cyanide-free alternative for depositing copper onto steel, zinc die cast, and other substrates that cannot accept acid copper directly. It operates at alkaline pH (8-13 depending on formulation) using complexing agents (pyrophosphate, HEDP, citrate, tartrate, or proprietary chelants) to keep copper in solution. It replaces cyanide copper strike in environmentally conscious operations.

**Substrates:** Steel, zinc die cast, brass, aluminum (after zincate), powdered metal. The primary application is as a strike/underplate before acid copper or further plating.

**Two main types:**

**Type 1 — Copper pyrophosphate:** [VERIFIED]
- pH 8-9; moderate alkalinity
- Well-established technology (decades of use)
- Good leveling and throwing power
- Relatively narrow operating window

**Type 2 — Copper HEDP or proprietary chelant:** [VERIFIED]
- pH 9-13; strongly alkaline
- Newer technology; directly replaces cyanide strike
- Simpler to operate
- Can plate directly on steel at high pH (>12) without immersion displacement

**Full process sequence:**
1. Receiving / Racking
2. Alkaline soak clean
3. Rinse
4. Electrocleaning (anodic)
5. Rinse
6. Acid activation (mild — 5-10% H2SO4 or proprietary)
7. Rinse
8. Alkaline non-cyanide copper strike/plate
9. Rinse
10. Acid dip (if proceeding to acid copper)
11. Acid copper plate (or proceed to Ni/other)
12. Continue process sequence

## 9.2 Cleaning Stage

Standard (Section 1.2 / 3.2). Same requirements as cyanide copper — thorough cleaning is essential. Unlike cyanide copper, the alkaline non-cyanide bath does NOT have the "self-cleaning" action of high-cyanide baths, so pre-cleaning must be more rigorous. [DOMAIN]

## 9.3 Rinse Stages

**Pre-plate:** Single overflow minimum. Must remove all acid from activation before entering alkaline copper bath.

**Post-plate:** Double counterflow. If proceeding to acid copper, an acid dip (5-10% H2SO4) follows the post-copper rinse to neutralize alkaline film.

## 9.4 Activation Stage

**For steel:** 5-10% H2SO4 or 5-10% HCl, 15-30 sec, room temperature. Mild activation preferred — the high-pH copper bath will finish activation.

**For zinc die cast:** 1-3% HF (hydrofluoric acid) or proprietary non-HF de-smut. Zinc die cast has an oxide/smut layer that must be removed. Some alkaline non-cyanide copper baths include a built-in activation step (the first 10-30 sec at high current). [DOMAIN]

## 9.5 Main Tank (Plating Bath)

### Copper Pyrophosphate Bath [VERIFIED]

| Component | Concentration | Purpose |
|---|---|---|
| Copper pyrophosphate [Cu2P2O7.3H2O] | 53-84 g/L (7-11 oz/gal) | Copper source |
| Potassium pyrophosphate [K4P2O7] | 200-350 g/L (27-47 oz/gal) | Complexant, conductivity |
| Ammonium hydroxide (NH4OH) | 1-5 mL/L | Anode corrosion aid, grain refiner |
| Potassium nitrate (KNO3) | 5-15 g/L | Depolarizer, reduces cathode polarization |
| Copper metal | 22-34 g/L | |
| P2O7:Cu ratio | 7:1 to 8:1 (weight) | Critical control ratio |

### Copper HEDP/Chelant Bath [VERIFIED]

| Component | Concentration | Purpose |
|---|---|---|
| Copper sulfate or copper carbonate | 5-30 g/L as Cu metal | Copper source |
| HEDP (1-hydroxyethylidene-1,1-diphosphonic acid) | 50-100 g/L | Primary chelant |
| Auxiliary chelant (citrate, tartrate) | 10-30 g/L | Co-complexant |
| Sodium or potassium hydroxide | 30-80 g/L | pH control, conductivity |
| Conductive salt (K2CO3 or KNO3) | 15-30 g/L | Conductivity |

### Operating Parameters

| Parameter | Pyrophosphate | HEDP/Chelant |
|---|---|---|
| Temperature | 100-140 deg F (38-60 deg C); typical 120-130 deg F (49-54 deg C) | 100-160 deg F (38-71 deg C); typical 120-140 deg F (49-60 deg C) |
| pH | 8.0-9.0 | 9.0-13.0; strike at pH 12-13; plate at pH 9-11 |
| Cathode CD | 10-80 ASF (1.1-8.6 A/dm2); typical 20-40 ASF | 5-30 ASF (0.5-3.2 A/dm2); typical 10-20 ASF |
| Voltage | 3-8 V | 3-8 V |
| Agitation | Air or mechanical | Air or mechanical |
| Anode material | Copper (OFHC or phosphorized) | Copper (OFHC) or insoluble (MMO/platinized Ti) |
| Anode:cathode ratio | 1:1 to 2:1 | 1:1 to 2:1 |
| Cathodic efficiency | 70-90% (pyrophosphate) | 30-70% (HEDP; varies widely with CD) |

### Analytical Methods [DOMAIN]
- Copper metal: iodometric titration (Na2S2O3 / starch indicator) or EDTA
- Free pyrophosphate: acid titration method (specific to pyrophosphate baths)
- pH: calibrated meter
- P2O7:Cu ratio: calculate from above analyses — this is the primary control ratio
- Hull cell: 267 mL, 1-2A, 5-10 min

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| No adhesion on steel | pH too low (immersion copper forms), insufficient CD at start | Raise pH for strike step, ensure live entry (current on before part enters) |
| Immersion copper | pH <10 on active metals, low CD | Increase pH, use live entry |
| Dull deposits | Low temperature, depleted brightener (if used) | Raise temp, add organic additives |
| Roughness | Particulates, orthophosphate buildup (pyro bath) | Filter, monitor ortho:pyro ratio |
| Poor throwing power | P2O7:Cu ratio out of range | Correct ratio to 7:1-8:1 |
| Orthophosphate buildup (pyro) | Hydrolysis at high temp or low pH | Maintain pH >8, temp <140 deg F; partial bath dump if ortho >100 g/L |

## 9.6 Post Treatment

Alkaline non-cyanide copper is almost always an intermediate layer. No post-treatment specific to this step — proceed to acid copper, nickel, or other plating.

### Applicable Specifications
No unique ASTM or AMS specification for alkaline non-cyanide copper specifically. Copper coatings are covered by:
- ASTM B734 (electrodeposited copper)
- AMS 2418 (copper plating)
- MIL-C-14550 (copper plating)

## 9.7 Safety and Regulatory

**Advantage:** Eliminates cyanide — the primary motivation for this process.

**Hazards:**
- Alkaline solutions (NaOH/KOH at pH 12-13): severe burn hazard
- Copper compounds: toxic by ingestion; aquatic toxicity
- Pyrophosphate: low acute toxicity; phosphate loading in wastewater
- HEDP: low toxicity; chelates heavy metals in wastewater (makes downstream treatment harder)

**Wastewater:** Copper precipitation at pH 8.5-9.5. HEDP and pyrophosphate are chelants — they keep copper in solution through standard hydroxide precipitation. May require sulfide precipitation (Na2S or NaHS), electrowinning, or ion exchange to meet copper discharge limits. [DOMAIN]

---

# CLUSTER 10: TIN PLATING (ACID / MSA)

## 10.1 Process Flow Poster Data

**What is this process?** Acid tin plating from methanesulfonic acid (MSA) electrolyte deposits bright or matte tin coatings. Tin provides excellent solderability, corrosion resistance in food-contact applications, low contact resistance for electrical connectors, and whisker-resistant coatings (with proper alloy or mitigation). MSA-based baths have largely replaced older fluoborate and sulfate tin baths due to environmental advantages and superior performance.

**Substrates:** Steel (tinplate for food cans), copper and copper alloys (electrical connectors, bus bars), nickel-plated surfaces, lead frames.

**Full process sequence:**
1. Receiving / Racking or reeling (continuous strip)
2. Alkaline soak clean
3. Rinse
4. Electrocleaning (anodic)
5. Rinse
6. Acid activation (5-10% H2SO4 or MSA dip)
7. Rinse
8. Tin plate (acid MSA)
9. Rinse (drag-out + overflow)
10. Hot water rinse / dry (or reflow for bright matte tin)
11. Inspection (thickness, solderability, porosity, whisker assessment if required)

## 10.2 Cleaning Stage

Standard alkaline clean + anodic electrocleaning. Tin plating on copper connectors requires removal of all oxide and organic residues. Copper oxides cause poor adhesion and solder rejection.

For continuous strip (tinplate steel): in-line alkaline spray clean and electrocleaning at high speed.

## 10.3 Rinse Stages

**Pre-plate:** Single overflow after acid activation. MSA baths tolerate some acid dragout (MSA is the bath acid anyway).

**Post-plate:** Double counterflow. Tin solutions stain if not rinsed quickly.

**DI water:** Recommended for final rinse on electronics components to prevent ionic contamination.

## 10.4 Activation Stage

**For copper substrates:** 5-10% H2SO4, 15-30 sec, room temperature. Or 5-10% MSA (methanesulfonic acid).

**For steel:** 10-20% HCl, 15-30 sec. Or 5-10% H2SO4.

**For nickel-plated surfaces:** 5% H2SO4, 10-15 sec (light activation only).

**Critical:** Tin baths are sensitive to copper contamination from dissolution of copper substrates. Minimize acid dip time on copper parts to prevent excessive dissolution and copper dragout into the tin bath. [DOMAIN]

## 10.5 Main Tank (Plating Bath)

### MSA Tin Bath Chemistry [VERIFIED]

| Component | Low-Speed (rack) | Typical | High-Speed (strip) |
|---|---|---|---|
| Stannous tin (Sn2+) as stannous methanesulfonate | 15-25 g/L (2-3.3 oz/gal) | 30-50 g/L (4-6.7 oz/gal) | 50-80 g/L (6.7-10.7 oz/gal) |
| Free methanesulfonic acid (MSA) | 100-150 g/L (13-20 oz/gal) | 130-200 g/L (17-27 oz/gal) | 150-250 g/L |
| Antioxidant (hydroquinone, catechol, or proprietary) | 0.5-2 g/L | 1-2 g/L | 1-3 g/L |
| Grain refiner / brightener | Per supplier TDS | | |
| Wetting agent | 0.5-3 mL/L | | |

### Operating Parameters [VERIFIED]

| Parameter | Value |
|---|---|
| Temperature | 60-100 deg F (16-38 deg C); typical 70-85 deg F (21-29 deg C) for rack; up to 120 deg F (49 deg C) for high-speed strip |
| pH | Not applicable (strongly acidic, pH <1) |
| Cathode CD (rack) | 10-30 ASF (1.1-3.2 A/dm2) |
| Cathode CD (barrel) | 5-15 ASF (0.5-1.6 A/dm2) |
| Cathode CD (strip, high-speed) | 50-200+ ASF (5.4-21.5 A/dm2) |
| Voltage | 1-5 V |
| Agitation | Air (oil-free) or mechanical; solution flow for strip |
| Anode material | Pure tin (99.9%+); or insoluble anodes (MMO/Ti) with separate Sn2+ replenishment |
| Anode:cathode ratio | 1:1 to 2:1 |
| Filtration | Continuous, 5-10 micron |

### Efficiency and Plating Rate [VERIFIED]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 85-99% (typically 90-95% at normal CD) |
| Plating rate at 15 ASF | ~0.5 mil/hr (12.7 microns/hr) |
| Plating rate at 30 ASF | ~1.0 mil/hr (25 microns/hr) |

### Sn2+ vs. Sn4+ (Oxidation Control) [DOMAIN]
- Tin in bath must remain as Sn2+ (stannous). Oxidation to Sn4+ (stannic) is irreversible and causes:
  - Sn4+ precipitates as stannic acid — causes roughness and haze
  - Reduces effective tin concentration
  - Wastes chemistry
- Antioxidants (hydroquinone, catechol) are ESSENTIAL — they scavenge dissolved oxygen
- Minimize air agitation exposure; use low-pressure, fine-bubble diffusers
- Keep soluble anodes submerged; avoid exposing hot anode surfaces to air

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| Haze/cloudiness | Sn4+ buildup, organic contamination | Carbon treat, ensure antioxidant level |
| Roughness | Stannic acid precipitate, particles | Filter, check antioxidant, replace aged bath |
| Dull deposits | Low brightener, low temperature | Add grain refiner/brightener, raise temp |
| Burning at HCD | Too high CD, too low Sn2+ | Reduce CD, add tin replenisher |
| Tin whiskers (post-plate) | Pure tin on copper; internal stress; ambient growth | Alloy with Pb, Bi, or Ag; or reflow; or specify minimum thickness >8 microns |
| Poor solderability | Oxidized surface, too thin, organic residue | Increase thickness, improve rinsing, check antioxidant |
| Staining after rinse | Inadequate rinsing, water quality | Improve rinse, use DI water |

## 10.6 Post Treatment

**Reflow (bright tin):** For matte tin deposits, reflow melting at 450-500 deg F (232-260 deg C) for 1-3 seconds produces a bright, fused tin surface with reduced porosity and improved solderability. Tin melting point: 449 deg F (232 deg C). [DOMAIN]

**Whisker mitigation:** Per JEDEC/IPC standards, pure tin on copper requires either:
- Alloy addition (Pb, Bi, Ag)
- Nickel underplate barrier (2-5 microns)
- Reflow
- Minimum thickness >8 microns

**HE baking:** Not typically required — tin plating has minimal hydrogen generation.

### Applicable Specifications

| Specification | Coverage |
|---|---|
| ASTM B545 | Electrodeposited coatings of tin |
| IPC-4554 | Electrodeposited tin on PCB |
| MIL-T-10727 | Tin plating (federal) |
| ASTM A623/A624 | Tin mill products (electrolytic tinplate for food cans) |

## 10.7 Safety and Regulatory

**Key hazards:**
- Methanesulfonic acid: corrosive; severe burns to skin and eyes
- Stannous compounds: low acute toxicity; irritant
- Hydroquinone (antioxidant): toxic by ingestion; skin sensitizer; suspected carcinogen at high exposure

**PPE:** Acid-resistant gloves, splash goggles, face shield for bath maintenance.

**Wastewater:** Tin hydroxide precipitation at pH 8-10. MSA is biodegradable (unlike fluoboric acid). Tin discharge limits are relatively lenient compared to other metals. [DOMAIN]

---

# CLUSTER 11: GOLD PLATING (ACID HARD)

## 11.1 Process Flow Poster Data

**What is this process?** Acid hard gold plating deposits a gold-cobalt or gold-nickel alloy (99.0-99.9% Au) from an acid citrate electrolyte. The cobalt or nickel hardener (0.1-0.5% in deposit) increases hardness from 60-80 HK (pure gold) to 130-250 HK. Used for electrical connectors, PCB edge fingers, semiconductor bonding pads, switch contacts, and aerospace electrical systems where wear resistance and low contact resistance are required simultaneously.

**Substrates:** Nickel-plated surfaces (standard), copper, Kovar, palladium-nickel underplate. Always over a nickel barrier layer (1-5 microns) to prevent gold diffusion into copper substrate.

**Full process sequence:**
1. Receiving / Racking
2. Alkaline soak clean (mild)
3. Rinse
4. Electrocleaning (anodic, low CD)
5. Rinse
6. Acid activation (5% H2SO4, brief)
7. Rinse
8. Nickel underplate (if not already present — Watts or sulfamate, 50-200 microinches)
9. Rinse
10. Gold strike (optional — dilute gold bath, 1-5 sec)
11. Acid hard gold plate
12. Rinse (DI water — gold is precious; recover dragout)
13. Hot DI water rinse / dry
14. Inspection (thickness by XRF, hardness by micro-Knoop, purity by XRF or fire assay)

## 11.2 Cleaning Stage

Mild alkaline clean. Gold plating substrates (connectors, PCB) are often already clean from nickel plating. Over-aggressive cleaning can damage delicate substrates. Electrocleaning at low CD (20-30 ASF) for 30-60 seconds if needed. [DOMAIN]

## 11.3 Rinse Stages

**All rinses:** DI water preferred (conductivity <5 microS/cm ideal). Ionic contamination ruins gold bath and deposit quality.

**Post-plate:** DI water drag-out recovery is economically critical — gold solutions are extremely expensive ($50-200+/troy oz recovered). A static DI drag-out tank should be maintained and periodically returned to the gold bath or sent to gold recovery.

## 11.4 Activation Stage

**For nickel surfaces:** 5% H2SO4, 10-15 sec, room temperature. Very light activation — just enough to remove the nickel oxide passive film.

**For copper:** 5% H2SO4, 15-30 sec.

**Do NOT use HCl** — chloride contamination in gold baths causes dark deposits and grain boundary embrittlement.

## 11.5 Main Tank (Plating Bath)

### Acid Hard Gold Bath Chemistry [VERIFIED]

| Component | Concentration | Purpose |
|---|---|---|
| Gold (as potassium gold cyanide, KAu(CN)2) | 4-16 g/L Au metal (typical 8-12 g/L) | Gold source |
| Potassium gold cyanide (68% Au) | 6-24 g/L | |
| Citric acid | 50-100 g/L (typical 90 g/L) | Complexant, buffer |
| Potassium citrate | 50-100 g/L (typical 90 g/L) | Buffer, conductivity |
| Cobalt (as cobalt sulfamate or cobalt chloride) | 0.1-1.0 g/L as Co metal | Hardener |
| Free potassium cyanide | 0-0.5 g/L (minimal — this is an ACID bath) | Anode dissolution aid |
| Potassium hydroxide | As needed for pH adjustment | |

**Note:** Despite being called "acid gold," these baths use potassium gold cyanide (KAu(CN)2) as the gold source. The bath is acidic (pH 3-5), not the gold salt itself. The free cyanide concentration is kept very low. [DOMAIN]

### Operating Parameters [VERIFIED]

| Parameter | Value |
|---|---|
| Temperature | 95-135 deg F (35-57 deg C); typical 110-130 deg F (43-54 deg C) |
| pH | 3.5-5.0; typical 4.0-4.5 |
| Cathode CD | 3-10 ASF (0.3-1.1 A/dm2) for rack; up to 50 ASF for selective/brush |
| Typical rack CD | 5 ASF (0.54 A/dm2) |
| Voltage | 2-6 V |
| Agitation | Solution flow or cathode bar movement; air agitation AVOIDED (oxidation) |
| Anode material | Platinized titanium (insoluble) or carbon |
| Anode:cathode ratio | 2:1 to 4:1 |
| Filtration | Continuous, 1-5 micron |

### Efficiency and Plating Rate [VERIFIED]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 30-45% (varies with CD, temperature, pH) |
| Plating rate at 5 ASF | ~5-8 microinches/min (~0.13-0.20 microns/min) |
| Gold deposit density | 19.3 g/cm3 (pure); ~18.5 g/cm3 (hard gold with Co) |
| Deposit hardness | 130-210 HK (Knoop) with Co; 170-250 HK with Ni hardener |

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| Dull/matte deposits | Low cobalt, organic contamination, low temperature | Add Co replenisher, carbon treat, raise temp |
| Dark deposits | Excess cobalt (>1 g/L), metallic contamination (Cu, Fe), Cl- contamination | Dilute/re-make, remove contaminants, check for HCl dragout |
| Poor adhesion | Passive Ni surface, inadequate activation | Improve activation, minimize transfer time |
| Low hardness | Low cobalt, low CD | Add cobalt, increase CD |
| Rough deposits | Particulates, stannic/organic precipitates | Filter, maintain bath, carbon treat |
| Staining | Inadequate rinsing, water spots | Improve DI rinsing, hot DI final rinse |

## 11.6 Post Treatment

**Typically none.** Gold is the final coating. Its inertness is the entire point.

**Heat treatment for diffusion bonding:** Some semiconductor applications heat to 300-400 deg F (149-204 deg C) to improve gold-to-substrate bond.

**HE baking:** Not applicable — gold is plated over nickel on non-ferrous substrates in most applications.

### Applicable Specifications

| Specification | Coverage |
|---|---|
| ASTM B488 | Electrodeposited gold coatings for engineering uses |
| MIL-G-45204 | Gold plating (Types I, II, III by purity; Classes A-C by hardness) |
| AMS 2422 | Gold plating (aerospace) |
| IPC-4552A | Electroless nickel / immersion gold (ENIG) — different process but related spec environment |

## 11.7 Safety and Regulatory

**Key hazards:**
- Potassium gold cyanide: cyanide compound — TOXIC. Handle as cyanide.
- Citric acid: mild irritant
- Cobalt salts: skin sensitizer, respiratory hazard
- Free cyanide (low level): still toxic — must maintain pH above 4 to prevent HCN generation

**CRITICAL pH SAFETY:** If bath pH drops below 4, free cyanide converts to hydrogen cyanide gas (HCN), which is lethal. pH must be monitored continuously. HCN monitors are recommended near gold plating lines. [DOMAIN]

**PPE:** Nitrile gloves, safety goggles, cyanide-rated ventilation, HCN alarm. Cyanide first aid kit (amyl nitrite, sodium thiosulfate, hydroxocobalamin) must be accessible.

**Wastewater:** Cyanide must be destroyed (alkaline chlorination: NaOCl at pH >10). Gold recovery from rinse water is economically mandated (gold is too valuable to discharge). Recovery methods: electrolytic recovery cells, ion exchange, activated carbon. [DOMAIN]

---

# CLUSTER 12: SILVER PLATING (CYANIDE)

## 12.1 Process Flow Poster Data

**What is this process?** Cyanide silver plating deposits silver from an alkaline cyanide electrolyte containing potassium silver cyanide [KAg(CN)2] and free potassium cyanide. Silver provides the highest electrical conductivity of any metal, excellent thermal conductivity, superior solderability, lubricity (anti-galling for threaded fasteners), and a bright white decorative finish. Used in electrical bus bars, connectors, waveguides, bearing surfaces, tableware, and aerospace applications.

**Substrates:** Copper and copper alloys (most common), nickel-plated steel, brass. Steel requires a copper cyanide strike first (mandatory — silver will not adhere directly to steel from cyanide silver bath).

**CRITICAL:** Silver is highly reactive with many base metals. A SILVER STRIKE is required before full plating to prevent immersion silver (non-adherent). The strike uses a dilute silver bath at high CD to plate past the immersion potential. [VERIFIED]

**Full process sequence:**
1. Receiving / Racking
2. Alkaline soak clean
3. Rinse
4. Electrocleaning (anodic)
5. Rinse
6. Acid activation (brief)
7. Rinse
8. Copper cyanide strike (for steel substrates) [skip if plating on copper]
9. Rinse
10. Silver cyanide strike (dilute, high CD, 10-30 sec)
11. Silver cyanide plate (full bath)
12. Rinse (DI — recover silver)
13. Anti-tarnish treatment (optional)
14. Hot DI water rinse / dry
15. Inspection

## 12.2 Cleaning Stage

Standard alkaline soak clean + anodic electrocleaning. Silver plating is very revealing of surface imperfections — any organic residue or oxide film will show through as staining, discoloration, or adhesion failure in the bright silver deposit. [DOMAIN]

## 12.3 Rinse Stages

**Pre-plate:** Single overflow after activation. For steel parts, rinse between Cu strike and Ag strike is needed.

**Post-plate:** DI water drag-out recovery tank (silver recovery is economically important). Double counterflow DI rinse.

## 12.4 Activation Stage

**For copper substrates:** 5-10% H2SO4, 10-15 sec, room temperature.

**For nickel surfaces:** 5% H2SO4, 10-15 sec.

**Do NOT use HCl** — chloride precipitates silver as AgCl, contaminating both the activation tank and the silver bath if dragged in.

## 12.5 Main Tank (Plating Bath)

### Silver Strike Bath [VERIFIED]

| Component | Concentration | Purpose |
|---|---|---|
| Potassium silver cyanide [KAg(CN)2] | 2-6 g/L as Ag metal | Silver source (dilute for strike) |
| Free potassium cyanide (KCN) | 75-120 g/L | Complexant, conductivity, prevents immersion |
| Potassium carbonate | 15-30 g/L | Conductivity |

| Parameter | Value |
|---|---|
| Temperature | Room temperature, 65-80 deg F (18-27 deg C) |
| Current density | 30-60 ASF (3.2-6.5 A/dm2) — HIGH CD for strike |
| Time | 10-30 seconds |

The high free cyanide concentration with low silver ensures current goes to electrodeposition (not immersion displacement) from the first instant.

### Silver Plate Bath (Full Bath) [VERIFIED]

| Component | Concentration | Purpose |
|---|---|---|
| Potassium silver cyanide [KAg(CN)2] | 30-60 g/L as Ag metal (typical 35-45 g/L) | Silver source |
| Free potassium cyanide (KCN) | 30-120 g/L (typical 50-80 g/L) | Complexant, anode dissolution |
| Potassium carbonate (K2CO3) | 15-60 g/L | Conductivity (builds up over time from CO2 absorption) |
| Brightener | Per supplier TDS | Grain refinement, brightness |

### Operating Parameters [VERIFIED]

| Parameter | Value |
|---|---|
| Temperature | 70-90 deg F (21-32 deg C); some bright baths up to 110 deg F (43 deg C) |
| pH | >12 (strongly alkaline; typically 12-13) |
| Cathode CD (rack) | 5-15 ASF (0.5-1.6 A/dm2) for standard; up to 40 ASF for high-speed |
| Cathode CD (barrel) | 3-10 ASF (0.3-1.1 A/dm2) |
| Voltage | 1-4 V (silver is very conductive) |
| Agitation | Cathode bar movement preferred; air agitation AVOIDED (CO2 absorption builds carbonate) |
| Anode material | Pure silver (99.9%+); or insoluble (graphite, stainless) with silver salt additions |
| Anode:cathode ratio | 1:1 to 2:1 |
| Filtration | Continuous, 5-10 micron |

### Efficiency and Plating Rate [DOMAIN]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 95-100% |
| Plating rate at 10 ASF | ~0.5-0.6 mil/hr (12-15 microns/hr) |
| Silver density | 10.5 g/cm3 |

### Free Cyanide Control [DOMAIN]
- Too low (<30 g/L): Anode passivation (black AgCN crust), poor throwing power, immersion silver
- Too high (>120 g/L): Reduced efficiency, brittle deposits, slower plating
- KCN:Ag ratio: 2:1 to 3:1 (by weight) is typical; higher ratio for better throwing power

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| Immersion silver (dull, non-adherent) | Insufficient silver strike, low CD at entry | Always use strike; live entry |
| Dark/stained deposits | Organic contamination, sulfide contamination, metallic impurities | Carbon treat, check for sulfide sources, dummy plate |
| Rough deposits | Particulates, anode sludge, high carbonate | Filter, anode bags, dilute to reduce carbonate |
| Poor throwing power | Low free KCN, low conductivity | Increase KCN, check carbonate level |
| Tarnishing (post-plate) | Sulfur-bearing atmosphere, lack of anti-tarnish | Apply anti-tarnish, store in sulfur-free environment |
| Burning at HCD | Too high CD, low Ag metal | Reduce CD, add silver replenisher |
| Carbonate buildup | CO2 absorption (from air agitation or age) | Chill and filter K2CO3 precipitate; or add Ca(OH)2 and filter CaCO3 |

## 12.6 Post Treatment

**Anti-tarnish:** Chromate dip (dilute), benzotriazole, or proprietary anti-tarnish. Silver tarnishes rapidly in sulfur-bearing atmospheres (forms black Ag2S).

**Lacquer:** Clear lacquer coating for decorative or storage protection.

**HE baking:** Silver plating on high-strength steel requires baking per ASTM B850. Silver has very low hydrogen diffusivity — it traps hydrogen in the base metal. Baking must be done before silver plate if possible (per ASTM B849) because baking after silver plating is less effective at hydrogen removal. [DOMAIN]

### Applicable Specifications

| Specification | Coverage |
|---|---|
| ASTM B700 | Electrodeposited silver coatings for engineering use |
| AMS 2410 / AMS 2411 / AMS 2412 | Silver plating (aerospace, different types) |
| QQ-S-365 | Silver plating (federal, superseded) |
| ASTM B487 | Thickness measurement by cross-section |

## 12.7 Safety and Regulatory

**KEY HAZARD: CYANIDE.** [VERIFIED]

- Potassium cyanide (KCN): lethal poison. LD50 oral ~5 mg/kg. Skin absorption possible.
- Potassium silver cyanide: releases cyanide; handle as cyanide compound
- **NEVER MIX CYANIDE WITH ACID.** Adding acid to cyanide generates HCN gas — lethal at >50 ppm.
- All cyanide operations require:
  - HCN gas monitors (fixed and portable)
  - Cyanide first aid kit (amyl nitrite, sodium thiosulfate, hydroxocobalamin)
  - Posted emergency procedures
  - Buddy system during tank maintenance
  - Dedicated drains (never connect cyanide waste to acid waste)
  - Alkaline conditions maintained at all times (pH >10)

**PPE:** Neoprene gloves (double-glove for immersion), face shield, splash-proof goggles, rubber apron, respiratory protection for confined spaces. Cyanide-specific training mandatory.

**Wastewater:** Cyanide destruction by alkaline chlorination (NaOCl at pH >10, two-stage: first to cyanate, then to CO2 + N2 at pH 8.5). Silver recovery by electrolytic cells or cementation. Silver discharge limits typically <0.5 mg/L. [DOMAIN]

---

# CLUSTER 13: CADMIUM PLATING (CYANIDE)

## 13.1 Process Flow Poster Data

**What is this process?** Cadmium plating from a cyanide electrolyte deposits a soft, ductile, sacrificial coating with exceptional lubricity and corrosion resistance, particularly in marine (salt air) and aerospace environments. Cadmium is galvanically protective to steel (like zinc) but with superior performance in salt spray, better lubricity (critical for threaded fasteners), and excellent paint adhesion. It is the legacy standard for military and aerospace hardware.

**CRITICAL REGULATORY NOTE:** Cadmium is a regulated toxic heavy metal and IARC Group 1 human carcinogen (inhalation). Its use is restricted or banned in many jurisdictions (EU RoHS, REACH). In the US, it remains permitted for military and aerospace applications under exemption but is being actively replaced by zinc-nickel in many applications. [VERIFIED]

**Substrates:** High-strength steel (dominant application — landing gear, fasteners, hydraulic fittings), alloy steel, stainless steel (with activation).

**Full process sequence:**
1. Receiving / Racking
2. Pre-bake for HE prevention (per ASTM B849, if high-strength steel)
3. Alkaline soak clean
4. Rinse
5. Electrocleaning (anodic)
6. Rinse
7. Acid activation (HCl or H2SO4)
8. Rinse
9. Cadmium cyanide plate
10. Rinse (triple — drag-out + double counterflow)
11. Chromate conversion coating (Type I, II, or III per QQ-P-416)
12. Rinse
13. HE bake (375 deg F, 23 hours minimum for aerospace)
14. Final inspection (thickness, adhesion, salt spray, HE test per ASTM F519)

## 13.2 Cleaning Stage

Standard alkaline soak clean + anodic electrocleaning. Same as zinc plating (Section 1.2). Stringent cleaning for aerospace — parts are often vapor degreased first.

## 13.3 Rinse Stages

**All rinses:** Must be segregated from other plating operations due to cadmium toxicity. Cadmium rinse water CANNOT be combined with general plating waste without cadmium-specific treatment.

**Pre-plate:** Single overflow after acid activation.

**Post-plate:** Triple rinse — drag-out recovery + double counterflow. All rinse water is cadmium-contaminated and must be treated as regulated waste.

## 13.4 Activation Stage

**For steel:** 10-25% HCl, 15-30 sec, room temperature.

**For high-strength steel:** Minimize acid contact. Some specs allow only 5% HCl for <15 seconds.

**For stainless steel:** Wood's nickel strike or anodic activation in the cadmium bath itself.

## 13.5 Main Tank (Plating Bath)

### Cadmium Cyanide Bath Chemistry [VERIFIED]

| Component | Low (bright) | Typical | High (barrel) |
|---|---|---|---|
| Cadmium oxide (CdO) | 20 g/L (2.7 oz/gal) | 30 g/L (4 oz/gal) | 42 g/L (5.6 oz/gal) |
| Cadmium metal (equivalent) | 17 g/L | 26 g/L | 37 g/L |
| Sodium cyanide (NaCN, total) | 87 g/L (11.6 oz/gal) | 100-120 g/L (13-16 oz/gal) | 150 g/L (20 oz/gal) |
| Sodium carbonate (Na2CO3) | 15-30 g/L | 30 g/L | 60 g/L |
| Sodium hydroxide (NaOH) | 15-30 g/L (optional) | 20 g/L | 30 g/L |
| Brightener | Per supplier TDS | | For bright cadmium |
| NaCN:Cd ratio | 3.5-6:1 (by weight) | 4:1 typical | |

### Operating Parameters [VERIFIED]

| Parameter | Value |
|---|---|
| Temperature | 70-90 deg F (21-32 deg C); typical 80 deg F (27 deg C) |
| pH | >12 (alkaline cyanide) |
| Cathode CD (rack) | 5-30 ASF (0.5-3.2 A/dm2); typical 10-20 ASF |
| Cathode CD (barrel) | 3-10 ASF (0.3-1.1 A/dm2) |
| Voltage | 1-4 V |
| Agitation | Cathode rod movement; air (mild) acceptable |
| Anode material | Cadmium balls in steel baskets; or cadmium slabs |
| Anode:cathode ratio | 2:1 to 3:1 |
| Filtration | Continuous, 5-10 micron |

### Efficiency and Plating Rate [DOMAIN]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 85-95% (bright Cd slightly lower) |
| Plating rate at 15 ASF | ~0.3-0.4 mil/hr (~8-10 microns/hr) |
| Cadmium density | 8.65 g/cm3 |

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| Burning at HCD | Low Cd, high CD, low NaCN | Increase CdO, reduce CD, add NaCN |
| Dull deposits | Low brightener, low temperature, organic contamination | Add brightener, raise temp, carbon treat |
| Staining | High carbonate, metallic contamination | Chill/filter carbonate, dummy plate |
| Roughness | Particles, anode sludge, high carbonate | Filter, maintain anodes, reduce carbonate |
| Poor adhesion | Inadequate cleaning/activation, passive substrate | Review pre-treatment |
| Hydrogen embrittlement | Inherent — Cd plating generates significant H2 | Post-plate bake per ASTM B850 |

## 13.6 Post Treatment

### Chromate Conversion [VERIFIED]

Per QQ-P-416 (and ASTM B766):

| Type | Description | Appearance |
|---|---|---|
| Type I | No supplementary treatment | Clear to slightly iridescent |
| Type II | Chromate conversion | Yellow/gold iridescent |
| Type III | Chromate conversion | Olive drab (heavy chromate) |

### Hydrogen Embrittlement Baking [VERIFIED]

Cadmium plating is one of the highest-risk processes for HE because:
1. The plating process generates significant hydrogen
2. Bright cadmium is an excellent hydrogen barrier — traps H2 in the steel
3. Post-plate baking is ESSENTIAL and CRITICAL

Per ASTM B850 / QQ-P-416:
- Temperature: 375 deg F (191 deg C)
- Time: 23 hours minimum (aerospace standard — regardless of hardness)
- Must commence within 4 hours of plating (1 hour preferred)
- For non-bright cadmium: some specs allow 12 hours
- ASTM F519 test specimens may be required to validate embrittlement relief

### Applicable Specifications

| Specification | Coverage |
|---|---|
| QQ-P-416F | Cadmium plating (federal — THE definitive Cd spec) |
| ASTM B766 | Electrodeposited coatings of cadmium |
| AMS-QQ-P-416 | Cadmium plating (aerospace version of QQ-P-416) |
| AMS 2400 | Cadmium plating (aerospace) |
| ASTM B850 | HE relief baking |
| ASTM F519 | Mechanical hydrogen embrittlement testing |
| ASTM B849 | Pre-plating HE prevention |

## 13.7 Safety and Regulatory

**CADMIUM IS AMONG THE MOST REGULATED METALS IN PLATING.** [VERIFIED]

**Cadmium hazards:**
- IARC Group 1 carcinogen (lung, prostate — inhalation route)
- OSHA PEL: 5 micrograms/m3 (TWA) — same stringency as hex chrome
- OSHA Action Level: 2.5 micrograms/m3
- Kidney damage (chronic exposure)
- Bone disease (itai-itai, at extreme exposure)
- EU RoHS: banned (exemptions for safety applications only)
- EU REACH: Annex XVII restrictions
- California Prop 65 listed

**Cyanide hazards:** Same as silver plating (Section 12.7). HCN generation risk if pH drops.

**Required controls:**
- Full enclosure or aggressive local exhaust
- Respiratory protection (supplied air for tank maintenance)
- Cadmium-specific medical surveillance (blood cadmium, urinary beta-2-microglobulin)
- Biological monitoring program
- Designated cadmium work area with decontamination shower
- Prohibited from eating/drinking/smoking in cadmium areas

**Wastewater:**
- Cyanide destruction first (alkaline chlorination)
- Then cadmium hydroxide precipitation at pH 10-11
- Cadmium discharge limits: 0.07 mg/L (monthly avg) per 40 CFR 433 — extremely tight
- Cadmium-bearing sludge is F006 listed hazardous waste
- Some states require additional treatment (sulfide precipitation) to meet discharge limits

---

# CLUSTER 14: TIN-LEAD PLATING

## 14.1 Process Flow Poster Data

**What is this process?** Tin-lead (solder) plating co-deposits a tin-lead alloy typically in the 60Sn/40Pb to 90Sn/10Pb composition range from an acid electrolyte (historically fluoborate; now predominantly MSA-based). Used for solderability preservation on electronic components, PCB surface finish (pre-RoHS), connector pins, and applications requiring a solderable, corrosion-resistant, and low-friction coating.

**CRITICAL NOTE:** Lead is restricted under EU RoHS (Directive 2011/65/EU). Tin-lead plating is declining in commercial electronics but remains in use for military, aerospace, and high-reliability applications under exemptions. Most commercial electronics have transitioned to lead-free alternatives (pure tin, tin-silver, tin-bismuth). [VERIFIED]

**Substrates:** Copper and copper alloys (PCB, connectors), nickel-plated surfaces, steel (with Cu strike).

**Full process sequence:**
1. Receiving / Racking or reeling
2. Alkaline soak clean
3. Rinse
4. Electrocleaning (optional for clean substrates)
5. Rinse
6. Acid activation (5-10% fluoboric acid or MSA)
7. Rinse
8. Tin-lead plate
9. Rinse
10. Hot water rinse / dry (or reflow at 400-450 deg F / 204-232 deg C for fused solder finish)
11. Inspection (alloy composition by XRF, solderability, thickness)

## 14.2 Cleaning Stage

Standard for electronics substrates. Mild alkaline clean or solvent clean. PCB panels may use spray cleaning in conveyorized lines. Electrocleaning is used for rack plating of discrete components. [DOMAIN]

## 14.3 Rinse Stages

**Pre-plate:** Single overflow. MSA dragout from activation is compatible with MSA tin-lead bath.

**Post-plate:** Double counterflow. Lead contamination in rinse water is regulated — segregate waste.

**DI water:** Recommended for electronics to prevent ionic contamination.

## 14.4 Activation Stage

**For copper:** 5-10% fluoboric acid (HBF4) or 5-10% MSA, 15-30 sec, room temperature.

**For nickel:** 5% H2SO4 or 5% MSA, 10-15 sec.

## 14.5 Main Tank (Plating Bath)

### MSA Tin-Lead Bath Chemistry [VERIFIED]

| Component | 60Sn/40Pb | 90Sn/10Pb |
|---|---|---|
| Stannous tin (Sn2+) as stannous methanesulfonate | 35-55 g/L (4.7-7.3 oz/gal) | 50-70 g/L |
| Lead (Pb2+) as lead methanesulfonate | 15-25 g/L (2-3.3 oz/gal) | 5-10 g/L |
| Free methanesulfonic acid (MSA) | 100-200 g/L (13-27 oz/gal) | 100-200 g/L |
| Antioxidant (hydroquinone) | 1-2 g/L | 1-2 g/L |
| Grain refiner / brightener | Per supplier TDS | Per supplier TDS |
| Wetting agent | Per supplier TDS | Per supplier TDS |

### Fluoborate Bath (Legacy) [DOMAIN]

| Component | Concentration |
|---|---|
| Stannous fluoborate | 100-200 g/L |
| Lead fluoborate | 25-75 g/L |
| Free fluoboric acid (HBF4) | 100-250 g/L |
| Boric acid | 20-30 g/L |
| Peptone or gelatin | 2-5 g/L (grain refiner) |

### Operating Parameters [VERIFIED]

| Parameter | MSA Bath |
|---|---|
| Temperature | 60-100 deg F (16-38 deg C); typical 75-85 deg F (24-29 deg C) |
| pH | Not applicable (strongly acidic) |
| Cathode CD (rack) | 10-40 ASF (1.1-4.3 A/dm2); typical 15-25 ASF |
| Cathode CD (barrel) | 5-15 ASF (0.5-1.6 A/dm2) |
| Voltage | 1-5 V |
| Agitation | Air (oil-free) or mechanical |
| Anode material | Tin-lead alloy (matching deposit composition); or separate Sn and Pb anodes |
| Anode:cathode ratio | 1:1 to 2:1 |
| Filtration | Continuous, 5-10 micron |

### Efficiency and Plating Rate [DOMAIN]

| Parameter | Value |
|---|---|
| Cathodic current efficiency | 90-98% |
| Plating rate at 20 ASF | ~0.5-0.7 mil/hr (~13-18 microns/hr) |

### Alloy Composition Control [DOMAIN]
- Alloy ratio in deposit is controlled by Sn:Pb ratio in solution
- Higher CD slightly favors tin deposition
- Temperature has minimal effect on composition
- Brightener type and concentration can shift alloy ratio
- Verify alloy composition by XRF (non-destructive) or dissolve in acid and analyze by AA/ICP

### Common Defects [DOMAIN]

| Defect | Cause | Corrective Action |
|---|---|---|
| Wrong alloy composition | Sn:Pb ratio out of balance | Analyze and adjust metal concentrations |
| Rough deposits | Stannic acid (Sn4+), particulates | Add antioxidant, filter, carbon treat |
| Dull deposits | Low brightener, low temperature | Add brightener, raise temp slightly |
| Pitting | Low wetting agent, particles | Add wetting agent, filter |
| Poor solderability | Oxide film, contamination, wrong alloy | Reflow, improve rinsing, check alloy |
| Tin pest (alpha tin) | Storage below 56 deg F (13 deg C) — gray tin conversion | Maintain storage temperature; alloy >3% Pb prevents tin pest |
| Sn4+ (stannic) buildup | Air oxidation, high temperature | Antioxidant, reduce air exposure |

## 14.6 Post Treatment

**Reflow (fused solder):** Heat treatment at 400-450 deg F (204-232 deg C) for 2-5 seconds. Melts the tin-lead coating, producing a bright, dense, fully fused solder surface. Reflow dramatically improves solderability and eliminates porosity. Methods: infrared, hot oil immersion (historical), or hot air. [DOMAIN]

**No chromate needed.** The tin-lead alloy is inherently solderable and corrosion-resistant for electronics environments.

**HE baking:** Not typically required — tin-lead is usually on non-ferrous substrates.

### Applicable Specifications

| Specification | Coverage |
|---|---|
| ASTM B579 | Electrodeposited tin-lead alloy (solder plate) |
| MIL-P-81728 | Tin-lead plating (military, superseded) |
| IPC J-STD-001 | Soldering requirements (references solder plating) |
| SAE AS5272 | Tin-lead plating (aerospace) |

## 14.7 Safety and Regulatory

**LEAD IS A MAJOR REGULATORY CONCERN.** [VERIFIED]

**Lead hazards:**
- IARC Group 2A (probably carcinogenic)
- OSHA PEL: 50 micrograms/m3 (TWA)
- OSHA Action Level: 30 micrograms/m3
- Blood lead level monitoring required at Action Level
- Neurological damage, kidney damage, reproductive toxicity
- CDC BLL reference value: 3.5 micrograms/dL (adults)

**EU RoHS:** Lead restricted to <0.1% by weight in homogeneous materials (electronics). Exemptions exist for high-reliability applications.

**MSA advantages:** MSA is biodegradable and much less hazardous than fluoboric acid. Fluoborate baths are being phased out due to fluoride wastewater issues.

**PPE:** Lead-resistant gloves, eye protection, respiratory protection if misting. Lead hygiene program per OSHA 29 CFR 1910.1025 (hand washing, separate eating areas, no dry sweeping).

**Wastewater:** Lead hydroxide precipitation at pH 9-10. Lead discharge limits: 0.43 mg/L (daily max per 40 CFR 433). Lead-bearing sludge may be F006 hazardous waste. MSA in wastewater is biodegradable (minimal BOD concern). Fluoborate wastewater requires fluoride treatment. [DOMAIN]

---

# CROSS-CUTTING DATA TABLE: QUICK COMPARISON

| Process | Bath pH | Temp (deg F) | CD Range (ASF) | Cathodic Eff. (%) | Primary Spec |
|---|---|---|---|---|---|
| Acid Chloride Zinc | 4.8-5.6 | 70-95 | 10-40 | 90-98 | ASTM B633 |
| Zinc-Nickel (Alk) | >13 | 75-95 | 10-40 | 40-70 | ASTM B841 |
| Zinc-Nickel (Acid) | 5.5-6.5 | 75-105 | 10-50 | 80-95 | ASTM B841 |
| Watts Nickel | 3.0-4.5 | 110-160 | 20-80 | 93-97 | ASTM B689 |
| Nickel Sulfamate | 3.5-4.5 | 90-140 | 10-100 | 95-100 | AMS 2424 |
| Nickel-Cobalt | 2.5-5.0 | 104-150 | 10-100 | 85-95 | OEM specs |
| Dec. Trivalent Cr | 2.7-3.8 | 85-115 | 50-200 | 15-25 | ASTM B456 |
| Hard Chrome (Hex) | N/A (acid) | 120-145 | 150-400 | 10-18 | AMS 2406 |
| Acid Copper | <1 | 70-90 | 10-50 | 97-100 | ASTM B734 |
| Alk Non-CN Copper (pyro) | 8-9 | 100-140 | 10-80 | 70-90 | ASTM B734 |
| Alk Non-CN Copper (HEDP) | 9-13 | 100-160 | 5-30 | 30-70 | ASTM B734 |
| Tin (MSA) | <1 | 60-100 | 10-30 | 85-99 | ASTM B545 |
| Gold (Acid Hard) | 3.5-5.0 | 95-135 | 3-10 | 30-45 | ASTM B488 |
| Silver (Cyanide) | >12 | 70-90 | 5-15 | 95-100 | ASTM B700 |
| Cadmium (Cyanide) | >12 | 70-90 | 5-30 | 85-95 | QQ-P-416 |
| Tin-Lead (MSA) | <1 | 60-100 | 10-40 | 90-98 | ASTM B579 |

---

# REGULATORY MATRIX: PROCESS RISK RANKING

| Process | Cyanide | Hex Chrome | Cadmium | Lead | Nickel (IARC) | Overall Reg. Burden |
|---|---|---|---|---|---|---|
| Acid Chloride Zinc | No | Post-treat only | No | No | No | LOW |
| Zinc-Nickel | No | No (trivalent) | No | No | Yes (bath) | MODERATE |
| Watts Nickel | No | No | No | No | Yes | MODERATE |
| Nickel Sulfamate | No | No | No | No | Yes | MODERATE |
| Nickel-Cobalt | No | No | No | No | Yes + Co | MODERATE-HIGH |
| Dec. Trivalent Cr | No | No | No | No | No | LOW |
| Hard Chrome (Hex) | No | YES (bath) | No | No (Pb anodes) | No | VERY HIGH |
| Acid Copper | No | No | No | No | No | LOW |
| Alk Non-CN Copper | No | No | No | No | No | LOW |
| Tin (MSA) | No | No | No | No | No | LOW |
| Gold (Acid Hard) | Yes (low) | No | No | No | No (or Co) | MODERATE |
| Silver (Cyanide) | YES | No | No | No | No | HIGH |
| Cadmium (Cyanide) | YES | Post-treat | YES | No | No | EXTREME |
| Tin-Lead | No | No | No | YES | No | HIGH |

---

# HYDROGEN EMBRITTLEMENT REFERENCE TABLE

Per ASTM B850 / AMS 2759/9 (applicable to ALL processes on high-strength steel):

| Steel Hardness (HRC) | Tensile Strength (ksi) | Min Bake Time (hr) | Bake Temp (deg F) | Max Time Before Bake Starts |
|---|---|---|---|---|
| 31-36 | 150-180 | 8 | 375 (min) | 4 hours |
| 37-39 | 180-220 | 12 | 375 (min) | 4 hours |
| 40-44 | 220-260 | 18 | 375 (min) | 2 hours |
| 45-48 | 260-300 | 20 | 375 (min) | 1 hour |
| 49-52 | 300+ | 22-24 | 375-430 | 1 hour |
| Aerospace (any HRC >=31) | Any | 23 (standard) | 375 +/-15 | 1-4 hours |

**Note:** Cadmium and hard chrome are the highest HE risk processes. Zinc and zinc-nickel are moderate. Acid copper and tin have minimal HE risk. Always bake BEFORE applying chromate/passivation (chromate degrades at bake temperatures). [VERIFIED]

---

## Sources and Confidence Assessment

### Web-Verified Sources
- Products Finishing (pfonline.com) — acid zinc, copper, silver, gold, chrome articles
- Nickel Institute (nickelinstitute.org) — zinc-nickel corrosion study
- Columbia Chemical — zinc metal buildup in acid chloride
- NMFRC — nickel sulfamate plating systems
- SubsTech — silver plating, hard chrome, tin-lead
- ScienceDirect — nickel-cobalt co-deposition, tin MSA
- ResearchGate — Watts bath composition, Ni-Co alloy parameters
- ASTM (astm.org) — B633, B841, B850, B766 standard summaries
- EPA (epa.gov) — 40 CFR 433 discharge limits, AP-42 Section 12.20
- CASF (casf.ca) — nickel electroplating handbook
- finishing.com — Wood's nickel strike, various process Q&A
- Google Patents — trivalent chrome, gold plating compositions

### Domain Expertise Sections (Watson knowledge, not multi-source verified this session)
All sections marked [DOMAIN] are from Watson's training in electroplating chemistry, consistent with ASM Handbook Vol. 5, Metal Finishing Guidebook, and industry practice. These are flagged for Tyler spot-check where noted.

### Known Gaps / Flags for Review
1. [FLAG] Nickel-cobalt: No widely adopted ASTM/AMS specifically for NiCo alloy plating identified. Drew/Tyler should verify if newer standards exist.
2. [DOMAIN] Metallic contamination thresholds for Watts nickel (Section 3.5) — these are approximate shop-floor numbers. Tyler should validate against Nickel Plating Handbook 2023.
3. [DOMAIN] Plating rates are calculated from Faraday's law and current efficiency estimates — actual rates vary with specific proprietary chemistries.
4. [DOMAIN] HE bake table is compiled from ASTM B850-98 and industry practice. Exact requirements vary by specification (AMS 2759/9 may differ slightly from B850 for specific hardness brackets).

---

*Watson — Chemistry Research Division*
*Plating Posters Inc*
*Research complete: 2026-04-26*
