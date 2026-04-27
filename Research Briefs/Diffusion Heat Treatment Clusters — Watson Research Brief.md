---
title: "Diffusion & Heat Treatment Clusters — Watson Research Brief"
author: Watson (Chemistry Researcher)
date: 2026-04-26
version: v2
status: Research Complete
purpose: Technical backbone for 90 educational posters (10 clusters x 9 posters each)
tags:
  - heat-treatment
  - diffusion
  - carburizing
  - nitriding
  - induction-hardening
  - plating-posters
---

# Diffusion & Heat Treatment Process Clusters — Watson Research Brief

> **Purpose:** This brief provides Alaina with comprehensive, poster-ready technical data for 10 heat treatment process clusters. Each cluster generates 9 posters: Process Flow, Safety & PPE, Part Preparation, Loading & Fixturing, Furnace/System Setup, Atmosphere Control, Heat Cycle, Quench, and Temper & Inspection. All numerical values are verified against ASM Handbook Vol. 4, AMS 2759 series, AGMA standards, and current industry sources.

---

## Master Specification Reference Table

| Specification | Coverage |
|---|---|
| AMS 2759/7E | Gas and vacuum carburizing and heat treatment of carburizing grade steel parts |
| AMS 2759/6D | Gaseous nitriding of steel parts (controlled by ammonia dissociation) |
| AMS 2759/10A | Automated gaseous nitriding (controlled by nitriding potential) |
| AMS 2759/12 | Selective induction hardening |
| AMS 2750H | Pyrometry — temperature sensors, instrumentation, TUS, SAT for all thermal processing |
| ASTM A897 | Austempered ductile iron (ADI) — five grades |
| ASTM E384 | Microindentation hardness testing |
| ASTM E112 | Grain size determination |
| ASTM E18 | Rockwell hardness |
| SAE J423 | Methods of measuring case depth |
| AGMA 2004-C08 | Gear materials, heat treatment, and processing |
| AGMA 923 | Metallurgical specifications for steel gearing |
| CQI-9 (4th ed.) | AIAG special process: heat treat system assessment |
| MIL-H-6875 | Heat treatment of steels (legacy, largely superseded by AMS 2759) |
| AMS-H-6875 | Heat treatment of steel raw materials |

---

## AMS 2750 Pyrometry — Universal Requirements (All Processes)

All furnaces used for aerospace heat treatment must comply with AMS 2750 (current revision H). Key parameters:

### Furnace Classes (Temperature Uniformity Tolerance)
| Class | Tolerance |
|---|---|
| 1 | +/-3 degC (+/-5 degF) |
| 2 | +/-6 degC (+/-10 degF) |
| 3 | +/-8 degC (+/-15 degF) |
| 4 | +/-10 degC (+/-20 degF) |
| 5 | +/-14 degC (+/-25 degF) |
| 6 | +/-28 degC (+/-50 degF) |

- **Carburizing furnaces:** Typically Class 3 (+/-8 degC / +/-15 degF) or Class 4 (+/-10 degC / +/-20 degF)
- **Nitriding furnaces:** Typically Class 2 (+/-6 degC / +/-10 degF) or Class 3
- **Austempering/martempering salt baths:** Class 2 or Class 3

### Instrumentation Types
| Type | Description |
|---|---|
| A | Recording instrument, separate control instrument, over-temperature instrument |
| B | Recording instrument combined with control, plus over-temperature instrument |
| C | Recording instrument, separate control instrument (no over-temp required) |
| D | Recording instrument combined with control (no over-temp required) |
| E | Load thermocouple with recording instrument |

### Thermocouple Types
- **Noble metal:** Types B, R, S (for temperatures above 1800 degF / 982 degC)
- **Base metal:** Types J, K, N, E, T (standard heat treating range)
- **Expendable:** Types used for one-time load verification

### System Accuracy Test (SAT)
- Compares process control thermocouple reading against independent reference thermocouple
- Maximum allowable offset varies by instrumentation type
- Frequency: typically weekly or monthly depending on furnace class and use

### Temperature Uniformity Survey (TUS)
- Verifies qualified work zone temperature uniformity
- Frequency: quarterly for most aerospace applications; semiannual if historical data supports
- Minimum 9 thermocouples for large work zones

---

# CLUSTER 1: GAS CARBURIZING (ATMOSPHERE CARBURIZING)

## 1.1 Process Flow Poster Data

### What Is Gas Carburizing?
Gas carburizing is a thermochemical diffusion process in which carbon is introduced into the surface of a low-carbon or low-alloy steel by heating it to the austenitic range (above Ac3) in a carbon-rich atmosphere. The carbon diffuses into the steel surface, creating a high-carbon case over a lower-carbon core. Upon quenching, the high-carbon case transforms to hard martensite while the core remains tough and ductile.

### Mechanism of Action
1. Carbon-bearing gas (endothermic atmosphere enriched with natural gas or propane) dissociates at the steel surface
2. Atomic carbon adsorbs onto the austenite surface
3. Carbon diffuses inward via interstitial diffusion (Fick's Second Law)
4. Diffusion rate follows the square-root-of-time relationship: **ECD = K x sqrt(t)**, where K is a temperature-dependent carburizing constant and t is time in hours
5. Surface carbon reaches equilibrium with the atmosphere carbon potential (typically 0.80-1.10% C)

### What It Produces
- **Effective case depth (ECD):** 0.010-0.250 in. (0.25-6.35 mm), measured to HRC 50 (or 550 HV)
- **Total case depth:** extends deeper than ECD to the point where carbon content equals base metal carbon
- **Surface hardness:** 58-63 HRC (typical)
- **Core hardness:** 25-45 HRC (depending on steel grade and section size)
- **Residual stress state:** Compressive residual stress in the case (beneficial for fatigue life); tensile in the transition zone
- **Surface carbon:** 0.75-1.10% per AMS 2759/7

### Steels Used
| Grade | Type | Typical Application |
|---|---|---|
| 8620 | Ni-Cr-Mo | General purpose gears, pinions |
| 4320 | Ni-Cr-Mo | Heavy-duty gears, high core toughness |
| 9310 | Ni-Cr-Mo | Aerospace gears (AMS 6265) |
| 3310 | Ni-Cr | High hardenability gears |
| 4620 | Ni-Mo | Worm gears, shafts |
| 4820 | Ni-Mo | Heavy sections, high core strength |
| 1018 / 1020 | Plain carbon | Light-duty pins, bushings |
| 17CrNiMo6 (EN) | European gear steel | Wind turbine gears |

### Key Applications & Industries
- **Automotive:** Transmission gears, ring and pinion sets, CV joints, camshafts
- **Aerospace:** Power transmission gears (9310 steel), bearing races
- **Heavy equipment:** Final drive gears, track pins, sprockets
- **Energy:** Wind turbine gearbox components
- **Off-highway:** Mining equipment gears, agricultural drivetrain

### Applicable Specifications
- **AMS 2759/7E** — Primary aerospace specification for gas and vacuum carburizing
- **AGMA 2004-C08** — Gear materials, heat treatment, and processing
- **AGMA 923** — Metallurgical specifications for steel gearing
- **SAE J423** — Methods of measuring case depth
- **CQI-9 (4th ed.)** — Automotive heat treat process assessment
- **MIL-H-6875** (legacy) — Superseded by AMS-H-6875 / AMS 2759

### 9-Step Process Sequence
1. **Pre-clean** — Solvent or alkaline wash to remove oils, chips, and contaminants
2. **Load** — Arrange parts on fixtures/baskets ensuring uniform gas flow
3. **Purge** — Evacuate air from furnace; backfill with endothermic atmosphere
4. **Heat to carburizing temperature** — Ramp to 1650-1750 degF (899-954 degC)
5. **Carburize (boost)** — High carbon potential (0.90-1.10% C) for rapid carbon absorption
6. **Diffuse** — Reduce carbon potential (0.75-0.85% C) to allow inward diffusion and reduce surface carbides
7. **Quench** — Direct quench into oil at 100-180 degF (38-82 degC), or cool to lower temperature and reheat quench
8. **Temper** — 300-375 degF (149-191 degC) for 2 hours minimum
9. **Inspect** — Hardness, case depth, microstructure, retained austenite

---

## 1.2 Safety & PPE

### Furnace/Atmosphere Hazards
- **Endothermic gas is explosive and toxic:** Composition is approximately 20% CO + 40% H2 + 40% N2 — both CO and H2 are flammable and CO is acutely toxic (OSHA PEL: 50 ppm TWA, IDLH: 1200 ppm)
- **LEL of endothermic gas mixture:** approximately 6% in air — all furnace purge procedures must ensure O2 is below 1% before introducing endo gas
- **Flame curtains** or burn-off pilots are mandatory at furnace vestibules to prevent endo gas escape into the shop
- **Carbon monoxide detectors** must be installed at working height near all furnaces using endothermic atmospheres
- **Furnace explosions:** Can occur if air infiltrates a hot furnace containing endo gas, or if endo gas is introduced into a cold furnace without proper purge. Nitrogen purge to below 1% O2 required before introducing endo

### Quench Media Hazards
- **Oil quench fires:** Water contamination in quench oil (even as little as 0.1%) can cause violent boil-over; oil flash point must be monitored (typical quench oil flash point: 300-400 degF / 149-204 degC)
- **Smoke and fumes:** Oil quenching produces dense smoke; ventilation/hood systems are mandatory
- **Quench oil temperature monitoring:** Maximum safe operating temperature is typically 40-50 degF (22-28 degC) below flash point

### High-Temperature PPE
- Face shield with IR protection (shade 3-5 for furnace observation)
- Heat-resistant gloves (Kevlar or similar, rated to 500 degF / 260 degC minimum for handling near furnace)
- Flame-resistant clothing (FRC) — no synthetic fabrics that melt
- Steel-toed boots with heat-resistant soles
- Full-face supplied-air respirator if CO levels exceed PEL

### Fire Suppression
- **Quench oil tank:** CO2 or dry chemical suppression system, automatic lid closure on fire detection
- **Furnace area:** Clean-agent or CO2 suppression; water-based systems are NOT used near quench oil
- **Emergency oil dump:** Some installations include an emergency drain to underground storage

---

## 1.3 Part Preparation

### Machining Allowance
- **Grinding stock after carburizing:** 0.005-0.015 in. (0.13-0.38 mm) per surface is standard
- For gear teeth: AGMA recommends minimum 0.002 in. (0.05 mm) stock removal to eliminate intergranular oxidation (IGO) layer
- Part must be machined oversize by grinding stock BEFORE carburizing

### Surface Condition Requirements
- **No scale, rust, or heavy oxide** — interferes with carbon absorption
- **No machining burrs** — create stress concentrations and uneven case
- **No residual cutting fluids** — sulfur-bearing cutting oils cause shallow decarburization
- **Surface roughness:** Ra 63 micro-inch (1.6 micrometers) or better typical for gear tooth flanks

### Pre-Cleaning
- Solvent degreasing (vapor or immersion)
- Alkaline wash at 140-180 degF (60-82 degC), 10-15 minutes
- Rinse and dry completely — moisture causes hydrogen embrittlement risk and interferes with atmosphere control

### Masking for Selective Hardening
- **Copper electroplate:** 0.001-0.002 in. (0.025-0.050 mm) copper plate acts as diffusion barrier; most effective and widely used
- **Stop-off paints:** Commercial copper-based or ceramic-based stop-off paints applied to areas that must remain soft
- **Carbon-stop compounds:** Proprietary paste/paint products (e.g., Condursal) applied by brush or spray; limited to approximately 0.060 in. (1.5 mm) case depth protection
- Copper plate is preferred for critical aerospace applications per AMS 2759/7

---

## 1.4 Loading & Fixturing

### Fixture Materials
- **Heat-resistant alloys:** HU (309), HK-40, RA 330, Inconel 601 for trays and baskets
- **Cast alloy fixtures** for high-volume continuous furnaces
- **Fixture life:** Degrades due to carburization of the fixture itself; periodic replacement required

### Part Orientation
- Parts must be oriented to allow uniform gas flow across all surfaces
- Gears placed with bore vertical or on pins to prevent soft spots from contact
- Avoid nesting — stacking parts causes gas starvation at contact points

### Load Density & Spacing
- Minimum 0.5 in. (12.7 mm) spacing between parts for adequate gas circulation
- Load density must be consistent between production loads and qualification loads
- Tray weight limits must be observed to prevent fixture creep at temperature

### Thermocouple Placement
- **Load thermocouples:** Placed at the coldest point in the load (center of densest area)
- **Trailing thermocouples:** On the last parts to enter the hot zone in continuous furnaces
- **Expendable thermocouples:** Embedded in representative parts for case depth verification
- Per AMS 2750, load thermocouple must be within the working zone and representative of actual part temperature

---

## 1.5 Furnace / System Setup

### Furnace Types
- **Batch (integral quench):** Most common for job shop; sealed quench furnace with internal oil quench
- **Continuous (pusher/roller hearth):** High-volume automotive production; parts pass through zones
- **Rotary retort:** Batch processing of small parts in a rotating drum
- **Pit furnace:** Vertical loading; good for long shafts and large gears

### Temperature Uniformity
- AMS 2750 Class 3 (+/-15 degF / +/-8 degC) minimum for most carburizing applications
- AMS 2750 Class 2 (+/-10 degF / +/-6 degC) for aerospace gears per AMS 2759/7

### Atmosphere System
- **Endothermic generator:** Catalytic reaction of natural gas (or propane) with air
  - Air-to-gas ratio for methane: 2.77:1
  - Air-to-gas ratio for propane: 7.16:1
  - Produces: ~20% CO, ~40% H2, ~40% N2 (methane feedstock)
  - Residual CH4: less than 0.5% indicates proper generator function
  - Generator retort temperature: 1900-2050 degF (1038-1121 degC)
- **Nitrogen-methanol system:** Alternative to endothermic generator; N2 + CH3OH cracked in furnace to produce equivalent atmosphere
  - Ratio: approximately 40% N2 + 60% methanol by volume
  - Advantage: no generator maintenance; disadvantage: methanol storage and handling

---

## 1.6 Atmosphere / Cycle Control

### Carbon Potential Control
- **Target range:** 0.75-1.10% C at surface (per AMS 2759/7)
- **Boost phase:** Carbon potential set to 0.90-1.10% C for rapid carbon uptake
- **Diffuse phase:** Carbon potential reduced to 0.75-0.85% C to create smoother gradient and dissolve surface carbides

### Control Methods
| Method | Principle | Accuracy |
|---|---|---|
| Oxygen probe (zirconia sensor) | Measures O2 partial pressure; calculates carbon potential via Nernst equation | +/-0.03% C (when calibrated) |
| Dew point analyzer | Measures water vapor in atmosphere; correlates to carbon potential | +/-0.05% C |
| Infrared CO2 analyzer | Measures CO2 in atmosphere; derives carbon potential from CO/CO2 ratio | +/-0.03% C |
| Shim stock (foil test) | Thin steel foil (0.002 in.) weighed before/after exposure; gravimetric carbon measurement | Definitive verification method |

### Atmosphere Composition Targets
| Component | Target (Methane-Based Endo) |
|---|---|
| CO | 18.8-20.5% |
| H2 | 38-42% |
| N2 | 38-42% (balance) |
| CO2 | 0.10-0.50% (varies with carbon potential) |
| CH4 | less than 0.5% (generator efficiency indicator) |
| Dew point | -5 to +10 degF (-20 to -12 degC) at 0.80% C potential; higher for higher carbon potential |

### Enrichment Gas
- Natural gas (CH4) or propane (C3H8) added to raise carbon potential above base endo level
- Flow rate controlled by feedback from oxygen probe or IR analyzer
- Over-enrichment causes soot — soot deposits insulate surfaces and cause non-uniform case

---

## 1.7 Heat Cycle

### Temperatures
- **Carburizing temperature:** 1650-1750 degF (899-954 degC)
  - Most common: 1700 degF (927 degC) for standard production
  - Higher temperatures (1750 degF / 954 degC) for faster diffusion but increased grain growth risk
  - Lower temperatures (1650 degF / 899 degC) for fine-pitch gears where grain size is critical
- **Above Ac3** (upper critical temperature) for the base steel — ensures fully austenitic structure

### Case Depth vs. Time (at 1700 degF / 927 degC)
Using ECD = K x sqrt(t), where K is approximately 0.018-0.025 in./sqrt(hr) at 1700 degF:

| Target ECD (in.) | Target ECD (mm) | Approximate Time at Temperature |
|---|---|---|
| 0.020 | 0.51 | 1.0-1.5 hours |
| 0.030 | 0.76 | 2.0-3.0 hours |
| 0.040 | 1.02 | 3.0-5.0 hours |
| 0.060 | 1.52 | 6.0-9.0 hours |
| 0.080 | 2.03 | 10-14 hours |
| 0.100 | 2.54 | 16-22 hours |
| 0.150 | 3.81 | 36-50 hours |

Note: Doubling the case depth requires approximately 4x the time (square-root relationship). A 100 degF increase in temperature roughly doubles the diffusion coefficient.

### Effective vs. Total Case Depth
- **Effective case depth (ECD):** Depth from the surface to the point where hardness equals 50 HRC (or equivalent: 513 HV, approximately 0.40% carbon)
- **Total case depth:** Depth to the point where the carbon content or hardness is indistinguishable from the core — typically 1.5-2.0x the ECD

### Cycle Structure (Typical Boost/Diffuse for 0.040 in. ECD at 1700 degF)
1. Heat to 1700 degF — approximately 1-2 hours depending on load mass
2. Boost at 1.0% carbon potential — 2.5 hours
3. Diffuse at 0.80% carbon potential — 1.5 hours
4. Cool to quench temperature (if reheat quench: cool to room temp; if direct quench: proceed to oil)

---

## 1.8 Quench Stage

### Quench Media Options
| Medium | H-Factor (Grossmann) | Typical Use |
|---|---|---|
| Still oil | 0.25-0.30 | Slow quench, low distortion |
| Agitated oil (moderate) | 0.35-0.50 | Standard production |
| Agitated oil (vigorous) | 0.50-0.80 | Higher hardenability demand |
| Marquench oil (hot oil) | 0.20-0.35 | Reduced distortion; oil at 250-400 degF (121-204 degC) |
| Polymer (10-20% PAG) | 0.30-0.80 | Adjustable; cleaner than oil |
| Agitated water | 1.0-1.5 | Severe quench (rarely used for carburized parts — cracking risk) |
| High-pressure gas (N2, 10 bar) | 0.10-0.20 | Vacuum furnace quenching |
| High-pressure gas (He, 20 bar) | 0.20-0.35 | Aerospace vacuum carburizing |

### Oil Quench Parameters
- **Standard quench oil temperature:** 100-160 degF (38-71 degC)
- **Marquench (hot oil) temperature:** 250-400 degF (121-204 degC) — held above Ms point briefly, then air cooled
- **Agitation:** Propeller or pump agitation; 50-200 ft/min flow velocity across the load
- **Oil maintenance:** Monitor viscosity, flash point, water content (less than 0.05%), and oxidation level

### Distortion Control Strategies
- Press quenching for flat parts (gears, discs)
- Plug quenching for bores and splined parts
- Controlled agitation direction to ensure uniform cooling
- Marquenching to reduce thermal gradient between surface and core
- Part orientation during quench (bore vertical for ring gears)

---

## 1.9 Temper & Inspection

### Tempering
- **Temperature:** 300-375 degF (149-191 degC) — low-temperature temper to relieve quench stress without significant hardness loss
- **Time:** 2 hours minimum at temperature per AMS 2759/7; many shops use 2-4 hours
- **Double temper:** Required for some aerospace applications (especially 9310 steel); two full temper cycles
- **Refrigeration (sub-zero treatment):** -100 to -120 degF (-73 to -84 degC) between tempers to transform retained austenite; specified when retained austenite must be below 10%

### Hardness Targets
| Location | Typical Range |
|---|---|
| Surface (case) | 58-63 HRC |
| Core | 25-45 HRC (varies by grade: 8620 ~30-40 HRC; 9310 ~35-44 HRC) |

### Case Depth Measurement (per SAE J423)
- **Microhardness traverse:** Knoop or Vickers indentations at incremental depths; ECD = depth to 50 HRC equivalent
- **Chemical method:** Step machining and carbon analysis at each depth (laboratory method)
- **File test:** Qualitative shop-floor check — hardened file will not cut properly hardened case
- **Fracture test:** Break test piece; case appears fine-grained and lighter than core

### Metallographic Examination
- Mount, polish, and etch cross-section (2% Nital or 4% Picral)
- Evaluate: case microstructure (fine tempered martensite desired), core microstructure, carbide morphology
- **Retained austenite:** Must not exceed 20% per AMS 2759/7 in the outer 10% of case; measured by point count or XRD
- **Intergranular oxidation (IGO):** Dark-etching network along prior austenite grain boundaries in the outer 0.0005-0.001 in. (0.013-0.025 mm); caused by oxidation of Cr, Mn, Si by CO2/H2O in atmosphere; must be removed by grinding
- **Non-martensitic transformation products (NMTP):** Bainite or pearlite in the case indicates insufficient quench severity

### Common Defects
| Defect | Cause | Remedy |
|---|---|---|
| Retained austenite (excess) | High surface carbon, high alloy content, insufficient quench | Reduce carbon potential; sub-zero treatment; ensure quench severity |
| Intergranular oxidation (IGO) | CO2 and H2O in endo atmosphere at grain boundaries | Vacuum carburize (eliminates IGO); or grind off 0.002-0.003 in. |
| Decarburization | Air leaks, improper purge, low carbon potential | Fix furnace seals; verify atmosphere composition |
| Soft spots | Part contact, gas starvation, oil contamination | Improve fixturing; increase agitation; clean quench oil |
| Carbide network | Surface carbon too high (above 1.0% C); insufficient diffuse time | Lower carbon potential; extend diffuse cycle |
| Excessive grain growth | Temperature too high or time too long | Reduce temperature; use fine-grain steels (Al-killed) |

---

# CLUSTER 2: VACUUM CARBURIZING (LOW PRESSURE CARBURIZING / LPC)

## 2.1 Process Flow Poster Data

### What Is Vacuum Carburizing?
Vacuum carburizing (also called Low Pressure Carburizing or LPC) is a carburizing process performed in a vacuum furnace at low pressures (5-15 mbar / 4-11 torr) using pulsed hydrocarbon gas — typically acetylene (C2H2) — instead of a continuous endothermic atmosphere. The carbon source gas is introduced in short "boost" pulses, followed by vacuum "diffuse" phases where no gas is present and carbon diffuses inward.

### Mechanism of Action
1. Furnace is evacuated to hard vacuum (less than 0.1 mbar)
2. Parts heated to carburizing temperature under vacuum (no atmosphere — no oxidation)
3. Acetylene (C2H2) pulsed into the chamber at 5-15 mbar (4-11 torr) during boost phases
4. Acetylene thermally decomposes on the hot steel surface, depositing atomic carbon
5. Boost pulse terminated; chamber re-evacuated to diffuse pressure
6. Carbon diffuses inward during diffuse phase (Fick's Law applies identically to gas carburizing)
7. Boost/diffuse cycles repeated until target carbon profile is achieved
8. Quench: either high-pressure gas quench (HPGQ) in the same chamber or transfer to oil quench

### What It Produces
- **Effective case depth:** 0.010-0.200 in. (0.25-5.0 mm) — same range as gas carburizing
- **Surface hardness:** 58-63 HRC
- **Core hardness:** 25-45 HRC
- **Surface carbon:** 0.75-1.05% C (controlled by boost/diffuse recipe simulation)
- **Critical advantage: Zero intergranular oxidation (IGO)** — vacuum atmosphere contains no O2, CO2, or H2O
- **Clean, bright surface finish** — no oxidation scale

### Steels Used
Same carburizing grades as gas carburizing: 8620, 4320, 9310, 3310, 4620, 4820, 17CrNiMo6, plus:
- **High-alloy steels:** M50NiL (AMS 6278) — aerospace bearing steel; LPC handles high-Cr steels better than gas (no Cr-oxide passivation layer)
- **Powder metallurgy steels:** LPC excels with PM gears due to surface porosity — endo gas penetrates pores in gas carburizing but vacuum avoids this

### Key Applications & Industries
- **Aerospace:** Helicopter transmission gears (9310, M50NiL), turbine engine bearing races
- **Automotive:** High-volume transmission gears (continuous LPC lines), differential components
- **Precision components:** Fuel injector parts, valve train components
- **Medical devices:** Implant-grade components requiring clean surfaces

### Applicable Specifications
- **AMS 2759/7E** — Covers both gas and vacuum carburizing
- **CQI-9 (4th ed.)** — Includes LPC process tables
- **AGMA 2004-C08** — References vacuum carburizing for gear applications
- **OEM-specific:** Many automotive OEMs have internal LPC specifications

### 9-Step Process Sequence
1. **Pre-clean** — Solvent wash; parts must be completely dry (moisture contaminates vacuum system)
2. **Load** — Carbon/graphite fixtures or ceramic supports (no alloy steel fixtures — would carburize)
3. **Evacuate** — Pump down to less than 0.1 mbar (hard vacuum)
4. **Heat** — Ramp to 1700-1850 degF (927-1010 degC) under vacuum; higher temperatures common because no grain boundary oxidation risk
5. **Boost** — Pulse acetylene at 5-15 mbar (4-11 torr) for controlled time (seconds to minutes per pulse)
6. **Diffuse** — Re-evacuate; hold at carburizing temperature with no gas flow; carbon diffuses inward
7. **Repeat boost/diffuse** — Multiple cycles per recipe (computer-controlled; 5-30+ cycles typical)
8. **Quench** — HPGQ with N2 at 10-20 bar, or He at 15-20 bar; alternatively, transfer to integrated oil quench
9. **Temper** — Same as gas carburizing: 300-375 degF (149-191 degC), 2+ hours

---

## 2.2 Safety & PPE

### Vacuum System Hazards
- **Acetylene is explosive** (lower explosive limit 2.5% in air, wide flammability range up to 100%) — stored in cylinders with acetone solvent; never exceed 15 psig (1 bar gauge) line pressure
- **Vacuum chamber implosion risk** — thick-walled vessels, but inspect viewports and seals regularly
- **Hot gas quench release:** 10-20 bar N2 or He release generates significant pressure in the vessel; verify all interlocks before initiating quench
- **Burn hazard:** Parts exit at elevated temperature after gas quench (typically 150-300 degF / 66-149 degC)

### PPE Requirements
- Same high-temperature PPE as gas carburizing for loading/unloading
- **Hearing protection** during high-pressure gas quench cycle (blower noise can exceed 90 dB)
- **Confined space awareness** if vacuum chamber maintenance is required — N2 asphyxiation risk
- No endothermic gas hazards — eliminates CO exposure risk (major safety advantage of LPC)

### Fire Suppression
- Oil quench systems (if equipped) require same fire suppression as gas carburizing
- Gas quench systems: no fire risk from quench media

---

## 2.3 Part Preparation

### Machining Allowance
- Same as gas carburizing: 0.005-0.015 in. (0.13-0.38 mm) grinding stock per surface
- **Advantage:** IGO layer is absent, so less grinding stock may be acceptable (some specs allow 0.001-0.002 in. less than gas carburized parts)

### Surface Condition
- Same cleanliness requirements as gas carburizing
- **Additional:** Parts must be completely free of moisture, chlorinated solvents, and volatile contaminants — these degrade vacuum quality and pump oil

### Masking
- **Copper plate** remains the standard for selective carburizing in vacuum
- **Mechanical masking:** Tight-fitting metal caps or plugs can exclude gas from bores/threads (more effective in vacuum than in gas due to low pressure)

---

## 2.4 Loading & Fixturing

### Fixture Materials
- **Carbon/graphite (CFC — carbon fiber composite):** Primary fixture material for LPC; does not carburize, stable at temperature, lightweight
- **Ceramic (silicon carbide, alumina):** Used for pins and supports
- **Alloy steel fixtures should NOT be used** — they absorb carbon from the acetylene and distort

### Part Orientation
- Same principles as gas carburizing: maximize uniform gas access
- LPC excels at carburizing blind holes and deep bores because acetylene penetrates at low pressure (mean free path effect)
- Dense loads may require more boost/diffuse cycles to ensure uniformity

### Thermocouple Placement
- Thermocouples must be sheathed to prevent damage to vacuum system
- Load TC in representative heavy section
- **Optical pyrometry** increasingly used in vacuum furnaces for non-contact temperature measurement

---

## 2.5 Furnace / System Setup

### Furnace Types
- **Single-chamber vacuum furnace:** Load, heat, carburize, and gas quench in one chamber; most versatile
- **Multi-chamber (modular):** Separate preheat, carburize, and quench chambers with internal transfer mechanism; higher throughput; e.g., ECM Icbp or SECO/WARWICK CaseMaster Evolution
- **Continuous multi-chamber:** Automotive high-volume production; parts move through on pallets

### Temperature Capability
- **Standard range:** 1700-1850 degF (927-1010 degC)
- **High-temperature carburizing:** Up to 1900 degF (1038 degC) is possible in vacuum (not practical in gas due to severe IGO and grain growth)
- Higher temperature = faster diffusion = shorter cycle times (major productivity advantage)

### Vacuum System
- **Roughing pump + roots blower** minimum; some systems add diffusion pump or turbo pump for harder vacuum
- Base pressure: less than 0.1 mbar (less than 0.075 torr) before heating
- Leak rate: less than 5 microns/hour for most specifications

---

## 2.6 Atmosphere / Cycle Control

### Carbon Source Gas
- **Acetylene (C2H2):** Preferred for most modern LPC systems; clean decomposition, no soot at low pressure, good uniformity
- **Propane (C3H8):** Used in some older systems; higher soot tendency
- **Ethylene (C2H4):** Alternative hydrocarbon; less common

### Boost/Diffuse Parameters
- **Boost pressure:** 5-15 mbar (4-11 torr) — acetylene flow controlled by mass flow controllers
- **Diffuse pressure:** less than 1 mbar (vacuum — no gas flow)
- **Boost pulse duration:** 30 seconds to 5 minutes (short pulses for thin case, longer for heavy case)
- **Diffuse duration:** 2-30 minutes depending on target case depth and cycle position
- **Number of cycles:** 5-30+ per recipe
- **Total cycle time example:** 0.040 in. ECD at 1800 degF (982 degC) — approximately 2.0-2.5 hours total boost/diffuse time (vs. 4-5 hours gas carburizing at 1700 degF)

### Process Simulation
- **SimVac, CarbTool, DANTE, DEFORM** — commercial software packages that simulate boost/diffuse cycles, predict carbon profiles, and optimize recipes
- Recipe is pre-calculated; furnace runs automatically per the simulation output
- **No oxygen probe or dew point** — carbon potential is not measured in real time; it is controlled by recipe (gas flow, pressure, time)

---

## 2.7 Heat Cycle

### Temperature
- Standard LPC: 1700-1800 degF (927-982 degC) — same as gas carburizing
- High-temp LPC: 1800-1900 degF (982-1038 degC) — reduces cycle time by 30-50%
- Ultra-high temp: up to 1950 degF (1066 degC) for specialty applications (requires vacuum grain size control steels)

### Case Depth vs. Time (approximate at 1800 degF / 982 degC)
| Target ECD (in.) | Target ECD (mm) | Total Boost+Diffuse Time |
|---|---|---|
| 0.020 | 0.51 | 0.5-1.0 hours |
| 0.030 | 0.76 | 1.0-1.5 hours |
| 0.040 | 1.02 | 1.5-2.5 hours |
| 0.060 | 1.52 | 3.0-5.0 hours |
| 0.080 | 2.03 | 5.0-8.0 hours |

Note: These times are significantly shorter than gas carburizing at 1700 degF due to the higher operating temperature.

### Distortion Comparison vs. Gas Carburizing
- HPGQ (gas quench) produces less distortion than oil quench — no film boiling, no vapor blanket nonuniformity
- Vacuum heating eliminates surface oxidation — cleaner parts, less post-processing
- Typical distortion reduction of 30-50% vs. gas carburizing with oil quench (application-dependent)

---

## 2.8 Quench Stage

### High-Pressure Gas Quench (HPGQ)
| Gas | Pressure | H-Factor (approx.) | Cooling Rate |
|---|---|---|---|
| Nitrogen (N2) | 10 bar | 0.10-0.15 | Slow-moderate |
| Nitrogen (N2) | 20 bar | 0.15-0.25 | Moderate |
| Helium (He) | 15 bar | 0.20-0.30 | Moderate-fast |
| Helium (He) | 20 bar | 0.30-0.40 | Fast |
| He/N2 mix | 20 bar | 0.25-0.35 | Moderate-fast |

- HPGQ is the primary quench method for LPC
- Helium provides higher cooling rate than nitrogen at equal pressure (better thermal conductivity)
- **Limitation:** HPGQ may not provide sufficient quench severity for thick sections (greater than 1.5 in. / 38 mm) in lean-alloy steels — oil quench may be required

### Oil Quench in Vacuum
- Some vacuum furnaces include an internal oil quench chamber
- Parts transferred from heating chamber to oil quench under vacuum or inert atmosphere
- Oil temperature and agitation same as gas carburizing parameters

---

## 2.9 Temper & Inspection

### Tempering
- Same as gas carburizing: 300-375 degF (149-191 degC), 2+ hours minimum
- Sub-zero treatment: -100 to -120 degF (-73 to -84 degC) if retained austenite reduction required
- Double temper for aerospace applications

### Inspection Advantages
- **No IGO to measure or remove** — eliminates a major inspection step and potential rejection cause
- **No surface oxidation** — cleaner metallographic sections
- Otherwise, same hardness traverse, case depth measurement, and microstructure evaluation as gas carburizing

### Common Defects Specific to LPC
| Defect | Cause | Remedy |
|---|---|---|
| Soot / carbon black deposits | Excessive boost pressure or time; propane vs. acetylene | Reduce boost pressure; switch to acetylene; verify mass flow calibration |
| Non-uniform case (variation across load) | Gas flow pattern in chamber; load density too high | Optimize loading pattern; increase diffuse time between boosts |
| Excessive retained austenite | Same causes as gas carburizing | Sub-zero treatment; verify surface carbon via simulation |
| Free carbides at surface | Too many boost cycles without sufficient diffuse | Extend diffuse phases; re-run simulation |
| Grain growth | Temperature too high (above 1900 degF without microalloy control) | Reduce temperature; use vacuum-grade fine-grain steel |

---

# CLUSTER 3: CARBONITRIDING

## 3.1 Process Flow Poster Data

### What Is Carbonitriding?
Carbonitriding is a modified gas carburizing process in which ammonia (NH3) is added to the endothermic carburizing atmosphere. This results in simultaneous diffusion of both carbon AND nitrogen into the steel surface. Nitrogen acts as an additional hardening element and lowers the critical cooling rate, allowing oil quenching of plain carbon steels that would otherwise not through-harden.

### Mechanism of Action
1. Parts heated to 1400-1650 degF (760-899 degC) — lower than straight carburizing
2. Endothermic atmosphere + enrichment gas provides carbon (same as carburizing)
3. Ammonia (2-10% by volume) dissociates at the steel surface: 2NH3 -> 2N + 3H2
4. Both carbon and nitrogen diffuse interstitially into the austenite
5. Nitrogen stabilizes austenite and increases hardenability, enabling oil quench on lean steels
6. Quench produces a hard case of carbon-nitrogen martensite

### What It Produces
- **Effective case depth:** 0.003-0.030 in. (0.076-0.76 mm) — shallower than carburizing
- **Maximum practical case depth:** ~0.030 in. (0.75 mm); deeper cases are not economical
- **Surface hardness:** 55-62 HRC
- **Core hardness:** Depends on steel grade; 15-35 HRC for plain carbon steels
- **Surface nitrogen content:** 0.10-0.40% N (absorbed from ammonia)
- **Residual stress:** Compressive in case (similar to carburizing)

### Steels Used
| Grade | Why Carbonitrided |
|---|---|
| 1018 / 1020 | Plain carbon — nitrogen addition provides hardenability that carbon alone cannot |
| 1022 | Low carbon; excellent response to carbonitriding |
| 12L14 | Free-machining; nitrogen compensates for low hardenability |
| 1117 / 1141 | Resulfurized; commonly carbonitrided for fastener applications |
| 8620 | Sometimes carbonitrided for shallow case; carburized for deeper case |
| 1045 / 1050 | Medium carbon; carbonitrided for thin hard case on already-tough core |

### Key Applications & Industries
- **Fasteners:** Screws, bolts, pins, clips (high-volume, shallow case)
- **Small parts:** Bushings, washers, rollers, pivot pins
- **Consumer goods:** Hand tools, locks, hinges
- **Automotive:** Rocker arm pads, valve lifters, small gears
- **Agriculture:** Equipment wear parts

### Applicable Specifications
- **AMS 2759/7E** — Includes carbonitriding
- **ASTM A1059** — Standard practice for measuring case depth
- **SAE J423** — Case depth measurement
- **CQI-9** — Automotive heat treat system assessment

### 9-Step Process Sequence
1. **Pre-clean** — Alkaline wash or solvent degrease
2. **Load** — Tumble-load small parts in baskets; orient larger parts for uniform gas access
3. **Purge** — Nitrogen purge then introduce endo atmosphere
4. **Heat** — Ramp to 1400-1650 degF (760-899 degC)
5. **Carbonitriding** — Endothermic atmosphere + enrichment gas + 2-10% ammonia; hold for 30 min to 4 hours
6. **Quench** — Oil quench (standard); oil at 100-160 degF (38-71 degC)
7. **Wash** — Remove quench oil
8. **Temper** — 300-375 degF (149-191 degC) for 1-2 hours
9. **Inspect** — Hardness, case depth, microstructure

---

## 3.2 Safety & PPE

### Atmosphere Hazards
- Same endothermic gas hazards as gas carburizing (CO + H2)
- **Ammonia (NH3):** OSHA PEL 50 ppm TWA, IDLH 300 ppm; pungent odor detectable at 5-25 ppm; causes respiratory irritation and chemical burns at higher concentrations
- **Ammonia leak detection:** Electronic sensors at floor level (NH3 is lighter than air — rises) and at cylinder storage area
- **Ammonia cylinder handling:** Must be stored upright, away from heat sources, with protective caps when not in use

### PPE
- Same as gas carburizing plus:
- **Ammonia-rated respiratory protection** (chemical cartridge or SCBA for emergency response)
- **Chemical splash goggles** when handling ammonia cylinders or connections
- **Emergency eyewash/shower** within 10 seconds of ammonia use area (OSHA 29 CFR 1910.151)

---

## 3.3 Part Preparation

### Machining Allowance
- Thin case depth (0.003-0.030 in.) means grinding stock is minimal: 0.002-0.005 in. (0.05-0.13 mm) per surface
- Many carbonitrided parts are used as-quenched-and-tempered (no post-grind)

### Surface Condition
- Same requirements as carburizing: clean, dry, free of scale and cutting fluids
- Small parts: tumble-deburr before processing

### Masking
- Copper plate (same as carburizing) for selective treatment
- Less common than in carburizing — most carbonitrided parts are fully case-hardened

---

## 3.4 Loading & Fixturing

### Fixture Materials
- Same heat-resistant alloys as carburizing (HU, RA 330)
- **Basket loading:** Small parts dumped into wire baskets with mesh sufficient to allow gas penetration; maximum basket depth typically 4 in. (100 mm) to ensure parts in center are treated

### Part Orientation
- Small parts: tumble-loaded; shake basket periodically if possible (some continuous furnaces have vibrating conveyors)
- Larger parts: space on trays same as carburizing

### Thermocouple Placement
- Load TC at center of heaviest basket or at core of largest part
- Multiple TCs for large loads to verify uniformity

---

## 3.5 Furnace / System Setup

### Furnace Types
- **Batch integral quench** (most common for job shops)
- **Continuous mesh belt** (high-volume small parts — most common for fastener industry)
- **Rotary retort** (small parts in rotating drum)
- **Shaker hearth** (continuous furnace with vibrating hearth for small parts)

### Temperature Uniformity
- AMS 2750 Class 3 or Class 4 typical
- Lower operating temperature than carburizing reduces thermal stress on furnace components

### Atmosphere System
- Same endothermic generator or N2/methanol system as carburizing
- **Plus ammonia (NH3) injection system:** Separate flow meter and metering valve; NH3 added directly to furnace
- NH3 flow rate: 2-10% of total atmosphere volume
- Higher ammonia percentages at the beginning of the cycle, reduced toward the end to control retained austenite

---

## 3.6 Atmosphere / Cycle Control

### Carbon Potential
- Controlled same as gas carburizing (oxygen probe, dew point, IR analyzer)
- Target: 0.70-0.95% C (slightly lower than straight carburizing to accommodate nitrogen contribution to hardness)

### Ammonia Control
| Parameter | Value |
|---|---|
| NH3 addition rate | 2-10% by volume of furnace atmosphere |
| Typical starting rate | 5-8% (beginning of cycle for nitrogen enrichment) |
| Typical ending rate | 2-3% (end of cycle to limit retained austenite) |
| Dissociation rate in furnace | Monitor at exhaust; 30-50% dissociation typical at carbonitriding temperatures |

### Nitrogen in the Case
- Surface nitrogen content: 0.10-0.40% N
- Nitrogen depresses the Ms (martensite start) temperature — increases retained austenite tendency
- Excessive ammonia (above 10%) causes porosity and excessive retained austenite
- **Rule of thumb:** For each 0.1% increase in nitrogen content, retained austenite increases by approximately 5%

---

## 3.7 Heat Cycle

### Temperature
- **Carbonitriding temperature range:** 1400-1650 degF (760-899 degC)
- Most common: 1550-1600 degF (843-871 degC) for general production
- Lower end (1400-1500 degF / 760-816 degC) for very thin case (0.003-0.005 in.)
- Higher end (1600-1650 degF / 871-899 degC) for deeper case (0.020-0.030 in.)
- **Always below straight carburizing temperature** — nitrogen diffuses more slowly and dissociates above ~1650 degF

### Case Depth vs. Time (at 1550 degF / 843 degC)
| Target ECD (in.) | Target ECD (mm) | Time at Temperature |
|---|---|---|
| 0.003-0.005 | 0.08-0.13 | 30-45 minutes |
| 0.008-0.010 | 0.20-0.25 | 1.0-1.5 hours |
| 0.015-0.020 | 0.38-0.51 | 2.0-3.0 hours |
| 0.025-0.030 | 0.64-0.76 | 3.0-4.0 hours |

---

## 3.8 Quench Stage

### Quench Media
- **Oil quench is standard** — the nitrogen in the case lowers critical cooling rate, making oil quench sufficient even for plain carbon steels
- Oil temperature: 100-160 degF (38-71 degC)
- Agitation: moderate to vigorous
- **This is the key advantage of carbonitriding:** 1018 and 1020 steel, which cannot be oil-quench hardened by carburizing alone (insufficient hardenability), achieve full case hardness when carbonitrided due to nitrogen's effect on hardenability

### Water and Polymer Quench
- Rarely used — oil is almost always adequate
- Water quench causes cracking risk on shallow-case parts

---

## 3.9 Temper & Inspection

### Tempering
- **Temperature:** 300-375 degF (149-191 degC)
- **Time:** 1-2 hours minimum
- Some high-volume operations use 350 degF (177 degC) for 1 hour as minimum

### Hardness Targets
| Location | Range |
|---|---|
| Surface | 55-62 HRC |
| Core (1018) | 15-25 HRC |
| Core (8620) | 30-40 HRC |

### Case Depth Measurement
- **Microhardness traverse:** Same method as carburizing; ECD to 50 HRC
- **Nitrogen profile:** Measured by GDOES (glow discharge optical emission spectrometry) or EPMA if required
- **File test:** Adequate for production screening

### Common Defects
| Defect | Cause | Remedy |
|---|---|---|
| Excessive retained austenite | Too much ammonia, high nitrogen content | Reduce NH3 flow; sub-zero treat |
| Porosity (surface voids) | NH3 too high (above 10%); nitrogen gas evolution at grain boundaries | Reduce ammonia addition rate |
| Soft spots | Part contact, insufficient quench severity | Improve fixturing and agitation |
| Shallow case | Insufficient time or temperature; low carbon potential | Extend time; verify atmosphere |
| Flaking/spalling | Case too hard on soft core; excessive case thickness on thin section | Reduce case depth; consider alternative process |

---

# CLUSTER 4: GAS NITRIDING

## 4.1 Process Flow Poster Data

### What Is Gas Nitriding?
Gas nitriding is a thermochemical surface hardening process in which nitrogen is diffused into the surface of a steel part at temperatures below the lower critical temperature (Ac1). The steel remains in the ferritic state throughout — there is no phase transformation and no quench. Hardening is achieved by the formation of hard nitride precipitates (iron nitrides and alloy nitrides) within the ferrite matrix.

### Mechanism of Action
1. Steel heated to 925-1050 degF (496-566 degC) — below Ac1 (approximately 1333 degF / 723 degC)
2. Ammonia (NH3) gas flows over the part surface
3. NH3 dissociates on the hot steel surface: 2NH3 -> 2N(adsorbed) + 3H2
4. Nascent nitrogen diffuses into the ferrite lattice
5. Nitrogen reacts with alloying elements (Cr, Mo, Al, V, W) to form fine, coherent nitride precipitates
6. Precipitates create extreme hardness (up to 70 HRC / 1100+ HV) without quenching
7. A compound zone ("white layer") of iron nitride (epsilon-Fe2-3N and/or gamma-prime-Fe4N) forms at the very surface

### What It Produces
- **Compound zone (white layer):** 0-0.001 in. (0-25 micrometers) of iron nitride at surface; very hard but brittle
- **Diffusion zone:** Below compound zone; nitride precipitates in ferrite; extends to 0.005-0.030 in. (0.13-0.76 mm)
- **Total case depth:** 0.005-0.030 in. (0.13-0.76 mm); deeper cases possible with extended time (40-90 hours)
- **Surface hardness:** 50-70 HRC equivalent (700-1200 HV) — varies greatly by steel grade
- **Core hardness:** Unchanged from pre-heat-treat condition (part must be quenched and tempered BEFORE nitriding)
- **Residual stress:** Compressive in the nitrided case (excellent fatigue resistance)
- **No distortion from quench** — no phase transformation occurs

### Steels Used
| Grade | Hardness Achievable (HV) | Notes |
|---|---|---|
| Nitralloy 135M (AMS 6470) | 950-1100 HV | Highest response; contains 1% Al |
| Nitralloy EZ | 900-1050 HV | Free-machining version |
| 4140 | 500-650 HV | Common medium-carbon alloy; moderate response |
| 4340 | 500-650 HV | Higher toughness core; similar nitriding response to 4140 |
| H13 | 900-1100 HV | Hot-work die steel; excellent nitriding response (5% Cr) |
| D2 | 800-1000 HV | Cold-work die steel |
| D6AC | 600-800 HV | Aerospace structural steel |
| H11 | 850-1050 HV | Hot-work die steel |
| 38CrMoAl (EN) | 950-1100 HV | European nitriding steel equivalent to Nitralloy |

**Key principle:** Steels containing nitride-forming elements (Al, Cr, Mo, V, W, Ti) develop the hardest nitrided cases. Plain carbon steels develop only iron nitride (relatively soft case around 350-450 HV) and are not normally gas nitrided.

### Key Applications & Industries
- **Aerospace:** Landing gear components (4340, D6AC), actuator shafts, bearing journals
- **Tooling:** Hot-work dies (H13, H11), extrusion dies, die-casting cores
- **Automotive:** Crankshafts (if nitriding steel), valve stems, piston pins
- **Firearms:** Barrel bores, bolt carriers
- **Gears:** Where distortion cannot be tolerated (no quench = minimal distortion)

### Applicable Specifications
- **AMS 2759/6D** — Gaseous nitriding controlled by ammonia dissociation (two-stage process)
- **AMS 2759/10A** — Automated gaseous nitriding controlled by nitriding potential (KN)
- **AMS 6470** — Nitralloy 135M material specification
- **SAE J423** — Case depth measurement

### White Layer Classes (per AMS 2759/10)
| Class | White Layer Maximum |
|---|---|
| 0 | No white layer permitted |
| 1 | 0.0005 in. (12.7 micrometers) maximum |
| 2 | 0.001 in. (25 micrometers) maximum |

### 9-Step Process Sequence
1. **Pre-heat-treat** — Part MUST be quenched and tempered to final core hardness BEFORE nitriding (temper temperature at least 50 degF / 28 degC above nitriding temperature to prevent core softening)
2. **Pre-clean** — Solvent wash; vapor degrease; surface must be free of all oils, oxides, and passivation films
3. **Activate surface** — Some shops do a light abrasive blast or chemical activation to remove passive Cr oxide on high-Cr steels
4. **Load** — Fixture parts with spacing for uniform gas flow
5. **Purge furnace** — Nitrogen purge to remove air; then introduce ammonia
6. **Stage 1 nitriding** — 925-975 degF (496-524 degC), 15-30% NH3 dissociation, 15-40 hours
7. **Stage 2 nitriding (if 2-stage)** — 1000-1050 degF (538-566 degC), 75-85% NH3 dissociation, 10-30 hours; controls white layer growth
8. **Cool** — Furnace cool under ammonia to 300 degF (149 degC), then air cool. NO QUENCH
9. **Inspect** — Surface hardness (superficial Rockwell or microhardness), case depth, white layer thickness

---

## 4.2 Safety & PPE

### Ammonia Hazards
- **Primary hazard** — anhydrous ammonia is the sole process gas
- OSHA PEL: 50 ppm TWA; IDLH: 300 ppm
- Corrosive to eyes, skin, and respiratory tract
- **Lighter than air** — accumulates at ceiling height; ventilate from top of building
- **Ammonia detection system** required at all nitriding installations
- Dissociated ammonia leaving the furnace contains H2 (flammable) — burn-off pilot required at exhaust

### PPE
- Ammonia-rated full-face respirator with chemical cartridge (NIOSH-approved for NH3)
- Chemical splash goggles when connecting/disconnecting ammonia cylinders
- Rubber or nitrile gloves for ammonia handling
- Emergency SCBA accessible within 30 seconds
- Standard heat-resistant PPE for furnace loading/unloading (lower risk than carburizing due to lower temperature)

### Emergency Response
- **Ammonia release:** Evacuate area; approach from upwind; water fog (NOT solid stream) to knock down vapor cloud
- **Hydrogen accumulation:** Ensure burn-off pilot is always lit during nitriding cycle; H2 explosion risk if pilot fails

---

## 4.3 Part Preparation

### Critical Pre-Treatment
- Parts MUST be in final heat-treated condition (quenched and tempered) before nitriding
- Tempering temperature of pre-treatment must exceed nitriding temperature by at least 50 degF (28 degC) to prevent core softening during nitriding
- Example: If nitriding at 975 degF (524 degC), temper at minimum 1025 degF (552 degC) during pre-treatment
- **Stress relief after rough machining** recommended to prevent distortion during long nitriding cycle

### Surface Preparation
- Surfaces must be free of:
  - Passivation films (Cr2O3 on high-Cr steels — may need mechanical abrasion or chemical activation)
  - Residual cutting fluids (sulfur compounds poison the nitriding reaction)
  - Fingerprints (oils block nitrogen diffusion — wear gloves when handling pre-nitrided parts)
  - Paint, ink, or marking compounds

### Masking for Selective Nitriding
- **Tin electroplate:** 0.0003-0.0005 in. (7.6-12.7 micrometers) — most common stop-off for nitriding
- **Nickel electroplate:** 0.001 in. (25 micrometers) — also effective
- **Copper plate:** NOT effective for nitriding stop-off (unlike carburizing) — copper does not block nitrogen diffusion
- **Proprietary stop-off paints:** Some commercial products available; less reliable than electroplate

---

## 4.4 Loading & Fixturing

### Fixturing
- **Alloy fixtures:** Standard alloy fixture materials acceptable (fixtures do not absorb nitrogen at these temperatures as aggressively as carbon)
- **Hanging vs. laying:** Hang parts vertically where possible to prevent contact marks and allow uniform gas flow
- **Spacing:** 0.5-1.0 in. (12.7-25.4 mm) minimum between parts
- **Long cycle time consideration:** Fixtures must support parts without creep for 40-90+ hours at temperature

---

## 4.5 Furnace / System Setup

### Furnace Types
- **Pit (vertical retort):** Most common for gas nitriding; parts hang vertically from top of retort; retort sealed with fan for atmosphere circulation
- **Bell furnace:** Similar to pit but inverted; bell lowers over base plate
- **Horizontal batch retort:** Parts loaded on trays into horizontal retort
- **Continuous furnaces:** Rare for gas nitriding due to long cycle times

### Atmosphere System
- **Anhydrous ammonia (NH3)** from cylinders or bulk tank
- **Flow rate:** Controlled by rotameter or mass flow controller; sufficient to maintain target dissociation rate
- **Dissociator (optional):** Pre-dissociates some NH3 to adjust nitriding potential
- **Exhaust system:** Burn-off pilot or catalytic converter to combust H2 and unreacted NH3

---

## 4.6 Atmosphere / Cycle Control

### Single-Stage Process
- Temperature: 925-975 degF (496-524 degC)
- NH3 dissociation: 15-30%
- Time: 24-90 hours (depending on case depth required)
- Produces relatively thick white layer (0.0005-0.001 in.)

### Two-Stage (Floe) Process (per AMS 2759/6)
- **Stage 1:** 925-975 degF (496-524 degC), 15-30% NH3 dissociation, 15-40 hours — builds case depth
- **Stage 2:** 1000-1050 degF (538-566 degC), 75-85% NH3 dissociation, 10-30 hours — reduces/controls white layer while extending diffusion zone
- The higher dissociation in Stage 2 reduces the nitriding potential at the surface, limiting further white layer growth

### Nitriding Potential Control (per AMS 2759/10)
- **Nitriding potential (KN)** = P(NH3) / P(H2)^(3/2)
- Directly controls the nitrogen activity at the steel surface
- **Stage 1 KN:** 4-15 (high potential for rapid nitrogen uptake)
- **Stage 2 KN:** Varies by class:
  - Class 0 (no white layer): KN = 0.2-0.8
  - Class 1 (0.0005 in. max WL): KN = 0.4-2.6
  - Class 2 (0.001 in. max WL): KN = 1.2-5.5
- Automated systems use hydrogen sensors and ammonia analyzers to calculate and control KN in real time

### Case Depth vs. Time
| Target Case Depth (in.) | Target (mm) | Approximate Time (single-stage, 975 degF) |
|---|---|---|
| 0.008-0.010 | 0.20-0.25 | 15-24 hours |
| 0.012-0.015 | 0.30-0.38 | 24-40 hours |
| 0.018-0.020 | 0.46-0.51 | 40-60 hours |
| 0.025-0.030 | 0.64-0.76 | 60-90 hours |

---

## 4.7 Heat Cycle

- Slow ramp to nitriding temperature (100-200 degF/hr / 56-111 degC/hr) to ensure uniform part temperature
- Hold at nitriding temperature for 15-90 hours depending on case depth
- **No quench** — furnace cool under ammonia atmosphere to 300 degF (149 degC), then open furnace and air cool

---

## 4.8 Quench Stage

**Gas nitriding has NO quench.** The entire process occurs below the lower critical temperature. Parts are furnace cooled and air cooled. This is a fundamental distinction from carburizing processes. The absence of quenching is what gives nitriding its near-zero distortion advantage.

---

## 4.9 Temper & Inspection

### No Tempering Required After Nitriding
- The nitriding process itself is essentially a long, low-temperature hold — no quench stress to relieve
- Parts retain their pre-nitriding core hardness (from the prior Q&T treatment)

### Hardness Testing
- **Superficial Rockwell (HR15N, HR30N, HR45N):** Used for surface hardness check on production parts
- **Microhardness (Vickers or Knoop):** Used for case depth profile; traverse at 0.001-0.002 in. increments
- **ECD definition for nitriding:** Depth to 50 HRC equivalent (approximately 513 HV), or depth to core hardness + 50 HV (depending on specification)

### Metallographic Examination
- **White layer measurement:** Polished cross-section, unetched or lightly etched with 2% Nital; white layer appears bright (non-etching)
- **Compound zone composition:** Epsilon (Fe2-3N) vs. gamma-prime (Fe4N) — epsilon is harder but more brittle; gamma-prime is tougher; ratio controlled by nitriding potential
- **Diffusion zone:** Etches darker than core due to nitride precipitates

### Common Defects
| Defect | Cause | Remedy |
|---|---|---|
| Excessive white layer | Too high nitriding potential; too long Stage 1 | Reduce KN; implement two-stage process |
| No white layer when required | KN too low; poor atmosphere control | Increase KN; verify ammonia flow |
| Spalling/flaking of white layer | Thick, brittle epsilon white layer | Control white layer composition to gamma-prime; reduce thickness |
| Soft spots | Surface contamination (oil, oxide, Cr passive film) | Improve cleaning; activate surface before nitriding |
| Core softening | Nitriding temperature exceeds original tempering temperature | Verify pre-heat-treat temper was above nitriding temp + 50 degF |
| Uneven case | Poor gas circulation; parts too close | Improve fixturing; increase fan speed |

---

# CLUSTER 5: PLASMA NITRIDING (ION NITRIDING)

## 5.1 Process Flow Poster Data

### What Is Plasma Nitriding?
Plasma nitriding (also called ion nitriding or glow-discharge nitriding) is a thermochemical surface hardening process that uses a high-voltage glow discharge plasma to ionize nitrogen gas and accelerate nitrogen ions into the steel surface. The plasma is generated by applying a DC voltage (typically 400-1000 V) between the part (cathode) and the furnace wall (anode) in a low-pressure nitrogen-hydrogen gas mixture.

### Mechanism of Action
1. Parts placed in vacuum vessel; pumped down to 1-5 mbar (0.75-3.75 torr)
2. N2/H2 gas mixture introduced (typical: 25-75% N2, balance H2; with optional CH4 or Ar)
3. DC voltage (400-1000 V) applied; part is the cathode
4. Glow discharge plasma forms around the part surfaces
5. N2 molecules ionized in the plasma; N+ and N2+ ions accelerated toward the cathodic part
6. Ions bombard the surface: (a) sputter-clean the surface, removing oxides; (b) implant nitrogen
7. Nitrogen diffuses inward by conventional solid-state diffusion (same as gas nitriding)
8. Compound zone and diffusion zone form exactly as in gas nitriding, but process control is superior

### What It Produces
- **Compound zone:** Controllable from zero to 0.001 in. (0-25 micrometers); composition (epsilon vs. gamma-prime) controlled by gas mix
- **Diffusion zone:** 0.002-0.025 in. (0.05-0.64 mm)
- **Surface hardness:** Same as gas nitriding: 700-1200 HV depending on steel grade
- **Advantages over gas nitriding:**
  - Treats stainless steels and high-Cr steels without pre-activation (plasma sputters away Cr2O3 passive layer)
  - Selective nitriding by mechanical masking (no electroplating required)
  - Shorter cycle times (typically 50-70% of gas nitriding time)
  - Lower temperature capability: down to 660 degF (350 degC) for stainless steel applications
  - No ammonia — eliminates NH3 handling and disposal concerns
  - No hydrogen embrittlement concerns for some applications

### Steels Used
All steels suitable for gas nitriding, PLUS:
- **Austenitic stainless steels:** 304, 316 — plasma can nitride these (gas nitriding cannot due to Cr2O3 passive layer)
- **Martensitic stainless steels:** 410, 420, 440C
- **Precipitation hardening stainless:** 17-4 PH, 15-5 PH
- **Tool steels:** M2, M42 (high-speed steels)
- **Titanium alloys:** Ti-6Al-4V (specialty application)

### Key Applications & Industries
- **Aerospace:** Landing gear, actuators (same as gas nitriding but shorter cycles)
- **Automotive:** Gears, crankshafts, camshafts, valve springs
- **Tooling:** Injection molds, extrusion dies, punches, cutting tools
- **Medical:** Surgical instruments (stainless steel nitriding)
- **Firearms:** Barrels (the "Melonite" or "QPQ" process is sometimes confused with plasma nitriding but is actually FNC — Cluster 6)

### Applicable Specifications
- **AMS 2759/8** — Ion nitriding
- **NASA PRC-2004** — Process specification for ion nitriding
- **ASTM A1059** — Case depth measurement

### 9-Step Process Sequence
1. **Pre-heat-treat** — Parts must be quenched and tempered before plasma nitriding (same as gas nitriding)
2. **Pre-clean** — Solvent or alkaline wash; dry completely; no fingerprints
3. **Load** — Position parts on fixtures in vacuum vessel; ensure parts are electrically connected to cathode
4. **Pump down** — Evacuate to less than 0.1 mbar
5. **Sputter clean** — Low-pressure H2 or Ar plasma at 400-600 V for 30-60 minutes to remove surface oxides
6. **Heat to nitriding temperature** — Plasma heating (ion bombardment generates heat); supplemental wall heating in some systems; 660-1050 degF (350-566 degC)
7. **Nitride** — N2/H2 plasma at 1-5 mbar, 400-800 V, pulsed DC; 4-40 hours depending on case depth
8. **Cool** — Plasma off; furnace cool under vacuum or flowing N2 to less than 300 degF (149 degC)
9. **Inspect** — Same as gas nitriding: hardness, case depth, white layer, microstructure

---

## 5.2 Safety & PPE

### Electrical Hazards
- **High voltage (400-1000 V DC)** — primary hazard unique to plasma nitriding; lethal shock risk
- All electrical interlocks must be verified before opening the vessel
- Lock-out / tag-out (LOTO) required for maintenance on power supply or vessel
- Arc discharge risk: if parts are too close to anode (furnace wall) or if insulation is compromised

### Vacuum/Gas Hazards
- **N2 asphyxiation** risk inside vessel during maintenance
- **H2 flammable** — any leak from the gas supply creates fire/explosion risk; H2 detectors required
- No ammonia hazards (major safety advantage vs. gas nitriding)

### PPE
- Standard heat-resistant PPE for loading/unloading
- Electrical safety: insulated gloves rated for voltage class when working near power supply
- Hearing protection during pump-down cycles (pumps can exceed 85 dB)

---

## 5.3 Part Preparation

- Same as gas nitriding (pre-quenched and tempered, clean, dry)
- **No need for surface activation on stainless steels** — the sputter-clean step in the plasma cycle removes Cr2O3 passive layer automatically (major advantage)

### Masking
- **Mechanical masking only** — close-fitting metal shields, caps, or sleeves placed over areas not to be nitrided
- The glow discharge does not penetrate into tightly shielded areas — mechanical masking is uniquely effective in plasma nitriding
- **No need for electroplated stop-off** (tin or nickel) — simplifies selective treatment

---

## 5.4 Loading & Fixturing

- Parts must be electrically conductive and connected to the cathode
- Fixtures must also be conductive (steel or graphite)
- **Hollow cathode effect:** Small holes, recesses, or gaps between closely spaced parts can concentrate the plasma and cause local overheating; minimum spacing of 0.5 in. (12.7 mm) recommended; avoid deep blind holes without adequate vent
- Sheathed thermocouples contacting the parts (must be electrically isolated from the plasma circuit)
- Infrared pyrometry through viewport also used

---

## 5.5 Furnace / System Setup

### System Components
- **Vacuum vessel:** Cold-wall stainless steel chamber with water cooling
- **DC power supply:** 0-1000 V, pulsed DC (pulse frequency 1-10 kHz typical); pulsing prevents arc formation
- **Gas supply:** N2, H2, Ar (for sputter cleaning), CH4 (for nitrocarburizing variant)
- **Vacuum pumps:** Rotary vane + roots blower; base pressure less than 0.1 mbar
- **Wall heaters (optional):** Supplemental radiant heaters to assist temperature uniformity for large loads

---

## 5.6 Atmosphere / Plasma Control

### Plasma Parameters
| Parameter | Typical Range |
|---|---|
| Voltage | 400-800 V (up to 1000 V for sputter cleaning) |
| Pressure | 1-5 mbar (0.75-3.75 torr) — some systems down to 0.5 mbar |
| Gas mix (N2:H2) | 25:75 to 75:25 (varies by compound zone requirement) |
| Pulse frequency | 1-10 kHz |
| Duty cycle | 20-80% (controls effective power input and temperature) |
| Temperature | 660-1050 degF (350-566 degC) |

### Compound Zone Control via Gas Mixture
| Desired Compound Zone | Gas Mix (N2:H2) |
|---|---|
| Gamma-prime (Fe4N) dominant | 20-30% N2, balance H2 |
| Mixed epsilon + gamma-prime | 40-60% N2, balance H2 |
| Epsilon (Fe2-3N) dominant | 70-80% N2, balance H2 |
| No compound zone | Low N2 (less than 10%) + high H2 at low KN |

### Cycle Times
- Significantly shorter than gas nitriding (50-70% of gas nitriding time)
- Example: 0.015 in. (0.38 mm) case depth in 12-20 hours vs. 40-60 hours in gas nitriding

---

## 5.7 Heat Cycle / Quench / Inspection

### Heat Cycle
- Same temperatures as gas nitriding but wider range: 660-1050 degF (350-566 degC)
- Low-temperature treatment (660-750 degF / 350-400 degC) possible for stainless steels where the goal is to avoid CrN precipitation (preserving corrosion resistance while adding hardness)

### Quench
- **No quench** — same as gas nitriding; parts cooled under vacuum or N2

### Inspection
- Same metallographic and hardness testing as gas nitriding
- **S-phase (expanded austenite)** may be observed on stainless steels — a metastable nitrogen-supersaturated austenite layer with extremely high hardness (up to 1500 HV); identified by X-ray diffraction showing shifted austenite peaks

### Defects Specific to Plasma Nitriding
| Defect | Cause | Remedy |
|---|---|---|
| Arcing (micro-arc damage) | Part too close to wall; insulation failure; contamination on surface | Increase spacing; clean parts; verify insulation |
| Hollow cathode overheating | Closely spaced parts or deep recesses concentrate plasma | Increase part spacing; use shields to break hollow cathode geometry |
| Non-uniform case | Temperature variation across load; shadowing by adjacent parts | Add wall heaters; optimize loading pattern; rotate parts if possible |
| Edge effect (excessive case at edges/corners) | Plasma concentrates at sharp edges and points | Radius edges before processing; adjust voltage/pressure |

---

# CLUSTER 6: FERRITIC NITROCARBURIZING (FNC / QPQ PROCESS)

## 6.1 Process Flow Poster Data

### What Is Ferritic Nitrocarburizing?
Ferritic nitrocarburizing (FNC) is a thermochemical surface treatment in which both nitrogen and carbon are diffused into the steel surface at temperatures below the lower critical temperature (Ac1), similar to nitriding. However, FNC operates at slightly higher temperatures than pure nitriding and deliberately produces a thick epsilon iron nitride (Fe2-3N) compound zone for wear and corrosion resistance. The **QPQ process** (Quench-Polish-Quench) is a trademarked variant that adds an oxidative quench in molten salt plus a mechanical polishing step for exceptional corrosion resistance and appearance.

### Mechanism of Action
1. Part heated to 975-1125 degF (524-607 degC) — below Ac1 (ferritic range)
2. Carbon and nitrogen simultaneously diffuse into the ferrite surface
3. A thick epsilon iron nitride (Fe2-3N) compound zone forms (0.0004-0.001 in. / 10-25 micrometers)
4. Below the compound zone, a nitrogen-enriched diffusion zone forms
5. In QPQ variant: part is quenched into oxidizing salt bath (~700-800 degF / 371-427 degC), creating a black oxide layer that fills the porous compound zone, dramatically improving corrosion resistance
6. Polish step mechanically smooths the surface
7. Second oxidizing salt quench (the "second Q") further enhances corrosion protection

### What It Produces
- **Compound zone:** 0.0004-0.001 in. (10-25 micrometers) — primarily epsilon Fe2-3N
- **Diffusion zone:** 0.005-0.025 in. (0.13-0.64 mm)
- **Surface hardness:** 55-65 HRC equivalent (600-1000 HV depending on substrate)
- **Corrosion resistance (QPQ):** Exceeds hard chrome plate in salt spray testing; 200-500+ hours neutral salt spray (ASTM B117) on low-carbon steel
- **Appearance (QPQ):** Uniform matte black finish
- **Minimal distortion:** Ferritic process — no phase transformation, no quench-related distortion

### Steels Used
| Grade | Application |
|---|---|
| 1018 / 1020 / 1045 | General engineering — dramatic improvement in wear and corrosion |
| 4140 / 4340 | Hydraulic cylinders, shafts, gun barrels |
| H13 | Die casting cores and pins |
| 410 / 420 stainless | Moderate corrosion + wear improvement |
| Ductile iron | Automotive crankshafts, camshafts |
| Cast iron | Cylinder liners, brake rotors |

### Key Applications & Industries
- **Firearms:** Barrel treatment (Tenifer/Melonite process); bolt carriers; slides
- **Automotive:** Crankshafts, camshafts, piston rings, brake rotors, shift forks
- **Hydraulics:** Cylinder rods (replacement for hard chrome plate — no hexavalent chromium)
- **Tooling:** Die casting pins, injection mold cores
- **Marine:** Corrosion-resistant fasteners and shafts
- **Military:** Weapon components

### Applicable Specifications
- **AMS 2753** — Ferritic nitrocarburizing of alloy and carbon steels
- **AMS 2755** — QPQ salt bath nitrocarburizing
- **ASTM B117** — Salt spray testing (used to qualify FNC/QPQ corrosion performance)
- **TT-C-490** — Federal specification for salt bath nitrocarburizing

### Trademarked Process Names
- **Tufftride** — Durferrit/HEF salt bath FNC
- **Tenifer** — Kolene Corporation salt bath FNC
- **Melonite** — Gas FNC variant (Bodycote)
- **QPQ (Quench-Polish-Quench)** — Kolene full process with oxidizing quench and polish
- **Arcor** — Gas FNC (Nitrex)

### 9-Step Process Sequence (QPQ Variant)
1. **Pre-clean** — Alkaline wash, rinse, dry
2. **Preheat** — 600-700 degF (316-371 degC) in air or protective atmosphere; drives off moisture
3. **Nitrocarburize** — Immerse in molten salt bath (cyanate-based) at 1050-1075 degF (566-580 degC) for 60-120 minutes; OR gas FNC in NH3 + CO2 atmosphere
4. **Oxidizing salt quench (Q1)** — Transfer to oxidizing salt bath at 700-800 degF (371-427 degC) for 15-30 minutes; produces black oxide
5. **Rinse** — Hot water rinse to remove salt residue
6. **Polish (P)** — Mechanical polishing (buffing, lapping, or centerless grinding) to Ra 8-16 micro-inch
7. **Second oxidizing salt quench (Q2)** — Return to oxidizing salt at 700-800 degF (371-427 degC) for 15-30 minutes
8. **Final rinse** — Hot water rinse; rust preventative if required
9. **Inspect** — Hardness, compound zone thickness, salt spray test, appearance

---

## 6.2 Safety & PPE

### Salt Bath Hazards
- **Molten salt temperature:** 1050-1125 degF (566-607 degC) for nitrocarburizing bath; 700-800 degF (371-427 degC) for oxidizing bath
- **Severe burn risk** — molten salt clings to skin and clothing
- **Moisture is the primary explosion trigger** — any water contact with molten salt causes violent steam explosion; parts MUST be completely dry before immersion; preheat step is critical
- **Cyanate salts (NaCNO, KCNO)** — less toxic than cyanide but still regulated; proper waste disposal required
- **Fume extraction** required — nitrogen oxide and salt fumes generated during processing

### PPE
- Full-face shield with splash guard
- Heat-resistant gauntlets (elbow-length, rated for molten salt splash)
- Flame-resistant coveralls (no exposed skin)
- Steel-toed boots with metatarsal guards
- Respiratory protection for salt fumes (P100 particulate + organic vapor cartridge)

### Fire Suppression
- **Dry chemical or dry sand only** — NEVER use water near molten salt baths
- Salt bath fire from organic contamination: smother with dry material; do NOT attempt to extinguish with water

---

## 6.3 Part Preparation

- Parts do NOT need to be pre-quenched-and-tempered (unlike gas nitriding) — FNC can be applied to parts in the as-machined, normalized, or annealed condition
- **Surface must be clean and dry** — soap residue, cutting fluid, and moisture cause salt bath contamination and explosion risk
- **Preheat to 600-700 degF (316-371 degC)** is mandatory to ensure all moisture is removed

### Masking
- Mechanical masking with close-fitting metal caps or plugs
- **Copper plate is NOT effective** as a stop-off for FNC (same as gas nitriding)
- Tight-tolerance threaded areas can be protected by threading in a plug

---

## 6.4 Loading & Fixturing

- Parts hung on fixtures made of low-carbon steel (fixtures also get treated — replace periodically)
- Wire, rod, or hook fixturing for immersion into salt bath
- Part spacing important but less critical than gas nitriding (liquid salt provides uniform heat transfer)
- Parts must be oriented to allow salt to drain on removal (no cupping)

---

## 6.5 Furnace / Salt Bath Setup

### Salt Bath Types
| Bath | Composition | Temperature | Function |
|---|---|---|---|
| Nitrocarburizing bath | Alkali cyanate (NaCNO/KCNO) + carbonate | 1050-1125 degF (566-607 degC) | Nitrogen and carbon diffusion |
| Oxidizing quench bath | Alkali nitrate/nitrite (NaNO3/NaNO2) | 700-800 degF (371-427 degC) | Black oxide formation; corrosion seal |

### Gas FNC Alternative
- Atmosphere: NH3 + CO2 (or endothermic gas + NH3)
- Temperature: 1050-1100 degF (566-593 degC)
- Time: 60-180 minutes
- No salt handling — cleaner process; but QPQ corrosion resistance requires the oxidizing quench step

### Salt Bath Maintenance
- Regular analysis of cyanate content (target 35-40% CNO in primary bath)
- Monitor cyanide (CN) buildup — regeneration cycle required when CN exceeds limits
- Sludge removal (iron fines, scale) from bath bottom
- Bath dragout recovery

---

## 6.6 Atmosphere / Cycle Control

### Cycle Parameters
| Parameter | Value |
|---|---|
| Nitrocarburizing temperature | 1050-1125 degF (566-607 degC); most common 1075 degF (580 degC) |
| Time in nitrocarburizing bath | 60-120 minutes (standard); up to 240 minutes for deeper case |
| Oxidizing quench temperature (Q1 and Q2) | 700-800 degF (371-427 degC) |
| Time in oxidizing quench | 15-30 minutes each |
| Total cycle (salt bath QPQ) | 2.5-5 hours from preheat to final rinse |

---

## 6.7 Heat Cycle / Quench / Inspection

### Quench (QPQ)
- The "quench" in QPQ is NOT a hardening quench — it is an oxidizing immersion in a lower-temperature salt bath
- No martensite is formed; the microstructure remains ferritic throughout
- The oxidizing quench creates a magnetite (Fe3O4) layer that seals the compound zone pores

### Inspection
- **Compound zone thickness:** Metallographic measurement on polished cross-section; 0.0004-0.001 in. (10-25 micrometers)
- **Surface hardness:** Vickers microhardness on cross-section; superficial Rockwell on surface
- **Salt spray testing (ASTM B117):** QPQ-treated 1018 steel: 200-500+ hours to first red rust (compare to hard chrome: 24-96 hours typical)
- **Appearance:** Uniform matte black for QPQ; gray for gas FNC without oxidizing quench
- **Surface roughness:** Ra 8-16 micro-inch after polish step
- **Dimensional change:** Negligible — typically less than 0.0002 in. (5 micrometers) growth

### Common Defects
| Defect | Cause | Remedy |
|---|---|---|
| Poor corrosion resistance | Insufficient oxidizing quench time; poor polish quality | Extend Q time; improve polish to specified Ra |
| Thin/absent compound zone | Low bath temperature; depleted cyanate | Verify bath temp; analyze and replenish salts |
| Staining or discoloration | Salt residue not fully rinsed; contamination in oxidizing bath | Improve rinse; maintain bath purity |
| Distortion | Part was previously hardened by other means and the FNC temperature exceeded temper temperature | Verify thermal history compatibility |
| Pitting | Moisture on parts before immersion (steam explosion micro-pits) | Improve preheat drying step |

---

# CLUSTER 7: INDUCTION HARDENING

## 7.1 Process Flow Poster Data

### What Is Induction Hardening?
Induction hardening is a surface hardening process that uses electromagnetic induction to rapidly heat the surface of a steel part above its austenitizing temperature, followed by immediate quenching. The part itself is the heat source — the steel's resistance to the induced eddy currents generates heat. Only the surface layer is heated; the core remains cool and unaffected.

### Mechanism of Action
1. Alternating current (AC) flows through a copper induction coil (inductor) surrounding or adjacent to the part
2. AC creates an alternating magnetic field
3. Magnetic field induces eddy currents in the steel part (skin effect — currents concentrated near surface)
4. Eddy currents generate resistive (I2R) heating — surface heats rapidly (seconds to minutes)
5. Depth of heating depends on frequency (higher frequency = shallower heating), power density, and time
6. Surface austenitizes (above Ac3)
7. Immediate quench (spray quench built into the inductor or following the coil in progressive hardening)
8. Surface transforms to martensite; core remains in original condition (ferrite/pearlite or tempered martensite)

### What It Produces
- **Case depth:** 0.020-0.300 in. (0.5-7.6 mm) — wide range controlled by frequency and power
- **Surface hardness:** 55-62 HRC (directly dependent on carbon content of the steel)
- **Core hardness:** Unchanged from pre-process condition
- **Residual stress:** Compressive at surface (beneficial for fatigue)
- **Selective hardening:** Only the area exposed to the inductor is hardened — inherently selective without masking

### Frequency vs. Case Depth
| Frequency | Typical Case Depth | Application |
|---|---|---|
| 1-3 kHz (low) | 0.120-0.300 in. (3.0-7.6 mm) | Large shafts, heavy sections |
| 3-10 kHz (medium) | 0.060-0.150 in. (1.5-3.8 mm) | Axle shafts, spindles |
| 10-50 kHz (medium-high) | 0.030-0.080 in. (0.76-2.0 mm) | Gears, cams, smaller shafts |
| 100-500 kHz (high) | 0.010-0.040 in. (0.25-1.0 mm) | Small parts, gear teeth, valve seats |

### Steels Used
- **Medium-carbon steels (0.40-0.55% C):** 1040, 1045, 1050, 4140, 4340, 4150 — most common
- **Carbon content dictates maximum hardness:**
  - 0.40% C -> 56-58 HRC maximum
  - 0.45% C -> 58-60 HRC maximum
  - 0.50% C -> 60-62 HRC maximum
- **Cast irons:** Gray iron, ductile iron (lower hardness achievable; matrix must contain sufficient carbon in solution)
- **Low-carbon steels (below 0.35% C):** Generally NOT suitable — insufficient carbon for adequate hardness

### Key Applications & Industries
- **Automotive:** Crankshafts, camshafts, axle shafts, CV joints, steering racks, suspension pins
- **Heavy equipment:** Track pins, idler shafts, hydraulic cylinder rods
- **Power transmission:** Spindles, drive shafts, splined shafts
- **Tooling:** Bearing races (when material allows), rollers
- **Fasteners:** Large bolts, studs (head or shank hardening)

### Applicable Specifications
- **AMS 2759/12** — Selective induction hardening
- **SAE J1739** — Potential failure mode and effects analysis (FMEA) applied to induction processes
- **ASTM A255** — End-quench hardenability test (Jominy)
- **Customer-specific specifications** are very common in induction hardening due to the process-specific nature of coil design and parameters

### Induction Hardening Methods
| Method | Description |
|---|---|
| Single-shot (static) | Entire area heated simultaneously; part does not move; quench follows |
| Progressive (scanning) | Part or coil moves so heating and quenching advance along the part |
| Spin hardening | Part rotates within a stationary coil; ensures uniformity on round parts |
| Tooth-by-tooth | Individual gear teeth hardened one at a time with shaped coil (Contour hardening) |

### 9-Step Process Sequence
1. **Pre-process heat treat** — Part should be in the quenched-and-tempered (or normalized) condition for best results; ensures uniform starting microstructure
2. **Pre-clean** — Remove oils, scale, and contamination (affects coupling efficiency and quench uniformity)
3. **Position in coil** — Secure part in inductor with correct coupling gap (distance between coil and part: typically 0.060-0.125 in. / 1.5-3.2 mm)
4. **Set parameters** — Frequency, power (kW), heat time, scan speed (if progressive), quench delay, quench flow
5. **Heat** — Energize coil; surface heats to above Ac3 in 1-30 seconds (depending on depth and method)
6. **Quench** — Immediate spray quench with polymer solution (5-20% PAG) or water; quench built into coil assembly
7. **Temper** — 300-400 degF (149-204 degC) for 1-2 hours; some high-volume operations use induction temper (rapid)
8. **Inspect** — Hardness (surface and pattern), case depth (acid etch or microhardness traverse), crack check (magnetic particle inspection — MPI)
9. **Verify pattern** — Acid etch cross-section to verify hardened zone location and depth; first-article inspection critical

---

## 7.2 Safety & PPE

### Electrical Hazards
- **Extremely high current in the coil:** Thousands of amps at the coil face (though at safe voltage, typically 100-800 V at the coil)
- **Power supply high voltage:** 480 V AC or higher at the power supply input; capacitor bank stores lethal energy
- **LOTO mandatory** for coil changes and maintenance
- **RF interference:** High-frequency units (100+ kHz) can interfere with medical devices (pacemakers); exclusion zone required

### Burns and Quench Hazards
- **Extremely hot parts** — part surface reaches 1500-1700 degF (816-927 degC) in seconds; no visible warning (induction heating is rapid)
- **Quench spray** — hot polymer/water spray can splash; eye and skin protection required
- **Coil burns** — copper coil operates at elevated temperature and carries high current; accidental contact causes both thermal and electrical burns

### PPE
- Safety glasses with side shields (minimum); face shield for coil changeover
- Heat-resistant gloves (Kevlar)
- Non-conductive footwear
- Hearing protection (some power supplies produce audible hum at high power)
- No loose clothing or jewelry (induction heating of metal objects near the coil)

---

## 7.3 Part Preparation

- Parts should be in a uniform starting microstructure (Q&T preferred; normalized acceptable)
- **Decarburization from prior operations must be removed** — a decarburized surface will not achieve full hardness
- Surface should be clean and free of scale (scale is an insulator — creates hot/cold spots)
- No machining required for stock removal after induction hardening in most cases (minimal distortion)

---

## 7.4 Loading & Fixturing

### Coil (Inductor) Design
- **Custom coils** required for each part geometry — coil design is the single most critical factor in induction hardening
- Coupling gap: 0.060-0.125 in. (1.5-3.2 mm) between coil and part surface
- Materials: copper tubing with integral water cooling; some with magnetic flux concentrators (Fluxtrol, Ferrotron)
- Coil life: 500-50,000+ cycles depending on design and application

### Fixturing
- Centers, chucks, or between-centers mounting for shafts
- Nesting fixtures for production of identical parts (CNC-controlled positioning)
- **Part must be concentric to the coil** — off-center parts produce non-uniform case depth

---

## 7.5 Furnace / System Setup

### Power Supply Types
| Type | Frequency Range | Power | Application |
|---|---|---|---|
| Solid-state (IGBT) | 1-50 kHz | 25-3000 kW | Most common; versatile |
| Solid-state (MOSFET) | 50-400 kHz | 5-500 kW | High-frequency applications |
| Vacuum tube (legacy) | 200-500 kHz | 10-200 kW | Older installations |
| Dual-frequency | Combination | Variable | Gear tooth contour hardening |

---

## 7.6 Heat Cycle

### Heat Cycle Parameters
- **Heating time:** 1-30 seconds (single-shot); scan rate 0.1-2.0 in./sec for progressive
- **Surface temperature:** 1500-1700 degF (816-927 degC) — above Ac3 of the specific steel
- **Power density:** 1-50 kW/in2 — higher power density = faster heating = shallower case
- **Quench delay:** 0.1-2.0 seconds after power off (minimal delay for most applications)

---

## 7.7 Quench Stage

### Quench Parameters
- **Quenchant:** 5-20% polymer (PAG) in water is standard; concentration controls quench severity
- **Quench spray pressure:** 20-60 psi
- **Quench flow rate:** Sufficient to cover entire heated zone within 1 second of power-off
- **Temperature:** Quenchant reservoir at 70-110 degF (21-43 degC)

---

## 7.8 Temper & Inspection

### Tempering
- **Temperature:** 300-400 degF (149-204 degC); 1-2 hours
- **Induction temper:** Some production lines use a second lower-power induction pass for rapid tempering (seconds)
- **Oven temper:** Traditional method; still required for most specification compliance

### Inspection
- **Hardness:** Surface Rockwell (HRC) at specified locations; minimum usually 55-58 HRC depending on carbon content
- **Pattern check:** Acid etch (10% ammonium persulfate or 5% nital) on sectioned part to reveal hardened zone boundary
- **Case depth:** Microhardness traverse; or acid etch measurement
- **Crack detection:** 100% magnetic particle inspection (MPI) on safety-critical parts — induction hardening creates high thermal stresses; cracking risk is highest at pattern transitions
- **Dimensional check:** OD growth of 0.0002-0.001 in. (0.005-0.025 mm) typical due to martensite expansion

### Common Defects
| Defect | Cause | Remedy |
|---|---|---|
| Soft spots | Part off-center in coil; decarburized surface; scale | Center part; verify stock; remove scale |
| Through-hardening (too deep) | Frequency too low; power too high; time too long | Increase frequency; reduce power; reduce time |
| Cracking | Too-rapid quench; too-deep case; sharp corners; inclusions | Reduce quench severity; radius transitions; inspect material |
| Non-uniform pattern | Coil design issue; coupling gap variation; part geometry | Re-design coil; verify fixturing; add flux concentrators |
| Overheating (grain growth, melting) | Power too high; dwell time too long | Reduce power; verify control system |

---

# CLUSTER 8: FLAME HARDENING

## 8.1 Process Flow Poster Data

### What Is Flame Hardening?
Flame hardening is a surface hardening process that uses a direct flame (typically oxy-acetylene or oxy-propane) to rapidly heat the surface of a steel part above its austenitizing temperature, followed by immediate quench. It is conceptually identical to induction hardening but uses combustion rather than electromagnetic induction as the heat source. It is the simplest and most versatile localized hardening method.

### Mechanism of Action
1. Oxy-fuel flame directed at the part surface
2. Surface heated rapidly to above Ac3 (1500-1600 degF / 816-871 degC for most medium-carbon steels)
3. Flame is a reducing (slightly carburizing) environment, which helps prevent surface oxidation
4. Heat conducts inward — case depth controlled by flame dwell time, flame-to-part distance, and traverse speed
5. Immediate water or polymer quench follows the flame
6. Surface transforms to martensite; core remains unaffected

### What It Produces
- **Case depth:** 0.050-0.250 in. (1.3-6.4 mm) — generally deeper than induction
- **Surface hardness:** 50-60 HRC (dependent on carbon content)
- **Core hardness:** Unchanged
- **Less precise than induction** — flame is broader, less controllable

### Steels Used
- Same as induction hardening: medium-carbon steels with 0.40-0.55% C (1045, 4140, 4340)
- **Cast irons:** Frequently flame hardened (gray iron, ductile iron) for wear surfaces
- **Large parts** where induction coil fabrication is impractical or cost-prohibitive

### Key Applications & Industries
- **Heavy equipment:** Large gears, sprockets, rail sections, ways and slides
- **Mining:** Crusher jaws, liner plates
- **Machine tools:** Lathe ways, press slides, large gear teeth
- **Agriculture:** Tillage tools, plow points
- **Repair/maintenance:** Field hardening of worn surfaces; one-off parts

### Flame Hardening Methods
| Method | Description |
|---|---|
| Spot (stationary) | Flame and part both stationary; small area hardened |
| Progressive (scanning) | Flame head traverses along the part, followed by quench spray |
| Spin | Part rotates under stationary flame head; for cylindrical parts |
| Combination | Part rotates AND flame traverses |

### Applicable Specifications
- **AMS 2759/12** — Can apply to flame hardening (selective surface hardening)
- **ASTM A255** — Hardenability (Jominy)
- Often governed by customer-specific or OEM specifications

### 9-Step Process Sequence
1. **Verify material** — Confirm carbon content is adequate (minimum 0.40% C for HRC 55+)
2. **Pre-clean** — Remove oil, grease, scale (flame will not penetrate heavy scale uniformly)
3. **Set up flame equipment** — Select torch tip, adjust oxy-fuel ratio, set flame-to-part distance
4. **Position part** — Secure on rotary table, between centers, or on bed for progressive hardening
5. **Preheat (optional)** — For large or complex parts, preheat to 300-400 degF (149-204 degC) to reduce thermal shock
6. **Heat** — Apply flame; heat surface to cherry-red to bright orange (1500-1650 degF / 816-899 degC)
7. **Quench** — Immediate water spray following the flame; or immersion quench
8. **Temper** — 300-400 degF (149-204 degC) for 1-2 hours
9. **Inspect** — Hardness, pattern (acid etch), crack detection (dye penetrant or MPI)

---

## 8.2 Safety & PPE

### Flame and Gas Hazards
- **Oxy-acetylene flame temperature:** Up to 5,600-6,300 degF (3,093-3,482 degC) — capable of melting steel; extreme burn risk
- **Acetylene:** Explosive; never exceed 15 psig (1 bar gauge); OSHA 29 CFR 1910.253 applies
- **Oxygen:** Accelerant; enriched-oxygen environments cause spontaneous ignition of oil, grease, and clothing
- **Flashback and backfire:** Use approved flashback arrestors on both hoses
- **Propane alternative:** Lower flame temperature (~4,530 degF / 2,499 degC); less explosion risk than acetylene

### PPE
- **Welding goggles** (shade 4-6) or auto-darkening face shield — UV and IR radiation from flame
- Heat-resistant leather gloves
- Flame-resistant clothing (leather apron or FRC)
- Steel-toed boots
- Hearing protection if using multiple torches or automated systems
- Fire extinguisher within 10 ft of work area

### Fire Suppression
- Water is acceptable (for general fire); CO2 or dry chemical for oil-quench areas
- Acetylene cylinder safety: shut off torch at cylinder immediately if flashback occurs; do not re-light until leak checked

---

## 8.3 Part Preparation

- Same as induction hardening: clean, decarburization-free surface
- Large castings: may need stress relief before flame hardening to prevent cracking
- Remove machining burrs that could overheat (thin edges concentrate heat)

---

## 8.4 Loading & Fixturing

- **Rotary tables** for spin hardening of cylindrical parts
- **Linear slides** for progressive hardening of flat surfaces (ways, rails)
- **Manual operation:** Flame hardening can be performed freehand by an experienced operator for one-off or repair work — the most flexible of all hardening processes
- **Torch head design:** Single-flame torch for small areas; multi-flame "banks" for wider coverage (lathe ways, large gears)

---

## 8.5 Furnace / System Setup

### Equipment
- **Oxy-fuel torch:** Oxy-acetylene or oxy-propane; neutral to slightly reducing flame
- **Flame head:** Can be a single rosebud tip, line burner, or shaped multi-port head matching the contour
- **Quench system:** Water spray bar following the flame head; 5-20 gpm flow depending on part size
- **Controls:** Manual or CNC-controlled traverse speed and flame parameters

---

## 8.6 Heat Cycle

### Heat Cycle Parameters
| Parameter | Value |
|---|---|
| Surface temperature target | 1500-1650 degF (816-899 degC) |
| Flame-to-part distance | 0.25-0.75 in. (6-19 mm) |
| Traverse speed (progressive) | 2-12 in./min (50-300 mm/min) — slower = deeper case |
| Rotation speed (spin) | 30-120 RPM depending on diameter |
| Heat time (spot) | 10-60 seconds per area |

### Case Depth Control
- No frequency variable like induction — case depth controlled by:
  - Flame intensity (gas pressure / tip size)
  - Flame-to-part distance
  - Traverse speed or dwell time
  - Preheat temperature
- **Less precise than induction** — typical tolerance +/-0.030 in. (0.76 mm) vs. +/-0.010 in. (0.25 mm) for induction

---

## 8.7 Quench Stage

- **Water spray** is most common (no polymer needed for most flame hardening)
- Spray follows 0.5-2.0 in. (13-51 mm) behind the flame in progressive hardening
- Immersion quench for spot and spin methods
- Self-quench (mass quench) possible on very large parts where the cold core acts as a heat sink

---

## 8.8 Temper & Inspection

### Tempering
- 300-400 degF (149-204 degC) for 1-2 hours

### Inspection
- Same as induction hardening: hardness, pattern (acid etch), MPI for cracks
- **Torch tracking pattern:** Look for overlap lines in progressive hardening (potential soft spots at overlap or hard spots at double-exposure)
- **Surface condition:** Check for excessive oxidation or decarburization from flame exposure

### Common Defects
| Defect | Cause | Remedy |
|---|---|---|
| Overheating / melting | Flame too close; dwell too long; wrong tip | Increase distance; increase traverse speed; select proper tip |
| Soft spots | Insufficient temperature; uneven flame coverage; overlap zone | Verify temperature (pyrometer); improve flame head design; adjust overlap |
| Cracking | Quench too severe; section too thin; pre-existing stress risers | Reduce quench; preheat; stress relieve before hardening |
| Non-uniform case depth | Manual technique variation; inconsistent traverse speed | Automate traverse; use CNC control; verify with test coupons |
| Distortion | Asymmetric heating; heating too deep into thin sections | Balance heat pattern; reduce case depth |

---

# CLUSTER 9: AUSTEMPERING

## 9.1 Process Flow Poster Data

### What Is Austempering?
Austempering is an isothermal heat treatment in which steel or ductile iron is austenitized, then quenched into a molten salt bath held at a temperature in the bainite transformation range (400-750 degF / 204-399 degC for steel; 450-750 degF / 232-399 degC for ductile iron). The part is held in the salt bath until transformation to bainite (or ausferrite in ductile iron) is complete. There is no subsequent quench to room temperature — the part is simply removed from the salt bath and air cooled.

### Mechanism of Action
1. Part austenitized at 1500-1650 degF (816-899 degC) — full austenitization
2. Part rapidly transferred to molten salt bath at isothermal hold temperature
3. Part temperature equalizes at the salt bath temperature (above Ms, the martensite start)
4. Isothermal transformation: austenite transforms to **bainite** (in steel) or **ausferrite** (in ductile iron)
5. **No martensite forms** — transformation is complete before the part cools below Ms
6. Part removed from salt and air cooled to room temperature
7. **No tempering required** — bainite is a stable microstructure; the process produces the final properties directly

### What It Produces
- **Microstructure:** Lower bainite (strong, tough) at lower salt temperatures; upper bainite (more ductile) at higher salt temperatures; ausferrite in ductile iron
- **Hardness:** 35-55 HRC for steel; 280-500 HB for ADI (varying by grade)
- **Tensile strength:** 150-300 ksi (1035-2070 MPa) for steel; 125-230 ksi (860-1585 MPa) for ADI
- **Elongation:** 2-15% (significantly higher than martensite at equivalent hardness)
- **Impact toughness:** 2-5x that of quenched and tempered martensite at equivalent hardness
- **Fatigue strength:** Excellent — compressive surface residual stress from bainite transformation
- **Distortion:** Significantly less than conventional quench and temper — isothermal transformation is uniform

### Steels Used
| Grade | Application |
|---|---|
| 1065-1095 | Springs, clips, stampings |
| 4150 / 4340 | Structural components, gears |
| 5160 | Leaf and coil springs, anti-roll bars |
| 6150 | Springs, snap rings |
| 52100 | Bearings (carbide-free bainite variant) |
| Ductile iron (65-45-12, 80-55-06, etc.) | Automotive, heavy equipment (ADI) |

### ASTM A897 ADI Grades
| Grade | Tensile Strength (ksi) | Yield Strength (ksi) | Elongation (%) | Hardness (HB) |
|---|---|---|---|---|
| 1 | 125 min | 80 min | 10 min | 269-321 |
| 2 | 150 min | 100 min | 7 min | 302-363 |
| 3 | 175 min | 125 min | 4 min | 341-444 |
| 4 | 200 min | 155 min | 1 min | 388-477 |
| 5 | 230 min | 185 min | 0 min | 444-555 |

### Key Applications & Industries
- **Automotive:** Suspension springs, clips, lock components, seat belt components
- **Agriculture:** Plow blades, tillage discs, implement teeth
- **Construction equipment:** ADI gears, sprockets, wear plates
- **Fasteners:** High-strength, high-toughness bolts and clips
- **Railroad:** Clips, tie plates, wheel components
- **Military:** Armor plate (some grades), gun parts

### Applicable Specifications
- **ASTM A897 / A897M** — Austempered ductile iron (5 grades)
- **SAE J2477** — Classification and properties of ADI
- **ASTM A933** — Standard test method for microhardness of metallic materials with elongated ferrite grains
- **AMS 2759/2** — Can cover austempering of steel (isothermal transformation)

### 9-Step Process Sequence
1. **Pre-clean** — Alkaline wash or solvent degrease
2. **Load** — Fixture parts for salt bath immersion; orient for drainage
3. **Austenitize** — Heat to 1500-1650 degF (816-899 degC) in atmosphere furnace or salt bath
4. **Transfer** — Rapid transfer (less than 15 seconds) from austenitizing furnace to austempering salt bath
5. **Isothermal hold** — Immerse in molten salt at 400-750 degF (204-399 degC); hold for 30-120 minutes
6. **Bainite transformation** — Complete transformation to bainite/ausferrite occurs during hold
7. **Remove from salt** — Part is now fully transformed; air cool to room temperature
8. **Wash** — Hot water rinse to remove salt residue
9. **Inspect** — Hardness, microstructure (bainite confirmation), mechanical testing if required

---

## 9.2 Safety & PPE

### Salt Bath Hazards
- **Two salt bath temperatures:** Austenitizing salt at 1500-1650 degF (816-899 degC) and austempering salt at 400-750 degF (204-399 degC)
- **Austenitizing salt (if used):** Barium chloride-based (toxic) or neutral salt mixtures; temperature causes severe burns
- **Austempering salt:** Nitrate/nitrite eutectic mixture (typically 50/50 NaNO2/KNO3); operating range 300-1100 degF (149-593 degC)
- **Moisture explosion risk:** Same as all molten salt operations — parts MUST be completely dry before immersion
- **Nitrate/nitrite salts are oxidizers** — will react violently with organic contamination (oil, grease); fire/explosion risk if quench oil contaminates the austempering salt

### PPE
- Same as FNC salt bath operations: face shield, gauntlets, FRC, metatarsal-guard boots
- **Cyanide awareness:** If barium chloride austenitizing salt is used, cyanide formation is possible; respiratory protection required

---

## 9.3 Part Preparation

- Parts may be in as-forged, as-rolled, or annealed condition before austempering
- **No pre-heat-treatment required** (unlike nitriding)
- Clean and dry — critical for salt bath operations
- For ductile iron: verify nodularity (minimum 80% nodularity per ASTM A897)

---

## 9.4 Loading & Fixturing

- Fixtures for salt bath immersion: alloy steel baskets, racks, or hooks
- **Drainage orientation:** Parts must allow molten salt to drain when removed — cupped geometries cause salt carryover and waste
- Transfer mechanism between furnaces: automated conveyor, overhead crane, or robot arm — speed is critical (less than 15 seconds to avoid pearlite nose on the TTT curve)

---

## 9.5 Furnace / Salt Bath Setup

### Furnace Configuration
- **Austenitizing:** Atmosphere furnace (endothermic or nitrogen-based) for steel; or neutral salt bath for either steel or ductile iron
- **Austempering:** Molten salt bath with agitation (propeller or pump) for temperature uniformity

### Austempering Salt Bath
| Parameter | Value |
|---|---|
| Salt composition | 50/50 NaNO2/KNO3 (typical eutectic) |
| Melting point | ~290 degF (~143 degC) |
| Operating range | 300-1100 degF (149-593 degC) |
| Austempering range | 400-750 degF (204-399 degC) for steel; 450-750 degF for ADI |
| Agitation | Required for uniform temperature and adequate quench severity |
| Temperature uniformity | +/-5 degF (+/-3 degC) typical |

---

## 9.6 Atmosphere / Cycle Control

### Salt Bath Temperature Effect on Properties
| Salt Temperature | Transformation Product | Hardness | Ductility |
|---|---|---|---|
| 400-500 degF (204-260 degC) | Lower bainite | 50-55 HRC / 460-550 HB | Low (1-4% elongation) |
| 500-600 degF (260-316 degC) | Mixed bainite | 42-50 HRC / 390-460 HB | Moderate (4-7%) |
| 600-700 degF (316-371 degC) | Upper bainite | 35-42 HRC / 320-390 HB | Higher (7-12%) |
| 700-750 degF (371-399 degC) | Coarse bainite/ausferrite | 30-38 HRC / 280-340 HB | Highest (10-18%) |

---

## 9.7 Heat Cycle

### Cycle Parameters
| Stage | Temperature | Time |
|---|---|---|
| Austenitize (steel) | 1525-1600 degF (829-871 degC) | 30-90 minutes (depending on section size) |
| Austenitize (ADI) | 1550-1650 degF (843-899 degC) | 60-120 minutes |
| Transfer | — | less than 15 seconds (critical to avoid pearlite) |
| Austempering hold | 400-750 degF (204-399 degC) | 30-120 minutes |
| Air cool | Room temperature | Until cool |

### Section Size Limitation
- Austempering works best on sections up to approximately 0.5 in. (12.7 mm) for unalloyed steels
- Alloy steels (4340, etc.) can be austempered in sections up to 1.0-2.0 in. (25-51 mm) due to higher hardenability
- ADI: up to 3-4 in. (76-102 mm) section size with proper alloy content (Cu, Ni, Mo additions)
- **Critical:** The part core must cool fast enough to avoid the pearlite nose on the TTT diagram — this is the limiting factor

---

## 9.8 Quench Stage

**Austempering uses an isothermal salt bath hold — NOT a conventional quench to room temperature.**

The salt bath serves as both the quench medium (rapid cooling from austenitizing to the bainite range) and the isothermal transformation medium. The part remains in the salt until bainite transformation is complete.

---

## 9.9 Temper & Inspection

### No Tempering Required
- Bainite is the final, stable microstructure — no temper needed
- This is a major advantage: eliminates a process step and avoids temper embrittlement ranges

### Inspection
- **Hardness:** Rockwell C or Brinell at specified locations
- **Microstructure:** Bainite confirmation; absence of pearlite (indicates incomplete transformation or too-slow transfer)
- **X-ray diffraction or metallography** to verify absence of retained austenite (excessive in ADI can indicate incomplete transformation)
- **Mechanical testing:** Tensile, impact (Charpy or Izod) per ASTM A897 requirements
- **Dimensional check:** Distortion is minimal but should be verified

### Common Defects
| Defect | Cause | Remedy |
|---|---|---|
| Pearlite (soft spots) | Transfer time too long; section too thick; insufficient hardenability | Reduce transfer time; alloy for hardenability; reduce section |
| Incomplete transformation | Hold time too short in salt bath | Extend isothermal hold; verify with TTT data |
| Retained austenite (ADI) | Austenitizing temperature too high; austempering time insufficient | Reduce austenitize temp; extend hold |
| Distortion (excessive) | Non-uniform salt bath temperature; asymmetric quenching | Improve agitation; optimize part orientation |
| Salt contamination | Oil carryover from cleaning; water contamination | Improve pre-cleaning; preheat parts |

---

# CLUSTER 10: MARTEMPERING (MARQUENCHING)

## 10.1 Process Flow Poster Data

### What Is Martempering?
Martempering (also called marquenching) is an interrupted quenching process in which steel is austenitized, then quenched into a hot medium (molten salt or hot oil) held at a temperature just above the martensite start (Ms) temperature. The part is held in this medium only until the surface and core temperatures equalize — NOT until transformation occurs. Then the part is removed and air cooled through the martensite transformation range. The result is martensite (same as conventional quenching) but with dramatically less distortion and reduced risk of cracking because the thermal gradient is minimized.

### Mechanism of Action
1. Part austenitized at standard temperature for the steel grade
2. Quenched rapidly into hot salt bath or hot oil held at a temperature just above Ms (typically 350-600 degF / 177-316 degC for most steels)
3. Held in the hot medium for 5-15 minutes — only until the surface and core temperatures equalize at the bath temperature
4. **No transformation occurs during the hold** — the part is still 100% austenite (temperature is above Ms)
5. Part removed from salt/oil and air cooled (or still-air cooled) through the martensite range
6. Martensite transformation occurs uniformly throughout the cross-section simultaneously
7. Because surface and core transform together, thermal stresses and distortion are minimized
8. Temper as for conventional quench and temper

### Key Distinction from Austempering
| Feature | Austempering | Martempering |
|---|---|---|
| Final microstructure | Bainite | Martensite (tempered) |
| Transformation occurs in salt? | Yes (full transformation to bainite) | No (temperature equalization only) |
| Salt bath temperature | In bainite range (400-750 degF) | Just above Ms (350-600 degF) |
| Hold time in salt | 30-120 min (complete transformation) | 5-15 min (equalization only) |
| Tempering required? | No | Yes |
| Hardness | 35-55 HRC | 45-65 HRC (higher with temper) |

### What It Produces
- **Microstructure:** Tempered martensite (same as conventional Q&T, but more uniform)
- **Hardness:** Same as conventional Q&T for the steel grade (45-65 HRC as-quenched; reduced by temper)
- **Distortion:** 50-80% less than conventional oil quench due to uniform transformation
- **Residual stress:** Lower than conventional quench — less cracking risk
- **Mechanical properties:** Equal to conventional Q&T

### Steels Used
- **High-hardenability steels preferred** (must remain austenitic during the equalization hold — lean alloys may transform to pearlite/bainite before equalizing)

| Grade | Ms Temperature (approx.) | Typical Salt Bath Temperature |
|---|---|---|
| 4340 | ~530 degF (277 degC) | 400-525 degF (204-274 degC) |
| 4140 | ~600 degF (316 degC) | 450-575 degF (232-302 degC) |
| 52100 | ~410 degF (210 degC) | 300-400 degF (149-204 degC) |
| D2 | ~375 degF (191 degC) | 275-365 degF (135-185 degC) |
| H13 | ~600 degF (316 degC) | 450-575 degF (232-302 degC) |
| M2 (HSS) | ~375 degF (191 degC) | 1000-1050 degF (538-566 degC)* |

*Note: High-speed steels use a different martempering approach — salt bath at higher temperature for equalization before air cool.

### Key Applications & Industries
- **Bearings:** Precision bearing races (52100 steel) — distortion control is critical
- **Gears:** High-performance gears where dimensional accuracy is critical
- **Tooling:** Die steels, HSS cutting tools
- **Aerospace:** Critical structural components where distortion rejection is costly
- **Springs:** Some high-carbon spring wire
- **Fasteners:** High-strength, close-tolerance fasteners

### Applicable Specifications
- **AMS 2759/1** — General heat treatment; martempering is referenced as an acceptable quench method
- **AMS 2759/2** — Hardening and tempering of steel
- **AMS-H-6875** — Heat treatment of steel raw materials
- **AGMA 2004** — References martempering as a distortion-control quench method for gears

### 9-Step Process Sequence
1. **Pre-clean** — Solvent or alkaline wash; dry completely (salt bath moisture safety)
2. **Load** — Fixture for salt bath immersion with drainage orientation
3. **Preheat (optional)** — 800-1000 degF (427-538 degC) for heavy sections to reduce thermal shock
4. **Austenitize** — Heat to proper austenitizing temperature for the steel grade (1475-1600 degF / 802-871 degC for most alloy steels; 1525-1575 degF / 829-857 degC typical)
5. **Quench into hot salt** — Rapid transfer to salt bath at temperature just above Ms; hold 5-15 minutes for temperature equalization
6. **Air cool** — Remove from salt; air cool to room temperature; martensite transformation occurs during this cooling
7. **Wash** — Hot water rinse to remove salt
8. **Temper** — Standard tempering for the grade and hardness requirement: 300-1100 degF (149-593 degC) depending on application
9. **Inspect** — Hardness, microstructure, distortion measurement, crack check

---

## 10.2 Safety & PPE

### Salt Bath Hazards
- Same as austempering: molten nitrate/nitrite salt at 350-600 degF (177-316 degC)
- **Moisture explosion risk** — same precautions as all molten salt operations
- **Organic contamination:** Nitrate/nitrite salts are strong oxidizers; contact with oil/grease causes violent exothermic reaction

### Hot Oil Alternative
- Some martempering uses marquench oil at 250-400 degF (121-204 degC) instead of salt
- **Oil fire risk** at elevated temperature — oil temperature closer to flash point
- Ventilation critical; fire suppression mandatory on hot oil quench tanks

### PPE
- Same as austempering salt bath operations
- For hot oil: same as standard oil quench PPE plus elevated awareness of fire risk

---

## 10.3 Part Preparation

- Parts may be in any starting condition (forged, normalized, annealed)
- **Critical cleanliness** for salt bath — same requirements as austempering
- Preheat recommended for heavy sections (above 2 in. / 51 mm) to reduce thermal shock during austenitizing and quenching

---

## 10.4 Loading & Fixturing

- Same salt bath fixturing as austempering
- **Transfer speed critical** — parts must move from austenitizing furnace to quench salt in less than 15 seconds
- However, the consequence of slow transfer is different: in martempering, it risks pearlite formation (same as austempering), which would prevent achieving full martensite

---

## 10.5 Furnace / Salt Bath Setup

### Quench Salt Bath
| Parameter | Value |
|---|---|
| Salt type | Nitrate/nitrite eutectic (same as austempering) |
| Temperature range | 350-600 degF (177-316 degC) — just above Ms for the specific steel |
| Hold time | 5-15 minutes (equalization only — NOT transformation) |
| Agitation | Required for adequate heat extraction during initial quench |
| Temperature uniformity | +/-5 degF (+/-3 degC) |

### Hot Oil Alternative
| Parameter | Value |
|---|---|
| Oil type | Marquench oil (high-temperature quench oil) |
| Temperature range | 250-400 degF (121-204 degC) |
| Flash point | Must exceed operating temp by at least 50 degF |
| Advantage | Less expensive than salt; no salt cleanup |
| Disadvantage | Narrower temperature range; fire risk; lower quench uniformity |

### H-Factor Comparison
| Medium | H-Factor |
|---|---|
| Martempering salt (agitated) | 0.30-0.50 |
| Marquench oil (agitated) | 0.20-0.35 |
| Conventional oil (room temp, agitated) | 0.35-0.50 |
| Conventional water (agitated) | 1.0-1.5 |

---

## 10.6 Heat Cycle

### Cycle Parameters
| Stage | Temperature | Time |
|---|---|---|
| Austenitize | 1475-1600 degF (802-871 degC) depending on steel | 30-90 minutes |
| Transfer | — | less than 15 seconds |
| Salt/oil hold | Just above Ms (350-600 degF / 177-316 degC) | 5-15 minutes |
| Air cool to RT | Through Ms to room temperature | 15-60 minutes |
| Temper | Per steel grade and required hardness | 1-4 hours |

---

## 10.7 Quench Stage

The martempering quench is an **interrupted quench** — not a complete quench to room temperature.

Key points:
- The rapid cooling from austenitizing to the salt bath temperature IS the quench phase
- The isothermal hold in the salt is the equalization phase — no transformation occurs here
- The air cool from salt bath through Ms to room temperature is where martensite forms
- The uniform temperature at the start of the martensite transformation (thanks to the equalization hold) is what gives martempering its distortion advantage

---

## 10.8 Temper & Inspection

### Tempering
- **Required** (unlike austempering where temper is unnecessary)
- Temperature and time same as conventional Q&T for the specific steel grade:
  - 4340: 400-1100 degF (204-593 degC) depending on desired hardness
  - 52100: 300-350 degF (149-177 degC) for bearing applications (HRC 60-62)
  - H13: 1000-1050 degF (538-566 degC), double or triple temper
- **Double temper** recommended for tool steels and any application where retained austenite must be minimized

### Inspection
- **Hardness:** Same targets as conventional Q&T for the grade
- **Distortion measurement:** Key metric for martempering — compare dimensional measurements before and after processing
  - Typical OD change: 0.0001-0.0005 in. (0.003-0.013 mm) — significantly less than conventional quench
  - Typical roundness variation: 0.0002-0.0010 in. (0.005-0.025 mm) on rings and cylinders
- **Microstructure:** 100% tempered martensite required; no pearlite, no bainite (would indicate hold temperature too high or hold time too long)
- **Crack detection:** MPI or dye penetrant — although cracking risk is lower than conventional quench, it is not zero

### Common Defects
| Defect | Cause | Remedy |
|---|---|---|
| Bainite in microstructure | Salt bath temperature in bainite range (too high); hold time too long | Reduce salt temperature to just above Ms; reduce hold time to equalization only |
| Pearlite (soft spots) | Transfer too slow; steel hardenability insufficient for section size | Faster transfer; select higher-hardenability grade |
| Retained austenite | High alloy content; as-quenched only (no temper) | Sub-zero treatment; double temper |
| Cracking | Section size variation; sharp stress risers; contaminated quench salt | Preheat; radius sharp corners; maintain salt purity |
| Distortion (still too much) | Salt bath temperature too far below Ms; non-uniform agitation | Verify Ms temperature; optimize salt temperature; improve agitation uniformity |

---

# CROSS-CLUSTER REFERENCE TABLES

## Grossmann H-Factor Summary (All Quench Media)

| Quench Medium | Condition | H-Factor |
|---|---|---|
| Still air | — | 0.02 |
| Forced air (fan) | — | 0.05-0.10 |
| Still oil | Room temp | 0.25-0.30 |
| Agitated oil | Room temp, moderate | 0.35-0.50 |
| Agitated oil | Room temp, vigorous | 0.50-0.80 |
| Marquench oil | 250-400 degF | 0.20-0.35 |
| Martempering salt | 350-600 degF, agitated | 0.30-0.50 |
| Austempering salt | 400-750 degF, agitated | 0.25-0.45 |
| Polymer (10% PAG) | Agitated | 0.30-0.50 |
| Polymer (20% PAG) | Agitated | 0.50-0.80 |
| Still water | Room temp | 1.0 |
| Agitated water | Room temp | 1.0-1.5 |
| Brine (10% NaCl) | Agitated | 2.0-5.0 |
| HPGQ (N2, 10 bar) | — | 0.10-0.15 |
| HPGQ (He, 20 bar) | — | 0.30-0.40 |

## Temperature Comparison Across All 10 Processes

| Process | Operating Temperature degF | Operating Temperature degC | Quench? |
|---|---|---|---|
| Gas carburizing | 1650-1750 | 899-954 | Yes (oil) |
| Vacuum carburizing (LPC) | 1700-1900 | 927-1038 | Yes (gas or oil) |
| Carbonitriding | 1400-1650 | 760-899 | Yes (oil) |
| Gas nitriding | 925-1050 | 496-566 | No |
| Plasma nitriding | 660-1050 | 350-566 | No |
| Ferritic nitrocarburizing (FNC) | 975-1125 | 524-607 | No (salt quench for QPQ only) |
| Induction hardening | 1500-1700 (surface) | 816-927 | Yes (polymer spray) |
| Flame hardening | 1500-1650 (surface) | 816-899 | Yes (water spray) |
| Austempering | 1500-1650 (austenitize) + 400-750 (salt) | 816-899 + 204-399 | Isothermal salt (not RT quench) |
| Martempering | 1475-1600 (austenitize) + 350-600 (salt) | 802-871 + 177-316 | Interrupted salt then air |

## Case Depth Comparison

| Process | Typical ECD Range (in.) | Typical ECD Range (mm) | Measurement Criterion |
|---|---|---|---|
| Gas carburizing | 0.010-0.250 | 0.25-6.35 | To 50 HRC |
| Vacuum carburizing | 0.010-0.200 | 0.25-5.0 | To 50 HRC |
| Carbonitriding | 0.003-0.030 | 0.08-0.76 | To 50 HRC |
| Gas nitriding | 0.005-0.030 | 0.13-0.76 | To core + 50 HV (or 50 HRC equiv.) |
| Plasma nitriding | 0.002-0.025 | 0.05-0.64 | Same as gas nitriding |
| FNC | 0.005-0.025 (diffusion zone) | 0.13-0.64 | Compound zone + diffusion zone |
| Induction hardening | 0.020-0.300 | 0.50-7.6 | To 50 HRC |
| Flame hardening | 0.050-0.250 | 1.3-6.4 | To 50 HRC |
| Austempering | Through-hardened | Through-hardened | N/A (not a case hardening process) |
| Martempering | Through-hardened | Through-hardened | N/A (not a case hardening process) |

## Masking / Stop-Off Methods by Process

| Process | Copper Plate | Tin Plate | Nickel Plate | Mechanical | Stop-Off Paint |
|---|---|---|---|---|---|
| Gas carburizing | Preferred | No | No | Limited | Yes |
| Vacuum carburizing | Preferred | No | No | Yes (effective) | Limited |
| Carbonitriding | Yes | No | No | Limited | Yes |
| Gas nitriding | NOT effective | Preferred | Yes | Limited | Some |
| Plasma nitriding | Not needed | Not needed | Not needed | Preferred | Not needed |
| FNC | NOT effective | Not tested | Limited | Yes | Limited |
| Induction hardening | N/A | N/A | N/A | Inherently selective | N/A |
| Flame hardening | N/A | N/A | N/A | Inherently selective | N/A |

---

# RESEARCH METHODOLOGY & CONFIDENCE NOTES

## Sources
- **Web searches** conducted 2026-04-26 for current AMS 2759/7E, AMS 2759/6D, AMS 2759/10A, AMS 2750H parameters; vacuum carburizing LPC data from ECM Technologies and Thermal Processing Magazine; FNC/QPQ data from Kolene Corporation and Metallurgical Solutions Inc.; plasma nitriding parameters from Bodycote, BorTec, and Ionitech; induction hardening from ASM and Gear Solutions Magazine; austempering from ASTM A897 and industry sources; martempering from Paulo, Bodycote, and SST; endothermic gas composition from Super Systems Inc. and Surface Combustion; Grossmann H-factors from ASM Handbook Vol. 4 and ScienceDirect.
- **Domain expertise (Watson):** ASM Handbook Vol. 4 (Heat Treating), AMS 2759 series, AGMA gear heat treatment standards, CQI-9 4th edition, Grossmann H-factor tables, carbon diffusion calculations, nitriding potential theory, induction heating theory.
- **Gemini:** Quota exhausted at time of research; domain expertise supplemented by web search verification.

## Confidence Assessment
| Cluster | Confidence | Notes |
|---|---|---|
| 1. Gas Carburizing | HIGH | Well-documented; AMS 2759/7E parameters verified via web search |
| 2. Vacuum Carburizing (LPC) | HIGH | ECM data confirmed boost/diffuse parameters; acetylene pressures verified |
| 3. Carbonitriding | HIGH | Standard variation of carburizing; well within domain expertise |
| 4. Gas Nitriding | HIGH | AMS 2759/6 and 2759/10 verified; nitriding potential values confirmed |
| 5. Plasma Nitriding | HIGH | NASA PRC-2004, Bodycote, and BorTec data cross-referenced |
| 6. FNC/QPQ | HIGH | Kolene and HEF data confirmed; ASTM B117 corrosion data verified |
| 7. Induction Hardening | HIGH | AMS 2759/12 confirmed; frequency-depth relationship verified |
| 8. Flame Hardening | MODERATE-HIGH | Less standardized process; fewer specifications; primarily domain expertise |
| 9. Austempering | HIGH | ASTM A897 grades confirmed; ADI property data verified |
| 10. Martempering | HIGH | Well-documented interrupted quench; Ms temperature data from domain expertise |

## Flags for Alaina
1. **AMS specification revision letters** may change — verify current revision at time of poster publication (e.g., AMS 2759/7E, AMS 2750H)
2. **Flame hardening** has the least standardization of all 10 processes — poster should emphasize operator skill and process validation as critical
3. **Austempering and martempering are NOT case hardening processes** — they are through-hardening with controlled quench; the "Heat Cycle" and "Quench" posters for these clusters will look very different from the carburizing/nitriding posters
4. **QPQ trademark:** "QPQ" is a Kolene Corporation trademark; poster should reference "ferritic nitrocarburizing with oxidative quench" as the generic term, with QPQ noted as the commonly used trademark
5. **Temperature values:** All temperatures are provided in both degF and degC throughout for direct poster use; degF is primary in US shops
6. **Copper plate as stop-off:** CRITICAL distinction — copper plate works for carburizing (stops carbon) but does NOT work for nitriding (does not stop nitrogen). Tin plate is the nitriding stop-off. This is a common misconception in shops.
7. **Electroplating cross-reference for posters:** Copper stop-off plating for selective carburizing, tin stop-off plating for selective nitriding, and nickel stop-off plating for nitriding are all electroplating operations — this creates a natural cross-reference between the heat treatment posters and the electroplating poster series.

---

*Watson — Chemistry Research Division*
*Plating Posters Inc.*
*2026-04-26*
