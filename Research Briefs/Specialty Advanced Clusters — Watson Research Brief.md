---
title: "Specialty & Advanced Coating Clusters — Watson Research Brief"
date: 2026-04-26
author: Watson (Chemistry Researcher)
version: v1
status: Complete
purpose: Technical backbone for 80 educational posters (8 clusters x 10 posters each)
note: Gemini quota exhausted at time of writing; all data sourced from Watson domain expertise (ASM Handbook Vol. 5, Mattox PVD Handbook, Ohring Thin Film Materials Science, semiconductor process literature, Products Finishing, ASTM standards). Tyler spot-check recommended for electropolishing and electroforming sections.
tags:
  - PlatingPostersInc
  - Research
  - AdvancedCoatings
  - PVD
  - CVD
  - PECVD
  - ALD
  - DLC
  - IonImplantation
  - Electropolishing
  - Electroforming
---

# Specialty & Advanced Coating Clusters — Watson Research Brief

**Prepared by Watson | 2026-04-26 | v1**

This brief covers 8 advanced coating/treatment process clusters. Each cluster maps to 10 posters (Process Flow, Safety & PPE, Part Preparation, Cleaning, Fixturing & Loading, Equipment/System Setup, Parameter Setup, Deposition/Treatment Stage, Cooling & Handling, Inspection & QA). All technical data is provided at the level needed for Alaina to write accurate, boardroom-quality Construction Workups.

---
---

# CLUSTER 1: PHYSICAL VAPOR DEPOSITION (PVD)

## 1.1 Process Flow Poster Data

### What Is PVD?

Physical Vapor Deposition is a family of vacuum-based thin-film deposition techniques in which material is physically transferred from a solid source (target) to a substrate. The two dominant industrial variants are:

- **Sputtering** — Energetic ions (typically Ar+) bombard a target, ejecting atoms that travel through the vacuum and condense on the substrate. Variants include DC sputtering, RF sputtering (for insulating targets), and magnetron sputtering (magnetic field confines plasma near the target, dramatically increasing deposition rate and reducing substrate heating).
- **Cathodic Arc Evaporation** — A high-current, low-voltage arc discharge erodes the target (cathode) surface, creating a highly ionized plasma plume. The ions are accelerated toward the substrate by a bias voltage. Produces denser, more adherent coatings than sputtering, but generates macroparticles (droplets).

**Reactive PVD**: When a reactive gas (N2, O2, C2H2) is introduced during deposition, compound coatings form (TiN, CrN, Al2O3, TiC). This is the basis of nearly all industrial hard-coating PVD.

### Key Industries and Applications

| Industry | Application | Typical Coatings |
|----------|------------|-----------------|
| Cutting tools | End mills, inserts, drills, taps | TiN, TiAlN, AlCrN, TiCN |
| Mold & die | Injection molds, stamping dies | CrN, TiCN, DLC |
| Medical | Orthopedic implants, surgical instruments | TiN (biocompatible gold color), ZrN, TiNbN |
| Decorative | Watch cases, faucets, door hardware | TiN (gold), ZrN (brass), TiAlN (dark), CrN (silver) |
| Automotive | Piston rings, fuel injectors, trim | CrN, DLC, decorative TiN |
| Aerospace | Turbine blades (erosion-resistant) | TiAlN, AlCrN |
| Semiconductor | Barrier layers, interconnects | Ta, TaN, Ti, TiN (via sputtering) |

### Substrate Compatibility

- **Metals**: Steel, stainless steel, titanium, aluminum (with temperature limitations), cemented carbide (WC-Co), high-speed steel
- **Ceramics**: Si3N4, Al2O3, SiC
- **Polymers**: Limited — low-temperature PVD (< 150 deg C) required; typically decorative only on ABS, polycarbonate
- **Glass**: Architectural low-E coatings via magnetron sputtering (inline)

### Coating Properties Produced

| Coating | Hardness (HV) | Friction Coeff. (dry) | Max Service Temp (deg C) | Color |
|---------|--------------|----------------------|--------------------------|-------|
| TiN | 2,000-2,400 | 0.4-0.6 | 600 | Gold |
| TiCN | 2,800-3,200 | 0.3-0.4 | 450 | Blue-gray |
| TiAlN | 2,800-3,300 | 0.3-0.5 | 800-900 | Dark violet |
| AlCrN | 2,800-3,200 | 0.3-0.5 | 1,100 | Gray |
| CrN | 1,800-2,200 | 0.3-0.5 | 700 | Silver |
| ZrN | 2,600-2,800 | 0.3-0.5 | 600 | Gold-yellow |

### 10-Step Process Sequence

1. **Part inspection & documentation** — Verify incoming dimensions, surface condition, material certification
2. **Precleaning** — Ultrasonic alkaline wash to remove bulk contamination (oils, chips, fingerprints)
3. **Precision cleaning** — Multi-stage ultrasonic: alkaline > DI rinse > solvent (IPA or acetone) > DI rinse > hot air dry
4. **Fixturing & loading** — Mount parts on planetary rotation fixtures; load into vacuum chamber
5. **Pumpdown** — Evacuate chamber to base pressure (< 5 x 10^-5 mbar / 5 x 10^-3 Pa typical)
6. **Heating** — Radiative or resistive heating to process temperature (350-500 deg C for tool coatings)
7. **Ion etching / plasma cleaning** — Argon ion bombardment of substrate surface (bias voltage -600 to -1200 V, 15-60 min) to remove oxide layer and activate surface
8. **Deposition** — Coating applied at working pressure (0.1-1.0 Pa); reactive gas introduced for compound coatings; substrate rotation engaged
9. **Cooldown** — Chamber cooled under vacuum or controlled backfill gas; prevents oxidation of hot coated parts
10. **Unload, inspect, package** — Visual inspection, thickness measurement, adhesion testing, documentation

---

## 1.2 Safety & PPE

### Hazards Specific to PVD

| Hazard | Source | Severity |
|--------|--------|----------|
| **High voltage** | DC sputtering: 300-700 V; RF sputtering: 13.56 MHz RF at 100-1000 W; Arc: 20-100 V at 50-200 A; Substrate bias: -50 to -1200 V | Electrocution risk — potentially lethal |
| **Vacuum chamber implosion** | Chambers at < 10^-5 mbar; glass viewports under atmospheric pressure differential (14.7 psi / 101 kPa) | Flying glass/debris; crush injury |
| **High temperature** | Substrates at 200-500 deg C; chamber walls and fixtures retain heat | Contact burns |
| **UV/IR radiation** | Plasma glow discharge, arc spots | Eye damage (cataracts, photokeratitis) |
| **Compressed gases** | Argon, nitrogen, oxygen cylinders at 2000-2500 psi; some toxic: NH3, H2S | Asphyxiation (Ar displaces O2), fire (O2 enrichment), cylinder projectile |
| **Toxic target materials** | Cadmium, beryllium, chromium (Cr6+ from Cr targets under certain conditions) | Inhalation of particles/fumes during target handling and chamber cleaning |
| **Cryopump hazards** | Helium refrigerant at 10-20 K; potential for condensed gas release on regeneration | Frostbite; O2 displacement; pressure burst if gate valve opened while cryopump saturated |
| **Pinch points** | Chamber doors, planetary fixtures, automated loading systems | Crush injuries |

### Required PPE

- **Electrical**: Lockout/Tagout before any maintenance; insulated gloves when working near power supplies; arc flash rated if working on > 50 V DC
- **Vacuum**: Safety glasses with side shields at all times near chambers; wire mesh or polycarbonate blast shields on viewports; never pressurize a chamber that has been under vacuum without verifying viewport integrity
- **Thermal**: Heat-resistant gloves (Kevlar or silicone, rated > 250 deg C) for handling hot fixtures; IR thermometer to verify surface temp before handling
- **Respiratory**: N95 minimum during chamber cleaning (target dust, coating flakes); P100 or supplied air if handling Cr, Cd, or Be targets
- **Gas safety**: O2 monitor in room (alarm at < 19.5% O2 for Ar/N2 asphyxiation hazard); gas cabinet with automatic shutoff for toxic gases; leak detection
- **General**: Cleanroom-compatible gloves (nitrile, lint-free) for part handling; ESD wrist straps in semiconductor applications

### Emergency Procedures

- **Electrical shock**: De-energize system immediately via E-stop; do not touch victim until power confirmed off; call emergency services
- **Gas leak (inert)**: Evacuate room; do not re-enter until O2 monitor reads > 19.5%; ventilate
- **Vacuum failure/implosion**: Evacuate immediate area; assess for flying debris injuries; do not approach chamber until pressure equalized
- **Burns**: Cool with running water 10+ min; do not apply ice to severe burns; seek medical attention for burns > 2nd degree

### Regulatory Considerations

- OSHA 29 CFR 1910.147 — Lockout/Tagout (LOTO) for all maintenance
- OSHA 29 CFR 1910.134 — Respiratory protection program if airborne metals exposure
- NFPA 70E — Electrical safety in the workplace
- OSHA PEL for chromium (Cr6+): 5 ug/m3 TWA; for cadmium: 5 ug/m3 TWA; for beryllium: 0.2 ug/m3 TWA
- Compressed gas storage: OSHA 29 CFR 1910.101; CGA pamphlets

---

## 1.3 Part Preparation

### Surface Finish Requirements

- **Tool coatings (TiN, TiAlN, CrN)**: Surface finish Ra < 0.2 um (8 uin) preferred; PVD replicates the substrate surface exactly — any defects (scratches, pits, grinding marks) will be visible through the coating
- **Decorative coatings**: Ra < 0.05 um (2 uin) — mirror polish required before deposition
- **Functional coatings (mold, die)**: Ra 0.05-0.4 um depending on application
- **Edge preparation**: Sharp edges (radius < 10 um) concentrate stress and cause coating delamination; hone or radius edges to > 20-50 um before coating

### Why Prep Is Critical

PVD coatings are thin (typically 1-5 um). They cannot fill, smooth, or bridge substrate defects. Unlike electroplating where thickness can be built up to mask imperfections, PVD is a conformal line-of-sight process. Any contamination, oxide, or surface defect becomes a nucleation site for coating failure.

### Masking Materials

| Material | Max Temp | Application |
|----------|----------|-------------|
| Kapton (polyimide) tape | 400 deg C | General masking; leaves no residue |
| Aluminum foil | 500+ deg C | Wrapping areas not to be coated |
| Copper tape | 500+ deg C | Electrical masking to control bias |
| Stainless steel fixtures | 500+ deg C | Permanent masks for production runs |
| High-temp silicone plugs | 300 deg C | Masking bores and holes |
| Boron nitride spray | 1000+ deg C | Release agent on fixtures to prevent coating buildup |

### Dimensional Tolerances

- PVD adds 1-5 um per side — for precision-ground cutting tools, this must be accounted for in pre-coating dimensions
- For tight-tolerance mold cavities (< +/- 5 um), coating thickness uniformity becomes critical — specify +/- 10% thickness uniformity

---

## 1.4 Cleaning

### Critical Cleanliness for Vacuum Processes

Contamination is the #1 cause of PVD coating adhesion failure. Even a monolayer of hydrocarbon contamination (~ 1 nm) can reduce coating adhesion by > 50%.

### Cleaning Sequence (Typical Industrial)

1. **Gross degreasing** — Vapor degreasing (where still permitted) or ultrasonic alkaline wash at 50-65 deg C, 5-10 min, 40 kHz
2. **Alkaline ultrasonic** — pH 10-12 alkaline cleaner, 50-60 deg C, 5-10 min, 40 kHz; removes oils, fingerprints, polishing compound
3. **DI water rinse** — 3-stage cascade rinse, > 10 Mohm-cm resistivity water
4. **Acid dip (optional)** — Dilute HCl or citric acid to remove surface oxides on steel; 2-5% concentration, ambient temp, 30-60 sec
5. **DI water rinse** — Final cascade rinse
6. **Solvent wipe (optional)** — IPA (isopropyl alcohol) or acetone wipe for spot cleaning
7. **Hot air dry** — Filtered hot air, 80-100 deg C; or vacuum dry
8. **In-chamber plasma cleaning** — Ar+ ion bombardment (this is step 7 of the 10-step process sequence above)

### Cleaning Validation

- **Water-break test** — Surface should sheet water uniformly with no beading (beading indicates hydrocarbon contamination)
- **UV fluorescence** — Black light inspection for residual oils/greases
- **Contact angle measurement** — < 5 deg contact angle indicates clean surface (research/QC labs)
- **OSEE (Optically Stimulated Electron Emission)** — Quantitative surface cleanliness measurement (semiconductor)

### Why Contamination Causes Failure

- Hydrocarbons decompose under ion bombardment, forming a weak amorphous carbon interlayer between substrate and coating
- Surface oxides (native oxide on steel is 2-5 nm) act as a weak boundary layer — the coating adheres to the oxide, which then delaminates from the substrate
- Particulate contamination creates shadows (PVD is line-of-sight), resulting in pinholes and non-uniform thickness
- Water vapor from inadequate drying increases pumpdown time and can react with target materials, forming unwanted oxides in the coating

---

## 1.5 Equipment / System Setup

### Chamber Types

| Type | Description | Throughput | Applications |
|------|-------------|-----------|--------------|
| **Batch box coater** | Single large chamber; load parts, pump down, coat, vent, unload | Low-medium; cycle time 4-8 hours | Cutting tools, molds, R&D |
| **Inline (in-line)** | Parts move through connected chambers (load lock > preheat > etch > deposit > cool > unload) | High; continuous or semi-continuous | Architectural glass, automotive trim, web coating |
| **Load-lock** | Separate loading chamber isolated by gate valve; main chamber stays under vacuum | Medium-high; reduced cycle time | Production tool coating, semiconductor |
| **Cluster tool** | Central transfer chamber with multiple process chambers (sputter, etch, CVD) around it | High | Semiconductor wafer fab |

### Vacuum Levels

| Stage | Pressure Range | Equipment |
|-------|---------------|-----------|
| Rough vacuum | 1013 mbar to 10^-1 mbar | Rotary vane pump, scroll pump, roots blower |
| High vacuum | 10^-1 to 10^-7 mbar | Turbomolecular pump, diffusion pump, cryopump |
| Ultra-high vacuum | < 10^-7 mbar | Ion pump, titanium sublimation pump (semiconductor) |
| **Typical PVD base pressure** | 1 x 10^-5 to 5 x 10^-5 mbar | Turbo + backing pump most common |
| **Typical PVD working pressure** | 0.1-1.0 Pa (0.75-7.5 mTorr) | Controlled by Ar/reactive gas flow + throttle valve |

### Target/Source Materials

- **Sputtering targets**: Ti, Cr, Al, Zr, TiAl (50/50 or 67/33 at%), AlCr, W, Ta, Cu, Mo — supplied as bonded discs (magnetron) or rectangular plates (inline)
- **Arc cathodes**: Same materials, typically supplied as cylindrical or disc cathodes; require periodic replacement when erosion track exceeds ~60% of material
- **Target purity**: 99.5% minimum for industrial; 99.99% (4N) or 99.999% (5N) for semiconductor

### Gas Systems

| Gas | Purpose | Typical Flow Rate |
|-----|---------|------------------|
| Argon (Ar) | Sputtering gas / plasma sustaining | 50-500 sccm |
| Nitrogen (N2) | Reactive gas for nitride coatings | 50-300 sccm |
| Oxygen (O2) | Reactive gas for oxide coatings | 10-100 sccm |
| Acetylene (C2H2) | Reactive gas for carbide/DLC coatings | 20-200 sccm |
| Hydrogen (H2) | Reducing gas (some processes) | 10-50 sccm |

Flow controlled by mass flow controllers (MFCs), accuracy +/- 1% of full scale.

### Temperature Control

- **Substrate heating**: Radiative heaters (quartz lamps or resistance elements), 200-500 deg C
- **Substrate cooling**: Water-cooled substrate table for low-temperature deposition (polymers, pre-hardened steel)
- **Target/cathode cooling**: Always water-cooled; typical water flow 2-5 L/min per cathode; inlet temp < 25 deg C

### Rotation Systems

- **Single-axis (turntable)**: Parts rotate around central axis; simplest; acceptable for flat parts
- **Double planetary**: Parts orbit central axis AND rotate on their own axis; good uniformity on 3D parts
- **Triple planetary**: Parts orbit, rotate, and tilt; best uniformity on complex geometries; standard for cutting tool coating

---

## 1.6 Parameter Setup

### Sputtering Parameters

| Parameter | Typical Range | Effect |
|-----------|--------------|--------|
| DC power | 1-20 kW per cathode | Higher power = higher deposition rate but more substrate heating |
| RF power | 100-1000 W | Used for insulating targets (Al2O3, SiO2) |
| Substrate bias | -50 to -300 V DC or pulsed | Controls ion bombardment energy; affects density, stress, adhesion |
| Working pressure | 0.1-1.0 Pa | Lower pressure = more energetic deposition (fewer gas-phase collisions); higher pressure = better throwing power |
| Ar flow | 50-500 sccm | Sustains plasma; higher flow = higher pressure |
| Reactive gas flow | Critical parameter — controlled to stay in "transition zone" | Too much = target poisoning (rate drops to < 10%); too little = substoichiometric coating |
| Deposition rate | Sputtering: 0.5-5 um/hr; Arc: 2-10 um/hr | Arc significantly faster due to high ionization |
| Substrate temp | 200-500 deg C | Higher temp = denser coating, better adhesion; limited by substrate material |

### Arc Evaporation Parameters

| Parameter | Typical Range |
|-----------|--------------|
| Arc current | 50-200 A per cathode |
| Arc voltage | 20-40 V (self-regulating) |
| Substrate bias | -20 to -1200 V (high bias for ion etching, -50 to -200 V for deposition) |
| Magnetic field (arc steering) | Controlled to move arc spot across target face for uniform erosion |

### Ramp Rates

- **Heating ramp**: 5-15 deg C/min to avoid thermal shock, especially on carbide or ceramic substrates
- **Cooling ramp**: Typically uncontrolled (radiative cooling under vacuum); 1-5 deg C/min depending on chamber size and thermal mass
- **Bias ramp**: Often stepped — start high (-800 to -1200 V) for ion etching, reduce to deposition bias (-50 to -200 V) over 1-2 minutes

### Recipe Development Considerations

- **Hysteresis in reactive sputtering**: The relationship between reactive gas flow and deposition rate is non-linear with hysteresis; process control often requires feedback from optical emission spectroscopy (OES) or partial pressure monitoring
- **Substrate material matters**: Pre-hardened tool steels (> 60 HRC) should not exceed 500 deg C (tempering risk); aluminum substrates limited to < 150-200 deg C; polymers < 80-150 deg C depending on Tg
- **Multilayer/gradient coatings**: Modern recipes stack multiple layers (e.g., TiN adhesion layer > TiAlN functional layer > TiAlSiN top layer) to optimize adhesion, hardness, and oxidation resistance

---

## 1.7 Deposition / Treatment Stage

### How the Coating Grows

1. **Nucleation**: Arriving atoms (adatoms) land on the substrate surface and migrate until they find an energetically favorable site (defect, step edge, or cluster of other adatoms)
2. **Island formation**: Adatoms cluster into nanoscale islands (Volmer-Weber growth mode for most PVD metal-on-metal systems)
3. **Coalescence**: Islands grow and merge into a continuous film (typically at 5-20 nm thickness)
4. **Columnar growth**: Film grows in columnar structures whose morphology depends on substrate temperature and ion bombardment energy — described by the Thornton Structure Zone Model:
   - Zone 1 (low T, low ion energy): Porous columnar; voided grain boundaries
   - Zone T (moderate T or ion energy): Dense fibrous; competitive grain growth
   - Zone 2 (higher T): Columnar with fully dense grain boundaries
   - Zone 3 (high T): Equiaxed recrystallized grains

### Thickness Monitoring

| Method | Principle | Accuracy | In-situ? |
|--------|-----------|----------|----------|
| Quartz Crystal Microbalance (QCM) | Frequency shift of piezoelectric crystal as mass deposits | +/- 0.1 nm | Yes |
| Optical emission spectroscopy (OES) | Monitors plasma composition | Qualitative (reactive gas control) | Yes |
| Time-based | Calibrated deposition rate x time | +/- 10-20% | Yes (by calculation) |
| Reflectance/transmittance (optical) | Interference fringes for transparent films | +/- 1-5 nm | Yes (optical coatings) |

### Typical Deposition Times

- **TiN cutting tool coating (3 um)**: Sputtering: 1.5-3 hours; Arc: 30-90 min
- **Decorative coating (0.3-0.5 um)**: 15-45 min
- **Multilayer tool coating (5-8 um total)**: 3-6 hours total cycle
- **Full cycle time including pumpdown, heating, etching**: 4-10 hours for batch process

### In-Situ Quality Indicators

- **Plasma color**: TiN plasma should be golden-pink; shift to blue indicates N2 excess; shift to bright metallic white indicates metallic Ti (N2 deficient)
- **Arc stability**: Unstable arcs (flickering, extinguishing) indicate target contamination or magnetic field issues
- **Pressure stability**: Drifting pressure indicates gas leak, outgassing, or MFC malfunction
- **Bias current**: Substrate bias current is proportional to ion flux; sudden changes indicate arcing or fixture issues

---

## 1.8 Cooling & Handling / Inspection & QA

### Cooling Requirements

- Cool under vacuum (< 10^-2 mbar) until substrate temperature drops below 150-200 deg C to prevent oxidation of freshly deposited coating
- Typical cool-down time: 1-3 hours depending on load mass and chamber size
- Some systems use controlled Ar or N2 backfill at intermediate pressure to accelerate cooling (convective cooling)
- **Never vent to atmosphere while parts are above 200 deg C** — coating surface will oxidize and discolor

### Adhesion Testing

| Method | Standard | Description |
|--------|----------|-------------|
| **Rockwell indentation (HRC)** | VDI 3198 | Indent coating with Rockwell C indenter at 150 kgf; examine crack pattern under microscope; classify HF1 (acceptable) through HF6 (failure) |
| **Scratch test** | ASTM C1624, ISO 20502 | Diamond stylus (200 um radius) drawn across coating with increasing load; critical load Lc (coating failure) recorded; Lc > 30 N typical for good adhesion on hard coatings |
| **Tape test** | ASTM D3359 | Cross-hatch pattern scribed through coating; adhesive tape applied and peeled; classify 0B (failure) to 5B (no removal) |

### Thickness Measurement (Post-Deposition)

| Method | Range | Accuracy | Destructive? |
|--------|-------|----------|-------------|
| **Calotest (ball crater)** | 0.1-50 um | +/- 2-5% | Yes (small crater) |
| **XRF** | 0.01-50 um | +/- 3-10% | No |
| **Profilometry (step height)** | 0.01-100 um | +/- 1-5% | Requires witness coupon |
| **SEM cross-section** | 0.01-100 um | +/- 2% | Yes (destructive) |
| **Ellipsometry** | 1 nm - 10 um | +/- 0.5 nm | No (transparent films only) |

### Common Defects

| Defect | Cause | Prevention |
|--------|-------|------------|
| **Macroparticles (droplets)** | Arc evaporation ejects molten droplets from target | Filtered arc (magnetic duct), lower arc current, polished cathode surface |
| **Delamination / poor adhesion** | Contamination, inadequate ion etching, excessive coating stress | Proper cleaning, optimized bias during etching, stress management via multilayering |
| **Pinholes** | Particulate contamination on substrate, shadowing from geometry | Cleanroom handling, optimized rotation, higher working pressure |
| **Non-uniform thickness** | Inadequate rotation, improper part placement, target erosion asymmetry | Triple planetary rotation, fixture design validation, target lifecycle management |
| **Wrong color (reactive coatings)** | Off-stoichiometry due to reactive gas control failure | OES feedback control, calibrated MFCs, process monitoring |
| **High compressive stress / flaking** | Excessive ion bombardment (bias too high), coating too thick | Reduce bias, multilayer architecture, limit single-layer thickness to < 5 um |
| **Arcing** | Insulating buildup on chamber walls/fixtures, substrate outgassing | Regular chamber cleaning, proper degassing cycle, conductive shields |

---
---

# CLUSTER 2: CHEMICAL VAPOR DEPOSITION (CVD)

## 2.1 Process Flow Poster Data

### What Is Thermal CVD?

Chemical Vapor Deposition is a process in which gaseous precursor chemicals react at or near a heated substrate surface to form a solid coating. Unlike PVD (physical transfer), CVD involves **chemical reactions** — the coating material is synthesized in the gas phase or at the surface from volatile compounds.

**Key mechanistic steps:**
1. Precursor gases transported to reaction zone by carrier gas
2. Gas-phase reactions may produce intermediate species
3. Precursors/intermediates adsorb on hot substrate surface
4. Surface chemical reactions form the solid coating + volatile byproducts
5. Byproducts desorb and are pumped away

**Thermal CVD** (this cluster) uses heat alone to drive the reactions — substrate temperatures typically 800-1100 deg C. This distinguishes it from PECVD (Cluster 3), which uses plasma to enable lower temperatures.

### Key Industries and Applications

| Industry | Application | Typical Coatings |
|----------|------------|-----------------|
| Cutting tools | Indexable inserts (dominant method for cemented carbide inserts) | TiC, TiN, TiCN, Al2O3 (alpha and kappa), multilayer stacks |
| Semiconductor | Epitaxial Si, SiO2, Si3N4, polysilicon, W (tungsten CVD) | Thin films for device fabrication |
| Wear protection | Extrusion dies, forming tools | TiC, TiN |
| Corrosion protection | Chemical process equipment | SiC, Si3N4 |
| Optical | Anti-reflection coatings, IR windows | Diamond, DLC, SiO2, TiO2 |
| Aerospace | Thermal barrier systems, SiC fiber coating | SiC, BN, PyC (pyrolytic carbon) |

### Substrate Compatibility

- **Cemented carbide (WC-Co)**: Primary substrate — tolerates CVD temperatures well
- **High-speed steel**: Generally NOT suitable — CVD temps exceed tempering temp (> 550 deg C)
- **Ceramics**: Si3N4, Al2O3, SiC — excellent for CVD
- **Graphite**: Common substrate for SiC CVD
- **Silicon wafers**: Semiconductor CVD
- **Limitation**: Substrates must withstand 800-1100 deg C without distortion, phase transformation, or decomposition

### Coating Properties

| Coating | Hardness (HV) | Typical Thickness | Max Service Temp | Precursors |
|---------|--------------|-------------------|------------------|-----------|
| TiC | 2,800-3,200 | 3-10 um | 500 deg C | TiCl4 + CH4 |
| TiN | 2,000-2,400 | 1-5 um | 600 deg C | TiCl4 + N2 + H2 |
| TiCN (MT-CVD) | 2,500-3,000 | 3-10 um | 450 deg C | TiCl4 + CH3CN (moderate temp: 700-900 deg C) |
| Al2O3 (alpha) | 2,000-2,200 | 2-8 um | 1,000+ deg C | AlCl3 + CO2 + H2 |
| Al2O3 (kappa) | 1,800-2,000 | 2-8 um | 1,000+ deg C | Same precursors, different conditions |
| SiC | 2,400-2,800 | 10-500 um | 1,600 deg C | SiCl4 + CH4 or methyltrichlorosilane |
| Diamond | 8,000-10,000 | 1-50 um | 600 deg C (in air) | CH4 + H2 (hot-filament or microwave plasma) |

### 10-Step Process Sequence

1. **Part inspection** — Verify substrate dimensions, material grade, surface condition
2. **Cleaning** — Ultrasonic wash; hydrogen pre-bake in furnace to remove surface oxides
3. **Loading** — Place parts on graphite or ceramic trays; stack in furnace retort
4. **Seal and purge** — Close retort; purge with inert gas (Ar or N2) to displace air
5. **Heat to process temperature** — Ramp to 900-1050 deg C under H2 flow (5-15 deg C/min)
6. **Stabilize** — Hold at temperature for 15-30 min; ensure uniform temperature distribution
7. **Deposition** — Introduce precursor gases (TiCl4, CH4, N2, CO2, AlCl3, etc.) in controlled sequence; each layer deposited sequentially for multilayer coatings
8. **Purge between layers** — H2 purge to clear previous precursors before introducing next layer chemistry
9. **Cooldown** — Controlled cooling under H2 or Ar atmosphere (2-10 deg C/min to avoid thermal shock and deformation)
10. **Unload, inspect, post-treat** — Visual inspection; thickness measurement; may require post-deposition blasting or polishing to smooth surface

---

## 2.2 Safety & PPE

### Hazards Specific to Thermal CVD

| Hazard | Source | Severity |
|--------|--------|----------|
| **Toxic/corrosive precursor gases** | TiCl4 (fumes in air, produces HCl), AlCl3, SiH4 (pyrophoric), BCl3, WF6 (toxic + produces HF) | Inhalation: pulmonary edema; contact: severe burns; SiH4: spontaneous ignition |
| **Hydrogen gas (H2)** | Carrier/reducing gas; used in large volumes (10-100 L/min) | Explosive: LEL 4%, UEL 75%; invisible flame; detonation risk in confined space |
| **HCl byproduct gas** | Product of TiCl4 and AlCl3 reactions | Corrosive to lungs, eyes, equipment; OSHA PEL 5 ppm ceiling |
| **High temperature** | Furnace operates at 800-1100 deg C; external surfaces > 50 deg C | Severe burns; ignition of flammable materials |
| **CO gas** | Byproduct of Al2O3 deposition (CO2 + H2 reaction) | Toxic: OSHA PEL 50 ppm TWA; odorless |
| **Compressed gas cylinders** | Multiple gas types at high pressure | Standard cylinder hazards |
| **Exhaust scrubber failure** | All CVD exhaust must be scrubbed (HCl, unreacted precursors) | Environmental release; equipment corrosion |

### Required PPE

- **Chemical-resistant apron and gloves** (butyl rubber or Viton for TiCl4/HCl exposure)
- **Full-face respirator with acid gas cartridge** or supplied air when working near open precursor systems
- **Fire-resistant clothing** (Nomex or treated cotton) near furnace
- **Safety glasses + face shield** for furnace operations
- **H2 gas detector** — continuous monitoring in furnace area (alarm at 10% LEL = 0.4% H2)
- **CO monitor** — continuous monitoring (alarm at 35 ppm)
- **HCl monitor** — continuous monitoring (alarm at 2 ppm)

### Emergency Procedures

- **SiH4 leak**: Evacuate area immediately; SiH4 ignites spontaneously in air; do not attempt to extinguish unless gas can be shut off; let it burn if isolated
- **H2 fire**: Shut off H2 supply; use CO2 or dry chemical extinguisher; H2 flame is invisible in daylight — use broom straw or thermal camera to locate
- **TiCl4 spill/leak**: Dense white fumes of TiO2 and HCl form on contact with moisture; evacuate; use supplied air; neutralize with soda ash or lime
- **Furnace thermal runaway**: E-stop; close precursor gas valves; maintain H2 or inert purge to prevent air infiltration (air + H2 at temperature = explosion)

---

## 2.3 Part Preparation

### Surface Requirements

- Surface finish requirements less critical than PVD because CVD coatings are thicker and the chemical process gives better "throwing power" (not line-of-sight)
- For cutting inserts: Ra < 0.4 um (16 uin) typical after grinding
- Edge preparation: K-land or chamfer per tool geometry spec; CVD can round sharp edges due to gas-phase nucleation
- Surface must be free of grinding burn, cobalt depletion, and sub-surface damage
- **Cobalt enrichment zone** on WC-Co substrates: CVD at high temp can cause cobalt to migrate to the surface, forming a weak eta-phase (Co3W3C); controlled by atmosphere and cooling rate

### Masking

- Less commonly masked than PVD (entire insert usually coated)
- When masking is needed: refractory pastes (Al2O3 or ZrO2 based) applied by brush or screen printing
- Graphite fixtures serve as inherent masks for non-deposition surfaces

---

## 2.4 Cleaning

- **Pre-cleaning**: Ultrasonic alkaline wash > DI rinse > dry
- **In-furnace oxide removal**: H2 reduction at process temperature effectively cleans surface oxides in situ
- **Furnace cleaning**: Periodic etch runs using HCl/Cl2 gas to remove coating buildup from retort walls and fixtures (every 20-50 runs)
- Contamination is less critical than PVD because the high-temperature chemical reaction provides inherent surface activation; however, organic contamination will produce carbon inclusions in the coating

---

## 2.5 Equipment / System Setup

### Reactor Types

| Type | Description | Application |
|------|-------------|-------------|
| **Hot-wall CVD** | Furnace heats both substrate AND reactor walls; walls also get coated | Standard for cutting tool CVD; batch process |
| **Cold-wall CVD** | Only substrate is heated (induction, resistance, lamp); walls stay cool | Semiconductor epitaxy; less waste; better control |
| **Fluidized bed CVD** | Parts suspended in upward gas flow; excellent uniformity on small parts | Powder coating, small components |

### Furnace Specifications (Hot-Wall Tool Coating)

- **Temperature range**: 800-1100 deg C (typical: 1000-1050 deg C for TiC/TiN; 700-900 deg C for MT-CVD TiCN)
- **Pressure**: 50-500 mbar (sub-atmospheric) or atmospheric (1013 mbar) depending on process
- **Retort material**: Inconel 600/601, graphite, or SiC
- **Capacity**: 500-5,000 inserts per batch depending on furnace size
- **Gas delivery**: Bubbler systems for liquid precursors (TiCl4 bp = 136 deg C; kept at 30-40 deg C in thermostatted bubbler); MFCs for gaseous reactants
- **Exhaust**: Water scrubber to neutralize HCl; particulate filter; may include thermal oxidizer

### Temperature Control

- Multi-zone resistance heating (3-5 zones) for temperature uniformity +/- 5 deg C across work zone
- Thermocouples (Type K or S) placed in multiple zones
- Temperature uniformity survey per AMS 2750 or equivalent

---

## 2.6 Parameter Setup

### Key Process Parameters

| Parameter | TiC Layer | TiN Layer | Al2O3 Layer | MT-CVD TiCN |
|-----------|----------|----------|------------|-------------|
| Temperature | 1000-1050 deg C | 1000-1050 deg C | 1000-1050 deg C | 700-900 deg C |
| Pressure | 50-200 mbar | 50-200 mbar | 50-100 mbar | 50-200 mbar |
| TiCl4 flow | 2-5% of total | 2-5% of total | — | 2-5% of total |
| CH4 flow | 3-6% | — | — | — |
| N2 flow | — | 20-40% | — | — |
| CH3CN flow | — | — | — | 0.5-2% |
| AlCl3 flow | — | — | 2-5% | — |
| CO2 flow | — | — | 3-6% | — |
| H2 (carrier) | Balance | Balance | Balance | Balance |
| Deposition rate | 1-3 um/hr | 0.5-2 um/hr | 0.5-1.5 um/hr | 2-5 um/hr |
| Layer time | 2-5 hrs | 1-3 hrs | 3-8 hrs | 1-3 hrs |

### Multilayer Recipe Example (Modern Cutting Insert)

Typical stack (inside to outside): TiN (0.5 um) > MT-CVD TiCN (8-12 um) > Al2O3 (4-8 um) > TiN (1 um, color layer)
Total cycle time: 12-24 hours including heat-up and cool-down

---

## 2.7 Deposition / Treatment Stage

### How CVD Coating Grows

- **Mass-transport limited regime** (high temp): Deposition rate controlled by how fast precursors can diffuse through the boundary layer to the surface; temperature dependence is weak; gives uniform coatings
- **Reaction-rate limited regime** (lower temp): Deposition rate controlled by surface reaction kinetics; strong temperature dependence (Arrhenius); can give non-uniform coatings if temperature varies across substrate
- MT-CVD operates in reaction-rate limited regime, which is why temperature uniformity is critical
- Grain structure: CVD coatings are typically columnar with grain sizes of 0.5-5 um; Al2O3 texture can be controlled (alpha vs. kappa phase) by nucleation conditions

### Thickness Monitoring

- **Time-based**: Primary method — deposition rate is well-characterized and stable for a given recipe
- **Weight gain**: Weigh parts before and after; calculate average thickness from known density and surface area
- **Witness coupons**: Flat test pieces included in each batch; measured post-run by calotest or cross-section
- In-situ monitoring is less common in industrial CVD than PVD; semiconductor CVD uses in-situ ellipsometry, reflectometry, or FTIR

---

## 2.8 Post-Treatment / Inspection

### Cooling Requirements

- Cool under H2 or inert atmosphere to prevent oxidation
- Cooling rate: 2-10 deg C/min; too fast causes thermal stress cracking of coating and/or substrate
- For WC-Co substrates: controlled cooling through the eta-phase formation region (900-700 deg C) is critical to avoid brittle intermetallic phases

### Post-Coating Treatment

- **Wet blasting or dry blasting**: Light blasting with fine Al2O3 media (400-800 grit) to smooth surface, remove excess nodules, and introduce compressive stress in the coating surface
- **Polishing rake face**: For cutting inserts, the rake face is often polished to reduce friction and improve chip flow
- **Edge treatment**: Post-coat honing to optimize cutting edge radius (typically 20-40 um)

### Common Defects

| Defect | Cause | Prevention |
|--------|-------|------------|
| **Coating delamination** | Eta-phase at interface (Co3W3C); poor cobalt adhesion | Control temperature, atmosphere; use TiN interlayer |
| **Egg-shell cracking** | Thermal expansion mismatch; coating too thick; cooling too fast | Limit individual layer thickness; control cooling rate |
| **Soot / carbon inclusions** | Excess hydrocarbon precursor; CH4 cracking | Optimize gas ratios; maintain furnace cleanliness |
| **Non-uniform thickness** | Temperature gradients; gas flow dead zones | Multi-zone heating; optimize retort/tray design |
| **Wrong Al2O3 phase** | Nucleation conditions incorrect | Control nucleation step precisely (oxidation pulse technique) |
| **Cobalt depletion** | CVD gases (HCl) etch cobalt from WC-Co surface at high temp | MT-CVD at lower temp; protective interlayer |

---
---

# CLUSTER 3: PLASMA-ENHANCED CVD (PECVD)

## 3.1 Process Flow Poster Data

### What Is PECVD?

Plasma-Enhanced Chemical Vapor Deposition uses electrical energy to generate a glow-discharge plasma, which provides the activation energy for chemical reactions that would otherwise require much higher temperatures. The plasma creates reactive species (radicals, ions, excited molecules) from precursor gases, enabling deposition at **100-400 deg C** instead of the 800-1100 deg C required for thermal CVD.

**Plasma generation methods:**
- **RF (radio frequency) PECVD**: 13.56 MHz RF applied between two parallel-plate electrodes; substrates typically sit on the grounded electrode; most common industrial variant
- **Microwave PECVD**: 2.45 GHz microwave energy creates plasma; substrate is downstream of plasma zone (remote plasma); lower ion bombardment damage; used for diamond deposition
- **DC PECVD**: Direct current between electrodes; less common; limited to conductive substrates
- **Pulsed DC PECVD**: Overcomes arcing problems of DC on insulating surfaces; growing in popularity

### Key Industries and Applications

| Industry | Application | Coating/Film |
|----------|------------|-------------|
| Semiconductor | Interlayer dielectrics, passivation, etch stop layers, gate dielectrics | SiO2, Si3N4, SiON, SiC, low-k dielectrics |
| Solar (photovoltaic) | Anti-reflection coating, passivation on Si wafers | SiNx:H (hydrogen-rich silicon nitride) |
| Display (LCD, OLED) | Thin-film transistor fabrication, encapsulation | a-Si:H (amorphous silicon), SiNx, SiOx |
| Packaging | Gas barrier films on polymers | SiOx on PET, PP |
| Optics | Anti-reflection, hard coats on plastic lenses | SiO2, Si3N4 |
| Biomedical | Biocompatible/hydrophobic coatings | Diamond-like carbon (DLC), fluoropolymer |
| Tool coating | DLC and a-C:H coatings | See Cluster 5 (DLC) |

### Substrate Compatibility

- **Silicon wafers**: Primary substrate for semiconductor PECVD
- **Glass**: LCD/OLED display fabrication
- **Polymers**: PET, PP, polycarbonate — key advantage of PECVD is low deposition temp
- **Metals**: Steel, aluminum, titanium
- **Temperature-sensitive substrates**: PECVD's major advantage over thermal CVD — can coat materials that cannot survive > 200 deg C

### Coating Properties

| Film | Hardness | Refractive Index | Dielectric Constant | Deposition Temp |
|------|----------|-----------------|---------------------|----------------|
| PECVD SiO2 | 6-8 GPa | 1.46-1.47 | 4.0-4.5 | 200-400 deg C |
| PECVD Si3N4 | 15-25 GPa | 1.8-2.1 | 6.0-7.5 | 200-400 deg C |
| PECVD SiNx:H (solar) | 12-18 GPa | 2.0-2.1 (tunable) | 5-7 | 350-450 deg C |
| PECVD a-Si:H | — | 3.5-4.5 | 11-12 | 150-300 deg C |
| PECVD DLC (a-C:H) | 10-30 GPa | 1.8-2.4 | 3-5 | 50-300 deg C |

### 10-Step Process Sequence

1. **Substrate inspection** — Verify wafer/part specifications, cleanliness, incoming measurements
2. **Pre-cleaning** — Wet chemical clean (semiconductor: RCA clean or dilute HF); ultrasonic for industrial parts
3. **Loading** — Place substrates on electrode/susceptor in vacuum chamber (single-wafer or batch)
4. **Pumpdown** — Evacuate to base pressure (10-50 mTorr / 1-7 Pa typical)
5. **Stabilize temperature** — Heat susceptor to process temperature (200-400 deg C); stabilize 5-10 min
6. **Gas flow stabilization** — Introduce precursor and carrier gases at set flow rates; stabilize pressure
7. **Plasma ignition** — Apply RF/microwave power; plasma strikes; deposition begins
8. **Deposition** — Maintain power, pressure, temperature, and gas flows for calculated time
9. **Plasma off and purge** — Extinguish plasma; purge chamber with inert gas
10. **Cooldown and unload** — Cool substrate; vent chamber; unload; inspect

---

## 3.2 Safety & PPE

### Hazards Specific to PECVD

| Hazard | Source | Severity |
|--------|--------|----------|
| **Silane (SiH4)** | Primary Si precursor; pyrophoric — ignites spontaneously in air at > 2% concentration | Fire/explosion; OSHA PEL 5 ppm; IDLH not established |
| **RF radiation** | 13.56 MHz at 100-2000 W; leakage from chamber, cables, matching network | RF burns; interference with pacemakers |
| **Ammonia (NH3)** | Nitrogen source for Si3N4 | Toxic: OSHA PEL 50 ppm TWA; corrosive to lungs |
| **Nitrous oxide (N2O)** | Oxygen source for SiO2 | Oxidizer; supports combustion; anesthetic at high concentrations |
| **TEOS (tetraethylorthosilicate)** | Liquid SiO2 precursor | Flammable; irritant; ethanol byproduct |
| **NF3 (nitrogen trifluoride)** | Chamber cleaning gas | Highly toxic: OSHA PEL 10 ppm TWA; strong greenhouse gas (GWP 17,200) |
| **Powder/particle hazard** | SiO2 and Si3N4 powder accumulates in exhaust lines; SiH4 + O2 in exhaust produces pyrophoric silica dust | Exhaust line fires; particle contamination |
| **Vacuum/electrical** | Same as other vacuum processes | Same as PVD |

### Required PPE

- **SiH4 handling**: Gas cabinet with automatic shutoff; continuous SiH4 detector (alarm at 0.5 ppm); fire suppression in gas cabinet
- **RF safety**: Shielded chamber; interlock on chamber door (plasma off when door open); RF leakage survey with field meter (< 10 mW/cm2 at operator position per OSHA)
- **Chemical**: Face shield + goggles for NH3/TEOS handling; acid-resistant gloves
- **Respiratory**: Supplied air for SiH4 emergency response; SCBA available
- **General**: ESD precautions for semiconductor wafers; cleanroom garments

### Emergency: SiH4 Leak

- If < 2% in air: may not autoignite; ventilate; shut off supply
- If > 2%: will ignite spontaneously; clear area; let it burn if flame is confined; do NOT attempt to extinguish — unburned SiH4 cloud is more dangerous than flame
- Explosion risk if SiH4 accumulates in dead space then ignites — prevention requires constant ventilation of gas cabinet and delivery lines

---

## 3.3-3.4 Part Preparation and Cleaning

### Semiconductor PECVD Cleaning

- **RCA clean (standard)**: SC-1 (NH4OH:H2O2:H2O = 1:1:5 at 75-80 deg C, 10 min) removes organics + particles; SC-2 (HCl:H2O2:H2O = 1:1:6 at 75-80 deg C, 10 min) removes metallic contamination
- **Dilute HF dip**: 1:100 HF:H2O, 30-60 sec — removes native oxide; leaves H-terminated Si surface (hydrophobic)
- **Cleanroom class**: Class 100 (ISO 5) or better for semiconductor PECVD; Class 1000 (ISO 6) for industrial/solar

### Industrial PECVD Cleaning

- Same as PVD: ultrasonic alkaline > rinse > IPA > dry
- In-situ Ar/O2 plasma cleaning (5-15 min, 100-500 W) to remove residual organics before deposition

---

## 3.5 Equipment / System Setup

### Chamber Configurations

| Type | Description | Application |
|------|-------------|-------------|
| **Parallel-plate (capacitively coupled)** | Two electrodes facing each other; substrate on bottom electrode; RF applied to top | Standard for SiO2, Si3N4, a-Si:H deposition |
| **Shower-head** | Top electrode has many small holes for uniform gas distribution | Better uniformity; standard in modern tools |
| **Tube/batch** | Multiple wafers in horizontal or vertical tube reactor | High throughput for solar SiNx |
| **Remote plasma** | Plasma generated separately; reactive species flow to substrate | Lower damage; better for sensitive devices |
| **Roll-to-roll** | Continuous web of polymer film moves through plasma zone | Barrier coatings on flexible packaging |

### Typical Operating Parameters

- **Base pressure**: 10-50 mTorr (1-7 Pa)
- **Working pressure**: 0.5-5 Torr (65-650 Pa) — much higher than PVD sputtering
- **RF power**: 13.56 MHz, 50-1000 W (power density 0.01-0.5 W/cm2)
- **Electrode spacing**: 15-30 mm
- **Substrate temperature**: 200-400 deg C (semiconductor); 80-200 deg C (polymers)
- **Pumping**: Roots blower + dry pump (no oil contamination for semiconductor)

### Precursor Gas Systems

| Film | Precursor Gases | Carrier |
|------|----------------|---------|
| SiO2 | SiH4 + N2O (or TEOS + O2) | N2 or Ar |
| Si3N4 | SiH4 + NH3 (or SiH4 + N2) | N2 or Ar |
| a-Si:H | SiH4 | H2 or Ar |
| SiON | SiH4 + N2O + NH3 | N2 |
| SiC | SiH4 + CH4 | Ar |

---

## 3.6 Parameter Setup

### PECVD SiO2 (Representative Recipe)

| Parameter | Value |
|-----------|-------|
| SiH4 flow | 30-100 sccm |
| N2O flow | 300-1000 sccm (SiH4:N2O ratio ~1:5 to 1:10) |
| RF power | 100-300 W (13.56 MHz) |
| Pressure | 1-3 Torr |
| Temperature | 300-400 deg C |
| Deposition rate | 50-200 nm/min |
| Refractive index target | 1.46-1.47 (matches thermal SiO2) |

### PECVD Si3N4 (Representative Recipe)

| Parameter | Value |
|-----------|-------|
| SiH4 flow | 50-200 sccm |
| NH3 flow | 20-100 sccm |
| N2 flow | 500-2000 sccm |
| RF power | 100-500 W |
| Pressure | 1-3 Torr |
| Temperature | 300-400 deg C |
| Deposition rate | 10-50 nm/min |
| Refractive index target | 1.85-2.05 (tunable by SiH4:NH3 ratio) |

### Key Tuning Relationships

- **Higher RF power** = denser film, higher stress, faster rate
- **Higher temperature** = less hydrogen in film, denser, more stable
- **Higher SiH4:N2O ratio** = Si-rich SiOx (higher refractive index, higher leakage)
- **SiH4:NH3 ratio** controls Si:N stoichiometry in nitride — silicon-rich nitride has higher refractive index and absorption (useful for solar AR coatings)

---

## 3.7-3.8 Deposition, Post-Treatment, Inspection

### Film Growth

- PECVD films are amorphous (no long-range crystal order) due to low substrate temperature
- Hydrogen is incorporated into the films (1-30 at% H depending on conditions) — affects density, etch rate, refractive index, and dielectric properties
- Film stress can be tensile or compressive depending on RF power, pressure, and temperature — typically targeted at low compressive stress (< 200 MPa) to avoid wafer bowing or film cracking

### In-Situ Monitoring

- **Laser interferometry**: Monitors film thickness during deposition by tracking reflected laser intensity oscillations (each fringe = lambda/2n thickness)
- **Optical emission spectroscopy**: Monitors plasma species
- **Residual gas analyzer (RGA)**: Mass spectrometer monitors gas-phase composition

### Post-Deposition

- **Anneal (optional)**: 400-450 deg C in N2 for 30-60 min — drives out hydrogen, densifies film, reduces etch rate; important for PECVD SiO2 used as interlayer dielectric
- **Thickness measurement**: Ellipsometry (most common; accuracy +/- 0.5 nm); reflectometry; profilometry over step
- **Stress measurement**: Wafer bow method (Stoney equation); target < 200 MPa
- **Composition**: FTIR spectroscopy — Si-H peak at ~2100 cm-1, N-H peak at ~3340 cm-1, Si-O peak at ~1060 cm-1; peak ratios indicate stoichiometry and hydrogen content
- **Etch rate**: Buffered HF (BOE) etch rate correlates with film quality — lower etch rate = denser, better-quality film; thermal SiO2 etches at ~100 nm/min in 6:1 BOE; good PECVD SiO2 at 200-400 nm/min

### Common Defects

| Defect | Cause | Prevention |
|--------|-------|------------|
| **Particles** | Powder formation from gas-phase nucleation; flaking from chamber walls | Optimize pressure/power to suppress gas-phase reactions; regular chamber cleans (NF3 or CF4 plasma) |
| **Pinholes** | Particles on substrate; too-thin film | Proper cleaning; minimum thickness > 50 nm |
| **High hydrogen content** | Low temperature, high SiH4 flow | Increase temperature; reduce SiH4 flow; post-anneal |
| **Poor step coverage** | Conformal deposition limited by geometry | TEOS-based SiO2 has better step coverage than SiH4-based; use HDP-CVD for gap fill |
| **Film cracking** | Excessive tensile stress; thick film | Adjust power/pressure for low stress; use multilayer approach for thick films |
| **Non-uniformity** | Gas distribution issues; showerhead clogging | Clean showerhead; verify gas flow pattern; optimize electrode spacing |

---
---

# CLUSTER 4: ATOMIC LAYER DEPOSITION (ALD)

## 4.1 Process Flow Poster Data

### What Is ALD?

Atomic Layer Deposition is a special variant of CVD that uses **sequential, self-limiting surface reactions** to deposit films one atomic layer at a time. Unlike CVD where all precursors are present simultaneously, ALD alternates between two (or more) precursor pulses, separated by purge steps.

**The ALD cycle (for Al2O3 as the canonical example):**
1. **Pulse A**: Trimethylaluminum (TMA, Al(CH3)3) vapor enters chamber; reacts with surface -OH groups; self-limiting (stops when all -OH sites are consumed)
2. **Purge**: Inert gas (N2 or Ar) removes excess TMA and byproducts (CH4)
3. **Pulse B**: Water (H2O) vapor enters chamber; reacts with surface -Al(CH3)x groups; regenerates -OH surface; self-limiting
4. **Purge**: Inert gas removes excess H2O and byproducts (CH4)
5. **Repeat**: Each cycle deposits ~0.1 nm (1 Angstrom) of Al2O3

**Key defining features of ALD:**
- **Self-limiting**: Film thickness determined only by number of cycles, not by exposure time or flux (once surface is saturated)
- **Atomic-level thickness control**: +/- 0.1 nm precision
- **100% conformal**: Coats inside high-aspect-ratio features (trenches, vias, pores) uniformly — impossible with PVD or most CVD
- **Pinhole-free**: Self-limiting nature eliminates pinholes at practical thicknesses (> 5-10 nm)

### Key Industries and Applications

| Industry | Application | Film |
|----------|------------|------|
| Semiconductor (dominant) | High-k gate dielectric, DRAM capacitor dielectric, diffusion barrier, spacer, passivation | HfO2, Al2O3, ZrO2, TiN, TaN, WN, SiO2 |
| Solar | Al2O3 passivation on PERC cells | Al2O3 (10-20 nm) |
| MEMS | Conformal coating of 3D microstructures | Al2O3, TiO2, ZnO |
| Optical | Precision optical filters, AR coatings | TiO2, SiO2, Al2O3 |
| Corrosion protection | Ultra-thin barrier on metals, jewelry, cultural artifacts | Al2O3 (5-50 nm) |
| Biomedical | Biocompatible coatings on implants, nanoparticle functionalization | TiO2, Al2O3, ZnO |
| Energy storage | Coating Li-ion battery electrode materials to improve cycle life | Al2O3 (1-5 nm on cathode particles) |
| Catalysis | Precise catalyst layer thickness on support structures | Pt, Pd, Ir (noble metal ALD) |

### Substrate Compatibility

Virtually unlimited — ALD works on any substrate that has surface functional groups for the precursor to react with:
- Silicon wafers, metals, polymers, textiles, powders, nanoparticles, porous materials, biological specimens
- Temperature limit of substrate is the main constraint (50-400 deg C range available depending on precursor chemistry)

### Film Properties

| Film | Growth per Cycle (GPC) | Typical Thickness | ALD Temp Window | Dielectric Constant |
|------|----------------------|-------------------|-----------------|---------------------|
| Al2O3 | 0.1-0.12 nm/cycle | 1-100 nm | 100-400 deg C | 7-9 |
| HfO2 | 0.1 nm/cycle | 1-30 nm | 200-350 deg C | 16-25 |
| TiO2 | 0.05-0.08 nm/cycle | 1-100 nm | 150-350 deg C | 40-80 (depends on crystallinity) |
| ZrO2 | 0.1 nm/cycle | 1-30 nm | 200-350 deg C | 20-40 |
| ZnO | 0.15-0.2 nm/cycle | 1-200 nm | 100-250 deg C | 8-9 |
| TiN | 0.04-0.06 nm/cycle | 1-30 nm | 250-400 deg C | — (conductor) |
| SiO2 | 0.1-0.15 nm/cycle (plasma-ALD) | 1-100 nm | 50-400 deg C | 3.9-4.5 |
| Pt | 0.05 nm/cycle | 1-50 nm | 250-350 deg C | — (conductor) |

### 10-Step Process Sequence

1. **Substrate preparation** — Clean per application requirements (RCA clean for Si wafers; plasma clean for industrial)
2. **Loading** — Place substrates in ALD reactor (single-wafer for semiconductor; batch for solar/industrial)
3. **Pumpdown** — Evacuate to base pressure (0.1-10 Torr depending on system; some ALD is near atmospheric)
4. **Heat to ALD temperature** — Stabilize at setpoint within "ALD window" (temperature range where GPC is constant)
5. **Thermal stabilization** — Hold for 5-15 min to ensure uniform substrate temperature
6. **ALD cycling** — Execute N cycles of: Precursor A pulse > Purge > Precursor B pulse > Purge
7. **In-situ monitoring** — Ellipsometry or QCM tracks film growth in real time
8. **Final purge** — Extended purge to remove all precursor residues
9. **Cooldown** — Cool under vacuum or inert atmosphere
10. **Unload and characterize** — Thickness (ellipsometry), composition (XPS), conformality (SEM cross-section)

---

## 4.2 Safety & PPE

### Hazards Specific to ALD

| Hazard | Source | Severity |
|--------|--------|----------|
| **TMA (trimethylaluminum)** | Al2O3 precursor; pyrophoric liquid (ignites spontaneously in air); reacts violently with water | Severe burns; fire; OSHA PEL 2 mg/m3 (as Al) |
| **Other metalorganic precursors** | TDMAT, TEMAH, DEZ — flammable to pyrophoric | Fire; inhalation hazard; skin/eye irritation |
| **Ozone (O3)** | Used as oxidant in some ALD processes (thermal ALD of SiO2) | Toxic: OSHA PEL 0.1 ppm TWA; strong oxidizer |
| **Hydrogen peroxide** | Used as oxidant | Oxidizer; corrosive |
| **Vacuum and electrical** | Same as other vacuum processes | Same as PVD/PECVD |
| **Plasma** | Plasma-enhanced ALD (PEALD) uses RF plasma for co-reactant step | RF exposure; same as PECVD |

### Required PPE

- **TMA handling**: Inert atmosphere glove box (Ar or N2) for cylinder changes; full face shield; flame-resistant clothing; leather gloves over chemical-resistant inner gloves; SCBA available for emergency
- **General**: Chemical splash goggles; nitrile gloves; lab coat; fume hood for precursor storage
- **Gas monitoring**: O3 detector if ozone is used (alarm at 0.05 ppm)

### Emergency: TMA Release

- TMA ignites on contact with air — dense white smoke of Al2O3 forms immediately
- **Do NOT use water** on TMA fire — violent exothermic reaction
- Use dry sand, dry chemical (Class D) extinguisher, or vermiculite
- Evacuate area; use SCBA for response
- Small spill: smother with dry sand; large spill: evacuate and call HAZMAT

---

## 4.3-4.4 Part Preparation and Cleaning

### Surface Preparation

- **Semiconductor**: RCA clean or equivalent; dilute HF dip for native oxide removal (if bare Si surface needed) or intentional native oxide retention (if oxide surface provides initial -OH groups for ALD nucleation)
- **Metals**: Ultrasonic clean; may use UV-ozone treatment (5-30 min) to create uniform oxide/hydroxyl surface
- **Polymers**: O2 plasma treatment (1-5 min at 50-200 W) to functionalize surface with -OH groups; critical for ALD nucleation on hydrophobic polymer surfaces
- **Powders/particles**: Fluidized-bed ALD or rotary reactor; no traditional wet cleaning; may use thermal desorption

### Why Cleanliness Matters for ALD

- ALD nucleation requires specific surface functional groups (-OH, -NH2, etc.); contamination blocks these sites
- However, ALD is more forgiving of particulate contamination than PVD because it is not line-of-sight — it conformally coats around particles
- Carbon contamination can block nucleation, resulting in islands instead of continuous film

---

## 4.5-4.6 Equipment and Parameters

### Reactor Types

| Type | Description | Throughput | Application |
|------|-------------|-----------|-------------|
| **Cross-flow (viscous flow)** | Precursor gas flows across substrate surface | Low-medium | R&D, semiconductor single-wafer |
| **Showerhead** | Gas distributed through perforated plate above substrate | Medium | Production semiconductor |
| **Batch (vertical furnace)** | 50-150 wafers stacked vertically; precursors flow between wafers | High | Solar cell Al2O3 passivation |
| **Spatial ALD** | Substrate moves through spatially separated precursor zones (instead of time-separated pulses) | Very high (inline) | Solar, display, flexible electronics |
| **Rotary/fluidized bed** | Particles tumbled or fluidized; precursors flow through | Batch (kg-scale) | Powder coating, battery materials, catalysts |
| **Roll-to-roll** | Continuous web moves through spatial ALD zones | Continuous | Flexible barriers |

### Typical Cycle Parameters (Al2O3 from TMA + H2O)

| Parameter | Value |
|-----------|-------|
| TMA pulse time | 0.015-0.2 sec (self-limiting; short pulse sufficient) |
| TMA dose pressure | 0.1-1 Torr pulse |
| Purge time after TMA | 5-30 sec (longer for high-aspect-ratio structures) |
| H2O pulse time | 0.015-0.2 sec |
| Purge time after H2O | 5-30 sec |
| Substrate temperature | 150-300 deg C (within ALD window) |
| Growth per cycle | 0.11 nm at 200 deg C |
| Cycle time | ~15-60 sec per cycle (thermal ALD) |
| Cycles for 10 nm film | ~90-100 cycles |
| Total time for 10 nm | ~25-100 min depending on purge times |

### The ALD Temperature Window

- **Below window**: Precursor condenses on surface (physisorption, not self-limiting); or reaction is too slow (incomplete surface reaction)
- **Within window**: GPC is constant; self-limiting behavior confirmed
- **Above window**: Precursor decomposes in gas phase (CVD-like, non-self-limiting); or desorbs before reacting
- Example for TMA/H2O: ALD window approximately 150-350 deg C; GPC ~0.11 nm/cycle throughout this range

---

## 4.7-4.8 Deposition, Post-Treatment, Inspection

### Layer-by-Layer Growth

This is ALD's defining feature and what makes it unique among all deposition methods. Every cycle deposits exactly one (sub-)monolayer because:
- Once all available surface sites have reacted with Precursor A, no more adsorption occurs (self-terminating)
- The purge removes all unreacted precursor, preventing CVD-like continuous deposition
- Precursor B then reacts only with the new surface created by A, again self-terminating

**Implication**: Thickness is digitally controlled by cycle count. 100 cycles of TMA/H2O at 200 deg C = 11.0 +/- 0.5 nm Al2O3, regardless of reactor geometry, gas flow pattern, or substrate shape. This is what enables conformal coating of 3D features.

### Thickness Monitoring

| Method | Type | Notes |
|--------|------|-------|
| **In-situ spectroscopic ellipsometry** | Real-time | Gold standard; measures thickness + optical constants every cycle |
| **QCM (quartz crystal microbalance)** | Real-time | Measures mass gain per cycle; QCM sensor inside chamber |
| **Ex-situ ellipsometry** | Post-deposition | Standard characterization; +/- 0.1 nm accuracy on flat substrates |
| **XRR (X-ray reflectivity)** | Post-deposition | Thickness + density + roughness; excellent for ultra-thin films |
| **TEM cross-section** | Post-deposition | Direct imaging of film on 3D structures; confirms conformality |

### Quality Metrics

- **Growth per cycle (GPC)**: Should match literature value for given precursor/temperature; deviation indicates precursor delivery problem, surface contamination, or temperature drift
- **Non-uniformity**: < 1% across wafer for semiconductor; measure at 49 or more points by ellipsometry mapping
- **Conformality (step coverage)**: Film thickness at bottom of trench / thickness at top; target > 95% for ALD; measured by TEM or SEM cross-section of test structures
- **Impurity content**: XPS or SIMS — carbon content < 2 at% for good-quality Al2O3 at > 200 deg C; higher carbon indicates insufficient purging or low temperature

### Common Defects

| Defect | Cause | Prevention |
|--------|-------|------------|
| **Non-self-limiting growth** | Insufficient purge (precursor overlap = CVD); temperature outside window | Increase purge time; verify temperature calibration |
| **Island growth / incomplete nucleation** | Surface lacking functional groups; contamination | Surface functionalization; proper cleaning |
| **Thickness non-uniformity** | Temperature gradients; gas depletion in batch reactor | Improve temperature control; optimize gas distribution |
| **High carbon contamination** | Low deposition temp (< 150 deg C); short purge times | Increase temp or use plasma-ALD (O2 plasma co-reactant) |
| **Crystallization (unwanted)** | HfO2, ZrO2 crystallize during deposition at higher temps | Control temperature; use laminate approach (HfO2/Al2O3 nanolaminates) |

---
---

# CLUSTER 5: DIAMOND-LIKE CARBON (DLC) COATINGS

## 5.1 Process Flow Poster Data

### What Is DLC?

Diamond-Like Carbon is a metastable form of amorphous carbon containing a significant fraction of sp3 (diamond-like) carbon bonds mixed with sp2 (graphite-like) bonds. The sp3 content determines the properties: more sp3 = harder, more transparent, more diamond-like.

**DLC Classification (per VDI 2840 standard):**

| DLC Type | Full Name | sp3 Content | Hydrogen | Hardness (GPa) | Deposition Method |
|----------|-----------|-------------|----------|----------------|-------------------|
| **a-C:H** | Hydrogenated amorphous carbon | 30-40% | 20-40 at% | 10-20 | PECVD (hydrocarbon gas) |
| **a-C:H:Me** | Metal-containing a-C:H | 20-40% | 15-30 at% | 5-15 | Reactive sputtering + PECVD |
| **ta-C:H** | Tetrahedral a-C:H (hard) | 40-60% | 15-30 at% | 20-40 | High-density plasma CVD |
| **a-C** | Hydrogen-free amorphous carbon | 5-20% sp3 | < 1 at% | 10-20 | Sputtering (graphite target) |
| **ta-C** | Tetrahedral amorphous carbon | 50-80% | < 1 at% | 40-80 | Filtered cathodic arc; PLD |

### Mechanism

- **PECVD-DLC (a-C:H)**: Hydrocarbon gas (CH4, C2H2, C6H6) is dissociated in an RF or DC plasma; carbon-containing radicals and ions deposit on the substrate; ion bombardment energy determines sp3/sp2 ratio
- **Sputtering-DLC (a-C)**: Graphite target sputtered with Ar; energetic C atoms form metastable sp3 bonds
- **Filtered cathodic arc (ta-C)**: Carbon cathode arc; macroparticle filter removes droplets; highly ionized C+ plasma produces very high sp3 content; hardest DLC variant

### Key Industries and Applications

| Industry | Application | DLC Type |
|----------|------------|----------|
| Automotive | Piston rings, valve train components (tappets, lifters), fuel injectors, gears | a-C:H, a-C:H:Me (W-DLC, Si-DLC), ta-C |
| Cutting tools | Machining non-ferrous metals (Al, Cu, plastics) | ta-C |
| Biomedical | Orthopedic implants, cardiovascular stents, surgical blades | a-C:H, ta-C |
| Optics | IR windows, protective coatings on germanium lenses | a-C:H (transparent in IR) |
| Magnetic storage | Hard drive read/write head overcoat | ta-C (2-5 nm) |
| Razor blades | Edge coating | a-C:H |
| Decorative | Watch cases, jewelry (black color) | a-C:H, a-C |
| Mold/die | Plastic injection molds (anti-stick) | a-C:H, Si-DLC |

### Substrate Compatibility

- **Steel**: Excellent; requires adhesion interlayer (Cr, CrN, or Si-containing gradient)
- **Cemented carbide**: Good for non-ferrous machining tools
- **Aluminum/titanium**: Good with proper interlayer
- **Polymers**: Low-temp DLC (< 100 deg C) possible via PECVD
- **Limitation**: DLC coatings on steel parts that operate above 300-400 deg C will graphitize (sp3 converts to sp2) and lose hardness

### Coating Properties

| Property | a-C:H | ta-C | Comparison to Diamond |
|----------|-------|------|----------------------|
| Hardness | 10-20 GPa | 40-80 GPa | Diamond: 80-100 GPa |
| Friction coefficient (dry) | 0.05-0.15 | 0.05-0.15 | Diamond: 0.05-0.1 |
| Friction (lubricated) | 0.02-0.08 | 0.02-0.08 | — |
| Young's modulus | 100-200 GPa | 300-700 GPa | Diamond: 1,000 GPa |
| Internal stress | 1-3 GPa (compressive) | 5-12 GPa (compressive) | — |
| Max service temp | 300-400 deg C | 500-600 deg C | Graphitizes in air > 600 deg C |
| Optical band gap | 1.0-2.5 eV | 2.0-3.5 eV | Diamond: 5.5 eV |
| Typical thickness | 1-5 um | 0.5-3 um | — |

### 10-Step Process Sequence

1. **Part inspection** — Verify substrate material, dimensions, surface condition
2. **Pre-cleaning** — Ultrasonic alkaline wash > DI rinse > IPA > dry (same as PVD)
3. **Fixturing** — Mount on rotation fixtures; ensure electrical contact for bias
4. **Load and pumpdown** — Base pressure < 5 x 10^-5 mbar
5. **Heating (optional)** — Substrate heating to 100-200 deg C (some processes are ambient)
6. **Ion etching** — Ar+ ion bombardment to clean substrate surface in vacuum
7. **Adhesion interlayer deposition** — Cr or Si by sputtering (50-300 nm); then gradient layer (CrN, CrC, or Si-C) transitioning to DLC composition
8. **DLC deposition** — PECVD from C2H2 or CH4; or sputtering from graphite target; or filtered arc from graphite cathode
9. **Cooldown under vacuum** — Cool below 100 deg C before venting
10. **Unload, inspect** — Color check (should be smooth, dark, reflective); adhesion test; thickness measurement

---

## 5.2 Safety & PPE

### Hazards

| Hazard | Source |
|--------|--------|
| **Acetylene (C2H2)** | Primary DLC precursor for PECVD; explosive (LEL 2.5%, UEL 81%); can decompose explosively without oxygen above 15 psig |
| **Methane (CH4)** | Alternative precursor; flammable (LEL 5%) |
| **High voltage bias** | Substrate bias -500 to -2000 V for some DLC processes |
| **Graphite dust** | From target/cathode handling; inhalation hazard |
| **All PVD hazards** | Vacuum, electrical, high temp apply |

### PPE

- Standard PVD PPE (see Cluster 1)
- **C2H2 handling**: No copper or copper alloy fittings (forms explosive copper acetylide); flash arrestors on all acetylene lines; continuous combustible gas monitoring
- **Graphite handling**: N95 respirator; carbon dust is a nuisance dust (OSHA PEL 15 mg/m3 total, 5 mg/m3 respirable) but can be slippery on floors

---

## 5.3-5.8 Part Preparation Through Inspection

### Adhesion: The Critical Challenge for DLC

DLC's extremely high compressive internal stress (1-12 GPa) makes adhesion the primary challenge. Without a proper interlayer system, DLC will spontaneously delaminate from most substrates.

**Standard interlayer architectures:**
- **Cr/CrN/CrC gradient**: Cr (50-100 nm) > CrN (100-300 nm) > CrCN (100-200 nm) > CrC (100-200 nm) > DLC; gradually transitions from metallic to carbon-based
- **Si gradient (for Si-DLC)**: Si (50-100 nm) > SiC:H gradient > a-C:H:Si > a-C:H
- **W-DLC (a-C:H:W)**: W sputtered simultaneously with DLC deposition; W-C nanocomposite provides inherent adhesion to steel
- **Direct ion bombardment**: For ta-C on WC-Co, very high bias during first few nm creates mixed interface (subplantation); no separate interlayer needed

### Surface Finish Requirements

- Ra < 0.05 um (2 uin) preferred for low-friction applications (piston rings, bearings)
- DLC replicates substrate surface exactly — any polishing must be done before coating
- For mold applications: mirror polish (Ra < 0.02 um) required

### Thickness Measurement

- **Calotest**: Standard for 0.5-5 um DLC; DLC appears as dark ring against light interlayer
- **Profilometry**: Step height over masked area
- **XRF**: Difficult for carbon films (low atomic number); not commonly used
- **Ellipsometry**: Works for transparent a-C:H on flat substrates
- **Cross-section SEM/TEM**: Definitive measurement; reveals individual layers

### Quality Testing

- **Rockwell indentation (VDI 3198)**: HF1-HF2 acceptable; DLC's high stress makes HF3-4 common — often acceptable depending on application
- **Scratch test**: Lc1 (first cohesive failure) and Lc2 (adhesive failure) reported; Lc2 > 10-30 N typical for good DLC adhesion
- **Ball-on-disc tribometry**: Measures actual friction coefficient; critical QC test
- **Raman spectroscopy**: Non-destructive; D peak (~1350 cm-1) and G peak (~1580 cm-1) ratio indicates sp3/sp2 content; ID/IG ratio and peak positions characterize DLC quality
- **Nanoindentation**: Measures hardness and modulus of thin DLC films; ISO 14577

### Common Defects

| Defect | Cause | Prevention |
|--------|-------|------------|
| **Delamination** | Inadequate interlayer; too-thick DLC; excessive stress | Proper gradient interlayer; limit thickness (< 3 um for ta-C, < 5 um for a-C:H) |
| **High friction** | Graphitic (sp2-rich) film; humidity sensitivity (hydrogen-free DLC) | Optimize deposition parameters; use a-C:H in humid environments (H provides low friction via surface passivation) |
| **Haze / cloudy appearance** | Gas-phase polymerization (PECVD at too-high pressure) | Reduce pressure; increase bias energy |
| **Soft coating** | Insufficient ion energy; too much hydrogen | Increase bias voltage; reduce hydrogen-containing gas fraction |
| **Pitting / pinholes** | Macroparticles (cathodic arc); particulate contamination | Filtered arc; cleanroom handling |
| **Color variation** | Thickness variation; compositional variation | Optimize rotation and gas flow uniformity |

---
---

# CLUSTER 6: ION IMPLANTATION

## 6.1 Process Flow Poster Data

### What Is Ion Implantation?

Ion implantation is a process in which energetic ions are accelerated and directed into a solid substrate surface, embedding themselves within the near-surface region (typically 10-500 nm depth). Unlike deposition processes (PVD, CVD, ALD) that add material on top of the surface, ion implantation **modifies the existing surface** by introducing foreign atoms into the crystal lattice.

**Mechanism:**
1. Ion source generates ions of the desired species (N+, C+, B+, P+, As+, Cr+, Ti+, etc.)
2. Ions are extracted, mass-separated (magnetic mass analyzer selects desired species), and accelerated to energies of 10 keV to 10 MeV
3. Ion beam is scanned across the substrate surface (electrostatic or mechanical scanning)
4. Ions penetrate the surface and come to rest at a depth determined by their energy and the substrate density (projected range, Rp)
5. The implanted ions modify surface composition, crystal structure, and properties (hardness, wear resistance, corrosion resistance, electrical conductivity)

**Not a coating** — no measurable thickness is added. The surface composition is changed at the atomic level.

### Key Industries and Applications

| Industry | Application | Ion Species | Effect |
|----------|------------|-------------|--------|
| **Semiconductor** (dominant) | Doping Si for transistors (source/drain, well implants) | B+, P+, As+, BF2+ | Controlled p-type or n-type conductivity |
| Cutting tools | Nitrogen implantation of HSS/WC tools | N+ | Increased surface hardness, wear resistance |
| Medical implants | Ti-6Al-4V hip/knee implants | N+, C+ | Reduced wear, improved biocompatibility |
| Bearings | Steel bearing races | N+, C+ | Wear resistance, fatigue life improvement |
| Aerospace | Turbine blade erosion resistance | N+, Cr+ | Surface hardening |
| Automotive | Piston rings, gears | N+, C+ | Wear reduction |
| Optics | Modifying refractive index of glass | Ag+, He+ | Waveguide formation |

### Substrate Compatibility

- Virtually any solid material: metals, ceramics, semiconductors, polymers (low energy only)
- No temperature limitation on the process itself (substrate can be cooled or heated independently)
- No adhesion issues — implanted atoms are part of the substrate lattice

### Treatment Properties

| Property | Before Implantation | After N+ Implantation (Steel) |
|----------|-------------------|------------------------------|
| Surface hardness | 800-1000 HV (tool steel) | 1,200-1,800 HV (50-100% increase) |
| Wear rate | Baseline | 2x-10x reduction |
| Friction coefficient | 0.5-0.7 (dry steel-on-steel) | 0.2-0.4 |
| Corrosion resistance | Baseline | Improved (nitrogen stabilizes passive film on stainless steel) |
| Fatigue life | Baseline | 2x-5x improvement (compressive residual stress) |
| Modified zone depth | — | 50-500 nm |

### Semiconductor Implantation Parameters

| Parameter | Typical Range |
|-----------|--------------|
| Ion species | B (p-type), P (n-type), As (n-type), BF2 |
| Energy | 0.2-200 keV (low energy for shallow junctions; high energy for wells) |
| Dose | 10^11 to 10^16 ions/cm2 |
| Beam current | 0.1-30 mA |
| Wafer temperature | Ambient to 500 deg C (high-temp implant for some processes) |
| Rp (projected range) in Si | B at 50 keV: ~170 nm; P at 100 keV: ~130 nm; As at 100 keV: ~50 nm |

### 10-Step Process Sequence

1. **Substrate inspection** — Verify material, dimensions, surface condition
2. **Cleaning** — Standard for application (RCA for semiconductor; ultrasonic for industrial)
3. **Masking (if needed)** — Photoresist (semiconductor) or metal masks (industrial) to define implant area
4. **Loading** — Place parts in vacuum chamber on cooled/heated platen; ensure good thermal contact
5. **Pumpdown** — Base pressure 10^-5 to 10^-6 Torr
6. **Ion source startup** — Ignite ion source; tune mass separator to select desired species; verify beam purity
7. **Beam tuning** — Set energy, beam current, and scan pattern; use Faraday cup to measure beam current and dose
8. **Implantation** — Beam scans across substrate surface; dose integrator counts total ions delivered
9. **Anneal (semiconductor)** — Rapid thermal anneal (RTA) at 900-1100 deg C for 5-60 sec to repair lattice damage and activate dopants
10. **Characterize** — SIMS depth profile to verify dopant distribution; sheet resistance measurement (4-point probe); for industrial: hardness testing, wear testing

---

## 6.2 Safety & PPE

### Hazards Specific to Ion Implantation

| Hazard | Source | Severity |
|--------|--------|----------|
| **Extremely high voltage** | Accelerating voltages 10 kV to 10 MV (MeV implants); stored energy in terminal | Lethal electrocution — this is one of the most dangerous pieces of equipment in a semiconductor fab |
| **X-rays** | Bremsstrahlung radiation generated when energetic ions/electrons strike metal surfaces | Radiation exposure; systems require lead shielding and interlock surveys |
| **Toxic source gases** | BF3 (boron source: toxic, OSHA PEL 1 ppm ceiling), AsH3 (arsine: extremely toxic, OSHA PEL 0.05 ppm), PH3 (phosphine: extremely toxic, OSHA PEL 0.3 ppm) | AsH3 is one of the most toxic industrial gases; IDLH 3 ppm; colorless |
| **Activated materials** | At MeV energies, neutron activation of chamber components is possible | Residual radioactivity; requires radiation survey |
| **Vacuum/mechanical** | Large vacuum chambers, heavy parts | Standard vacuum hazards |

### Required PPE and Controls

- **Multi-level interlock system**: Personnel interlocks on all access doors; beam off before door opens; high-voltage discharge and ground verification before maintenance entry
- **Radiation monitoring**: TLD (thermoluminescent dosimeter) badges for operators; area radiation monitors; annual X-ray survey
- **Toxic gas monitoring**: Continuous AsH3, PH3, BF3 monitors in tool area; alarm at 0.005 ppm AsH3 (10% of PEL); emergency SCBA available
- **Gas cabinets**: All toxic source gases in gas cabinets with automatic shutoff, exhaust, and scrubbing
- **Lockout/Tagout**: Critical — ion implanters have multiple lethal energy sources (high voltage, stored charge, compressed gas, moving parts)

### Emergency: AsH3 Exposure

- Arsine causes massive hemolysis (destruction of red blood cells); symptoms may be delayed 2-24 hours
- Any suspected exposure: evacuate; administer oxygen; transport to hospital immediately
- Threshold for concern: any detectable exposure above 0.01 ppm warrants medical evaluation

---

## 6.3-6.4 Part Preparation and Cleaning

### Semiconductor

- Standard fab cleaning (RCA or equivalent)
- Screen oxide may be grown on Si wafers before implant (10-20 nm SiO2) to prevent channeling (ions traveling along crystal planes to anomalous depth)
- Photoresist mask: 0.5-5 um thick; must be thick enough to stop ions at the implant energy used (stopping range in resist must be < resist thickness)

### Industrial

- Parts must be clean and free of surface contamination that would scatter or stop ions before reaching the metal surface
- Surface finish: Ra < 0.4 um preferred; ion implantation does not change surface finish (no material added)

---

## 6.5-6.8 Equipment, Parameters, Treatment, and Inspection

### Equipment Architecture

**Semiconductor ion implanter components (beam-line type):**
1. **Ion source**: Gas/solid vaporizer + plasma chamber (Freeman, Bernas, or IHC source); produces ions
2. **Extraction**: 10-80 kV extraction electrode pulls ions from source
3. **Mass analyzer**: 90-degree or 70-degree analyzing magnet; resolves ion species by mass-to-charge ratio (e.g., separates B-11 from B-10, BF2 from BF)
4. **Acceleration/deceleration**: Post-analysis acceleration column or decel stage for energy control
5. **Beam scanning**: Electrostatic x-y scan (or hybrid electrostatic + mechanical scan); ensures uniform dose across wafer
6. **Process chamber**: Wafer handling under vacuum; may include heating/cooling stage
7. **Faraday system**: Measures beam current and integrates total dose; critical for dose accuracy

### Dose Control

- **Faraday cup**: Absolutely calibrated charge collector; dose = (beam current x time) / (charge per ion x implant area)
- Accuracy requirement: +/- 1-2% dose uniformity across wafer; +/- 1-3% wafer-to-wafer
- **4-point probe**: Post-implant sheet resistance measurement; rapid feedback on dose and annealing

### Annealing (Semiconductor)

| Method | Temperature | Time | Application |
|--------|-------------|------|-------------|
| Rapid Thermal Anneal (RTA) | 900-1100 deg C | 5-60 sec | Standard activation |
| Spike anneal | 1050-1100 deg C | < 1 sec peak | Ultra-shallow junctions |
| Flash anneal | 1100-1350 deg C | 1-5 ms | Advanced nodes |
| Laser anneal | 1200-1400 deg C | microseconds | Localized activation |
| Furnace anneal | 800-1000 deg C | 15-60 min | Legacy; deep implants |

### Characterization Methods

| Method | What It Measures |
|--------|-----------------|
| **SIMS (Secondary Ion Mass Spectrometry)** | Depth profile of implanted species; gold standard for dose and depth verification |
| **4-point probe (sheet resistance)** | Electrical activation of dopant; quick inline measurement |
| **Spreading resistance profiling (SRP)** | Carrier concentration vs. depth |
| **Nanoindentation** | Surface hardness (industrial applications) |
| **Pin-on-disc wear test** | Wear rate and friction coefficient (industrial) |

### Common Issues

| Issue | Cause | Prevention |
|-------|-------|------------|
| **Dose non-uniformity** | Beam scan non-linearity; Faraday cup error | Calibrate scan; verify Faraday cup with external standard |
| **Channeling** | Ions aligned with crystal lattice planes penetrate deeper than expected | Tilt wafer 7 deg off-axis; use screen oxide; implant through amorphous layer |
| **Lattice damage** | Implanted ions displace substrate atoms (knock-on damage) | Planned: damage repaired by anneal; control implant temperature to prevent amorphization (or intentional pre-amorphization implant) |
| **Sputtering** | Surface atoms ejected by incoming ions (yield depends on energy and species) | Acceptable at normal doses; at very high doses (> 10^17/cm2), surface erosion is significant |
| **Charging** | Insulating substrates/masks accumulate charge; beam deflected | Use electron flood gun (charge neutralization); plasma immersion implantation (PIII) for complex parts |

---
---

# CLUSTER 7: ELECTROPOLISHING

## 7.1 Process Flow Poster Data

### What Is Electropolishing?

Electropolishing is an electrochemical process that selectively dissolves metal from the surface of a workpiece, preferentially removing peaks and high points to produce a smooth, bright, passivated surface. It is the reverse of electroplating — the workpiece is the **anode** (positive electrode) and metal ions are removed into the electrolyte.

**Mechanism:**
1. Part is immersed in an electrolyte (typically phosphoric/sulfuric acid blend) and connected as the anode
2. Direct current applied; metal dissolves anodically: M -> M^n+ + ne^-
3. A viscous film (anodic film, rich in dissolved metal salts and reaction products) forms on the surface
4. This viscous layer is thicker in valleys (recesses) and thinner on peaks (protrusions)
5. Because the diffusion layer is thinner over peaks, dissolution rate is higher at peaks than valleys
6. Result: surface roughness decreases; peaks are leveled; bright, reflective finish produced
7. Simultaneously, chromium and/or nickel are enriched at the surface (selective dissolution of iron from stainless steel), improving the Cr:Fe ratio and corrosion resistance

### Key Industries and Applications

| Industry | Application | Benefit |
|----------|------------|---------|
| Pharmaceutical | Vessels, piping, valves, fittings | Ultra-smooth surface (Ra < 0.4 um / 16 uin); easy to clean; reduces biofilm adhesion |
| Food & beverage | Process equipment, tanks, mixers | Sanitary finish; corrosion resistance; FDA/3A compliance |
| Semiconductor | Gas delivery systems, ultra-pure water piping | Ultra-clean surface; reduces particle generation; outgassing reduction |
| Medical devices | Surgical instruments, implants, stents | Smooth, burr-free, biocompatible surface; passive layer |
| Aerospace | Turbine blades, hydraulic components | Fatigue life improvement; stress-free surface; corrosion resistance |
| Nuclear | Decontamination, piping | Smooth surface resists contamination pickup |
| Decorative | Jewelry, architectural stainless | Mirror finish |

### Substrates

- **Stainless steel**: 300 series (304, 316, 316L) — dominant application; 400 series possible but results less consistent
- **Carbon steel**: Possible but less common; requires careful control
- **Aluminum**: Different electrolyte required (perchloric acid or phosphoric/chromic acid blends)
- **Copper and copper alloys**: Phosphoric acid based electrolytes
- **Titanium**: Specialized electrolytes (H2SO4/HF, methanol-based)
- **Nickel and cobalt alloys (Inconel, Hastelloy)**: Modified phosphoric/sulfuric acid; challenging

### Surface Properties Produced

| Property | Before EP | After EP |
|----------|----------|---------|
| Surface roughness (Ra) | 0.8-1.6 um (32-63 uin) typical machined | 0.2-0.4 um (8-16 uin) typical; < 0.1 um (4 uin) achievable |
| Surface finish | Dull, matte, machining marks visible | Mirror-bright, highly reflective |
| Cr:Fe ratio (316 SS) | ~1.5:1 to 2:1 (native passive film) | 3:1 to 5:1 (enhanced passive film) |
| Passivation | Native oxide, variable | Enhanced, uniform passive oxide layer |
| Micro-burrs | Present after machining/grinding | Removed |
| Surface area | Higher (rough surface) | Reduced 20-50% (smoother = less surface area) |

### 10-Step Process Sequence

1. **Incoming inspection** — Verify material (alloy grade critical for recipe selection), dimensions, surface condition
2. **Pre-cleaning** — Alkaline soak clean or ultrasonic clean to remove oils, grease, shop soil
3. **Rinse** — Hot DI water rinse
4. **Rack/fixture** — Connect part to bus bar as anode; titanium or copper contact points; ensure good electrical contact
5. **Electropolish** — Immerse in electrolyte; apply current; maintain temperature; time per recipe (typically 2-20 min)
6. **Rinse** — Drag-out rinse (collect spent electrolyte); then flowing water rinse
7. **Post-treatment (optional)** — Citric acid passivation (per ASTM A967) or nitric acid passivation (per ASTM A380/A967) to further enhance passive layer
8. **Final rinse** — DI water cascade rinse
9. **Dry** — Hot air dry or clean compressed air; no water spots
10. **Inspect and document** — Visual inspection (brightness, uniformity); Ra measurement (profilometer); document per quality requirements

---

## 7.2 Safety & PPE

### Hazards

| Hazard | Source | Severity |
|--------|--------|----------|
| **Concentrated acids** | H3PO4 (75-85% w/w) + H2SO4 (10-25% w/w); bath operates at 50-80 deg C; highly corrosive | Chemical burns — severe; splash to eyes can cause blindness |
| **Hydrogen gas** | Evolved at cathode; explosive at > 4% in air | Fire/explosion risk; ventilation critical |
| **Metal fumes/mist** | Acid mist from hot bath surface; dissolved metals (Cr, Ni, Fe) | Inhalation of Cr(VI) if present; acid irritation |
| **Electrical** | DC power supply: 5-18 V, 100-10,000+ A depending on part size | Electrocution (amperage is lethal); arc flash at bus bar connections |
| **Thermal** | Bath at 50-80 deg C; parts emerge hot | Burns from hot acid splashing |
| **Chromic acid (Al EP)** | Aluminum electropolishing may use CrO3 | Hexavalent chromium — carcinogen; OSHA PEL 5 ug/m3 |
| **Perchloric acid (Al EP)** | Some aluminum EP uses HClO4 | Explosion risk if concentrated perchloric acid contacts organics; dehydrated perchloric acid is a powerful oxidizer |

### Required PPE

- **Full-length chemical-resistant apron** (PVC or rubber)
- **Chemical splash goggles + face shield** (both — goggles alone insufficient for splashes)
- **Acid-resistant gloves** (PVC, neoprene, or butyl rubber; NOT nitrile — too thin for concentrated acid handling)
- **Rubber boots or chemical-resistant shoe covers**
- **Emergency eyewash and safety shower** within 10 seconds of work area (ANSI Z358.1)
- **Ventilation**: Local exhaust at tank lip; 100-150 cfm per linear foot of tank
- **Respiratory**: OSHA may require supplied air or P100 acid gas cartridge if mist concentrations exceed PELs

### Emergency Procedures

- **Acid splash on skin**: Flush with water 15-20 min; remove contaminated clothing; seek medical attention
- **Acid splash in eyes**: Flush with eyewash 15-20 min; do not rub; emergency medical treatment
- **Acid spill**: Dike with absorbent; neutralize with soda ash (Na2CO3) or lime; clean up; do not use sawdust (fire risk with H2SO4)
- **Hydrogen accumulation**: Ventilate immediately; eliminate ignition sources; never weld near electropolishing tanks

---

## 7.3-7.4 Part Preparation and Cleaning

### Pre-Cleaning Requirements

- Parts MUST be free of all oils, grease, wax, paint, markers, tape adhesive
- Organic contamination causes staining, uneven polishing, gas pocketing
- **Alkaline soak clean**: 5-10% alkaline cleaner at 60-75 deg C, 10-30 min; ultrasonic recommended
- **Acid pickle (optional)**: 10-20% H2SO4 or HCl at ambient, 5-10 min; removes heat tint and heavy oxide scale
- **Pre-mechanical finishing**: For best results, surface should be mechanically finished to Ra < 1.6 um (63 uin) before electropolishing; EP typically removes 5-25 um of surface metal per side; it will not remove deep scratches, tool marks, or pits

### Masking

- **Stop-off lacquer**: Acid-resistant lacquer painted on areas not to be polished
- **Plastisol dip coating**: Removable PVC-based coating
- **Tape**: Acid-resistant tape (PTFE or PVC) — limited to short exposure times at low temperatures
- **Wax**: Acid-resistant wax for plugging holes and cavities

---

## 7.5 Equipment / System Setup

### Electrolyte Chemistry

#### Stainless Steel Electropolishing (Most Common)

| Component | Concentration | Purpose |
|-----------|--------------|---------|
| Phosphoric acid (H3PO4, 85%) | 40-70% by volume | Primary acid; forms viscous anodic film |
| Sulfuric acid (H2SO4, 96%) | 15-40% by volume | Increases conductivity; raises limiting current density |
| Water | Balance (typically 5-20%) | Dilution |
| Glycerin or ethylene glycol (some formulations) | 0-10% | Viscosity modifier |

**Typical ready-to-use bath composition:**
- H3PO4: 50-60% v/v
- H2SO4: 20-30% v/v
- Water: 10-30% v/v
- Specific gravity: 1.65-1.80

#### Operating Parameters (Stainless Steel)

| Parameter | Range |
|-----------|-------|
| Temperature | 50-80 deg C (optimal: 55-70 deg C for 300 series SS) |
| Current density | 5-30 A/dm2 (50-300 A/ft2); optimal varies by alloy |
| Voltage | 5-18 V DC (most common: 8-14 V) |
| Time | 2-20 min (typically 5-15 min for standard finish) |
| Agitation | Mild or none — excessive agitation disrupts the viscous anodic film |
| Cathode material | 316 SS, lead, or copper |
| Cathode-to-anode area ratio | > 2:1 preferred |
| Metal content (dissolved Fe, Ni, Cr) | Control below 8-10% by weight total dissolved metals; replace or dilute bath above this level |
| Water content | Maintain 5-15%; excess water (> 20%) causes pitting; too little water (< 5%) causes gas streaks |

#### Aluminum Electropolishing

| Component | Concentration |
|-----------|--------------|
| **Standard (Brytal-type)**: H3PO4 + H2SO4 + CrO3 | 75% H3PO4 + 20% H2SO4 + 5% CrO3 (by weight, approximate) |
| Temperature | 60-90 deg C |
| Current density | 5-20 A/dm2 |
| **Perchloric acid type (lab/research)** | 70% EtOH + 20% 2-butoxyethanol + 10% HClO4 |
| Temperature | -10 to +5 deg C |
| **Warning**: Perchloric acid baths are explosion hazards; industrial use declining |

#### Copper Electropolishing

| Component | Concentration |
|-----------|--------------|
| H3PO4 | 50-75% by volume |
| Temperature | 20-40 deg C |
| Current density | 10-50 A/dm2 |

---

## 7.6-7.8 Parameters, Treatment, and Inspection

### Current-Voltage Relationship

The E-P curve (current density vs. voltage) for electropolishing has four regions:
1. **Etching region** (low voltage): Active dissolution; surface roughens; not useful
2. **Transition region**: Viscous film begins to form
3. **Plateau (polishing) region**: Current is nearly constant despite increasing voltage; this is the electropolishing region — viscous film controls dissolution; peaks dissolve faster than valleys; **operate here**
4. **Gas evolution region** (high voltage): Oxygen evolution begins; pitting and staining; avoid

**Finding the plateau is critical**: Run a voltammetry sweep (slowly increase voltage while measuring current) for each new alloy/electrolyte combination. The plateau is typically at 8-14 V for stainless steel.

### Metal Removal Rate

- Typical removal: 5-25 um per side per 10 min at optimal conditions
- Removal is non-uniform — more metal removed from edges, corners, and thin sections (current concentration)
- For precision parts, account for dimensional change: a part electropolished at 10 A/dm2 for 10 min loses approximately 10-15 um per side (0.0004-0.0006 in per side) on 304 SS

### Thickness and Surface Measurement

| Method | Purpose |
|--------|---------|
| **Profilometer (stylus or optical)** | Ra, Rz surface roughness measurement; most important QC metric |
| **Weight loss** | Calculate average removal depth from weight change and density |
| **Dimensional measurement** | Caliper or CMM to verify dimensional tolerance compliance |
| **Glossmeter** | Quantify reflectivity/gloss |
| **ESCA/XPS** | Surface composition analysis (Cr:Fe ratio, passive layer thickness) — research/high-spec QC |
| **Ferroxyl test** | Tests for free iron on surface (should be negative after EP + passivation) |
| **Copper sulfate test** | Tests for free iron per ASTM A380 |
| **Water-break test** | Verifies cleanliness of electropolished surface |

### Common Defects

| Defect | Cause | Prevention |
|--------|-------|------------|
| **Orange peel** | Over-polishing; grain boundaries preferentially attacked on coarse-grained material | Reduce time; optimize current density; ensure fine grain structure in base metal |
| **Pitting** | Too much water in electrolyte; insufficient current density; contaminant in bath | Maintain water < 15%; increase current density; filter bath |
| **Streaking** | Insufficient water in electrolyte; gas trails from trapped bubbles | Add water; reposition part to allow gas escape |
| **Staining / discoloration** | Operating above the plateau (O2 evolution region); inadequate rinsing | Reduce voltage; improve rinse procedure |
| **Etching (matte finish instead of bright)** | Operating below the plateau; temperature too low; electrolyte too dilute | Increase voltage to plateau region; increase temperature |
| **Selective attack / uneven finish** | Mixed alloys in same load; weld heat-affected zones; inclusions in base metal | Process similar alloys together; grind welds before EP; specify clean base metal |
| **Contact marks** | Rack contact points shield surface from electrolyte | Minimize contact area; reposition and re-run if necessary |
| **Hydrogen embrittlement** | Hydrogen absorption (primarily in high-strength steels and titanium) | Post-bake at 190-220 deg C for 4-24 hours if HE susceptible (per ASTM B850) |

---
---

# CLUSTER 8: ELECTROFORMING

## 8.1 Process Flow Poster Data

### What Is Electroforming?

Electroforming is the production of metal parts by electrodeposition onto a shaped mandrel (form, mold, or master) which is subsequently separated from the deposit. Unlike electroplating (which permanently coats a part), the electroformed shell IS the final product. The mandrel is either reusable (permanent) or sacrificed (dissolved, melted, or mechanically removed).

**Key distinction from electroplating:**
- Electroplating = coating on a permanent substrate
- Electroforming = free-standing metal part made by electrodeposition; mandrel is removed

**Mechanism:** Identical to electroplating — metal ions from solution are reduced at the cathode (mandrel) surface: M^n+ + ne^- -> M. The deposit is built up to the required thickness (typically 25 um to 25 mm), then the mandrel is separated.

### Key Industries and Applications

| Industry | Application | Metal | Typical Thickness |
|----------|------------|-------|-------------------|
| Aerospace/defense | Waveguides, reflectors, radar horns, thrust chambers | Ni, Cu | 0.5-5 mm |
| Printing | Embossing dies, holograms, CD/DVD stampers, banknote printing plates | Ni | 100-500 um |
| Electronics | Precision screens, meshes, shadow masks, lead frames | Ni, Cu | 25-250 um |
| Mold making | Blow mold shells, injection mold inserts, tooling | Ni, Ni-Co | 2-10 mm |
| Optics | Precision reflectors, telescope mirrors (mandrel formed to optical spec then electroformed) | Ni | 0.5-3 mm |
| Musical instruments | Saxophone bells, trumpet bells (rare) | Cu, Ag | 0.5-2 mm |
| Jewelry/art | Complex decorative shapes, sculpture reproduction | Cu, Au, Ag | 0.1-2 mm |
| Micro/nano | LIGA process (lithography + electroforming for microstructures) | Ni | 10-1000 um |

### Bath Chemistry

Electroforming uses the same plating bath chemistries as conventional electroplating:

#### Nickel Electroforming (Most Common)

| Bath Type | Composition | Application |
|-----------|------------|-------------|
| **Nickel sulfamate** | Ni(NH2SO3)2: 300-450 g/L; NiCl2: 5-30 g/L; H3BO3: 30-45 g/L; pH 3.5-4.5; temp 40-55 deg C | Primary electroforming bath; low stress deposit; ductile |
| **Watts nickel** | NiSO4: 225-300 g/L; NiCl2: 37-53 g/L; H3BO3: 30-45 g/L; pH 3.5-4.5; temp 44-66 deg C | Harder deposit; higher stress; used when hardness needed |
| **Nickel-cobalt sulfamate** | Same as sulfamate + CoCl2 (to provide 5-25% Co) | Harder deposits; mold inserts; improved wear resistance |

#### Copper Electroforming

| Bath Type | Composition | Application |
|-----------|------------|-------------|
| **Acid copper sulfate** | CuSO4*5H2O: 180-250 g/L; H2SO4: 45-90 g/L; Cl-: 50-100 mg/L; temp 21-38 deg C | Electrical components; waveguides; heat sinks |
| **Copper pyrophosphate** | Cu2P2O7: 55-85 g/L; K4P2O7: 150-400 g/L; pH 8-9; temp 50-60 deg C | When acid sulfate is not suitable |

#### Other Metals Electroformed

- **Gold**: Acid or neutral gold baths; electronics, precision optics
- **Silver**: Cyanide silver bath; art, musical instruments, reflectors
- **Iron**: Sulfate/chloride bath; printing plates, tooling

### 10-Step Process Sequence

1. **Mandrel fabrication** — Machine, cast, or 3D-print mandrel to final part shape (+ any undercuts/draft angles)
2. **Mandrel surface preparation** — Polish to required surface finish; the mandrel surface becomes the exterior surface of the electroformed part
3. **Apply release agent** — Conductive release agent (chromate passivation, or proprietary parting compound) on permanent mandrels; or no release agent needed for expendable mandrels
4. **Make mandrel conductive** — If mandrel is non-conductive (wax, plastic, glass), apply conductive layer: electroless nickel, silver paint, graphite spray, or vacuum-deposited metal
5. **Rack and connect** — Mount mandrel in tank; connect as cathode; position anodes (Ni or Cu rounds/bars in Ti baskets)
6. **Initial low-current strike** — Begin at 50-75% of full current density for 10-30 min to ensure uniform initial nucleation
7. **Electroform at full current density** — Build to required thickness at controlled current density, temperature, pH, and agitation
8. **Remove from bath** — Rinse thoroughly
9. **Separate from mandrel** — Mechanical separation (pry, flex), thermal differential (heat/cool to break bond), chemical dissolution (dissolve expendable mandrel), or a combination
10. **Post-processing** — Trim flash, machine to final dimensions, inspect, plate exterior if needed (decorative or corrosion protection)

---

## 8.2 Safety & PPE

### Hazards

| Hazard | Source | Severity |
|--------|--------|----------|
| **Nickel sulfamate/sulfate solutions** | Nickel salts are sensitizers (allergic contact dermatitis) and classified carcinogens (inhalation of nickel compounds — IARC Group 1 for nickel compounds) | Skin sensitization; respiratory cancer risk with chronic inhalation |
| **Acid mist** | Sulfuric acid, chloride additions | Respiratory irritation |
| **Electrical** | DC power supplies: 3-12 V, 100-10,000+ A | Electrocution risk; arc flash at bus bars |
| **Hydrogen evolution** | At cathode, especially at high current densities | Explosive atmosphere above bath; ventilation critical |
| **Mandrel dissolution chemicals** | Aluminum mandrels dissolved in NaOH (strong alkali); wax melted at elevated temp; lead mandrels dissolved in acid | Chemical burns from NaOH; thermal burns |
| **Cyanide** | Silver and some gold electroforming baths use cyanide | Extremely toxic; OSHA PEL 5 mg/m3 (as CN); fatal at low doses if ingested or inhaled |
| **Mechanical** | Heavy mandrels, hot baths, overhead cranes | Standard shop hazards |

### Required PPE

- **Chemical-resistant gloves** (nitrile inner + PVC outer for nickel handling; barrier cream under gloves)
- **Chemical splash goggles + face shield**
- **Rubber apron and boots**
- **Respiratory protection**: Ventilation at tank lip; P100 particulate filter + acid gas cartridge if mist monitoring indicates exposure above 50% of PEL (0.05 mg/m3 for insoluble Ni compounds; 0.1 mg/m3 for soluble Ni)
- **Cyanide baths**: Full face SCBA or supplied air available; cyanide antidote kit (amyl nitrite, sodium nitrite, sodium thiosulfate) accessible; **never mix cyanide baths with acid — produces HCN gas**

---

## 8.3-8.4 Part Preparation and Cleaning (Mandrel Preparation)

### Mandrel Types

| Type | Material | Separation Method | Reusable? |
|------|----------|------------------|-----------|
| **Permanent** | Stainless steel, nickel, chrome-plated steel, glass | Mechanical (pry/flex); thermal differential; release agent | Yes — hundreds of cycles |
| **Expendable (dissolvable)** | Aluminum (dissolved in NaOH); zinc (dissolved in HCl); wax (melted); ABS plastic (dissolved in acetone); 3D-printed polymer | Chemical dissolution; melting | No — single use |
| **Semi-expendable** | Low-melting alloys (Cerrolow, Cerrobend, Wood's metal — mp 47-70 deg C) | Melt out at low temperature | Yes — re-melt and re-cast |

### Release Agents (Permanent Mandrels)

| Agent | Application |
|-------|-------------|
| **Chromate passivation (dichromate dip)** | Classic method: immerse SS or Ni mandrel in 2-5% K2Cr2O7 solution at 20-50 deg C for 30-60 sec; forms a thin Cr(III) oxide layer that allows deposit separation; widely used |
| **Proprietary parting compounds** | Various organic or inorganic coatings applied to mandrel surface |
| **Wax or grease film** | Simple but less reliable; can cause adhesion problems in deposit |
| **Electrolytic oxidation** | Anodic treatment in NaOH to form thin oxide on Ni mandrel surface |

**Note**: Chromate release agent has RoHS/REACH implications if it contains Cr(VI). Trivalent chromium passivation alternatives exist but may be less reliable as release agents.

### Mandrel Surface Finish

- **Critical concept**: The mandrel's surface finish is replicated exactly on the exterior of the electroformed part
- For optical-quality reflectors: mandrel must be polished to Ra < 0.01 um (< 0.4 uin) — optical quality
- For general industrial: Ra < 0.2 um (8 uin) typical
- For molds: mandrel surface texture IS the mold texture — any surface texture desired on the plastic part must be in the mandrel

### Making Non-Conductive Mandrels Conductive

| Method | Thickness | Application |
|--------|-----------|-------------|
| **Electroless nickel** | 0.5-2 um | Universal; excellent adhesion to activated plastic/wax; preferred method |
| **Silver paint (conductive paint)** | 5-25 um | Quick; commonly used for art/jewelry; less uniform |
| **Graphite spray/suspension** | 1-5 um | Quick; some porosity; acceptable for non-critical applications |
| **Vacuum metallization (sputtered or evaporated)** | 50-200 nm | Excellent for precision work; LIGA process |
| **Conductive lacquer (copper or silver filled)** | 5-50 um | Commercial products available |

---

## 8.5-8.6 Equipment and Parameters

### Tank Setup

- **Tank construction**: Polypropylene or PVC lined; heated (in-tank heaters or external heat exchanger); filtered (continuous filtration through 1-5 um filters)
- **Anodes**: Sulfur-depolarized nickel rounds (electrolytic Ni, S-activated) in titanium baskets for nickel sulfamate; OFHC copper anodes or phosphorized copper for acid copper
- **Anode bags**: Polypropylene bags on anodes to contain particles
- **Anode-to-cathode ratio**: 1:1 to 2:1; conforming anodes shaped to follow mandrel contour for uniform current distribution
- **Agitation**: Filtered air agitation (standard for Ni sulfamate); cathode bar reciprocation; solution circulation through external filter
- **Power supply**: DC rectifier with < 5% ripple; for thick deposits, pulse plating can improve density and reduce stress

### Deposition Parameters

#### Nickel Sulfamate Electroforming

| Parameter | Range | Notes |
|-----------|-------|-------|
| Current density | 1-10 A/dm2 (10-100 A/ft2); typical 3-5 A/dm2 | Higher current = faster but more stress and rougher deposit |
| Deposition rate | ~12 um/hour at 1 A/dm2; ~60 um/hour at 5 A/dm2 | Rate proportional to current (Faraday's law) |
| Temperature | 40-55 deg C (optimal: 50-54 deg C) | Higher temp = lower stress, better ductility |
| pH | 3.5-4.5 (optimal: 3.8-4.2) | Low pH: pitting; high pH: precipitation, high stress |
| Stress | Target: < 35 MPa (5000 psi) tensile; ideally near zero or slightly compressive | Controlled by bath chemistry (saccharin 0.5-3 g/L as stress reducer), temperature, and current density |
| Hardness | 150-250 HV (sulfamate, no additives); 300-500 HV (with stress reducers/hardeners) | |
| Deposit purity | > 99.5% Ni | |
| Sulfur content | 0.01-0.1% (from sulfamate decomposition) | High S makes deposit brittle at elevated temp |
| Cathode efficiency | 95-99% | |

### Build Thickness Control

- **Time-based**: Primary method — calculate from Faraday's law: thickness (um) = (current density in A/dm2 x time in hours x M) / (n x F x density x 10^-4); for Ni at 1 A/dm2: ~12 um/hr
- **Weight gain**: Weigh mandrel + deposit periodically; calculate average thickness
- **Micrometer/caliper**: Measure mandrel + deposit at accessible points during long builds
- **Current integrator (amp-hour meter)**: Total charge passed correlates directly to total metal deposited (Faraday's law)
- **For thick electroforms (> 1 mm)**: Process may take days to weeks; periodic removal for measurement and inspection is standard

### Typical Build Times

| Target Thickness | Current Density | Approximate Time |
|-----------------|----------------|-----------------|
| 100 um (0.004 in) | 5 A/dm2 | ~2 hours |
| 500 um (0.020 in) | 5 A/dm2 | ~8 hours |
| 1 mm (0.040 in) | 5 A/dm2 | ~17 hours |
| 5 mm (0.200 in) | 5 A/dm2 | ~83 hours (~3.5 days) |
| 10 mm (0.400 in) | 3 A/dm2 | ~140 hours (~6 days) |

---

## 8.7-8.8 Deposition, Post-Treatment, and Inspection

### How the Electroformed Part Grows

- Deposition occurs preferentially at high-current-density areas (edges, corners, protrusions on the mandrel)
- **Current distribution management** is critical: auxiliary cathodes (thieves/robbers), shields, and conforming anodes are used to achieve uniform thickness
- For very thick deposits, the deposit surface roughens over time — periodic mechanical polishing of the growing surface may be needed for critical applications (waveguides)
- Internal stress builds during deposition — if not controlled, the deposit can crack, curl, or peel from the mandrel prematurely

### Mandrel Separation

| Method | Application |
|--------|-------------|
| **Mechanical** | Slight taper on mandrel (1-3 deg draft); flex deposit or thermal shock (dip in hot then cold water); pry gently |
| **Thermal differential** | Exploit different CTE (coefficient of thermal expansion) — for Ni on SS mandrel: heat to 150-200 deg C then cool rapidly; Ni (CTE 13 um/m/deg C) vs SS (CTE 16 um/m/deg C) |
| **Chemical dissolution** | Dissolve Al mandrel in 10-20% NaOH at 60-80 deg C; dissolve Zn in 10-20% HCl; dissolve wax in trichloroethylene or heat |
| **Low-melt alloy** | Heat above mp of mandrel material (47-70 deg C); mandrel melts out; collect and re-use |

### Post-Processing

- **Trim flash**: Cut or grind excess deposit at edges
- **Machine to final dimensions**: Mill, turn, grind, or EDM the electroformed shell to final tolerances
- **Heat treatment**: Anneal at 400-600 deg C for 1-2 hours in inert atmosphere to relieve stress and increase ductility (reduces hardness from 300 HV to 150-180 HV)
- **External plating**: May plate exterior of electroform for corrosion protection or appearance (chrome, gold, tin)
- **Interior surface**: This is the precision surface (replicated from mandrel) — handle with care; do not scratch

### Quality Inspection

| Test | What It Measures | Method |
|------|-----------------|--------|
| **Thickness (uniformity)** | Total deposit thickness across the part | Micrometer, ultrasonic thickness gauge (for non-magnetic substrates), cross-section microscopy |
| **Internal stress** | Residual stress in deposit (must be low for dimensional stability) | Spiral contractometer (during deposition); X-ray diffraction (post-deposition); strip deflection test |
| **Hardness** | Mechanical properties | Vickers microhardness (HV) on cross-section or surface |
| **Ductility** | Elongation at break | Tensile test of companion coupon (plated flat strip) |
| **Surface roughness (interior)** | Precision surface quality | Profilometer — should match mandrel finish |
| **Porosity** | Pinholes in thin sections | Ferroxyl test (for Ni); bend test; pressurized leak test |
| **Dimensional accuracy** | Does the part meet dimensional tolerances? | CMM (coordinate measuring machine) |
| **Sulfur content** | Affects elevated-temperature properties | Combustion analysis (LECO); keep < 0.03% for applications involving heat (brazing, soldering) |
| **Visual** | Surface quality, defects, discoloration | Inspect interior (mandrel-replica) surface under magnification |

### Common Defects

| Defect | Cause | Prevention |
|--------|-------|------------|
| **Pitting** | Hydrogen bubbles adhering to surface during deposition; contamination; low pH | Wetting agents (sodium lauryl sulfate 0.01-0.05 g/L); air agitation; maintain pH > 3.5; carbon treat bath |
| **Burning (rough, dark deposit)** | Current density too high; metal concentration too low; pH too high | Reduce current density; maintain metal concentration; control pH |
| **High stress / cracking** | Bath contamination (especially organic); decomposition products; low temperature; high current | Carbon treatment; maintain saccharin or stress reducer addition; increase temperature; reduce current |
| **Poor separation from mandrel** | Inadequate release agent; deposit too thick at edges; mechanical lock | Fresh release agent application; use thieves at edges; ensure draft angle |
| **Non-uniform thickness** | Poor current distribution; mandrel geometry | Auxiliary cathodes, shields, conforming anodes; optimize rack design |
| **Lamination / layering** | Power interruption during deposition; bath chemistry excursion | Uninterruptible power supply (UPS); automated bath monitoring and chemical addition |
| **Rough deposit (nodules)** | Particulate contamination; anode sludge; organic contamination | Continuous filtration; anode bags; regular carbon treatment |
| **Brittle deposit** | Metallic contamination (Cu, Zn, Pb, Cd in Ni bath); organic decomposition products | Hull cell testing; purification (dummy plating at 0.2-0.5 A/dm2 overnight; carbon treatment) |

---
---

# CROSS-CUTTING REFERENCE TABLES

## Vacuum Process Comparison

| Parameter | PVD Sputtering | PVD Arc | Thermal CVD | PECVD | ALD |
|-----------|---------------|---------|-------------|-------|-----|
| Base pressure (mbar) | 10^-5 | 10^-5 | N/A (purge) | 10^-2 | 10^-1 to 10^-2 |
| Working pressure (mbar) | 10^-3 to 10^-2 | 10^-2 to 10^-1 | 50-1000 | 0.5-5 (Torr) | 0.1-10 (Torr) |
| Temperature (deg C) | 200-500 | 200-500 | 800-1100 | 100-400 | 50-400 |
| Deposition rate | 0.5-5 um/hr | 2-10 um/hr | 0.5-5 um/hr | 50-200 nm/min | 0.1 nm/cycle |
| Line-of-sight? | Yes | Mostly | No | No | No |
| Conformality | Poor-moderate | Moderate | Good | Moderate | Excellent (100%) |
| Film stress | Moderate-high | High | Low-moderate | Low-moderate | Low |
| Typical thickness | 1-10 um | 1-10 um | 1-30 um | 0.01-5 um | 1-100 nm |

## Wet Process Comparison (Electropolishing vs. Electroforming)

| Parameter | Electropolishing | Electroforming |
|-----------|-----------------|----------------|
| Part is... | Anode | Cathode (mandrel) |
| Metal is... | Removed | Deposited |
| Electrolyte | Phosphoric/sulfuric acid | Plating bath (Ni sulfamate, acid Cu, etc.) |
| Temperature | 50-80 deg C | 40-55 deg C |
| Current density | 5-30 A/dm2 | 1-10 A/dm2 |
| Time | 2-20 min | Hours to weeks |
| Result | Smooth, bright, passive surface | Free-standing metal part |

---
---

# SOURCES AND CONFIDENCE ASSESSMENT

## Sources

All data in this brief is sourced from Watson's domain expertise, drawing on:

- **ASM Handbook, Volume 5: Surface Engineering** — primary reference for PVD, CVD, electropolishing, electroforming
- **Mattox, D.M., "Handbook of Physical Vapor Deposition (PVD) Processing"** — PVD parameters, processes, equipment
- **Ohring, M., "Materials Science of Thin Films: Deposition and Structure"** — thin film growth mechanisms, Thornton zone model
- **Pierson, H.O., "Handbook of Chemical Vapor Deposition"** — CVD process parameters, precursor chemistry
- **George, S.M., "Atomic Layer Deposition: An Overview," Chemical Reviews (2010)** — ALD fundamentals (canonical ALD review)
- **Robertson, J., "Diamond-Like Amorphous Carbon," Materials Science and Engineering R (2002)** — DLC classification, properties
- **VDI 2840:2012 — Carbon films — basic knowledge, film types, and properties** — DLC nomenclature
- **Products Finishing magazine and PFonline.com** — electropolishing and electroforming practical data
- **ASTM A967/A967M — Standard Specification for Chemical Passivation Treatments for Stainless Steel Parts** — post-EP passivation
- **ASTM B832 — Standard Guide for Electroforming with Nickel** — electroforming parameters and best practices
- **Wolf, S. and Tauber, R.N., "Silicon Processing for the VLSI Era"** — semiconductor CVD, PECVD, ion implantation
- **Semiconductor industry experience** — ALD, PECVD, ion implant parameters from IC manufacturing context

## Confidence Assessment

| Cluster | Confidence | Notes |
|---------|-----------|-------|
| PVD | HIGH | Well-established domain expertise; parameters verified against multiple sources over years |
| CVD | HIGH | Thermal CVD for cutting tools and semiconductor well documented in Watson's knowledge base |
| PECVD | HIGH | Semiconductor PECVD parameters are among the most precisely characterized processes in industry |
| ALD | HIGH | ALD literature is extensive and well-standardized; GPC values are highly reproducible |
| DLC | HIGH | DLC classification per VDI 2840 is well established; property ranges may vary by vendor |
| Ion Implantation | HIGH (semiconductor); MODERATE (industrial) | Semiconductor implant is extremely well documented; industrial ion implantation for surface hardening has fewer standardized references |
| Electropolishing | HIGH | This falls within Watson's core electrochemistry expertise; electrolyte compositions well known |
| Electroforming | HIGH | Same core electrochemistry knowledge; Ni sulfamate parameters are standard plating industry knowledge |

## Flags for Alaina

- **Gemini was rate-limited** during this research session. All data came from Watson's stored domain expertise. The data is reliable but has not been cross-verified with live sources for this particular brief. Tyler spot-check recommended for electropolishing and electroforming clusters (these overlap with Tyler's analytical chemistry domain).
- **Ion implantation industrial applications** — the hardness improvement numbers (50-100% increase) are representative but vary significantly by substrate material, ion species, dose, and energy. Poster should note "typical" or "representative" values, not absolute.
- **Perchloric acid electropolishing** — strongly recommend the poster include a prominent safety warning. Perchloric acid baths have caused fatal explosions. Many shops have banned them entirely.
- **DLC classification** — the VDI 2840 naming convention (a-C:H, ta-C, etc.) is the industry standard but can be confusing for a poster audience. Recommend simplifying for the poster while maintaining accuracy.
- **ALD cycle animation** — the self-limiting pulse/purge/pulse/purge mechanism is ideal for a visual poster. Consider illustrating one complete ALD cycle as a 4-panel sequence.

---

*End of Research Brief — Watson, 2026-04-26*
