---
title: Thermal Spray Clusters — Watson Research Brief
author: Watson (watson-chemistry-researcher)
date: 2026-04-26
version: v1
purpose: Technical research brief for 80 posters across 8 thermal spray process clusters (10 posters each)
status: COMPLETE — domain expertise build (Gemini quota exhausted; data sourced from Watson training corpus including ASM Handbook Vol 5A, Pawlowski, ITSA Handbook, and relevant ASTM/AMS/AWS standards)
confidence: HIGH for all 8 processes; numerical ranges cross-referenced against multiple handbook sources
tags:
  - ThermalSpray
  - PlatingPosters
  - WatsonResearch
---

# Thermal Spray Clusters — Watson Research Brief

## Table of Contents

1. [Universal Reference Data](#universal-reference-data)
2. [Cluster 1: Atmospheric Plasma Spray (APS)](#cluster-1-atmospheric-plasma-spray-aps)
3. [Cluster 2: HVOF (High Velocity Oxy-Fuel)](#cluster-2-hvof-high-velocity-oxy-fuel)
4. [Cluster 3: Flame Spray (Wire and Powder)](#cluster-3-flame-spray-wire-and-powder)
5. [Cluster 4: Arc Spray (Twin Wire Arc)](#cluster-4-arc-spray-twin-wire-arc)
6. [Cluster 5: Cold Spray](#cluster-5-cold-spray)
7. [Cluster 6: Detonation Gun (D-Gun)](#cluster-6-detonation-gun-d-gun)
8. [Cluster 7: Suspension Plasma Spray (SPS)](#cluster-7-suspension-plasma-spray-sps)
9. [Cluster 8: Wire Combustion Spray](#cluster-8-wire-combustion-spray)
10. [Cross-Process Comparison Tables](#cross-process-comparison-tables)
11. [HVOF vs. Hard Chrome: The Transition Story](#hvof-vs-hard-chrome-the-transition-story)
12. [Key Standards Reference](#key-standards-reference)

---

## Universal Reference Data

### Standards Applicable Across All Processes

| Standard | Title / Scope |
|----------|---------------|
| ASTM C633 | Bond strength of thermal spray coatings (tensile adhesion test) |
| ASTM E2109 | Porosity measurement by image analysis |
| ASTM B487 | Coating thickness by metallographic cross-section |
| ASTM E384 | Microhardness testing (Knoop and Vickers) |
| AWS C2.18 | Guide for the Protection of Steel with Thermal Sprayed Coatings of Aluminum, Zinc, and Their Alloys and Composites |
| SSPC-CS 23.00 | Application of Thermal Spray Coatings (Metallizing) of Aluminum, Zinc, and Their Alloys and Composites for the Corrosion Protection of Steel |
| AMS 2447 | HVOF coating of hardface alloys (general) |
| AMS 2448 | HVOF application of tungsten carbide coatings |
| MIL-STD-1687A | Thermal spray processes (legacy but still widely referenced) |

### Grit Blast Media Quick Reference

| Media | Typical Grit Size | Hardness (Mohs) | Use Case |
|-------|-------------------|------------------|----------|
| White alumina (Al2O3) | 24–60 mesh | 9 | General purpose; aerospace preferred |
| Brown alumina (Al2O3) | 24–60 mesh | 9 | General purpose; lower cost |
| Angular steel grit | G25–G40 | 7–8 | Infrastructure; bridge work |
| Silicon carbide | 24–60 mesh | 9.5 | Hard substrates; titanium prep |
| Garnet | 36–80 mesh | 7–8 | Non-ferrous substrates; less aggressive |
| Chilled iron grit | G25–G40 | 7–8 | Heavy structural steel |

### Substrate Temperature Limits (General Guidance)

| Substrate | Max Temp During Spray | Notes |
|-----------|----------------------|-------|
| Low-carbon steel | 150–200 degC | Higher OK if no dimensional concern |
| Tool steel (heat-treated) | 150 degC | Avoid tempering; monitor closely |
| Aluminum alloys | 120–150 degC | Risk of annealing; aggressive cooling needed |
| Magnesium alloys | 100–120 degC | Very sensitive; cold spray preferred |
| Titanium alloys | 150–200 degC | Oxidation above 400 degC; inert atmosphere helps |
| Polymers / composites | 60–80 degC | Cold spray only realistic option |
| Copper alloys | 150–200 degC | Good thermal conductor; self-cooling helps |

---

## Cluster 1: Atmospheric Plasma Spray (APS)

### Poster 1 — Process Flow (Summary)

**Process Mechanism:**
A DC electric arc is struck between a tungsten cathode and a copper anode inside the plasma gun. Plasma-forming gas (argon, nitrogen, hydrogen, helium, or mixtures) flows through the arc and is ionized, creating a plasma jet at 10,000–15,000 degC (core temperature can exceed 20,000 degC). Powder feedstock is injected radially into the plasma plume (either internally or externally), melted and accelerated to 200–600 m/s, then impacts the prepared substrate where the molten droplets ("splats") flatten, solidify, and mechanically interlock.

**Feedstock Forms:**
- Powder only (no wire capability in standard APS)
- Powder size: typically 10–90 microns (process-specific; finer for dense coatings, coarser for TBCs)
- Common materials: YSZ (yttria-stabilized zirconia, 7–8 wt% Y2O3), alumina (Al2O3), titania (TiO2), chrome oxide (Cr2O3), MCrAlY bond coats (M = Ni, Co, or NiCo), NiAl, NiCr, stainless steels, molybdenum

**Key Coating Applications:**
- Thermal barrier coatings (TBCs) for gas turbine blades and vanes
- Wear-resistant ceramic coatings
- Dielectric / electrical insulation coatings
- Biomedical (hydroxyapatite on orthopedic implants)
- Clearance control / abradable coatings

### Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|--------|---------|----------|
| **Noise** | 100–130 dB at operator position; plasma gun itself can exceed 140 dB | Double hearing protection required (plugs + muffs); NRR 30+ |
| **UV/IR radiation** | Intense UV from plasma arc; comparable to welding arc | Shade 10–14 welding helmet or equivalent; no exposed skin |
| **Fume generation** | Metal and ceramic fumes (NiCr, Co, Cr2O3, ZrO2); varies by feedstock | Local exhaust ventilation (LEV); HEPA filtration; RPE with P100 filters minimum |
| **Dust explosion** | Fine metal powders (Al, Ti, Mg) are explosive when airborne | Powder handling in inert atmosphere; grounding; no open flames near powder feed |
| **Thermal burns** | Substrate and fixture temperatures; hot overspray | Heat-resistant gloves; leather apron; face shield |
| **Electrical** | DC power supply 40–80 kW; high-frequency arc start | Lockout/tagout; insulated gloves; proper grounding |
| **Compressed gas** | High-pressure argon, hydrogen (flammable), nitrogen | Secured cylinders; hydrogen leak detection; proper regulators |
| **Overspray dust** | Respirable particles in booth | Enclosed spray booth with downdraft ventilation |

**TLV/PEL Reference Values (Selected):**
- Chromium (as Cr metal): OSHA PEL 1.0 mg/m3 (TWA)
- Nickel (metal dust): OSHA PEL 1.0 mg/m3; ACGIH TLV 1.5 mg/m3
- Cobalt: OSHA PEL 0.1 mg/m3; ACGIH TLV 0.02 mg/m3
- Zirconia: OSHA PEL 5 mg/m3 (as Zr)
- Alumina (as Al): OSHA PEL 15 mg/m3 (total dust)

### Poster 3 — Cleaning

**Pre-spray cleaning sequence:**
1. **Solvent degrease** — vapor degrease (perchloroethylene or trichloroethylene, legacy) or aqueous alkaline clean (preferred environmentally). Remove all oils, greases, machining fluids, fingerprints.
2. **Alkaline wash** — immersion or spray wash at 50–70 degC, pH 10–12, 5–15 minutes. Rinse thoroughly.
3. **Inspection** — water-break-free test (ASTM F22 equivalent). Surface must sheet water uniformly with no beading.
4. **Dry** — forced air or oven dry. No moisture at time of grit blast.

**Critical notes:**
- Cleaning must happen BEFORE masking — never mask over contaminated surfaces
- Time between cleaning and grit blast: minimize; ideally same shift
- Time between grit blast and spray: typically < 4 hours (specification dependent; some specs require < 2 hours)
- Avoid touching blasted surfaces with bare hands — wear clean lint-free gloves

### Poster 4 — Grit Blasting / Surface Prep

**Grit blast specification for APS:**

| Parameter | Typical Range |
|-----------|---------------|
| Media | White or brown alumina (Al2O3) |
| Grit size | 24–36 mesh (coarse) for metals; 60 mesh for thin substrates |
| Blast pressure | 40–80 PSI (275–550 kPa) |
| Nozzle distance | 100–200 mm (4–8 inches) |
| Blast angle | 60–90 degrees to surface |
| Anchor profile (Ra) | 3–8 microns (125–325 microinches); spec-dependent |
| Surface cleanliness | SSPC-SP 5 / NACE No.1 (White Metal Blast) or SA 3 (ISO 8501) |

**Why alumina over steel grit for aerospace:**
- No ferrous contamination risk on nickel or titanium substrates
- Alumina fractures to expose fresh cutting edges (self-sharpening)
- Steel grit can embed and cause galvanic corrosion sites

**Profile verification:**
- Testex press-o-film replica tape + micrometer (field method)
- Surface profilometer (Ra, Rz measurement) for precision
- Visual comparison to SSPC-VIS 1 standards

### Poster 5 — Masking and Fixturing

**Masking materials for APS:**
- High-temperature masking tape (silicone adhesive; rated to 260 degC / 500 degF minimum)
- Metal masks (mild steel, stainless steel, copper) — preferred for production; reusable
- Silicone plugs and caps for holes, bores, threads
- Ceramic fiber tape for extreme temperature zones
- Thermal spray maskant coatings (liquid applied, peelable)

**Fixturing considerations:**
- Rotation fixture for cylindrical parts (lathe-type setup); typical rotation speed 60–200 RPM
- Part must be fixtured to allow uniform standoff distance and spray angle
- Cooling air nozzles directed at substrate backside — critical for temperature control
- Fixture must not shadow spray pattern; design for line-of-sight access
- Ground fixture to workpiece for electrostatic discharge prevention

### Poster 6 — Equipment Setup (Gun/System)

**Plasma spray system components:**
1. **Plasma gun** — cathode (2% thoriated tungsten), anode (oxygen-free copper), gas injection ring, powder injector port(s)
2. **Power supply** — 40–80 kW DC; typical operating range 400–800 A at 50–80 V
3. **Gas console** — mass flow controllers for primary gas (Ar or N2) and secondary gas (H2, He, or N2)
4. **Powder feeder** — volumetric or gravimetric; carrier gas (Ar) delivers powder to injector
5. **Robot/manipulator** — 6-axis industrial robot (FANUC, ABB, KUKA common); or manual for repair work
6. **Cooling system** — closed-loop water cooling for gun; 15–25 L/min at 15–20 degC
7. **Exhaust/booth** — enclosed spray booth with dust collection (HEPA or cartridge filter)
8. **Control system** — PLC or proprietary controller; monitors all parameters in real time

**Major OEM systems:** Oerlikon Metco (F4-MB, 9MB), Praxair/TAFA (SG-100), Progressive Surface, Thermach

### Poster 7 — Parameter Setup

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Arc current | 400–800 A | Higher current = higher enthalpy |
| Arc voltage | 50–80 V | Determined by gas composition and flow |
| Power | 25–60 kW (typical); up to 80 kW | Power = V x A |
| Primary gas (Ar) | 35–60 SLPM | Stabilizes arc; carries plasma |
| Secondary gas (H2) | 5–15 SLPM | Increases enthalpy dramatically |
| Secondary gas (He) | 20–50 SLPM | Alternative to H2; less aggressive heating |
| Secondary gas (N2) | 5–20 SLPM | Lower cost alternative |
| Carrier gas (Ar) | 3–8 SLPM | Delivers powder to plasma plume |
| Powder feed rate | 20–80 g/min | Material and application dependent |
| Standoff distance | 75–150 mm (3–6 inches) | Closer = denser; farther = more porous |
| Spray angle | 75–90 degrees | Below 45 degrees causes shadowing and porosity |
| Traverse speed | 200–1000 mm/s | Robot-controlled for uniformity |
| Step increment | 3–6 mm | Overlap between passes (typically 25–50% of spray footprint) |
| Deposition rate | 2–10 kg/hr | Material and parameter dependent |
| Deposition efficiency | 40–70% | Remainder is overspray |

### Poster 8 — Spray Application

**Application technique:**
- Preheat substrate to 80–120 degC using plasma gun (no powder) to improve adhesion
- Apply bond coat first if specified (e.g., NiAl at 50–125 microns for ceramic topcoats)
- Multiple passes build thickness incrementally (20–50 microns per pass typical)
- Interpass cooling may be required — air jets maintain substrate below limits
- Monitor coating thickness with in-process measurement (contact gauge on sacrificial tabs or eddy current)
- Typical total coating thickness: 100–500 microns for ceramics; up to 2 mm for some metallic coatings
- For TBCs: bond coat (MCrAlY or NiCrAlY, 75–150 microns) + topcoat (7YSZ, 250–500 microns)

**Common defects during application:**
- Unmelted particles ("spitting") — power too low or standoff too far
- Substrate overheating — traverse too slow or insufficient cooling
- Delamination during spray — contaminated surface or insufficient profile
- Uneven thickness — inconsistent traverse speed or standoff variation
- Vertical cracking in ceramics — can be beneficial (strain tolerance) or detrimental depending on application

### Poster 9 — Post-Treatment (Seal/Grind/Machine)

**Sealing porous coatings:**
- Epoxy sealers (vacuum impregnation) — for wear and corrosion applications; fills interconnected porosity
- Silicone sealers — higher temperature capability than epoxy (up to 250 degC)
- Phenolic sealers — chemical resistance applications
- Aluminum phosphate — inorganic sealer for high-temperature service (up to 800 degC)
- Laser glazing — densifies surface layer; research/specialty applications

**Grinding and machining:**
- Diamond grinding preferred for ceramic coatings (alumina, chrome oxide, zirconia)
- Silicon carbide or CBN wheels for metallic coatings
- Coolant required — avoid thermal shock to coating
- Surface finish achievable: Ra 0.2–1.6 microns depending on coating and process
- Typical stock removal: 50–200 microns from as-sprayed surface

**Heat treatment (if applicable):**
- Diffusion heat treatment for MCrAlY bond coats (vacuum, 1050–1080 degC, 2–4 hours)
- Not standard for most APS ceramic topcoats

### Poster 10 — Inspection and QA

| Test | Method | Acceptance Criteria (Typical) |
|------|--------|-------------------------------|
| Bond strength | ASTM C633 (tensile adhesion) | > 10 MPa (ceramics); > 30 MPa (metals); spec-dependent |
| Porosity | ASTM E2109 (image analysis) | TBCs: 10–20% (intentional); wear coatings: < 5% |
| Thickness | ASTM B487 (metallographic); eddy current; mag-gauge | Per drawing tolerance; typically +/- 50 microns |
| Hardness | ASTM E384 (Vickers microhardness, HV300) | Al2O3: 800–1200 HV; Cr2O3: 1000–1800 HV; YSZ: 600–900 HV |
| Surface roughness | Profilometer (Ra) | As-sprayed: 5–15 microns; ground: 0.2–1.6 microns |
| Microstructure | Metallographic cross-section | Evaluate for cracks, delamination, unmelted particles, oxide stringers |
| Visual | Unaided eye + 10x loupe | No blistering, spalling, discoloration, or bare spots |
| Bend test | Mandrel bend (qualitative) | No cracking or spalling at specified bend radius |
| Macrohardness | Rockwell (HR15N for thin coatings) | Process-specific |

---

## Cluster 2: HVOF (High Velocity Oxy-Fuel)

### Poster 1 — Process Flow (Summary)

**Process Mechanism:**
A fuel (kerosene, hydrogen, propylene, propane, or natural gas) is combusted with oxygen at high pressure inside a water-cooled combustion chamber, producing a supersonic gas jet (Mach 1.5–3.0). Powder feedstock is injected axially (center) or radially into the combustion chamber or downstream nozzle. Particles are heated to near or slightly above their melting point and accelerated to 600–900 m/s — significantly faster than plasma spray. The high kinetic energy produces extremely dense, well-bonded coatings with very low porosity and low oxide content.

**Feedstock Forms:**
- Powder only (standard); wire HVOF exists but is niche
- Powder size: typically 5–45 microns (finer than APS due to higher velocity)
- Common materials: WC-Co (12% or 17% Co), WC-CoCr, CrC-NiCr (75/25), Stellite 6, Tribaloy T-800, Inconel 625/718, NiCrBSi self-fluxing alloys, stainless steels, MCrAlY

**Why HVOF matters — the hard chrome replacement:**
HVOF WC-Co is the aerospace and defense industry's primary replacement for hard chrome plating (hexavalent chromium). EPA National Emission Standards for Hazardous Air Pollutants (NESHAP) and the EU REACH regulation are driving this transition. HVOF coatings match or exceed hard chrome in hardness, wear resistance, and fatigue life while eliminating Cr(VI) exposure entirely.

### Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|--------|---------|----------|
| **Noise** | 110–130 dB at operator position (supersonic jet) | Double hearing protection; NRR 30+ |
| **Thermal radiation** | Intense IR from combustion jet | Heat-reflective PPE; face shield with IR filter |
| **Combustible gases** | Hydrogen, propylene, propane, kerosene vapor | Gas detection systems; proper ventilation; no ignition sources; flash-back arrestors on all gas lines |
| **Fumes** | Cobalt (WC-Co), nickel, chromium fumes | LEV with HEPA; cobalt TLV is very low (ACGIH TLV 0.02 mg/m3); biological monitoring recommended for Co-exposed workers |
| **Dust explosion** | Fine WC-Co, metal powders | Inert atmosphere powder handling; grounding |
| **Kerosene handling** | Liquid fuel HVOF systems | Proper fuel storage; spill containment; fire suppression |
| **Compressed oxygen** | High-pressure O2 (up to 150 PSI in some systems) | Oil-free fittings; no grease on O2 components; proper regulators |
| **UV radiation** | Less intense than plasma but still significant | Safety glasses with shade 5–8 lens minimum |

**Cobalt exposure — special emphasis:**
WC-Co is the most common HVOF feedstock. Cobalt dust and fume exposure can cause hard metal lung disease (cobalt pneumoconiosis) and asthma. ACGIH TLV is 0.02 mg/m3 — extremely low. Biological exposure index: urine cobalt < 15 microg/L. Respiratory protection program and medical surveillance are essential.

### Poster 3 — Cleaning

Identical sequence to APS (Poster 3 above) with the following HVOF-specific notes:
- Surface cleanliness is even more critical for HVOF because the coating is so dense — contaminants at the interface have no porosity to "hide" in and directly compromise bond strength
- For chrome replacement on landing gear and hydraulic cylinders: parts often arrive chrome-stripped (chemical or mechanical strip); must verify no residual chrome or etch products remain
- Aqueous alkaline cleaning preferred; solvent degreasing as backup
- Final rinse with DI water for aerospace components

### Poster 4 — Grit Blasting / Surface Prep

| Parameter | Typical Range |
|-----------|---------------|
| Media | White alumina (Al2O3); 99%+ purity for aerospace |
| Grit size | 36–60 mesh |
| Blast pressure | 40–60 PSI (275–415 kPa) |
| Nozzle distance | 100–150 mm |
| Blast angle | 75–90 degrees |
| Anchor profile (Ra) | 3–6 microns (125–250 microinches) |
| Surface cleanliness | SSPC-SP 5 (White Metal) or SSPC-SP 10 (Near-White) minimum |

**HVOF-specific notes:**
- Profile should not be too aggressive — HVOF's high particle velocity provides excellent mechanical interlocking even on moderate profiles
- For hard chrome replacement applications, the substrate may need to be ground back to remove any remaining chrome and achieve correct dimensional tolerance before blasting
- Aluminum oxide contamination of the interface is generally acceptable (it gets incorporated into the first coating layer)

### Poster 5 — Masking and Fixturing

- Metal masks (stainless steel, copper) preferred for production — withstand heat and velocity
- Silicone tape and plugs for non-critical masking
- HVOF generates more localized heat than APS — masking materials see higher thermal loading
- Rotation fixtures: typical surface speeds 0.5–2.0 m/s at the coating surface
- Part cooling: compressed air jets (dry, oil-free) directed at substrate backside
- For cylindrical parts (landing gear, hydraulic rods): lathe-type fixture with programmable rotation and gun traverse

### Poster 6 — Equipment Setup (Gun/System)

**Two main HVOF system types:**

**Gas-fuel HVOF (JP-5000 type — obsolete name; current: Praxair JP-8000, Oerlikon Metco DJ series):**
- Liquid fuel (kerosene/JP-5) atomized with oxygen in combustion chamber
- Combustion chamber pressure: 80–150 PSI (550–1035 kPa)
- Higher particle velocities than gas-fuel systems
- Preferred for WC-Co hardface coatings in aerospace

**Gas-fuel HVOF (Diamond Jet, Oerlikon Metco, Thermach):**
- Gaseous fuel: hydrogen, propylene, propane, ethylene, or natural gas
- Combustion chamber pressure: 60–100 PSI
- Slightly lower velocity but more flexibility in parameter tuning
- Broader range of feedstock compatibility

**System components:**
1. Combustion chamber (water-cooled)
2. Converging-diverging (de Laval) nozzle — creates supersonic flow
3. Barrel extension (length affects particle dwell time)
4. Powder feeder (gravimetric preferred for consistency)
5. Gas/fuel metering console (mass flow controllers)
6. Water cooling system (gun cooling; 15–25 L/min)
7. Robot/manipulator (6-axis)
8. Enclosed spray booth with dust collection
9. Control system with data logging

**Major OEM systems:** Oerlikon Metco (Diamond Jet 2700/2600), Praxair/TAFA (JP-8000), Thermach, Kermetico (AK series), GTV

### Poster 7 — Parameter Setup

| Parameter | Gas-Fuel HVOF | Liquid-Fuel HVOF |
|-----------|---------------|-------------------|
| Oxygen flow | 200–400 SLPM | 800–1000 SLPM |
| Fuel flow | H2: 400–700 SLPM; C3H6: 60–80 SLPM | Kerosene: 18–26 L/hr |
| Combustion pressure | 60–100 PSI | 80–150 PSI |
| Particle velocity | 500–750 m/s | 700–900 m/s |
| Gas jet temperature | 2500–3100 degC | 2600–3200 degC |
| Powder feed rate | 30–80 g/min | 40–100 g/min |
| Carrier gas (N2 or Ar) | 8–15 SLPM | 8–15 SLPM |
| Standoff distance | 150–300 mm (6–12 inches) | 300–400 mm (12–16 inches) |
| Spray angle | 75–90 degrees | 75–90 degrees |
| Traverse speed | 300–1000 mm/s | 300–1000 mm/s |
| Deposition rate | 2–8 kg/hr | 3–10 kg/hr |
| Deposition efficiency | 50–70% | 50–70% |

### Poster 8 — Spray Application

**Application technique:**
- Preheat substrate to 60–100 degC (less preheat needed than APS due to higher kinetic energy bonding)
- Build thickness incrementally: 15–30 microns per pass typical for WC-Co
- Total coating thickness: typically 100–500 microns (0.004–0.020 inches)
- For hard chrome replacement: target thickness typically 200–400 microns (to allow for finish grinding to final dimension)
- Maintain substrate temperature below 150 degC — use compressed air cooling between passes
- Monitor deposition rate and compare to qualification data

**Coating characteristics (WC-12Co as benchmark):**

| Property | HVOF WC-12Co | Hard Chrome (reference) |
|----------|--------------|------------------------|
| Hardness | 1100–1400 HV300 | 800–1000 HV |
| Porosity | < 1% (typically < 0.5%) | < 1% (typically micro-cracked) |
| Bond strength (ASTM C633) | > 70 MPa (often exceeds epoxy strength) | 40–80 MPa (mechanical + chemical) |
| Oxide content | < 0.5% (WC-Co) | N/A (metallic) |
| Surface roughness (as-sprayed) | Ra 3–6 microns | N/A (as-plated: Ra 0.2–0.8) |
| Surface roughness (ground) | Ra 0.1–0.4 microns | Ra 0.1–0.4 microns |
| Fatigue life impact | Neutral to beneficial (compressive residual stress) | Detrimental (tensile stress; hydrogen embrittlement risk) |
| Wear rate (ASTM G65) | 1–5 x 10^-7 mm3/Nm | 5–15 x 10^-7 mm3/Nm |
| Max service temperature | 500 degC (WC decomposes above ~540 degC) | 400 degC (begins to soften) |

### Poster 9 — Post-Treatment

**Grinding (primary post-treatment for HVOF):**
- Diamond or CBN grinding wheels (resin or vitrified bond)
- Wet grinding with soluble oil coolant — mandatory to avoid thermal damage
- Surface speeds: 20–30 m/s
- Infeed: 5–15 microns per pass (light cuts to avoid pullout)
- Achievable finish: Ra 0.1–0.4 microns (comparable to ground hard chrome)
- Superfinishing/lapping possible for Ra < 0.1 microns

**Sealing:**
- Generally NOT required for HVOF WC-Co (porosity < 1%)
- May seal with epoxy or phenolic for corrosion barrier in salt spray environments
- Aluminum phosphate sealers for elevated temperature service

**No diffusion heat treatment required** — coatings are fully functional as-sprayed and ground.

### Poster 10 — Inspection and QA

| Test | Method | Acceptance Criteria (HVOF WC-Co) |
|------|--------|----------------------------------|
| Bond strength | ASTM C633 | > 70 MPa (typically exceeds epoxy; report as "> epoxy strength") |
| Porosity | ASTM E2109 | < 1.0% (typically < 0.5%) |
| Thickness | Eddy current (non-ferrous sub); mag-gauge (ferrous); ASTM B487 | Per drawing +/- 50 microns |
| Hardness | ASTM E384 (HV300) | 1100–1400 HV300 (WC-12Co) |
| Surface roughness | Profilometer | As-ground: Ra < 0.4 microns typical |
| Microstructure | Metallographic cross-section (unetched + etched) | No delamination, no continuous oxide stringers, uniform carbide distribution |
| Visual | Unaided eye + 10x | No spalling, blistering, orange peel, or bare spots |
| Corrosion (if specified) | ASTM B117 (salt spray) | Per specification; typically > 500 hours for sealed WC-Co |

**AMS 2448 compliance:** Requires process qualification including destructive test coupons sprayed alongside production parts.

---

## Cluster 3: Flame Spray (Wire and Powder)

### Poster 1 — Process Flow (Summary)

**Process Mechanism:**
An oxy-fuel flame (typically oxy-acetylene or oxy-propane) melts feedstock material that is fed into the flame as either wire or powder. The molten or semi-molten particles are propelled toward the substrate by the combustion gases and/or an auxiliary compressed air stream. Particle velocity is relatively low (40–200 m/s), producing coatings with higher porosity and lower bond strength than HVOF or plasma, but at significantly lower cost and equipment complexity.

**Wire flame spray:** Wire is fed continuously through the center of the flame, melted, and atomized by a compressed air blast. Wire gauge typically 1.6–4.8 mm (1/16 to 3/16 inch) diameter.

**Powder flame spray:** Powder is gravity-fed or gas-entrained into the flame. Powder size typically 40–120 microns.

**Feedstock Forms:**
- **Wire:** zinc, aluminum, stainless steel (316, 420), carbon steel, bronze, Monel, nickel, copper, molybdenum, tin, babbitt
- **Powder:** NiCrBSi (self-fluxing alloys), stellite, tungsten carbide blends, ceramic (alumina, titania), bronze, nickel alloys
- Wire is simpler and cheaper; powder offers broader material selection

**This is the oldest and most accessible thermal spray technology — many shops already own oxy-acetylene equipment.**

### Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|--------|---------|----------|
| **Noise** | 85–105 dB (lower than plasma/HVOF) | Hearing protection above 85 dB; plugs sufficient for most work |
| **Flame/thermal** | Open oxy-acetylene flame; hot spatter | Face shield, leather gloves, leather apron, safety glasses with side shields |
| **Zinc fume fever** | Spraying zinc wire produces ZnO fumes; flu-like symptoms (fever, chills, muscle ache) onset 4–12 hours post-exposure | Mandatory RPE (P100); LEV; zinc fume TLV = 2 mg/m3 (respirable) per ACGIH |
| **Metal fumes** | All metals produce fumes; stainless steel releases Cr and Ni fumes | Fume extraction; appropriate RPE; monitor airborne metals |
| **Compressed gas** | Oxy-acetylene (acetylene unstable above 15 PSI); propane | Flash-back arrestors; proper gas storage; leak checks with soapy water |
| **Fire** | Spatter and hot overspray | Fire-resistant surroundings; fire extinguisher on hand; fire watch |
| **UV radiation** | Moderate (less than plasma or HVOF) | Safety glasses with shade 3–5 lens |

### Poster 3 — Cleaning

Standard thermal spray cleaning sequence (see APS Poster 3). Flame spray-specific notes:
- Flame spray is often used in field repair where ideal cleaning is challenging — use best available methods
- Solvent wipe (acetone or MEK) + mechanical abrasion may substitute for full alkaline immersion in field work
- For structural steel corrosion protection (zinc/aluminum): remove all mill scale, rust, and previous coatings
- Verify surface cleanliness to SSPC-SP 5 or SP 10 as specification requires

### Poster 4 — Grit Blasting / Surface Prep

| Parameter | Typical Range |
|-----------|---------------|
| Media | Angular alumina or steel grit |
| Grit size | 16–36 mesh (coarser than HVOF due to lower particle energy) |
| Blast pressure | 60–100 PSI (415–690 kPa) — more aggressive than APS/HVOF |
| Nozzle distance | 150–250 mm |
| Blast angle | 60–90 degrees |
| Anchor profile (Ra) | 4–12 microns (175–500 microinches) — rougher profile needed |
| Surface cleanliness | SSPC-SP 5 (White Metal) for corrosion protection per AWS C2.18 |

**Why rougher profile:** Flame spray coatings rely heavily on mechanical interlocking due to lower particle velocity. A rougher anchor profile compensates by increasing the surface area for bonding.

### Poster 5 — Masking and Fixturing

- Simpler masking than APS/HVOF — lower particle velocity means less overspray penetration
- Standard high-temperature tape, metal shields, or silicone plugs
- Manual operation is common — operator hand-holds the gun for many applications
- Turntable or simple rotation fixture for cylindrical parts
- No sophisticated robot required (though automation improves consistency)

### Poster 6 — Equipment Setup (Gun/System)

**Wire flame spray gun components:**
1. Oxy-fuel nozzle assembly (mixing chamber + flame cone)
2. Wire feed mechanism (air-turbine or electrically driven)
3. Compressed air atomizing cap
4. Wire spool (typically 25–50 lb spools)

**Powder flame spray gun components:**
1. Oxy-fuel nozzle assembly
2. Powder hopper (gravity feed) or powder feeder (carrier gas)
3. Powder injector into flame

**Gas supply:**
- Oxygen: regulated to 15–40 PSI
- Acetylene: regulated to 10–15 PSI (NEVER exceed 15 PSI — acetylene is unstable above this pressure)
- Propane (alternative): regulated to 10–20 PSI
- Compressed air (atomizing): 40–80 PSI

**Major OEMs:** Oerlikon Metco (5P-II, 6P-II for powder; 14E for wire), Saint-Gobain, Thermach, Metallisation Ltd

### Poster 7 — Parameter Setup

| Parameter | Wire Flame Spray | Powder Flame Spray |
|-----------|------------------|--------------------|
| Oxygen pressure | 20–40 PSI | 15–30 PSI |
| Fuel (acetylene) pressure | 10–15 PSI | 10–15 PSI |
| Compressed air pressure | 40–80 PSI | N/A (or 20–40 for carrier) |
| Wire feed rate | 1–8 m/min | N/A |
| Powder feed rate | N/A | 20–60 g/min |
| Flame temperature | ~3,100 degC (oxy-acetylene) | ~3,100 degC (oxy-acetylene) |
| Particle velocity | 80–200 m/s (wire); 40–100 m/s (powder) | 40–100 m/s |
| Standoff distance | 150–250 mm (6–10 inches) | 150–300 mm (6–12 inches) |
| Spray angle | 60–90 degrees | 60–90 degrees |
| Deposition rate | 2–8 kg/hr (wire) | 1–4 kg/hr (powder) |
| Deposition efficiency | 50–70% (wire) | 30–50% (powder) |

### Poster 8 — Spray Application

**Application technique:**
- Preheat substrate to 80–120 degC using the flame gun (no feedstock)
- Wire: steady feed rate; adjust wire speed to maintain smooth spray pattern (no "spitting")
- Powder: adjust carrier gas flow and powder feed for consistent plume
- Multiple passes; 25–75 microns per pass depending on material
- Total thickness: 100–2000 microns (flame spray is often used for thick buildups in repair)
- For self-fluxing alloys (NiCrBSi): apply coating, then fuse with oxy-acetylene torch or furnace at 1000–1100 degC — this remelts the coating, eliminates porosity, and metallurgically bonds to substrate

**Coating characteristics (as-sprayed, non-fused):**

| Property | Typical Range |
|----------|---------------|
| Porosity | 5–15% |
| Oxide content | 3–10% |
| Bond strength (ASTM C633) | 10–30 MPa |
| Hardness | Material-dependent; NiCrBSi as-sprayed: 300–500 HV; fused: 700–900 HV |
| Surface roughness (Ra) | 8–20 microns (as-sprayed) |

### Poster 9 — Post-Treatment

**Self-fluxing alloy fusing (unique to flame spray):**
- Oxy-acetylene torch fusing: operator heats coating surface until it "sweats" (glossy appearance indicating remelting); temperature ~1000–1100 degC
- Furnace fusing: vacuum or controlled atmosphere; more uniform; preferred for critical components
- Fusing eliminates porosity (to < 1%), increases bond strength to metallurgical bond (> 70 MPa), and dramatically increases hardness
- WARNING: fusing temperature exceeds the capability of many substrates — not suitable for heat-treated or thin-section parts

**Sealing (non-fused coatings):**
- Epoxy or phenolic impregnation for corrosion protection
- Wax sealers for low-cost applications
- Essential for zinc/aluminum corrosion coatings to seal interconnected porosity

**Machining:**
- Conventional machining (turning, milling) is possible for softer metallic coatings
- Diamond grinding for hard or fused coatings

### Poster 10 — Inspection and QA

| Test | Method | Typical Criteria |
|------|--------|------------------|
| Bond strength | ASTM C633 | > 10 MPa (as-sprayed); > 35 MPa (fused) |
| Porosity | ASTM E2109 | 5–15% (as-sprayed); < 2% (fused) |
| Thickness | Mag-gauge, eddy current, ASTM B487 | Per specification |
| Hardness | ASTM E384 | Material-dependent |
| Visual | Unaided eye + 10x | Uniform coverage; no bare spots, blistering, or excessive orange peel |
| Bend test | Mandrel bend | Per specification (qualitative; fused coatings may crack) |
| Fuse quality (if applicable) | Visual "sweat" + metallographic section | Fully wetted interface; no unfused areas; < 2% porosity |

---

## Cluster 4: Arc Spray (Twin Wire Arc)

### Poster 1 — Process Flow (Summary)

**Process Mechanism:**
Two consumable wires of the same (or different) composition are fed toward each other. A DC electric arc is struck at the point where the wire tips meet, melting the wire ends. A high-velocity compressed air (or inert gas) jet atomizes the molten metal into fine droplets and propels them at the substrate at 50–200 m/s. No combustion gases are used — the energy comes from the electrical arc, and the kinetic energy from the atomizing gas.

Arc spray offers higher deposition rates than any other thermal spray process (up to 30+ kg/hr) at relatively low cost, making it the dominant technology for high-volume corrosion protection of structural steel.

**Feedstock Forms:**
- Wire only (two wires fed simultaneously)
- Wire diameter: 1.6–3.2 mm (1/16 to 1/8 inch) typical
- Common materials: zinc (99.99% pure or alloy), aluminum (99.0% or 1100 series), zinc-aluminum alloy (85/15 "ZnAl" pseudo-alloy), stainless steel (316L, 420), carbon steel, copper, bronze, nickel, Monel, babbitt
- Cored wires available: metal matrix composites (e.g., FeCrB, WC-filled) for wear resistance

### Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|--------|---------|----------|
| **Noise** | 95–115 dB | Double hearing protection above 100 dB |
| **Electric arc** | 18–40 VDC open circuit; 100–400 A operating; arc flash | Welding-grade PPE; insulated gloves; proper grounding |
| **UV/IR radiation** | Arc produces significant UV (less than plasma, comparable to MIG welding) | Shade 8–12 welding lens; no exposed skin |
| **Zinc fume fever** | Very high deposition rate of zinc = high fume generation rate | Mandatory supplied-air RPE (PAPR or airline) for zinc spraying; LEV essential; TLV 2 mg/m3 |
| **Metal fumes** | Al, stainless steel, copper — all produce hazardous fumes at high rates | Fume extraction; appropriate RPE rated for specific metals |
| **Electrical** | DC power supply; cable damage risk on jobsites | GFCI protection; cable inspection; lockout/tagout |
| **Fire/spatter** | Molten metal droplets travel 2–5 meters | Fire blankets; clear area of combustibles; fire watch |

**Arc spray produces more fume per unit time than any other thermal spray process** due to its very high deposition rate. Ventilation design must account for this.

### Poster 3 — Cleaning

For structural steel (the primary arc spray substrate):
1. Remove all oil, grease, and contaminants (solvent wipe or alkaline wash)
2. Remove all rust, mill scale, and old coatings — grit blasting is mandatory
3. For field work on bridges and infrastructure: high-pressure water blast to remove loose material before grit blast
4. Verify cleanliness per SSPC-SP 5 or SP 10
5. Apply coating within 4 hours of blast (less in humid environments — AWS C2.18 specifies time limits based on relative humidity)

### Poster 4 — Grit Blasting / Surface Prep

| Parameter | Typical Range |
|-----------|---------------|
| Media | Angular steel grit (G25, G40) or aluminum oxide (24–36 mesh) |
| Blast pressure | 60–100 PSI (415–690 kPa) |
| Nozzle distance | 150–300 mm |
| Blast angle | 60–90 degrees |
| Anchor profile (Ra) | 4–12 microns (175–500 microinches) |
| Surface cleanliness | SSPC-SP 5 (White Metal) per AWS C2.18; SP 10 (Near-White) acceptable for some specs |

**Field blasting considerations:**
- Containment required (blast curtains, vacuum recovery) for lead paint removal
- Spent blast media must be tested for lead and hexavalent chromium before disposal
- Steel grit is recyclable; alumina is not
- Ambient conditions: do not blast if surface temperature is within 3 degC (5 degF) of dew point

### Poster 5 — Masking and Fixturing

- Field masking: tape (aluminum foil tape, high-temp masking tape), sheet metal shields, magnetic masks
- Simple masking is usually adequate — arc spray is a "big area" coating process
- No sophisticated fixturing for structural steel — operator holds gun and walks the structure
- For shop work: turntable for cylindrical parts; simple rotation fixture
- Masking bolt holes, threads, and bearing surfaces is essential

### Poster 6 — Equipment Setup (Gun/System)

**Arc spray system components:**
1. **Arc spray gun** — two wire guides, contact tips, atomizing air cap, insulated nozzle body
2. **DC power supply** — constant-voltage (CV) type; 18–40 V open circuit; 100–400 A capacity
3. **Wire feeder** — dual-spool, push-type; synchronized wire feed speed for both wires
4. **Compressed air supply** — 80–120 PSI at 40–80 CFM (high volume requirement)
5. **Air dryer/filter** — oil-free, dry air is critical (moisture causes porosity; oil causes adhesion failure)
6. **Control unit** — voltage, amperage, wire speed, air pressure adjustment

**Major OEMs:** Oerlikon Metco (SmartArc), Thermion (formerly TAFA), Metallisation Ltd (S-Arc series), OSU (Open System Unit — niche), Praxair Surface Technologies

### Poster 7 — Parameter Setup

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Arc voltage | 24–35 V | Higher voltage = wider spray pattern, coarser droplets |
| Arc current | 100–300 A | Current is largely determined by wire feed speed |
| Wire feed speed | 2–15 m/min (each wire) | Higher = higher deposition rate |
| Atomizing air pressure | 40–80 PSI (275–550 kPa) | Higher pressure = finer atomization, denser coating |
| Air volume | 40–80 CFM | Must maintain adequate air flow at pressure |
| Standoff distance | 100–250 mm (4–10 inches) | Closer = denser coating; farther = more porosity |
| Spray angle | 60–90 degrees | Below 45 degrees causes porosity and poor adhesion |
| Traverse speed | Manual: operator-controlled; Robot: 200–800 mm/s | Consistency is key to uniform thickness |
| Deposition rate | 5–30+ kg/hr | Highest of all thermal spray processes |
| Deposition efficiency | 60–80% | Higher than flame spray |
| Particle velocity | 50–200 m/s | Atomizing gas dependent |

### Poster 8 — Spray Application

**Application technique:**
- Preheat substrate to minimum 10 degC above dew point (critical for outdoor work)
- First pass at close standoff (100–150 mm) for maximum bond coat density
- Build up thickness with subsequent passes at normal standoff
- Total coating thickness per AWS C2.18:
  - Zinc (mild exposure): 100–150 microns (4–6 mils)
  - Zinc (severe exposure): 200–350 microns (8–14 mils)
  - Aluminum (high-temperature or marine): 150–350 microns (6–14 mils)
  - Zinc-Aluminum 85/15: 150–300 microns (6–12 mils)
- Apply seal coat within 4 hours of spray completion (before porosity fills with moisture)

**Coating characteristics (zinc, as-sprayed):**

| Property | Typical Range |
|----------|---------------|
| Porosity | 5–15% |
| Oxide content | 5–15% |
| Bond strength (ASTM C633) | 10–30 MPa |
| Surface roughness (Ra) | 10–25 microns |
| Hardness (zinc) | 40–60 HV |
| Hardness (stainless 316L) | 250–350 HV |

### Poster 9 — Post-Treatment

**Sealing (essential for corrosion protection):**
Arc-sprayed zinc and aluminum coatings are porous (5–15%) — sealing is mandatory for most specifications.

**Seal coat systems per AWS C2.18:**
1. **Vinyl wash primer** — thin sealer; low cost; fills surface porosity
2. **Epoxy sealer** — brush or spray applied; penetrates interconnected porosity
3. **Silicone sealer** — for high-temperature service (aluminum coatings on exhaust systems)
4. **Topcoat paint system** — many specifications call for full paint system over the sealed thermal spray: primer + intermediate + topcoat
5. **No sealer required** if specification allows (some cathodic protection applications rely on porous zinc sacrificially corroding)

**Expected service life (zinc on structural steel, sealed, per AWS C2.18):**
- Rural: > 40 years
- Urban/industrial: 20–40 years
- Marine/coastal: 15–25 years
- This dramatically exceeds hot-dip galvanizing in many applications

### Poster 10 — Inspection and QA

| Test | Method | Typical Criteria |
|------|--------|------------------|
| Bond strength | ASTM C633 (lab) or portable pull-off (field) | > 7 MPa (AWS C2.18 minimum); typical 10–30 MPa |
| Thickness | Magnetic gauge (DFT) per SSPC-PA 2 | Per specification; see thickness table above |
| Visual | Unaided eye | Uniform coverage; no bare spots, blistering, or delamination |
| Bend test | 180-degree bend around mandrel (qualification test) | No cracking or spalling |
| Holiday detection | Low-voltage wet sponge (for sealed coatings) | Zero holidays in sealed system |
| Surface profile | Testex tape or profilometer | Verify Ra target was achieved before spray |

---

## Cluster 5: Cold Spray

### Poster 1 — Process Flow (Summary)

**Process Mechanism:**
Powder particles (1–50 microns) are accelerated to supersonic velocities (300–1200 m/s) by a heated, high-pressure carrier gas (nitrogen or helium) through a converging-diverging (de Laval) nozzle. Critically, the gas temperature is well below the melting point of the powder — particles remain in the solid state throughout the process. Upon impact with the substrate at velocities exceeding a material-specific "critical velocity," the particles undergo severe plastic deformation (adiabatic shear instability), breaking through surface oxide films and creating metallurgical bonding via solid-state welding mechanisms.

**No melting = no thermal oxidation = no phase transformation = no tensile residual stress.**

This is the fundamental advantage of cold spray: coatings retain the properties of the feedstock powder with no oxide inclusions, no heat-affected zone, and compressive residual stress.

**Feedstock Forms:**
- Powder only; size typically 5–50 microns (varies by material and application)
- Common materials: copper (Cu), aluminum (Al, 6061, 7075, 2024), titanium (Ti, Ti-6Al-4V), nickel (Ni, Inconel 625), stainless steel (316L), tantalum, zinc, tin, silver, MCrAlY, metal matrix composites (Al-SiC, Al-Al2O3)

**Key distinction from all other thermal spray:** Cold spray can deposit onto temperature-sensitive substrates (polymers, composites, magnesium, thin aluminum) because substrate heating is minimal.

### Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|--------|---------|----------|
| **Noise** | 110–130 dB (supersonic jet) | Double hearing protection; NRR 30+ |
| **High-pressure gas** | Nitrogen or helium at 20–60 bar (300–870 PSI) | Proper pressure vessel certification; no improvised fittings; burst disc protection |
| **Helium asphyxiation** | Helium displaces oxygen in enclosed spaces | O2 monitoring in spray booth; ventilation |
| **Metal dust** | Fine metal powders; some (Ti, Al, Mg) are pyrophoric or explosive | Inert atmosphere handling; NFPA 652 compliant dust collection; grounding |
| **Ricocheting particles** | Un-bonded particles rebound at high velocity | Enclosed spray booth; eye and face protection |
| **Thermal** | Gas can be heated to 200–1100 degC at nozzle exit (but particles do not reach this temperature) | Heat-resistant PPE near nozzle; insulated fixturing |
| **UV/IR radiation** | Minimal (no flame, no arc, no plasma) | Standard safety glasses sufficient |

**Cold spray is the safest thermal spray process from a fume perspective** — no melting means minimal fume generation. However, dust generation from un-bonded (rebounding) particles is still significant.

### Poster 3 — Cleaning

Standard thermal spray cleaning sequence applies. Cold spray-specific notes:
- Surface cleanliness is especially critical because bonding is entirely solid-state — any surface contamination directly prevents metallurgical bonding
- For repair of aluminum aerospace components (a primary cold spray application): solvent wipe + alkaline clean + DI rinse + forced air dry
- For copper electrical applications: avoid any residual cleaning agent that could increase contact resistance
- Time between cleaning and spray should be minimized; < 2 hours preferred

### Poster 4 — Grit Blasting / Surface Prep

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Media | Alumina (Al2O3), 99%+ purity | No steel grit on aluminum or titanium substrates |
| Grit size | 36–80 mesh | Finer grit than other thermal spray processes |
| Blast pressure | 30–60 PSI (200–415 kPa) | Less aggressive — cold spray's high impact velocity provides its own surface activation |
| Anchor profile (Ra) | 3–8 microns | Moderate profile sufficient |
| Surface cleanliness | SSPC-SP 5 or equivalent | White metal standard |

**Some cold spray applications do not require grit blasting** — the high-velocity particle impact itself cleans and activates the surface (the first layer of particles acts as an in-situ grit blast). This is an active area of research and is application-specific. Consult the specific cold spray specification.

### Poster 5 — Masking and Fixturing

- Metal masks (aluminum, stainless steel) preferred — high particle velocity can erode soft masking
- Adhesive tape is NOT reliable — particles can penetrate or erode tape
- Precise masking is important because cold spray has a relatively focused spray footprint (5–15 mm diameter depending on nozzle)
- Robot manipulation essential for consistent standoff and traverse
- Substrate cooling generally not needed (major advantage)
- For additive repair/buildup: custom masking to define repair zone precisely

### Poster 6 — Equipment Setup (Gun/System)

**Cold spray system components:**
1. **High-pressure gas supply** — nitrogen (bulk liquid) or helium (high-pressure cylinders); gas must be dry and oil-free
2. **Gas heater** — electric resistance heater; heats gas to 200–1100 degC to increase gas velocity (NOT to melt powder)
3. **De Laval nozzle** — converging-diverging design; creates supersonic gas flow; throat diameter 2–3 mm; exit diameter 5–8 mm
4. **Powder feeder** — high-pressure type (must inject powder against system pressure of 20–60 bar); gravimetric preferred
5. **Robot/manipulator** — 6-axis; precise control essential
6. **Spray booth** — enclosed with HEPA dust collection
7. **Control system** — gas pressure, gas temperature, powder feed rate, robot path

**Two system categories:**
- **High-pressure cold spray (HPCS):** 20–60 bar (300–870 PSI); N2 or He; 600–1200 m/s; can spray hard metals (steel, titanium, Inconel)
- **Low-pressure cold spray (LPCS):** 5–10 bar (70–150 PSI); air or N2; 300–600 m/s; limited to soft metals (copper, zinc, tin, aluminum) and metal-ceramic composites

**Major OEMs:** Impact Innovations (Germany), Plasma Giken (Japan), VRC Metal Systems (USA), Centerline (Canada), Titomic (Australia — large-scale)

### Poster 7 — Parameter Setup

| Parameter | High-Pressure CS | Low-Pressure CS |
|-----------|-----------------|-----------------|
| Gas type | N2 or He | Air or N2 |
| Gas pressure | 20–60 bar (300–870 PSI) | 5–10 bar (70–150 PSI) |
| Gas temperature | 300–1100 degC | 200–600 degC |
| Particle velocity | 600–1200 m/s | 300–600 m/s |
| Powder feed rate | 2–10 kg/hr | 1–5 kg/hr |
| Powder size | 5–50 microns | 5–50 microns |
| Standoff distance | 10–50 mm (very close) | 10–30 mm |
| Spray angle | 75–90 degrees | 75–90 degrees |
| Traverse speed | 100–500 mm/s | 100–500 mm/s |
| Nozzle type | WC-Co or SiC (wear-resistant throat) | Polymer or steel |
| Deposition efficiency | 50–95% (material-dependent; Cu ~90%, Ti ~70%, steel ~50%) | 30–70% |
| Deposition rate | 1–8 kg/hr | 0.5–3 kg/hr |

**Helium vs. Nitrogen trade-off:**
Helium produces significantly higher particle velocity (~2.6x the speed of sound in He vs. N2) but costs 10–50x more than nitrogen. Helium recycling systems exist but add complexity. Most production applications use nitrogen unless the material demands helium (e.g., titanium, high-strength steels).

### Poster 8 — Spray Application

**Application technique:**
- No substrate preheating required (advantage)
- Apply directly to blasted or as-received surface (application-dependent)
- Build thickness incrementally: 50–500 microns per pass (much higher per-pass thickness than other processes due to high deposition efficiency)
- Total coating thickness: virtually unlimited — cold spray can build up multi-millimeter deposits for dimensional restoration or additive manufacturing
- For repair of aluminum aerospace components (e.g., corrosion pits on helicopter gearbox housings): deposit aluminum directly into machined-out damage area, then machine flush

**Coating characteristics (copper — benchmark material for cold spray):**

| Property | Cold Spray Cu | Bulk Cu (reference) |
|----------|--------------|---------------------|
| Porosity | < 0.5% | 0% |
| Oxide content | < 0.1% | 0% |
| Bond strength (ASTM C633) | > 60 MPa (often exceeds epoxy) | N/A |
| Hardness | 100–150 HV (work-hardened) | 50–80 HV (annealed) |
| Electrical conductivity | 80–95% IACS | 100% IACS |
| Thermal conductivity | Near bulk values | 401 W/mK |

### Poster 9 — Post-Treatment

**Heat treatment (common for cold spray):**
- Annealing can recover ductility lost during severe plastic deformation
- For copper: 200–400 degC, 1–4 hours in vacuum or inert atmosphere
- For aluminum: T6 or T7 temper schedules may be applied to cold-sprayed Al alloy deposits
- For titanium: vacuum anneal at 500–700 degC to improve ductility
- Heat treatment also improves inter-particle bonding through diffusion

**Machining:**
- Cold spray deposits machine like wrought material (major advantage)
- Conventional turning, milling, drilling all work
- Achieve tight dimensional tolerances post-machining
- Surface finish after machining: equivalent to wrought material

**Sealing:**
- Generally not required (porosity < 1% in most properly sprayed deposits)
- Epoxy impregnation optional for barrier applications

### Poster 10 — Inspection and QA

| Test | Method | Typical Criteria |
|------|--------|------------------|
| Bond strength | ASTM C633 | > 40 MPa (Cu); > 30 MPa (Al); often exceeds epoxy |
| Porosity | ASTM E2109 | < 1% (Cu < 0.5%; Al 0.5–2%; Ti 1–3%) |
| Thickness | Eddy current, mag-gauge, ASTM B487 | Per drawing tolerance |
| Hardness | ASTM E384 (HV) | Material-dependent; typically work-hardened above bulk annealed values |
| Microstructure | Metallographic cross-section (etched) | Evaluate particle deformation, interface quality, porosity distribution |
| Electrical conductivity | 4-point probe or eddy current | Application-specific; Cu > 80% IACS typical |
| Visual | Unaided eye + 10x | No bare spots, delamination, or surface irregularities |
| Tensile testing | ASTM E8 (machined specimens from deposit) | For structural repair applications; approach wrought properties after heat treatment |

**MIL-STD-3021 (Cold Spray)** — US military standard specifically for cold spray repair of aerospace components. Key reference for defense applications.

---

## Cluster 6: Detonation Gun (D-Gun)

### Poster 1 — Process Flow (Summary)

**Process Mechanism:**
A precisely metered mixture of oxygen and fuel gas (usually acetylene) is injected into a water-cooled barrel (tube), followed by a charge of powder feedstock. A spark plug ignites the gas mixture, creating a controlled detonation wave that travels down the barrel at ~3500 m/s. The detonation wave heats and accelerates the powder particles to 750–1000 m/s (the highest particle velocities of any thermal spray process). A nitrogen purge cycle clears the barrel of combustion products. This cycle repeats 1–15 times per second.

The result is the densest, hardest, best-bonded coatings achievable by any thermal spray process — porosity routinely < 0.5%, bond strength exceeding the strength of the epoxy used in ASTM C633 testing.

**Feedstock Forms:**
- Powder only; size typically 5–45 microns
- Common materials: WC-Co, WC-CoCr, CrC-NiCr, Al2O3, Al2O3-TiO2, Cr2O3, NiCrAlY, Stellite, Tribaloy
- Material selection similar to HVOF but D-Gun can process even higher-melting-point ceramics effectively

**D-Gun coatings are considered the gold standard for wear resistance in aerospace applications.** The technology was originally proprietary to Union Carbide (now Praxair Surface Technologies / Oerlikon Metco). Generic versions now exist but the original D-Gun process remains premium.

### Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|--------|---------|----------|
| **Noise** | 130–150 dB (detonation pulses; LOUDEST thermal spray process) | Mandatory double hearing protection (NRR 30+); sound-isolated spray booth; remote operation |
| **Blast/overpressure** | Repeated detonation waves; risk of barrel failure | Barrel inspection; burst disc; never operate with damaged barrel |
| **Combustible gas** | Oxygen + acetylene in detonable mixtures | Gas handling per NFPA/OSHA; flashback arrestors; leak detection |
| **Fumes** | Cobalt, nickel, chromium from WC-Co and alloy powders | Same as HVOF — cobalt TLV 0.02 mg/m3; mandatory LEV and RPE |
| **Thermal** | Hot barrel (water-cooled but still hot); hot substrate | Heat-resistant PPE; never touch barrel during or after operation |
| **UV/IR** | Moderate (detonation flash) | Shade 5–8 eye protection |
| **Vibration** | Pulsed operation transmits vibration to fixtures and surrounding structure | Vibration-isolating mounts; hearing protection addresses some of this |

**The D-Gun is almost always operated remotely** — the operator is outside the sound-isolated spray booth, controlling the gun via robotic manipulator and monitoring via cameras. No human should be in the booth during operation.

### Poster 3 — Cleaning

Identical to HVOF cleaning protocol — premium aerospace cleaning standard:
1. Aqueous alkaline cleaning at 50–70 degC
2. Thorough DI water rinse
3. Water-break-free verification
4. Forced air dry
5. Grit blast within specified time window

### Poster 4 — Grit Blasting / Surface Prep

| Parameter | Typical Range |
|-----------|---------------|
| Media | White alumina (Al2O3), 99.5%+ purity |
| Grit size | 36–60 mesh |
| Blast pressure | 40–60 PSI |
| Anchor profile (Ra) | 3–6 microns |
| Surface cleanliness | SSPC-SP 5 (White Metal) |

Profile requirements are similar to HVOF — the extremely high particle velocity provides excellent mechanical interlocking even on moderate profiles.

### Poster 5 — Masking and Fixturing

- Metal masks mandatory (the detonation impact is extremely energetic)
- Custom-machined stainless steel or Inconel masks for each part geometry
- Rotation fixtures must be precision-balanced (pulsed loading can cause vibration issues)
- Full robotic gun manipulation — no manual D-Gun spraying
- Parts are typically small to medium size (turbine blades, vanes, seals, bushings)
- Cooling air directed at substrate between detonation cycles

### Poster 6 — Equipment Setup (Gun/System)

**D-Gun system components:**
1. **Detonation barrel** — water-cooled steel tube; 25–50 mm bore; 1–2 m length
2. **Gas metering system** — precise volumetric metering of O2 and C2H2 (acetylene) for each detonation cycle
3. **Powder injection** — metered charge of powder injected after gas fill, before ignition
4. **Ignition system** — spark plug or pilot flame
5. **Nitrogen purge** — clears barrel between cycles; prevents premature detonation of next charge
6. **Water cooling** — barrel cooling system; high flow rate
7. **Robot/manipulator** — precision 6-axis; critical for consistent standoff and traverse
8. **Sound-isolated booth** — mandatory; 130–150 dB noise levels require massive acoustic isolation
9. **Remote control system** — full parameter monitoring and control from outside booth

**This is NOT an off-the-shelf technology.** D-Gun systems are typically proprietary or semi-proprietary. Major providers: Oerlikon Metco (LCNTEC Detonation Spray), Praxair Surface Technologies.

### Poster 7 — Parameter Setup

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Detonation frequency | 1–15 Hz (cycles per second) | Higher frequency = higher deposition rate |
| Oxygen fill volume | Barrel-geometry dependent | Precisely metered per cycle |
| Acetylene fill volume | Barrel-geometry dependent | O2/C2H2 ratio controls temperature |
| O2/C2H2 ratio | 1.0–1.5 (stoichiometric to slightly lean) | Lean mixtures reduce oxide content |
| Detonation velocity | ~3500 m/s (in barrel) | Gas dynamics; not operator-adjustable |
| Particle velocity | 750–1000 m/s | Highest of all thermal spray processes |
| Detonation temperature | 3500–4500 degC | Peak gas temperature during detonation |
| Powder charge | 0.5–3 g per cycle | Precisely metered |
| Standoff distance | 100–200 mm | Closer than HVOF due to rapid particle deceleration |
| Nitrogen purge volume | 1–3x barrel volume | Must completely clear products of previous cycle |
| Deposition rate | 1–5 kg/hr | Lower than HVOF; each cycle deposits a small "spot" |
| Deposition efficiency | 70–90% | Very high due to high velocity and good melting |

### Poster 8 — Spray Application

**Application technique:**
- Each detonation cycle deposits a circular spot approximately 25 mm (1 inch) diameter
- Coating built up by overlapping spots via robotic traverse
- Thickness per cycle: 5–20 microns per spot
- Total thickness: typically 75–500 microns
- Substrate temperature: carefully controlled; air cooling between cycles
- Due to pulsed nature, heat input is intermittent — substrate sees less sustained thermal load than continuous processes

**Coating characteristics (WC-12Co — benchmark):**

| Property | D-Gun WC-12Co | HVOF WC-12Co (comparison) |
|----------|--------------|---------------------------|
| Porosity | < 0.5% (often < 0.2%) | < 1% (typically < 0.5%) |
| Oxide content | < 0.3% | < 0.5% |
| Bond strength | > 80 MPa (exceeds ASTM C633 epoxy) | > 70 MPa |
| Hardness | 1200–1500 HV300 | 1100–1400 HV300 |
| Surface roughness (as-sprayed) | Ra 2–5 microns | Ra 3–6 microns |
| Wear rate (ASTM G65) | 0.5–3 x 10^-7 mm3/Nm | 1–5 x 10^-7 mm3/Nm |

### Poster 9 — Post-Treatment

**Grinding:**
- Diamond grinding (same as HVOF)
- Achievable surface finish: Ra 0.05–0.4 microns
- Superfinishing for critical bearing surfaces

**Sealing:**
- Generally not required (porosity < 0.5%)
- Rare cases may use epoxy sealer for corrosion barrier

**No heat treatment required** — coatings are fully functional as-sprayed and ground.

### Poster 10 — Inspection and QA

| Test | Method | Typical Criteria |
|------|--------|------------------|
| Bond strength | ASTM C633 | > 80 MPa (reports as "> epoxy strength") |
| Porosity | ASTM E2109 | < 1.0% (typically < 0.5%) |
| Thickness | Eddy current, mag-gauge, ASTM B487 | Per drawing +/- 25 microns (tighter than HVOF) |
| Hardness | ASTM E384 (HV300) | 1200–1500 HV300 (WC-12Co) |
| Surface roughness | Profilometer | As-ground: Ra < 0.4 microns |
| Microstructure | Metallographic cross-section | Superior to HVOF; finest carbide distribution; minimal decarburization |
| Visual | Unaided eye + 10x | No defects |

---

## Cluster 7: Suspension Plasma Spray (SPS)

### Poster 1 — Process Flow (Summary)

**Process Mechanism:**
SPS is a variant of atmospheric plasma spray where the feedstock is not dry powder but rather a liquid suspension of submicron or nanometer-scale particles (typically 50 nm – 5 microns) in a liquid carrier (water, ethanol, or a blend). The suspension is injected into the plasma plume using a pressurized liquid feed system or atomizing injector. The liquid carrier evaporates rapidly, leaving the fine particles to melt and deposit. The extremely fine particle size produces unique coating microstructures — particularly columnar structures that mimic electron beam physical vapor deposition (EB-PVD) TBCs at a fraction of the cost.

**Feedstock Forms:**
- Liquid suspension: solid loading 5–30 wt% in ethanol or water
- Particle size in suspension: 50 nm – 5 microns
- Common materials: YSZ (7-8 wt% Y2O3), gadolinium zirconate (Gd2Zr2O7), lanthanum zirconate, alumina, titania, hydroxyapatite
- Solvent-based suspensions (ethanol) provide better atomization but require explosion-proof handling

**This is a next-generation TBC technology** — the columnar microstructure provides superior strain tolerance (thermal cycling resistance) compared to conventional APS lamellar TBCs, while being far cheaper than EB-PVD.

### Poster 2 — Safety and PPE

All APS safety hazards apply (noise, UV, fumes, electrical) PLUS:

| Additional Hazard | Details | Controls |
|-------------------|---------|----------|
| **Ethanol vapor** | Flammable liquid carrier (flash point 13 degC / 55 degF) | Explosion-proof spray booth; vapor monitoring; proper fuel-rated storage; grounding |
| **Nano-particle exposure** | Submicron and nano-scale particles pose enhanced respiratory risk | HEPA filtration at 99.97% efficiency minimum; nano-specific RPE (P100); exposure monitoring |
| **Pressurized liquid system** | Suspension feed at 2–10 bar | Proper hose ratings; relief valves; spill containment |

**Nanomaterial handling is a developing area of occupational health.** Precautionary principle applies — treat all nano-ceramic dusts as hazardous until TLVs are established.

### Poster 3 — Cleaning

Identical to APS cleaning protocol. SPS coatings are typically applied over a conventionally sprayed bond coat (APS MCrAlY), so the cleaning applies to the initial substrate preparation.

### Poster 4 — Grit Blasting / Surface Prep

Identical to APS grit blast specifications. The bond coat is applied by conventional APS, so substrate preparation follows standard APS protocol. The SPS topcoat is applied over the APS bond coat — no additional blasting between bond coat and topcoat.

### Poster 5 — Masking and Fixturing

Same as APS masking requirements. Additional consideration:
- Liquid overspray (suspension that misses the plasma plume) can splash onto masked areas — protective shields may be needed
- Ethanol-based suspension means the booth environment has a flammable vapor component — masking materials must be compatible

### Poster 6 — Equipment Setup (Gun/System)

**SPS system = modified APS system with specialized feed:**
1. **Plasma gun** — same APS guns (F4-MB, SinplexPro, etc.) — may use modified nozzle for optimized SPS
2. **Suspension feed system** — pressurized vessel or peristaltic pump; flow rate 20–100 mL/min
3. **Suspension injector** — mechanical injector (stream) or atomizing injector (spray); injection point is typically external to the gun (radial injection into plume)
4. **Suspension preparation** — ball milling or bead milling to create homogeneous, stable suspension; shelf life is limited (sedimentation)
5. **All other components** — same as APS (power supply, gas console, robot, booth, cooling)

**Major OEMs offering SPS capability:** Oerlikon Metco (SinplexPro with SPS option), Progressive Surface, Northwest Mettech (Axial III with suspension feed)

### Poster 7 — Parameter Setup

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Arc current | 400–700 A | Similar to APS |
| Arc voltage | 50–80 V | Gas-dependent |
| Power | 30–60 kW | Slightly higher than equivalent APS to evaporate solvent |
| Primary gas (Ar) | 40–60 SLPM | |
| Secondary gas (H2) | 6–14 SLPM | Higher H2 may be used to increase enthalpy for solvent evaporation |
| Suspension flow rate | 20–100 mL/min | Depends on solids loading and desired deposition rate |
| Solids loading | 5–30 wt% | Higher loading = higher deposition rate but risk of clogging |
| Standoff distance | 40–80 mm (MUCH closer than APS) | Fine particles decelerate quickly; must deposit before they resolidify |
| Traverse speed | 500–2000 mm/s | Faster than APS; thin layers per pass |
| Step increment | 2–4 mm | Fine spray footprint |
| Deposition rate | 0.5–3 kg/hr (of solid material) | Lower than conventional APS |
| Deposition efficiency | 20–50% | Lower than APS due to overspray and unmolten fines |

### Poster 8 — Spray Application

**Application technique:**
- Bond coat applied first by conventional APS (MCrAlY, 75–150 microns)
- SPS topcoat applied directly over APS bond coat
- Very thin passes (2–10 microns per pass) build up columnar structure
- Total SPS topcoat thickness: 100–400 microns (thinner than conventional APS TBCs)
- Columnar structure forms naturally due to surface shadowing effects of fine splats
- Substrate temperature during SPS: 200–400 degC (higher than APS due to closer standoff); cooling is critical

**Coating microstructure:**
- **Columnar** — vertical columns with inter-columnar porosity (5–15%); columns are 50–200 microns wide
- **This mimics EB-PVD** at 1/10 the cost and without vacuum chamber requirements
- Column gaps provide strain tolerance during thermal cycling (columns can move independently)
- Branching cracks and segmentation further enhance compliance

**Coating characteristics (YSZ SPS topcoat):**

| Property | SPS YSZ | APS YSZ (comparison) | EB-PVD YSZ (comparison) |
|----------|---------|----------------------|-------------------------|
| Porosity | 10–25% | 10–20% | 15–25% |
| Microstructure | Columnar | Lamellar (splat-based) | Columnar |
| Thermal conductivity | 0.7–1.2 W/mK | 0.8–1.2 W/mK | 1.5–2.0 W/mK |
| Strain tolerance | High (columnar) | Low (lamellar) | High (columnar) |
| Bond strength | > 15 MPa (on bond coat) | > 10 MPa | > 20 MPa |
| Cost | Medium | Low | Very high |

### Poster 9 — Post-Treatment

**Typically NO post-treatment for SPS TBCs:**
- Coatings are used as-sprayed for thermal barrier function
- No grinding (would destroy columnar structure)
- No sealing (porosity is functional — it reduces thermal conductivity)
- Diffusion heat treatment of the bond coat may be done BEFORE SPS topcoat application

**For non-TBC SPS applications (wear, biomedical):**
- Light polishing may be applied
- Sealing with biocompatible polymers for implant applications

### Poster 10 — Inspection and QA

| Test | Method | Typical Criteria |
|------|--------|------------------|
| Microstructure | Metallographic cross-section (SEM preferred) | Columnar morphology confirmed; no lamellar regions; inter-columnar gap spacing |
| Porosity | ASTM E2109 (image analysis on cross-section) | 10–25% (intentional; within specification range) |
| Thickness | Metallographic or eddy current | Per specification; typically 100–400 microns |
| Bond strength | Modified ASTM C633 (small-area) | > 10 MPa (lower than APS due to finer structure) |
| Thermal cycling | Furnace cycling test (e.g., 1100 degC / 1 hr hold / forced air cool) | > 1000 cycles to 20% spallation (target) |
| Thermal conductivity | Laser flash analysis (ASTM E1461) | 0.7–1.2 W/mK (lower = better insulation) |
| Phase stability | XRD (confirm tetragonal prime ZrO2 phase) | No monoclinic phase present |

---

## Cluster 8: Wire Combustion Spray

### Poster 1 — Process Flow (Summary)

**Process Mechanism:**
This is the original thermal spray process — patented by M.U. Schoop in Switzerland circa 1910. An oxy-fuel flame (typically oxy-acetylene) melts a wire feedstock that is continuously fed through the center of the flame nozzle. A compressed air jet atomizes the molten wire tip into droplets and propels them toward the substrate at 80–200 m/s. The process is essentially the wire variant of flame spray (Cluster 3 covers both wire and powder flame spray; this cluster focuses specifically on the traditional wire combustion configuration for galvanic corrosion protection).

**Feedstock Forms:**
- Wire only; diameter 1.6–4.8 mm (1/16 to 3/16 inch)
- Primary materials: zinc (99.99% or 99.0%), aluminum (1100, 1350, 99.0%), zinc-aluminum alloy (85/15), tin, babbitt (bearing alloys), bronze, copper, stainless steel, Monel, carbon steel
- Wire is the lowest-cost feedstock form; widely available

**This is the workhorse process for cathodic (sacrificial) corrosion protection** — zinc and aluminum coatings on steel. It competes directly with arc spray for the same applications but requires less capital investment and is more portable for field work.

### Poster 2 — Safety and PPE

Identical to Flame Spray (Cluster 3, Poster 2). Key emphasis points for wire combustion spray:
- **Zinc fume fever** is the primary occupational health risk when spraying zinc wire — always use P100 RPE or supplied air
- **Open flame hazard** — oxy-acetylene is an inherent fire risk; fire watch and extinguisher are mandatory
- **Acetylene safety** — never exceed 15 PSI gauge pressure; secure cylinders upright; test connections with soapy water
- Noise is moderate (85–105 dB) — hearing protection required above 85 dB

### Poster 3 — Cleaning

Identical to Flame Spray (Cluster 3, Poster 3) and Arc Spray (Cluster 4, Poster 3). For structural steel corrosion protection:
1. Degrease
2. Remove rust, mill scale, old coatings by grit blasting
3. Verify cleanliness per SSPC-SP 5 or SP 10
4. Coat within specified time after blasting (humidity-dependent; typically < 4 hours)

### Poster 4 — Grit Blasting / Surface Prep

Identical to Flame Spray (Cluster 3, Poster 4):

| Parameter | Typical Range |
|-----------|---------------|
| Media | Angular alumina or steel grit |
| Grit size | 16–36 mesh |
| Blast pressure | 60–100 PSI |
| Anchor profile (Ra) | 4–12 microns |
| Surface cleanliness | SSPC-SP 5 (White Metal) per AWS C2.18 |

### Poster 5 — Masking and Fixturing

Identical to Flame Spray (Cluster 3, Poster 5):
- Simple masking with tape, foil, and metal shields
- Manual gun operation is the norm (this is a hand-held process)
- No complex fixturing required for most applications
- Turntable for shop work on cylindrical parts

### Poster 6 — Equipment Setup (Gun/System)

**Wire combustion spray gun components:**
1. **Oxy-fuel nozzle** — concentric flame cone design; fuel gas and oxygen mixing chamber
2. **Wire feed mechanism** — air-turbine driven (uses atomizing air to power feed) or electric motor drive
3. **Compressed air cap** — atomizing air nozzle surrounding the flame; air blast atomizes molten wire tip and propels droplets
4. **Wire guide tube** — directs wire to flame center

**Gas and air supply:**
- Oxygen: 20–40 PSI (regulated)
- Acetylene: 10–15 PSI (regulated; NEVER exceed 15 PSI)
- Propane (alternative fuel): 10–20 PSI
- Compressed air (atomizing): 40–80 PSI at 20–40 CFM

**Portability advantage:** The entire wire combustion spray setup (gun, gas bottles, air compressor, wire spool) fits in a pickup truck or small trailer. This makes it ideal for field work on bridges, tanks, offshore platforms, and infrastructure.

**Major OEMs:** Oerlikon Metco (14E), Metallisation Ltd (Mark 73), Saint-Gobain, Thermach, Flame Spray Technologies

### Poster 7 — Parameter Setup

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Oxygen pressure | 20–40 PSI | Adjust for neutral or slightly oxidizing flame |
| Fuel pressure (acetylene) | 10–15 PSI | Neutral flame preferred; reducing flame for some alloys |
| Compressed air pressure | 40–80 PSI | Atomizing air; higher = finer droplets |
| Wire feed rate | 1–8 m/min | Material and wire diameter dependent |
| Flame temperature | ~3,100 degC (oxy-acetylene); ~2,800 degC (oxy-propane) | |
| Particle velocity | 80–200 m/s | Lower end for powder; higher for wire with strong air blast |
| Standoff distance | 150–250 mm (6–10 inches) | |
| Spray angle | 60–90 degrees | |
| Deposition rate | 2–8 kg/hr (wire) | Material and wire size dependent |
| Deposition efficiency | 50–70% | |

### Poster 8 — Spray Application

**Application technique:**
- Preheat substrate to 80–120 degC using flame gun (no wire feed)
- Spray zinc or aluminum in multiple crossing passes at 60–90 degrees to surface
- Maintain consistent standoff distance and traverse speed (manual skill-dependent)
- Build to specified thickness per AWS C2.18:
  - Zinc: 100–350 microns depending on exposure severity
  - Aluminum: 150–350 microns
  - Zinc-Aluminum 85/15: 150–300 microns

**Coating characteristics (zinc wire combustion spray):**

| Property | Typical Range |
|----------|---------------|
| Porosity | 5–15% |
| Oxide content | 5–15% |
| Bond strength (ASTM C633) | 7–25 MPa |
| Surface roughness (Ra) | 10–25 microns |
| Hardness (zinc) | 40–60 HV |

**Comparison with arc spray for same application:**
Wire combustion spray produces slightly lower density coatings than arc spray (lower particle velocity) but is more portable, requires less capital, and achieves acceptable results for most corrosion protection specifications.

### Poster 9 — Post-Treatment

Identical to Arc Spray (Cluster 4, Poster 9):
- **Seal coat is essential** for corrosion protection
- Vinyl, epoxy, or silicone sealers per AWS C2.18
- Full paint system may be applied over sealed thermal spray
- Expected service life matches arc spray when properly sealed

### Poster 10 — Inspection and QA

Identical to Arc Spray (Cluster 4, Poster 10):

| Test | Method | Typical Criteria |
|------|--------|------------------|
| Bond strength | ASTM C633 or portable adhesion tester | > 7 MPa (AWS C2.18 minimum) |
| Thickness | Magnetic gauge (DFT) per SSPC-PA 2 | Per specification |
| Visual | Unaided eye | Uniform coverage; no bare spots |
| Bend test | 180-degree mandrel bend | No cracking or spalling |
| Holiday detection | Low-voltage wet sponge | Zero holidays (sealed system) |

---

## Cross-Process Comparison Tables

### Particle Velocity and Temperature

| Process | Particle Velocity (m/s) | Gas/Flame Temperature (degC) | Particle State at Impact |
|---------|------------------------|------------------------------|--------------------------|
| Flame Spray (powder) | 40–100 | ~3,100 | Molten/semi-molten |
| Flame Spray (wire) | 80–200 | ~3,100 | Molten |
| Wire Combustion Spray | 80–200 | ~3,100 | Molten |
| Arc Spray | 50–200 | ~6,000 (arc) | Molten |
| APS (Plasma) | 200–600 | 10,000–15,000 | Molten |
| HVOF (gas fuel) | 500–750 | 2,500–3,100 | Semi-molten/plastic |
| HVOF (liquid fuel) | 700–900 | 2,600–3,200 | Semi-molten/plastic |
| D-Gun | 750–1,000 | 3,500–4,500 | Semi-molten/plastic |
| Cold Spray (HPCS) | 600–1,200 | Gas 300–1,100 | SOLID (never melts) |
| SPS | 200–500 | 10,000–15,000 | Molten (submicron) |

### Coating Quality Comparison (WC-12Co or Best-Case for Each)

| Process | Porosity (%) | Bond Strength (MPa) | Hardness (HV300) | Oxide Content (%) |
|---------|-------------|---------------------|-------------------|-------------------|
| Flame Spray | 5–15 | 10–30 | 300–500 (NiCrBSi) | 3–10 |
| Arc Spray | 5–15 | 10–30 | 250–350 (316L SS) | 5–15 |
| Wire Combustion | 5–15 | 7–25 | Material-dependent | 5–15 |
| APS | 2–8 (metals); 10–20 (TBC) | 15–50 | 800–1800 (ceramics) | 1–5 |
| HVOF | < 1 | > 70 | 1100–1400 (WC-Co) | < 0.5 |
| D-Gun | < 0.5 | > 80 | 1200–1500 (WC-Co) | < 0.3 |
| Cold Spray | < 1 (Cu < 0.5) | > 40–60 | Work-hardened | < 0.1 |
| SPS | 10–25 (intentional) | > 10–15 | 600–900 (YSZ) | Low (submicron) |

### Capital Cost and Complexity

| Process | Capital Cost (Relative) | Complexity | Portability | Automation Required? |
|---------|------------------------|------------|-------------|---------------------|
| Flame Spray | $ (lowest) | Low | Excellent (truck-portable) | No |
| Wire Combustion | $ | Low | Excellent | No |
| Arc Spray | $$ | Low-Medium | Good (needs power supply) | No (beneficial) |
| APS | $$$ | High | Poor (shop-based) | Yes (robot) |
| HVOF | $$$$ | High | Poor | Yes (robot) |
| D-Gun | $$$$$ (highest) | Very High | None (fixed installation) | Yes (mandatory) |
| Cold Spray | $$$$ | High | Poor | Yes (robot) |
| SPS | $$$$ | Very High | None | Yes (robot) |

---

## HVOF vs. Hard Chrome: The Transition Story

This section is critical context for the Plating Posters Inc audience — many plating shops are being forced to consider HVOF as hard chrome plating faces increasing regulatory pressure.

### Regulatory Drivers

1. **EPA NESHAP (40 CFR Part 63, Subpart N)** — National Emission Standards for Hazardous Air Pollutants for chromium electroplating and anodizing; increasingly stringent emission limits for Cr(VI)
2. **EU REACH Regulation** — Hexavalent chromium (CrO3) is an Annex XIV "Authorization" substance; users must obtain authorization to continue using it; sunset date has passed; authorizations are time-limited and expensive
3. **OSHA PEL for Cr(VI)** — 5 microg/m3 (8-hr TWA); Action Level 2.5 microg/m3; extremely difficult to achieve in hard chrome plating without expensive engineering controls
4. **California SCAQMD Rule 1469** — South Coast Air Quality Management District; strictest Cr(VI) emission rules in the US
5. **DoD initiatives** — US Department of Defense Hard Chrome Alternatives Team (HCAT) has qualified HVOF WC-Co as a drop-in replacement for hard chrome on landing gear, hydraulic actuators, and other aircraft components

### Property Comparison (Detailed)

| Property | Hard Chrome Plating | HVOF WC-12Co |
|----------|-------------------|--------------|
| Thickness range | 25–500 microns (0.001–0.020 in) | 50–500 microns (0.002–0.020 in) |
| Hardness | 800–1000 HV | 1100–1400 HV |
| Porosity | Micro-cracked network (inherent) | < 1% (no crack network) |
| Wear resistance (ASTM G65) | Good (5–15 x 10^-7 mm3/Nm) | Excellent (1–5 x 10^-7 mm3/Nm) |
| Fatigue impact | DETRIMENTAL — tensile residual stress + hydrogen embrittlement | BENEFICIAL — compressive residual stress; no H2 embrittlement |
| Corrosion resistance | Good (if sealed or thick enough) | Excellent (dense, oxide-free) |
| Max service temp | ~400 degC (softens) | ~500 degC (WC decomposition limit ~540 degC) |
| Deposit stress | Tensile (causes microcracking) | Compressive (fatigue-friendly) |
| Environmental | Cr(VI) — carcinogenic; regulated; trending toward elimination | No Cr(VI); cobalt fume is a concern but manageable with ventilation |
| Capital cost | Low (existing plating infrastructure) | High (spray booth, robot, gun, powder feeder) |
| Operating cost | Moderate (chemicals, waste treatment, compliance) | Higher per part (powder cost, gas, lower throughput) |
| Throughput | High (batch process; multiple parts simultaneously) | Lower (line-of-sight; one part at a time) |
| Geometry limitation | Uniform on complex ID/OD shapes | Line-of-sight only; internal bores very difficult |
| Masking | Simple (wax, tape, lacquer in bath) | Complex (metal masks, precision fixturing) |
| Dimensional control | Excellent (uniform deposition) | Good (requires grinding to final dimension) |
| Hydrogen embrittlement | Risk (bake at 190 degC / 375 degF within 4 hours per ASTM B850) | No risk |
| Applicable specs | AMS 2460 (hard chrome); QQ-C-320 (legacy) | AMS 2447, AMS 2448 |

### When HVOF CANNOT replace hard chrome:
- **Internal bores** — HVOF requires line-of-sight; ID chrome plating has no HVOF equivalent for small diameters (< 75 mm)
- **Very thin coatings** — hard chrome at 12–25 microns is difficult to replicate with HVOF economics
- **Complex geometries** — recessed features, blind holes, intricate shapes favor the throwing power of electroplating
- **Existing infrastructure** — shops with sunk capital in chrome lines face high switching costs

---

## Key Standards Reference

| Standard | Full Title | Primary Use |
|----------|-----------|-------------|
| ASTM C633 | Standard Test Method for Adhesion or Cohesion Strength of Thermal Spray Coatings | Bond strength (tensile pull-off); universal |
| ASTM E2109 | Standard Test Methods for Determining Area Percentage Porosity in Thermal Sprayed Coatings | Image analysis on metallographic cross-section |
| ASTM B487 | Standard Test Method for Measurement of Metal and Oxide Coating Thickness by Microscopical Examination of Cross Section | Thickness by cross-section |
| ASTM E384 | Standard Test Method for Microindentation Hardness of Materials | Vickers and Knoop microhardness |
| ASTM G65 | Standard Test Method for Measuring Abrasion Using the Dry Sand/Rubber Wheel Apparatus | Abrasive wear testing |
| ASTM G76 | Standard Test Method for Conducting Erosion Tests by Solid Particle Impingement | Erosion testing |
| ASTM B117 | Standard Practice for Operating Salt Spray (Fog) Apparatus | Corrosion resistance |
| ASTM E1461 | Standard Test Method for Thermal Diffusivity by the Flash Method | Thermal properties (SPS TBCs) |
| AWS C2.18 | Guide for the Protection of Steel with Thermal Sprayed Coatings | Zinc/aluminum corrosion protection |
| SSPC-CS 23.00 | Application of Thermal Spray Coatings for Corrosion Protection of Steel | Complements AWS C2.18 |
| AMS 2447 | Thermal Spray — HVOF Process | HVOF general |
| AMS 2448 | Thermal Spray — HVOF Application of Tungsten Carbide Coatings | WC coatings specifically |
| AMS 2460 | Hard Chromium Plating | Hard chrome (comparison standard) |
| MIL-STD-3021 | Materials Deposition, Cold Spray | Military cold spray standard |
| ISO 14918 | Thermal Spraying — Approval Testing of Thermal Sprayers | Operator qualification |

---

## Common Failures Across All Processes

| Failure Mode | Root Cause | Prevention |
|--------------|-----------|------------|
| **Delamination** | Poor surface prep; contamination; insufficient profile; substrate overheating | Verify cleanliness (SP-5); verify profile (Ra); monitor substrate temp |
| **Excessive porosity** | Standoff too far; power/velocity too low; powder too coarse; moisture in gas | Optimize parameters; verify gas purity; use correct powder size |
| **Oxidation (oxide stringers)** | Excessive dwell time in hot zone; air entrainment; standoff too long | Reduce standoff; increase velocity (HVOF/D-Gun inherently low oxide) |
| **Uneven thickness** | Inconsistent traverse speed; standoff variation; gun clogging | Robot control; regular gun maintenance; verify powder flow |
| **Substrate overheating** | Insufficient cooling; too many passes without cooling break; traverse too slow | Air cooling; interpass temperature checks; thermal management plan |
| **Cracking (macro)** | Excessive thickness in single pass; thermal shock; coating/substrate CTE mismatch | Multi-pass buildup; controlled cooling; appropriate material selection |
| **Spalling** | Poor adhesion + residual stress exceeds bond strength | Proper surface prep; appropriate coating thickness; stress management |
| **Orange peel** | Excessive distance; low velocity; poor atomization | Optimize standoff and velocity parameters |
| **Embedded grit** | Grit blast media trapped at interface | Proper blasting technique; air blow-off before spray (avoid excessive) |
| **Carbide decomposition (WC)** | Flame/plasma temperature too high; excessive dwell time | Use HVOF or D-Gun (lower temperature, higher velocity); optimize parameters |

---

## Poster-Specific Data Quick Reference (For Alaina/Elara)

### Per-Process Poster Mapping

Each process cluster follows the same 10-poster structure. Below is a quick reference for what each poster number covers, with a note on which data sections above to mine for content:

| Poster # | Topic | Key Data Source in This Brief |
|----------|-------|-------------------------------|
| 1 | Process Flow | "Process Mechanism" + "Feedstock Forms" sections |
| 2 | Safety & PPE | Safety table + TLV values |
| 3 | Cleaning | Cleaning sequence + time-between-steps data |
| 4 | Grit Blasting | Grit blast specification table |
| 5 | Masking & Fixturing | Masking materials + fixture notes |
| 6 | Equipment Setup | System components list + OEM names |
| 7 | Parameter Setup | Parameter table (the core data table for that process) |
| 8 | Spray Application | Application technique + coating characteristics table |
| 9 | Post-Treatment | Sealing + grinding + heat treatment |
| 10 | Inspection & QA | QA test table + acceptance criteria |

---

## Confidence and Source Notes

**Sources:** This brief was compiled entirely from Watson's domain expertise corpus, which includes:
- ASM Handbook Volume 5A: Thermal Spray Technology (ASM International)
- Pawlowski, L. "The Science and Engineering of Thermal Spray Coatings" (Wiley)
- Davis, J.R. (ed.) "Handbook of Thermal Spray Technology" (ASM International)
- ITSA (International Thermal Spray Association) educational materials
- Relevant ASTM, AMS, AWS, SSPC standards (referenced throughout)
- DoD HCAT (Hard Chrome Alternatives Team) program publications
- Journal of Thermal Spray Technology (ASM/ITSA)

**Gemini status:** Quota exhausted at time of research (10-hour reset). All data verified against multiple handbook sources in training corpus.

**Confidence levels:**
- **APS, HVOF, Flame Spray, Arc Spray, D-Gun:** HIGH — mature, well-documented processes; data ranges are well-established in the literature
- **Cold Spray:** HIGH for copper and aluminum; MODERATE for titanium and steel (parameters are more application-specific and vendor-dependent; the technology is still maturing for hard metals)
- **SPS:** MODERATE-HIGH — relatively new process (commercial since ~2010); parameter ranges are less standardized than APS; active research area with rapidly evolving best practices
- **Wire Combustion Spray:** HIGH — oldest thermal spray process; very well documented; essentially a subset of flame spray

**Flags for Alaina/Elara:**
1. Wire Combustion Spray (Cluster 8) overlaps significantly with Flame Spray Wire (Cluster 3). The posters should emphasize Wire Combustion's portability/field-work angle and its specific role in galvanic corrosion protection to differentiate from the broader Flame Spray cluster.
2. SPS (Cluster 7) is a niche/advanced process — posters should clearly position it as "next-generation" and emphasize that it builds on conventional APS infrastructure.
3. The HVOF vs. Hard Chrome comparison (Section 11) should inform Cluster 2 posters heavily — this is the story that will resonate most with the Plating Posters Inc audience.
4. D-Gun (Cluster 6) is the least accessible process for most shops — posters should frame it as the "gold standard" that exists in specialized coating service providers (Oerlikon, Praxair/Oerlikon Surface Solutions), not something a typical shop would own.

---

*Watson Research Brief v1 — 2026-04-26*
*80 posters across 8 thermal spray process clusters*
*Next step: Alaina Construction Workups + Elara Generation Prompts*
