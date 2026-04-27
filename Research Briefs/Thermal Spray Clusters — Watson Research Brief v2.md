---
title: Thermal Spray Clusters — Watson Research Brief v2
author: Watson (watson-chemistry-researcher)
date: 2026-04-26
version: v2
supersedes: v1 (same date; v2 adds expanded equipment tables, defect matrices, OSHA PEL master table, post-treatment detail, and cross-process selection guide)
purpose: Technical research brief for 80 posters across 8 thermal spray process clusters (10 posters each)
status: COMPLETE — domain expertise build (Gemini quota exhausted)
confidence: HIGH for APS, HVOF, Flame Spray, Arc Spray, Cold Spray, D-Gun; MODERATE-HIGH for SPS; HIGH for Wire Combustion
tags:
  - ThermalSpray
  - PlatingPosters
  - WatsonResearch
---

# Thermal Spray Clusters — Watson Research Brief v2

> **Note to Alaina:** This v2 brief merges and expands v1 data. Each cluster covers all 10 poster topics with numerical data. The 10-step process sequence is deliberately consistent across all 8 clusters so poster layouts can share a common template. Items marked ^ have moderate confidence and should be verified when Gemini quota resets.

---

# TABLE OF CONTENTS

- [Master Comparison Table](#master-comparison-table)
- [Universal Reference Data](#universal-reference-data)
- [Cluster 1: Atmospheric Plasma Spray (APS)](#cluster-1-atmospheric-plasma-spray-aps)
- [Cluster 2: HVOF (High Velocity Oxy-Fuel)](#cluster-2-hvof-high-velocity-oxy-fuel)
- [Cluster 3: Flame Spray (Wire and Powder)](#cluster-3-flame-spray-wire-and-powder)
- [Cluster 4: Arc Spray (Twin Wire)](#cluster-4-arc-spray-twin-wire)
- [Cluster 5: Cold Spray](#cluster-5-cold-spray)
- [Cluster 6: Detonation Gun (D-Gun)](#cluster-6-detonation-gun-d-gun)
- [Cluster 7: Suspension Plasma Spray (SPS)](#cluster-7-suspension-plasma-spray-sps)
- [Cluster 8: Wire Combustion Spray](#cluster-8-wire-combustion-spray)
- [Cross-Process Selection Guide](#cross-process-selection-guide)
- [HVOF vs. Hard Chrome: The Transition Story](#hvof-vs-hard-chrome-the-transition-story)
- [Key Standards Reference](#key-standards-reference)
- [Confidence and Source Notes](#confidence-and-source-notes)

---

# MASTER COMPARISON TABLE

| Parameter | APS | HVOF | Flame Spray | Arc Spray | Cold Spray | D-Gun | SPS | Wire Combustion |
|---|---|---|---|---|---|---|---|---|
| Particle velocity (m/s) | 200-600 | 600-1000 | 30-180 | 100-250 | 300-1200 | 800-1000 | 200-600 | 30-180 |
| Particle/gas temp (C) | 10,000-15,000 (plasma) | 2,500-3,100 | 2,500-3,100 | 5,000-6,000 (arc) | 300-1,100 (gas; particles solid) | 3,000-4,500 | 10,000-15,000 | 2,500-3,100 |
| Standoff distance (mm) | 75-150 | 150-380 | 120-250 | 100-200 | 10-50 | 75-120 | 50-80 | 120-250 |
| Deposit efficiency (%) | 40-70 | 50-75 | 30-70 | 50-70 | 70-95 | 80-95 | 30-50^ | 50-70 |
| Coating thickness (um) | 50-2,000+ | 50-500 | 50-2,500 | 50-5,000 | 50-5,000+ | 25-500 | 5-100 | 50-2,500 |
| Porosity (%) | 3-10 | <2 | 5-15 | 5-15 | <1 | <2 | 2-8^ | 5-15 |
| Bond strength (MPa) | 20-70 | 50-90+ | 10-30 | 15-40 | 30-100+ | 60-90+ | 20-60^ | 10-30 |
| Noise level (dB) | 110-130 | 125-140 | 90-105 | 100-115 | 110-130 | 140-160 | 110-130 | 90-105 |
| Spray rate (kg/hr) | 2-10 | 3-12 | 2-12 | 10-50 | 1-8 | 1-5 | <1 | 2-12 |
| Power input (kW) | 40-80 | 80-300+ (combustion) | 10-50 (combustion) | 5-15 (electrical) | 20-60 (gas heater) | N/A (pulsed) | 40-80 | <1 (wire motor only) |

---

# UNIVERSAL REFERENCE DATA

## Standards Applicable Across All Processes

| Standard | Title / Scope |
|----------|---------------|
| ASTM C633 | Bond strength of thermal spray coatings (tensile adhesion test) |
| ASTM E2109 | Porosity measurement by image analysis |
| ASTM E1920 | Metallographic preparation of thermal sprayed coatings |
| ASTM B487 | Coating thickness by metallographic cross-section |
| ASTM E384 | Microhardness testing (Knoop and Vickers) |
| ASTM B499 | Thickness by magnetic method (coating on ferrous substrate) |
| ASTM B244 | Thickness by eddy current method |
| ASTM B568 | Thickness by XRF |
| ASTM B117 | Salt spray (fog) testing |
| ASTM D4541 | Pull-off strength (portable adhesion tester) |
| AWS C2.18/C2.23 | Thermal spray of Al, Zn, and alloys for corrosion protection of steel |
| SSPC-SP5 / NACE No. 1 | White Metal Blast Cleaning |
| ISO 8501 (SA 3) | Visual cleanliness of blast-cleaned surfaces |
| AMS 2447 | HVOF coating of hardface alloys (general) |
| AMS 2448 | HVOF application of tungsten carbide coatings |
| MIL-STD-1687A | Thermal spray processes (legacy; still referenced) |

## OSHA PELs for Common Thermal Spray Materials

| Material | OSHA PEL (mg/m3, 8-hr TWA) | ACGIH TLV (mg/m3) | Notes |
|---|---|---|---|
| Chromium metal / Cr(III) | 1.0 | 0.5 | |
| Chromium Cr(VI) | 0.005 | 0.01 | Carcinogen; hexavalent form |
| Nickel (insoluble) | 1.0 | 0.2 (inhalable) | IARC Group 1 (some Ni compounds) |
| Cobalt | 0.1 | 0.02 | Sensitizer; IARC 2B with WC |
| Aluminum (metal dust) | 15 (total) / 5 (resp.) | 1.0 (resp.) | |
| Zinc oxide (fume) | 5.0 | 2.0 | Metal fume fever |
| Copper (fume) | 0.1 | 0.2 | |
| Tungsten (insoluble, as W) | 5.0 | 3.0 | |
| Molybdenum (insoluble) | 10.0 | 0.5 (resp.) | |
| Yttrium compounds | 1.0 | 1.0 | |
| Iron oxide (fume) | 10.0 | 5.0 (resp.) | Siderosis |
| Titanium dioxide | 15.0 (total) | 10.0 | IARC 2B |
| Zirconia (as Zr) | 5.0 | 5.0 | |

## Grit Blast Media Quick Reference

| Media | Typical Grit Size | Hardness (Mohs) | Best For | Avoid On |
|---|---|---|---|---|
| White alumina (Al2O3 99.5%) | 24-60 mesh | 9 | Aerospace; Ti; stainless; no Fe contamination | -- |
| Brown alumina (Al2O3 96%) | 24-60 mesh | 9 | General steel; lower cost | Ti (Fe contamination risk) |
| Steel grit (angular) | G25-G80 | 7-8 | Heavy structural steel; bridges | Al, Ti, stainless, Cu alloys |
| Silicon carbide | 24-80 mesh | 9.5 | Very hard substrates | Soft substrates (embeds) |
| Garnet | 36-80 mesh | 7-8 | Moderate profiles; aluminum | -- |
| Glass bead | -- | 5-6 | Peening; cosmetic | NOT for thermal spray prep |

## Substrate Temperature Limits During Spray

| Substrate | Max Temp (C) | Notes |
|---|---|---|
| Low-carbon steel | 150-200 | Higher OK if no dimensional concern |
| Tool steel (heat-treated) | 150 | Avoid tempering |
| Aluminum alloys | 120-150 | Annealing risk |
| Magnesium alloys | 100-120 | Very sensitive; cold spray preferred |
| Titanium alloys | 150-200 | Oxidation above 400 C |
| Polymers / composites | 60-80 | Cold spray only realistic option |
| Copper alloys | 150-200 | Good thermal conductor |
| Nickel superalloys | 200-300 | More tolerant; still monitor |

## Universal Masking Materials

| Material | Max Service Temp (C) | Adhesive | Reusable | Best For |
|---|---|---|---|---|
| Glass cloth / silicone tape | 260-315 | Silicone | No | General high-temp masking |
| Aluminum foil tape | 315+ | Acrylic or silicone | No | Heat-reflective; good conformability |
| Polyester tape | 150-200 | Silicone | No | Low-temp processes (cold spray, arc spray) |
| Sheet metal shields | N/A | Clamped/magnetic | Yes | Large flat areas; straight edges |
| Silicone rubber plugs | 260-315 | N/A | Yes | Holes, bores, threaded holes |
| Copper or brass shims | N/A | Clamped | Yes | Precision edge masking |
| Moldable putty (silicone) | 260 | Self-adhering | Limited | Complex contours |
| Liquid maskant (peel-off) | 200-260 | Self-leveling | No | Complex geometry; large areas |
| Ceramic fiber tape | 1000+ | Adhesive or wire-tied | No | Extreme temperature zones |

---

# CLUSTER 1: ATMOSPHERIC PLASMA SPRAY (APS)

## Poster 1 — Process Flow

**How It Works:**
A DC electric arc is struck between a tungsten cathode and a copper anode inside the plasma gun. Plasma-forming gas (argon, nitrogen, or mixtures with hydrogen or helium) flows through the arc and ionizes, creating a plasma jet at 10,000-15,000 C (core can exceed 20,000 C). Powder feedstock is injected radially (or axially in newer designs) into the plasma plume, melted and accelerated to 200-600 m/s. Molten droplets ("splats") impact the prepared substrate, flatten, solidify, and mechanically interlock to build the coating layer by layer.

**What Makes APS Different:**
- Highest flame temperature of any atmospheric thermal spray process
- Most versatile: can spray virtually any material that melts without decomposing (ceramics, cermets, metals)
- The workhorse of thermal spray; largest installed base worldwide
- Coatings are inherently lamellar (pancake-splat microstructure) with oxide inclusions between splats

**Feedstock:**
- Powder only (no wire capability in standard APS)
- Powder size: 10-90 um (finer for dense coatings, coarser for TBCs)

**Key Applications:**
- Thermal barrier coatings (TBCs): YSZ (7-8 wt% Y2O3) on turbine blades/vanes — largest APS application by volume
- Wear-resistant ceramics: Cr2O3, Al2O3-TiO2 on rolls, plungers, cylinders
- Abradable coatings: NiCrAl-Bentonite, AlSi-Polyester for blade tip clearance
- Bond coats: MCrAlY (NiCoCrAlY, NiCrAlY) under TBCs
- Biomedical: Hydroxyapatite on orthopedic implants
- Corrosion: Al and Zn on structural steel

**Typical Coating Materials:**

| Material | Composition | Hardness (HV0.3) | Primary Use |
|---|---|---|---|
| YSZ | ZrO2-8%Y2O3 | 900-1200 | Thermal barrier |
| Chromium oxide | Cr2O3 | 1400-1800 | Wear / printing rolls |
| Alumina-titania | Al2O3-3%TiO2 or -13%TiO2 | 800-1100 | Wear / dielectric |
| MCrAlY | NiCoCrAlY or NiCrAlY | 250-350 | Bond coat / oxidation |
| Molybdenum | Mo | 400-600 | Wear (piston rings) |
| Hydroxyapatite | Ca10(PO4)6(OH)2 | 300-500 | Biomedical |
| NiAl (80/20) | Ni-20Al | 150-250 | Bond coat (exothermic) |
| Abradable | NiCrAl-Bentonite / AlSi-Polyester | 50-200 | Clearance control |

**10-Step Process Sequence:**
1. Part receipt, inspection, documentation (identify substrate, drawing requirements)
2. Pre-blast cleaning: solvent wipe or aqueous degrease
3. Grit blast to specified profile (Ra 3-12 um typical)
4. Mask and fixture: tape, plugs, shields; mount cylindrical parts on rotation fixture
5. Equipment setup: verify gas pressures, powder feeder cal, gun cooling water
6. Parameter setup: arc current, gas flows, powder feed rate, standoff per qualified recipe
7. Spray application: traverse gun at controlled speed; monitor part temperature
8. Post-spray inspection: visual, thickness measurement
9. Post-treatment: grinding/polishing to final dimension; sealing if required
10. Final QA: bond strength coupon, metallographic cross-section, hardness, dimensional check

---

## Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|---|---|---|
| **Noise** | 110-130 dB at operator position | Double hearing protection (plugs NRR 29-33 + muffs NRR 25-30); OSHA 90 dBA 8-hr TWA limit |
| **UV/IR radiation** | Intense UV-A/B/C and near-IR from plasma arc; equivalent to welding | Shade 6-10 welding helmet or full face shield; no exposed skin |
| **Metal/ceramic fume** | NiCr, Co, Cr, ZrO2, Al2O3 fumes; varies by feedstock | PAPR with P100 or supplied-air respirator; HEPA booth filtration |
| **Dust explosion** | Fine metal powders (Al, Ti, Mg) explosive when airborne | Inert atmosphere powder handling; grounding; no open flames near feeder |
| **Thermal burns** | Hot substrate, fixtures, overspray | Heat-resistant leather gloves; leather apron; face shield |
| **Electrical** | DC power 40-80 kW; 500-1000 A; 50-80 V; HF arc start | Lockout/tagout; deionized cooling water; insulated gloves for gun work |
| **Compressed gas** | Argon (asphyxiant); hydrogen (4-75% LEL, explosive); helium, nitrogen | Flash-back arrestors on H2; gas leak detection; O2 monitors in booth |
| **Overspray dust** | Respirable particles settle throughout booth | Enclosed booth; 100+ lfm face velocity; cartridge/baghouse collector |

**Full PPE Table:**

| Item | Specification |
|---|---|
| Hearing protection | NRR 25+ (dual plug + muff recommended above 115 dB) |
| Eye/face | Full face shield, shade 6-10, or auto-darkening welding helmet |
| Respiratory | PAPR with P100 or supplied air; minimum N95 outside booth |
| Hands | Heavy leather gauntlets; heat-resistant to 300 C |
| Body | Flame-resistant coveralls or leather apron; NO synthetic fabrics near booth |
| Feet | Steel-toe boots with metatarsal guards |
| Head | Hard hat or bump cap if overhead work |

**Booth Requirements:**
- Enclosed spray booth; minimum 100 linear feet per minute (lfm) face velocity
- Typical exhaust: 4,000-8,000 CFM for walk-in booth
- Walls: non-combustible (steel or concrete block)
- Dust collection: cartridge or baghouse with HEPA secondary; spark arrestor upstream
- Fire suppression (dry chemical or CO2) mandatory for metallic powder operations
- Explosion-proof electrical fittings (Class II, Division 1 per NEC)

---

## Poster 3 — Cleaning

**Pre-spray cleaning sequence:**
1. **Solvent degrease:** Acetone, IPA, or MEK on lint-free cloth using two-cloth method (wet wipe then dry wipe before evaporation). Removes oils, grease, machining fluids, fingerprints.
2. **Aqueous alkaline wash (alternative):** pH 10-12, 50-70 C, 5-15 minutes immersion or spray. Rinse thoroughly with DI water.
3. **Vapor degrease (legacy):** Perchloroethylene or trichloroethylene vapor. Effective but declining due to EPA NESHAP regulations. Still used in some aerospace shops.
4. **Ultrasonic cleaning:** 25-40 kHz in aqueous solution. Excellent for complex geometry.
5. **Inspection:** Water-break-free test (ASTM F22 equivalent) — clean surface sustains unbroken water film for 30+ seconds.
6. **Dry:** Forced air or oven dry. No moisture at time of grit blast.

**Critical rules:**
- Clean BEFORE masking — never mask over contaminated surfaces
- Minimize time between cleaning and grit blast (same shift preferred)
- Time between grit blast and spray: <4 hours (specification dependent; some aerospace specs require <2 hours; titanium: immediately)
- Never touch blasted surfaces with bare hands — wear clean lint-free gloves

---

## Poster 4 — Grit Blasting

| Parameter | Steel Substrate | Aluminum Substrate | Titanium Substrate |
|---|---|---|---|
| Abrasive | Brown or white Al2O3, 24-36 grit | White Al2O3, 36-60 grit | White Al2O3, 36 grit |
| Blast pressure (PSI) | 40-80 | 30-50 | 30-60 |
| Nozzle standoff (inches) | 4-8 | 6-10 | 6-8 |
| Blast angle | 60-90 degrees | 45-75 degrees | 60-90 degrees |
| Target Ra (um) | 4-10 | 3-8 | 4-8 |
| Target Ra (microinches) | 160-400 | 120-320 | 160-320 |
| Target Rz (um) | 30-80 | 20-60 | 30-60 |
| Surface cleanliness | SSPC-SP5 / NACE No. 1 (White Metal) or ISO SA 3 | Same | Same |

**Why alumina over steel grit for aerospace:**
- No ferrous contamination risk on nickel or titanium substrates
- Alumina fractures to expose fresh cutting edges (self-sharpening)
- Steel grit embeds and causes galvanic corrosion sites

**Profile verification methods:**
- Testex press-o-film replica tape + micrometer (field method)
- Contact profilometer (Ra, Rz measurement) for precision
- Visual comparison to SSPC-VIS 1 standards

**Why grit blast is critical:** Thermal spray adhesion is PRIMARILY MECHANICAL INTERLOCKING. Molten splats flow into surface irregularities and lock on solidification. Unlike electroplating (metallurgical/chemical bond), thermal spray depends almost entirely on mechanical bonding + Van der Waals forces. Insufficient roughness = delamination. Excessive roughness on soft substrates = fold-over peaks trapping porosity at interface.

---

## Poster 5 — Masking and Fixturing

**APS masking materials:**
- High-temperature masking tape (glass cloth / silicone adhesive; rated 260-315 C)
- Aluminum foil tape (315+ C; heat-reflective)
- Metal masks (mild steel, stainless, copper) — preferred for production; reusable
- Silicone plugs and caps for holes, bores, threads
- Ceramic fiber tape for extreme temperature zones
- Thermal spray maskant (liquid peel-off; 200-260 C)
- Copper or brass shims for precision edge masking

**Fixturing:**
- Cylindrical parts: lathe-type rotation fixture; 50-200 RPM depending on diameter
- Flat parts: angle fixture; gun traverses in raster pattern
- Cooling air nozzles directed at substrate backside — critical for temperature control
- Fixture must not shadow spray pattern; design for line-of-sight access
- Ground fixture to workpiece for electrostatic discharge prevention
- Fixtures must be robust — APS gun recoil and heat are significant

**Overspray management:**
- APS generates 30-60% overspray — settles on everything in booth
- Regular booth cleaning to prevent debris contaminating coatings
- Booth floor grating with collection bin below

---

## Poster 6 — Equipment Setup

**System components:**
1. **Plasma gun:** Cathode (2% thoriated tungsten), anode (oxygen-free copper), gas injection ring, powder injector port(s)
2. **Power supply:** 40-80 kW DC; 500-1000 A at 50-80 V; three-phase 480V input, 200-400A service
3. **Gas console:** Mass flow controllers for primary + secondary gas
4. **Powder feeder:** Volumetric or gravimetric; carrier gas (Ar) delivers powder; feed rate 20-100 g/min
5. **Robot/manipulator:** 6-axis industrial robot for production; manual for repair
6. **Cooling system:** Closed-loop deionized water; 15-25 L/min at 15-25 C inlet; <40 C outlet; conductivity <5 uS/cm
7. **Spray booth:** Enclosed with cartridge/baghouse dust collection; HEPA secondary
8. **Control system:** PLC or proprietary controller; monitors all parameters real-time

**Gas supply table:**

| Gas | Role | Flow (SLPM) | Supply Pressure (PSI) |
|---|---|---|---|
| Argon | Primary plasma gas | 30-50 | 80-120 |
| Nitrogen | Alternate primary | 30-60 | 80-120 |
| Hydrogen | Secondary (enthalpy) | 5-15 | 50-80 |
| Helium | Alternate secondary | 20-50 | 50-80 |
| Argon | Powder carrier | 3-8 | 40-60 |

**Powder notes:** Powder must be dry (oven dry at 100-120 C for 2-4 hrs if needed). Standard sizes: -45/+15 um for Cr2O3, YSZ; -106/+45 um for abradables.

---

## Poster 7 — Parameter Setup

| Parameter | Typical Range | Effect of Increase |
|---|---|---|
| Arc current (A) | 400-800 | Higher particle temperature; better melting; risk of overheating substrate |
| Arc voltage (V) | 50-80 | Determined by gas composition/flow; higher with H2 |
| Power (kW) | 25-80 | = V x A; higher = more enthalpy |
| Primary gas — Ar (SLPM) | 35-60 | Higher velocity; shorter dwell time; less melting |
| Secondary gas — H2 (SLPM) | 5-15 | Dramatically higher enthalpy; better heat transfer to powder |
| Secondary gas — He (SLPM) | 20-50 | Milder than H2; more uniform heating |
| Carrier gas — Ar (SLPM) | 3-8 | Delivers powder; too high pushes powder through plume |
| Powder feed rate (g/min) | 20-80 | Higher throughput; risk of unmelted particles |
| Standoff distance (mm) | 75-150 | Closer = denser, hotter at impact; farther = cooler, more oxide |
| Traverse speed (mm/s) | 200-1000 | Faster = thinner per pass; less substrate heating |
| Step increment (mm) | 3-6 | 25-50% overlap of spray footprint |
| Spray angle | 75-90 degrees optimal | Below 45 degrees: shadowing and porosity |

**Effect on coating properties:**
- **Porosity:** Controlled by particle temp, velocity, spray angle. Higher temp + velocity = lower porosity. APS typical: 3-10%; TBCs often intentionally 10-15% (strain tolerance).
- **Hardness:** Function of material + degree of melting. Well-melted Cr2O3: 1400-1800 HV. Undermelted = softer with visible unmelted particles.
- **Bond strength:** Maximized by high velocity, clean substrate, proper roughness, perpendicular angle. APS: 20-70 MPa (ASTM C633).
- **Oxidation:** Oxide inclusions between splats from atmospheric exposure. Higher traverse speed and shorter standoff reduce oxidation.
- **Deposit efficiency:** 40-70%; axial-injection guns achieve higher DE than radial-injection.

---

## Poster 8 — Spray Application

**Application technique:**
- Preheat substrate to 80-120 C using plasma gun (no powder) to improve first-layer adhesion
- Apply bond coat first if specified (e.g., NiAl or MCrAlY at 50-150 um)
- Build thickness in multiple passes:
  - 10-30 um/pass for ceramics (YSZ, Cr2O3)
  - 15-50 um/pass for metals and MCrAlY
  - 25-75 um/pass for abradables
- Typical total: 100-500 um for ceramics; up to 2000 um for some metallic/abradable
- For TBCs: bond coat (MCrAlY, 75-150 um) + topcoat (YSZ, 250-500 um)
- Spray spot diameter: 8-15 mm
- Step size: 3-6 mm (50-75% of spot width)
- Monitor part temperature with pyrometer; keep below substrate limits (see Universal table)
- Interpass cooling with compressed air jets when needed

**Common defects:**

| Defect | Cause | Prevention |
|---|---|---|
| High porosity | Low particle temp; excessive standoff; worn electrodes | Optimize power; reduce standoff; replace electrodes per maintenance schedule |
| Delamination | Contaminated substrate; insufficient roughness; excessive thickness | Re-blast; verify cleanliness; limit thickness per spec |
| Vertical cracking (ceramics) | Tensile stress from rapid splat cooling | Often acceptable/desirable for TBCs (segmentation cracking improves thermal cycling life) |
| Unmelted particles | Insufficient power; oversized powder; high feed rate | Increase power; verify powder size distribution; reduce feed rate |
| High surface roughness | Low traverse speed; large step size | Increase traverse speed; reduce step size |
| Oxidation (dark coating) | Excessive standoff; slow traverse | Reduce standoff; increase traverse speed |
| Substrate overheating | Traverse too slow; insufficient cooling | Faster traverse; add interpass cooling air jets |

---

## Poster 9 — Post-Treatment

**Sealing:**
- Organic sealants (epoxy, phenolic, silicone): vacuum impregnation or brush-applied; seals interconnected porosity; max service 200-300 C
- Inorganic sealants (chrome phosphate, aluminum phosphate): higher temperature service (540 C for CrPO4, 700+ C for AlPO4); used on TBCs and wear coatings
- Wax or oil: low-temperature corrosion sealing for Zn/Al coatings on structural steel
- Laser glazing: densifies surface; specialty/research applications

**Grinding and finishing:**
- As-sprayed Ra: 5-15 um
- Diamond or CBN wheels for ceramics; SiC or Al2O3 for metals
- Grinding coolant must be compatible (no chlorinated coolants on Ti substrates)
- Finish targets: Ra 0.2-0.8 um for bearing surfaces; 0.8-3.0 um general wear
- Typical stock removal: 50-200 um from as-sprayed surface
- Honing or lapping for precision bores (e.g., Cr2O3 on hydraulic cylinders)

**Heat treatment:**
- Diffusion HT for MCrAlY bond coats: 1050-1100 C in vacuum (<10^-4 torr), 2-4 hours — creates metallurgical bond to superalloy substrate
- Stress relief for thick metallic coatings: 400-600 C, 1-2 hours, inert atmosphere
- TBC topcoats generally NOT heat treated

---

## Poster 10 — Inspection and QA

| Test | Method | Typical Acceptance |
|---|---|---|
| Bond strength | ASTM C633 (25.4 mm pull stub, FM1000 epoxy, cure 175 C/1hr, pull 1.3 mm/min) | Ceramics: >10-20 MPa; metals: >30-50 MPa; spec-dependent |
| Porosity | ASTM E2109 image analysis on polished cross-section (200-500x) | TBCs: 10-20% (intentional); wear coatings: <5%; dense ceramics: <3% |
| Thickness | ASTM B487 (metallographic); B499 (magnetic); B244 (eddy current) | Per drawing; typically +/- 50 um |
| Hardness | ASTM E384 Vickers (HV0.3 or HV0.1 on cross-section; min 5 indents averaged) | Cr2O3: 1400-1800 HV; YSZ: 900-1200 HV; MCrAlY: 250-350 HV |
| Surface roughness | Profilometer (Ra, Rz) | As-sprayed: 5-15 um; ground: 0.2-1.6 um |
| Microstructure | Metallographic cross-section | No unexpected cracks, delamination, unmelted particles, excessive oxide stringers |
| Visual | Unaided eye + 10x loupe | No blistering, spalling, discoloration, bare spots; clean masking lines |
| Bend test | Mandrel bend (qualitative) | No cracking or spalling at specified radius |
| Macro-hardness | Rockwell HR15N (thick coatings >300 um, porosity <3%) | Process-specific |

**ASTM C633 failure mode interpretation:**
- Adhesive (at interface): poor surface prep — investigate substrate cleanliness and roughness
- Cohesive (within coating): weak coating — investigate spray parameters, powder quality
- Glue failure: test invalid — re-test. If consistent glue failure above 70 MPa, coating bond likely exceeds test method capability

---

# CLUSTER 2: HVOF (HIGH VELOCITY OXY-FUEL)

## Poster 1 — Process Flow

**How It Works:**
A fuel (hydrogen, propane, propylene, kerosene, or natural gas) combusts with oxygen at high pressure (5-10 bar) inside a water-cooled combustion chamber. The hot gases (2500-3100 C) accelerate through a converging-diverging (de Laval) nozzle to supersonic velocity (Mach 1.5-3.0). Powder feedstock injected axially into the gas stream is heated to near-melting/semi-molten state and accelerated to 600-1000 m/s. The extremely high kinetic energy produces dense, well-bonded coatings with minimal porosity and low oxide content.

**What Makes HVOF Different:**
- Highest velocity of combustion-based processes (600-1000 m/s vs 200-600 for APS)
- Lower particle temperature than APS — particles semi-molten, not fully molten. Preserves carbide phases in WC-Co (less decarburization)
- Produces the densest atmospheric thermal spray coatings (porosity <2%)
- Compressive residual stress (vs tensile in APS) — allows thicker coatings without cracking
- The gold standard for hard chrome replacement

**The hard chrome replacement story:** HVOF WC-Co/CoCr is the aerospace and defense industry's primary replacement for hard chromium electroplating. EPA NESHAP and EU REACH regulations on hexavalent chromium are driving this transition globally. HVOF coatings match or exceed hard chrome in hardness (1100-1400 HV vs 800-1000 HV for chrome), wear resistance, and fatigue life while eliminating all Cr(VI) exposure.

**Key Applications:**
- Hard chrome replacement: WC-Co, WC-CoCr on landing gear, hydraulic rods, printing rolls
- Wear: WC-Co, Cr3C2-NiCr on pump shafts, valves, turbine components
- Corrosion: NiCr, Hastelloy, Inconel on oil and gas components
- Aerospace: midspan dampers, compressor blade tips
- Paper/printing: Cr2O3 and WC on rolls

**Typical Coating Materials:**

| Material | Composition | Hardness (HV0.3) | Primary Use |
|---|---|---|---|
| WC-12%Co | Tungsten carbide-cobalt | 1100-1400 | Wear; hard chrome replacement |
| WC-10%Co-4%Cr | WC-CoCr | 1100-1450 | Wear + corrosion (best all-around) |
| Cr3C2-25%NiCr | Chromium carbide-NiCr | 800-1000 | High-temp wear (to 870 C) |
| Stellite 6 (CoCrW) | Cobalt alloy | 400-600 | Erosion; valve seats |
| Tribaloy T-800 | CoMoCrSi | 500-700 | Wear + corrosion at high temp |
| Inconel 625 | NiCrMoNb | 250-400 | Corrosion; oil and gas |

**10-Step Process Sequence:**
1. Part receipt, inspection, dimensional documentation
2. Pre-blast cleaning: solvent wipe or aqueous degrease
3. Grit blast: white Al2O3, 24-36 grit, to Ra 3-8 um
4. Mask and fixture: heat-resistant tape, metal shields; rotation for cylindrical parts
5. Equipment setup: fuel/O2 supply pressures, combustion chamber purge, powder feeder calibration
6. Parameter setup: O2/fuel ratio, chamber pressure, powder feed rate, standoff per recipe
7. Spray application: controlled traverse; part temperature monitoring (HVOF transfers significant heat)
8. Post-spray visual inspection and thickness check
9. Diamond grinding to final dimension: Ra 0.1-0.4 um for chrome replacement
10. Final QA: hardness, bond strength, porosity, dimensional verification, salt spray if specified

---

## Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|---|---|---|
| **Noise** | 125-140 dB (supersonic jet) — one of the loudest thermal spray processes | MANDATORY dual hearing protection (plugs NRR 29-33 + muffs NRR 25-30); double-wall booth construction recommended |
| **IR radiation** | Intense IR from combustion; less UV than plasma (no arc) | Shade 3-5 face shield |
| **Combustible gas** | H2 (4-75% LEL); propane (2.1% LEL); propylene (2.0% LEL); kerosene vapor | Gas detection + auto-shutoff; flash-back arrestors; flame-out detection |
| **Cobalt fume** | WC-Co is the primary HVOF material; Co PEL 0.1 mg/m3, TLV 0.02 mg/m3; IARC 2B with WC | PAPR P100 or supplied air; HEPA booth filtration; biological monitoring for Co-exposed workers |
| **Cr, Ni fume** | From Cr3C2-NiCr, Inconel, Stellite | Same respiratory protection as Co |
| **Combustion chamber pressure** | 5-10 bar continuous; catastrophic failure risk if maintenance is neglected | Fuel/O2 flow interlocks; regular chamber inspection; pressure relief valve |
| **Dust explosion** | WC-Co powder is combustible in fine sizes | Inert atmosphere handling; grounding; NFPA 652 compliant collector |

**Full PPE Table:**

| Item | Specification |
|---|---|
| Hearing | NRR 29+ foam plugs AND over-ear muffs simultaneously |
| Eye/face | Full face shield, shade 3-5 |
| Respiratory | PAPR P100 or supplied air (cobalt/Cr exposure concern) |
| Hands | Heavy leather gauntlets |
| Body | FR coveralls; leather apron for direct spray |
| Feet | Steel-toe boots |

**Booth:** Same as APS plus: fuel gas leak detection with automatic shutoff; acoustic baffles for noise attenuation; HEPA filtration recommended for WC-Co.

---

## Poster 3 — Cleaning

Same as APS (Cluster 1, Poster 3). Particular emphasis on removing machining coolant residue — WC-Co coatings are very sensitive to interface contamination. Two-cloth solvent wipe is standard.

---

## Poster 4 — Grit Blasting

| Parameter | Value |
|---|---|
| Abrasive | White Al2O3, 24-36 grit (preferred) |
| Blast pressure | 40-60 PSI (steel); 30-50 PSI (aluminum) |
| Nozzle standoff | 4-8 inches |
| Angle | 60-90 degrees |
| Target Ra | 3-8 um (120-320 microinches) |
| Target Rz | 25-60 um |
| Cleanliness | SSPC-SP5 or equivalent |
| Time to spray | 2 hours max; 30 min preferred |

**Note:** HVOF achieves excellent bond strength even at moderate roughness due to the very high particle velocity. Some specs allow Ra as low as 2.5 um for thin coatings on precision substrates. For hard chrome replacement on hydraulic rods: blast to Ra 3-5 um, spray WC-CoCr, grind to Ra 0.1-0.2 um.

---

## Poster 5 — Masking and Fixturing

- HVOF generates more heat at the part than APS due to continuous high-enthalpy gas impingement
- Metal shields preferred over tape (tape can char at HVOF heat levels)
- Masking materials must withstand continuous 200-300 C
- Cylindrical parts: rotation fixture at 100-300 RPM (rods) or 50-100 RPM (large cylinders)
- Precise masking for hard chrome replacement work (tight dimensional tolerances)

---

## Poster 6 — Equipment Setup

**System components:**
1. **Combustion chamber:** Water-cooled; fuel and O2 injected, ignited, and pressurized to 5-10 bar
2. **De Laval nozzle:** Accelerates gas to supersonic velocity
3. **Fuel/O2 control:** Mass flow controllers; automatic ratio control
4. **Powder feeder:** Gravimetric or volumetric; 30-100 g/min; powder must be dry (WC-Co is hygroscopic)
5. **Robot:** 6-axis; precise traverse for uniform coating
6. **Cooling:** Water-cooled gun; 15-25 L/min; no deionization required (no arc)
7. **Ignition system:** Spark or pilot flame; flame-out detection with auto-shutoff

**Gas/fuel supply:**

| Gas/Fuel | Flow Rate | Supply Pressure (PSI) |
|---|---|---|
| Oxygen | 400-1000 SLPM | 150-250 |
| Hydrogen (fuel) | 400-800 SLPM | 100-200 |
| Propane (fuel) | 40-80 SLPM | 80-120 |
| Propylene (fuel) | 50-100 SLPM | 80-120 |
| Kerosene (liquid fuel) | 15-25 L/hr | Pumped at 100-200 PSI |
| Nitrogen (carrier) | 10-20 SLPM | 60-100 |

**Power:** HVOF guns are combustion-powered (no DC arc). Total electrical: 5-15 kW for controls, feeder, robot.

---

## Poster 7 — Parameter Setup

| Parameter | Gas Fuel (H2, propane) | Liquid Fuel (kerosene) |
|---|---|---|
| O2 flow (SLPM) | 400-900 | 800-1000 |
| Fuel flow | H2: 400-700 SLPM; C3H8: 50-80 SLPM | 15-25 L/hr |
| O:F ratio | Slightly fuel-lean (1.05-1.20x stoichiometric O2) | Slightly fuel-lean |
| Chamber pressure (bar) | 5-8 | 6-10 |
| Powder feed rate (g/min) | 30-80 | 40-100 |
| Standoff (mm) | 200-350 | 300-380 |
| Traverse speed (mm/s) | 300-1000 | 300-1000 |

**Parameter effects:**
- **O:F ratio:** Controls flame temp and gas velocity. Lean = hotter, more oxide; rich = cooler, risk of carbon inclusion. Optimal: slightly lean.
- **Chamber pressure:** Higher = higher velocity = denser coating. Limited by hardware design.
- **Standoff:** HVOF has the longest standoff of any thermal spray (up to 380 mm for liquid fuel). Closer = hotter part; farther = lower velocity at impact.
- **Porosity:** <2% routinely; <1% with optimized parameters on WC-Co
- **Hardness:** WC-12Co HVOF: 1100-1400 HV. Key: preserve WC phase — avoid decarburization (W2C, eta phase)
- **Bond strength:** 50-90+ MPa; ASTM C633 glue failure at 70-80 MPa is common (actual bond higher)
- **Deposit efficiency:** 50-75% (WC-Co); higher for metallic powders

---

## Poster 8 — Spray Application

- Traverse speed: 300-1000 mm/s (typically 500-750)
- Step size: 3-5 mm
- Spray spot: 6-12 mm diameter
- Thickness per pass: 10-25 um (WC-Co); 15-40 um (Cr3C2-NiCr); 20-50 um (metallic)
- Part temperature: must stay below 150-200 C; compressed air cooling between passes
- Pyrometer monitoring essential

**Common defects:**

| Defect | Cause | Prevention |
|---|---|---|
| Decarburization (WC decomposition to W2C/eta) | Excessive particle temp; high O:F ratio; long dwell | Optimize O:F; reduce power; shorter standoff |
| Delamination | Poor surface prep; excessive coating stress; too thick | Proper blast; control thickness; interpass cooling |
| Spalling at edges | Stress concentration at coating terminations | Feather edges; radius substrate edges before spray |
| Orange peel texture | Excessive feed rate; partially melted particles | Reduce feed rate; optimize combustion |
| Microcracking (post-grind) | Excessive grinding heat | Diamond wheels; flood coolant; 0.01-0.02 mm/pass |

---

## Poster 9 — Post-Treatment

**Grinding (critical for HVOF):**
- WC-Co: 1100-1400 HV — REQUIRES diamond grinding wheels
- Parameters: 100-150 SFPM, 0.01-0.02 mm per pass, flood coolant (water-based)
- **NEVER dry grind HVOF carbide coatings** — thermal damage causes microcracking
- Final Ra for chrome replacement: 0.1-0.4 um (4-16 microinches)
- Superfinishing or lapping achieves Ra <0.1 um

**Sealing:** Generally not required (porosity <1-2%). For corrosion applications: optional epoxy seal after grinding.

**Heat treatment:** Generally not required. Some aerospace specs: low-temp stress relief 150-200 C for 2-4 hrs. Avoid >500 C on WC-Co (metastable carbide phase can decompose).

---

## Poster 10 — Inspection and QA

| Test | Method | Typical HVOF Values |
|---|---|---|
| Bond strength | ASTM C633 | WC-Co: >70 MPa (glue failure common = actual bond >70); Cr3C2-NiCr: 50-70; metallics: 50-80 |
| Porosity | Metallographic image analysis | WC-Co: <2% (typically <1%); Cr3C2-NiCr: 1-3% |
| Hardness | HV0.3 on cross-section | WC-12Co: 1100-1400; WC-CoCr: 1100-1450; Cr3C2-NiCr: 800-1000 |
| Thickness | Eddy current (non-ferrous) or magnetic (ferrous); micrometer | Typical WC-Co: 100-300 um (0.004-0.012") |
| Surface finish (post-grind) | Profilometer Ra, Rz | Chrome replacement: Ra 0.1-0.4 um |
| Salt spray | ASTM B117 | HVOF WC-CoCr routinely >1000 hrs (sealed or unsealed) |
| XRD (if specified) | Verify WC phase retention; check for W2C / eta phase | Confirm no decarburization |
| Bend/ductility | Mandrel bend (qualification) | Per specification |

---

# CLUSTER 3: FLAME SPRAY (WIRE AND POWDER)

## Poster 1 — Process Flow

**How It Works:**
An oxy-fuel flame (acetylene/O2 or propane/O2) melts feedstock delivered as wire or powder. For **wire flame spray**, wire feeds continuously into the flame center, melts, and is atomized by compressed air into droplets propelled toward the substrate. For **powder flame spray**, powder enters the flame by gravity or carrier gas and is carried to the substrate by combustion gases + air cap. Particle velocities are the lowest of all thermal spray: 30-180 m/s. Flame temperature: 2500-3100 C (oxy-acetylene hottest at ~3100 C).

**What Makes Flame Spray Different:**
- Simplest and lowest-cost thermal spray method
- Most portable — lightweight guns, minimal equipment
- Lowest particle velocity = highest porosity (5-15%), lowest bond strength (10-30 MPa)
- Limited to materials with melting point below ~2800 C (cannot effectively spray most ceramics)
- Excellent for large-area corrosion protection (Zn, Al)
- Unique capability: self-fluxing alloys (NiCrBSi) — spray + fuse for true metallurgical bond

**Key Applications:**
- Corrosion protection: Zn and Al on bridges, offshore platforms, storage tanks per AWS C2.23
- Dimensional restoration: worn journals, shafts, bearing housings (bronze, steel, babbitt)
- Bearing surfaces: bronze, babbitt on journal bearings
- Self-fluxing wear coatings: NiCrBSi spray + fuse at 1050-1100 C
- Field/portable repair work

**Typical Coating Materials:**

| Material | Form | Hardness (HV) | Spray Rate (kg/hr) | Primary Use |
|---|---|---|---|---|
| Zinc | Wire 1.6-4.8 mm | 40-60 | 3-12 | Cathodic corrosion protection |
| Aluminum | Wire 1.6-3.2 mm | 30-50 | 2-8 | Corrosion / oxidation |
| 85/15 ZnAl | Wire | 50-70 | 3-10 | Enhanced corrosion |
| Bronze (CuSn, CuAl) | Wire or powder | 100-200 | 2-6 | Bearing surfaces |
| Stainless steel | Wire | 200-400 | 2-6 | Corrosion/wear repair |
| NiCrBSi | Powder | 700-900 (fused) | 1-4 | Wear (after fusing) |
| Molybdenum | Wire | 400-600 | 1-4 | Wear (piston rings) |
| Babbitt | Wire | 20-30 | 3-8 | Bearing surfaces |

**Service life (Zn on structural steel, sealed, per AWS C2.18):**
- Rural: >40 years; Urban/industrial: 20-40 years; Marine: 15-25 years

**10-Step Process Sequence:**
1. Part receipt, inspection; document wear/corrosion damage
2. Pre-blast cleaning: solvent wipe, steam clean (field), or aqueous clean (shop)
3. Grit blast to Ra 4-12 um; or undercut machining for dimensional restoration
4. Mask non-spray areas
5. Equipment setup: verify gas supply (O2, fuel, air), wire/powder feed
6. Set flame parameters: gas pressures, wire feed speed, standoff
7. Apply bond coat if required (NiAl or NiCr wire, 50-100 um)
8. Spray primary coating to thickness
9. Post-spray: machine/grind to dimension; seal for corrosion applications
10. Inspect: thickness, visual, adhesion check (tap test, bend test for field)

---

## Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|---|---|---|
| **Noise** | 90-105 dB — quietest thermal spray process | NRR 20-25 hearing protection |
| **IR/flame** | Moderate IR from oxy-fuel flame; minimal UV | Shade 3-5 safety glasses or face shield |
| **Zinc fume** | Primary concern — causes metal fume fever ("zinc shakes"); PEL 5.0 mg/m3, TLV 2.0 mg/m3 | P100 half-face (outdoors); PAPR (indoor/booth) |
| **Oxy-fuel gases** | Acetylene: LEL 2.5%, NEVER exceed 15 PSI (decomposition); propane: LEL 2.1%; O2 enrichment | Flash-back arrestors; check valves; proper storage |
| **Compressed air** | 50-80 PSI | Standard high-pressure safety |

**PPE:** NRR 20-25 earplugs; shade 3-5 glasses/shield; P100 respiratory; leather gloves; cotton or FR coveralls; steel-toe boots.

---

## Poster 3 — Cleaning

Standard pre-spray cleaning. Field operations: steam clean, solvent wipe, or power wash with detergent. For large structural steel, blast cleaning often serves as both cleaning and roughening (provided surface is free of heavy grease — degrease first).

---

## Poster 4 — Grit Blasting

| Parameter | Value |
|---|---|
| Abrasive | Brown/white Al2O3, 16-36 grit; steel grit G25-G40 for structural steel |
| Blast pressure | 60-100 PSI (steel); 40-60 PSI (aluminum) |
| Standoff | 6-12 inches |
| Angle | 60-90 degrees |
| Target Ra | 4-12 um (160-500 microinches) |
| Target anchor profile | 2-4 mils (50-100 um) for corrosion coatings |
| Cleanliness | SSPC-SP5 / NACE No. 1 (White Metal) |
| Time to spray | 4 hrs max; less in humid conditions |

**Notes:** Flame spray relies heavily on mechanical interlocking — lower velocity means rougher profiles help adhesion. NiAl/NiCr bond coats are "self-bonding" (exothermic reaction at impact) and help on smooth/difficult substrates.

---

## Poster 5 — Masking and Fixturing

- Lower temps and velocities than APS/HVOF simplify masking
- Standard masking tape adequate in many cases
- Sheet metal shields for straight edges
- Handheld operation is common — skilled operator controls gun manually
- Machine-held gun + lathe rotation for cylindrical parts (journal restoration)

---

## Poster 6 — Equipment Setup

**Gas supply (oxy-acetylene wire flame spray):**

| Gas | Pressure (PSI) | Flow (SLPM) |
|---|---|---|
| Oxygen | 30-50 | 30-60 |
| Acetylene | 10-15 (NEVER exceed 15) | 15-30 |
| Compressed air | 50-80 | 200-500 |

**Gas supply (oxy-propane powder flame spray):**

| Gas | Pressure (PSI) | Flow (SLPM) |
|---|---|---|
| Oxygen | 20-40 | 20-50 |
| Propane | 10-20 | 10-25 |
| Carrier gas (N2/air) | 20-40 | 5-15 |

**Wire:** 1.6-4.8 mm diameter; 2-10 kg/hr feed rate. **Powder:** -106/+45 um; 10-60 g/min.
**Power:** Minimal — wire feed motor only. Can operate from portable generator or battery. Most portable thermal spray setup.

---

## Poster 7 — Parameter Setup

| Parameter | Wire Flame | Powder Flame |
|---|---|---|
| O2 pressure (PSI) | 30-50 | 20-40 |
| Fuel pressure (PSI) | 10-15 (C2H2) | 10-20 (propane) |
| Air pressure (PSI) | 50-80 | -- |
| Wire/powder feed | 2-10 kg/hr | 10-60 g/min |
| Standoff (mm) | 120-250 | 150-300 |
| Traverse speed (mm/s) | 100-500 | 100-400 |
| Deposit efficiency | 50-70% | 30-50% |

**Flame adjustment:** Neutral = cleanest coating; slightly oxidizing = hotter (good for high-MP wire); carburizing = avoid (carbon inclusion).

---

## Poster 8 — Spray Application

- Layer thickness: 30-100 um/pass; step size 5-10 mm
- Total thickness: 150-400 um (corrosion); 250-2500 um (restoration)
- Handheld requires skilled operator for uniformity
- Part temp generally <150 C
- Self-fluxing NiCrBSi exception: spray then fuse at 1050-1100 C with oxy-acetylene torch — creates metallurgical bond, pore-free coating, hardness 700-900 HV

**Common defects:** High porosity (low air pressure, long standoff); poor adhesion (contamination, blunt profile); rough/lumpy (wire feed inconsistency); thin spots (non-uniform traverse); wire stubbing (contacting substrate).

---

## Poster 9 — Post-Treatment

**Sealing (critical for corrosion coatings):** Zn/Al coatings are porous (5-15%) — sealing essential. Vinyl wash primer + epoxy + polyurethane topcoat per AWS C2.23 within 8 hours of spray. Typical bridge system: blast + Zn spray (150-300 um) + seal system = 20+ year service life.

**Self-fluxing fusing:** NiCrBSi powder sprayed then fused 1050-1100 C. B and Si act as fluxing agents. Only thermal spray method that produces true metallurgical bond through post-treatment.

**Machining:** Metallic coatings (bronze, stainless, babbitt) machine with standard tooling. Fused NiCrBSi requires diamond/CBN.

---

## Poster 10 — Inspection and QA

| Test | Method | Typical Values |
|---|---|---|
| Bond strength | ASTM C633 (lab); D4541 portable (field) | 10-25 MPa (wire); 15-30 with NiAl bond coat; fused NiCrBSi: 50-80 |
| Porosity | Metallographic | 5-15% (wire); 8-20% (powder); <1% (fused) |
| Thickness | Magnetic gauge, eddy current, micrometer | 150-400 um (corrosion); spec-dependent |
| Visual | Eye + loupe | Uniform coverage; no bare spots |
| Holiday detection | Low-voltage wet sponge (sealed coatings) | Zero holidays |
| Bend test | 180-degree mandrel (qualification) | No cracking/spalling |
| Tap test (field) | Hammer tap — bonded = solid; delaminated = hollow | Qualitative |

---

# CLUSTER 4: ARC SPRAY (TWIN WIRE)

## Poster 1 — Process Flow

**How It Works:**
A DC electric arc (5000-6000 C) is struck between two consumable wires that continuously feed toward each other. A high-velocity compressed air jet atomizes molten metal from the wire tips into fine droplets propelled at 100-250 m/s. No combustion gases needed — only electricity and compressed air.

**What Makes Arc Spray Different:**
- Highest spray rate of all thermal spray: 10-50 kg/hr (vs 2-10 for flame, 3-8 for plasma)
- Most economical per kg deposited (electricity + air; no expensive gases)
- Limited to electrically conductive wire (cannot spray ceramics or cermets directly)
- Can spray cored wires (metal sheath + ceramic/carbide fill) to extend material range
- Dominant process for large-area metallic corrosion coatings
- Higher oxidation than flame spray (extremely hot arc vaporizes more metal)

**Key Applications:**
- Anti-corrosion: Zn, Al, ZnAl on structural steel, tanks, offshore platforms
- EMI shielding: Zn or Cu on plastics and composites
- Dimensional restoration: steel, stainless, bronze buildups on worn parts
- Bond coats: NiAl 80/20 exothermic bond coat
- Boiler tubes: NiCr or FeCrAl cored wires for high-temp corrosion

**Typical Coating Materials:**

| Material | Wire Type | Spray Rate (kg/hr) | Primary Use |
|---|---|---|---|
| Zinc | Solid | 10-30 | Cathodic corrosion protection |
| Aluminum | Solid | 8-25 | Corrosion / oxidation |
| Zn-15Al | Solid or pseudo-alloy (dual wire) | 10-25 | Enhanced corrosion |
| NiAl 80/20 | Solid or cored | 5-15 | Bond coat |
| Carbon steel | Solid | 15-40 | Dimensional restoration |
| Stainless 316/420 | Solid | 10-30 | Corrosion/wear repair |
| Copper | Solid | 10-25 | EMI shielding |
| FeCrAl cored | Metal-cored | 8-20 | High-temp boiler corrosion |

**10-Step Process Sequence:**
1. Part receipt, inspection, dimensional measurement
2. Degrease or power wash
3. Grit blast to Ra 5-12 um (aggressive profile)
4. Mask; fixture cylindrical parts for rotation
5. Equipment setup: power supply, air compressor, wire feeders, wire alignment
6. Parameter setup: voltage, current, air pressure, wire feed speed, standoff
7. Bond coat if needed (NiAl 80/20, 50-100 um)
8. Spray primary coating; monitor thickness
9. Seal (corrosion) or machine (restoration)
10. Inspect: thickness, adhesion, visual

---

## Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|---|---|---|
| **Noise** | 100-115 dB | NRR 25+ hearing protection |
| **UV from arc** | Electric arc = UV (similar to welding) | Shade 5-8 face shield or welding helmet |
| **Zinc fume** | Arc spray of Zn produces copious fume (more per kg than flame spray due to higher arc temp) | PAPR P100 mandatory for indoor Zn |
| **Electrical** | 20-40 VDC, 100-400 A; wire is live during operation | Lockout/tagout for maintenance |
| **Splatter** | Large droplets from arc; wider spread than flame spray | Wider masking margins; face protection |

---

## Poster 3 — Cleaning

Same as flame spray. Field: power wash + solvent wipe. Shop: aqueous alkaline or solvent.

---

## Poster 4 — Grit Blasting

| Parameter | Value |
|---|---|
| Abrasive | Brown Al2O3 16-24 grit; steel grit G25-G40 |
| Blast pressure | 60-100 PSI |
| Standoff | 6-12 inches |
| Angle | 60-90 degrees |
| Target Ra | 5-12 um (200-500 microinches) |
| Profile depth | 2-4 mils (50-100 um) for corrosion coatings |
| Cleanliness | SSPC-SP5 |
| Time to spray | 4 hrs max; 2 hrs in high humidity |

Arc spray produces large/fast splats — needs coarse anchor profile. Rougher-is-better vs HVOF.

---

## Poster 5 — Masking and Fixturing

- Moderate temp/velocity — standard masking tape works
- Sheet metal shields for edges
- WIDER masking margins than flame spray — arc spray produces more splatter (large droplets)
- Rotation fixture 50-200 RPM for cylindrical parts
- Gun: handheld (field) or robot/manipulator (production)

---

## Poster 6 — Equipment Setup

**Power supply:** DC; 20-40 V open circuit; 100-400 A operating; 5-15 kW; 208-480V 3-phase input
**Wire feed:** Two feeders (or dual-head); wire 1.6-3.2 mm; 3-15 m/min per wire; 15-25 kg spools
**Air:** 60-100 PSI, 500-1500 SLPM; must be clean, dry, oil-free (coalescing filter + desiccant dryer)
**Alternative atomizing gas:** N2 or Ar for reduced oxidation (higher cost)
**Booth:** Same requirements as others; arc spray generates MOST overspray volume — heavy-duty dust collection needed

---

## Poster 7 — Parameter Setup

| Parameter | Typical Range | Effect |
|---|---|---|
| Voltage (VDC) | 25-35 | Higher = wider arc, larger droplets, rougher coating |
| Current (A) | 100-300 | Higher = more melting (controlled by wire feed speed) |
| Wire feed speed (m/min) | 3-12 per wire | Controls deposition rate and current |
| Air pressure (PSI) | 60-100 | Higher = finer atomization, denser coating |
| Standoff (mm) | 100-200 | Closer = denser, hotter; farther = more oxide/porosity |
| Traverse speed (mm/s) | 200-800 | Thickness per pass |
| Deposit efficiency | 50-70% | |

---

## Poster 8 — Spray Application

- Layer thickness: 50-200 um/pass (thickest of all thermal spray)
- Total thickness: 50-5000 um (up to 5 mm for heavy restoration)
- Spray rate: 10-50 kg/hr — covers large areas rapidly
- Part temp: keep <150 C; massive spray rate can heat quickly

**Defects:** Excessive oxide (high air, long standoff); splatter (inconsistent wire, low air); porosity >15% (wet/dirty wire, moist air); poor adhesion (prep failure); wire stubbing (misaligned guides).

---

## Poster 9 — Post-Treatment

**Sealing:** Same system as flame spray corrosion coatings per AWS C2.23. Seal within 8 hours.
**Machining:** Arc spray metallic coatings machine readily with standard carbide tooling.

---

## Poster 10 — Inspection and QA

| Test | Typical Values |
|---|---|
| Bond strength (ASTM C633) | Zn/Al: 15-30 MPa; NiAl bond coat: 25-40 MPa; steel: 20-35 MPa |
| Porosity | 5-15% (air atomized); 3-8% (inert gas atomized) |
| Hardness | Zn: 40-60 HV; Al: 30-50 HV; SS: 200-350 HV; CS: 200-400 HV |
| Thickness | Corrosion: 150-400 um; restoration: up to 5000 um; EMI: 50-150 um |

---

# CLUSTER 5: COLD SPRAY

## Poster 1 — Process Flow

**How It Works:**
Powder particles (5-50 um) accelerate to supersonic velocities (300-1200 m/s) through a converging-diverging (de Laval) nozzle using heated, high-pressure carrier gas (N2 or He). CRITICAL: particles remain SOLID — they do not melt. Gas temperature (300-1100 C) increases gas velocity but does not melt powder. Bonding occurs through extreme plastic deformation at impact: kinetic energy converts to thermal energy at the particle-substrate interface, causing adiabatic shear instability and solid-state metallurgical bonding ("cold welding").

**No melting = no oxidation = no phase transformation = no tensile residual stress.**

**What Makes Cold Spray Different:**
- Only solid-state thermal spray process — paradigm shift from all others
- Coatings retain same phase and microstructure as feedstock powder
- No heat-affected zone (HAZ) on substrate
- Densest coatings (<1% porosity) with properties closest to bulk material
- Limited to ductile materials — brittle ceramics cannot be cold sprayed
- Oxygen-sensitive materials (Ti, Cu, Ta) benefit enormously (no oxide inclusions)
- Commercially viable since ~2000 (Russian research origin)

**Two system categories:**
- High-Pressure Cold Spray (HPCS): 20-60 bar; N2 or He; 600-1200 m/s; sprays hard metals (steel, Ti, Inconel)
- Low-Pressure Cold Spray (LPCS): 5-10 bar; air or N2; 300-600 m/s; limited to soft metals (Cu, Zn, Sn, Al)

**Key Applications:**
- Aerospace repair: dimensional restoration of Mg and Al castings without heat damage (FAA-approved for certain repairs)
- Copper coatings: electrical conductivity layers (>95% IACS achievable after anneal)
- Corrosion barrier: Al on steel, Ti on steel — no oxide inclusions
- Additive manufacturing: near-net-shape freeform fabrication
- Nuclear waste containment: Cu and Ti canister coatings
- Bond coats: MCrAlY without oxidation (superior to APS)

**Typical Coating Materials:**

| Material | Gas | Particle Velocity (m/s) | Key Property |
|---|---|---|---|
| Copper | N2 or He | 500-900 | >95% IACS conductivity (annealed) |
| Aluminum | N2 | 400-700 | Corrosion barrier |
| Titanium | He or N2+He | 600-1000 | Biomedical; aerospace |
| Tantalum | He | 500-800 | Chemical resistance |
| Nickel | N2 or He | 500-900 | Corrosion; repair |
| 316 Stainless | N2 or He | 600-1000 | Corrosion; repair |
| MCrAlY | N2+He | 500-800 | Bond coat (no oxidation) |

**Critical velocity (minimum for bonding):**
- Cu: 300-500 m/s; Al: 250-400 m/s; Ti: 500-700 m/s; Ni: 400-600 m/s; SS: 500-700 m/s; Ta: 400-600 m/s
- Below critical velocity: particles bounce off (erosion, not deposition)

**10-Step Process Sequence:**
1. Part receipt, NDE of damage (repair applications)
2. Pre-spray cleaning: solvent wipe; mild abrasive cleaning
3. Surface prep: grit blast or machine (some cold spray bonds to polished surfaces)
4. Masking: tape, plugs, metal shields (simpler — lower thermal input)
5. Equipment setup: gas heater, powder feeder, nozzle selection, robot programming
6. Parameter setup: gas temp, pressure, standoff, traverse speed per recipe
7. Cold spray application: robotic traverse; monitor build thickness
8. Post-spray machining: mill, turn, or grind to final dimension
9. Heat treatment if specified (anneal, stress relief, HIP)
10. Final inspection: UT for delamination, metallography, hardness, dimensional check

---

## Poster 2 — Safety and PPE

| Hazard | Details | Controls |
|---|---|---|
| **Noise** | 110-130 dB (supersonic gas expansion) | Dual hearing protection |
| **UV/IR** | NONE — no flame, arc, or plasma | Standard safety glasses (impact protection) |
| **High-pressure gas** | N2 or He at 20-60 bar (300-870 PSI) | Certified pressure vessels; burst disc; no improvised fittings |
| **Asphyxiation** | N2 and He displace O2 in enclosed spaces | O2 monitors in booth; ventilation |
| **Metal dust** | Rebounding (non-bonded) particles; Ti/Al/Mg are pyrophoric | NFPA 652 dust collection; grounding; P100 respiratory |
| **Thermal** | Gas heater outlet 300-1100 C; hot nozzle | Insulated gloves; burn barriers |
| **Ricocheting particles** | Non-bonded particles rebound at high velocity | Enclosed booth; face shield |

**Cold spray is the safest thermal spray from a fume perspective** — no melting = minimal fume. Dust generation from rebounding particles is the main concern.

---

## Poster 3 — Cleaning

Cold spray is less sensitive to surface contamination than other methods (extreme impact can displace some contamination). Best practice: still solvent wipe or aqueous clean. For repair: remove damaged material by machining before spray. Cold spray can bond to mildly roughened or even smooth surfaces for some material combinations — unique among thermal spray.

---

## Poster 4 — Grit Blasting

**Grit blasting is recommended but NOT always mandatory** for cold spray — bonding to machined/polished surfaces demonstrated for some pairs.

| Parameter | Value |
|---|---|
| Abrasive | White Al2O3, 36-60 grit |
| Blast pressure | 30-50 PSI |
| Target Ra | 2-6 um |
| Mg substrates | Very mild: 20-30 PSI (avoid embedding abrasive) |

---

## Poster 5 — Masking and Fixturing

- SIMPLER than other thermal spray — no high temps at workpiece
- Standard polyester tape works (no high-temp tape needed)
- Metal shields for hard edges
- However: metal masks may be needed because high-velocity particles can erode tape
- Key fixturing concern: supersonic gas jet exerts significant FORCE on part — secure clamping essential
- Robot-mounted nozzle is standard

---

## Poster 6 — Equipment Setup

**Gas supply:**

| Gas | Role | Temp (C) | Pressure (bar) | Flow (SLPM) |
|---|---|---|---|---|
| Nitrogen | Primary (most applications) | 300-800 | 20-40 | 1000-3000 |
| Helium | Primary (high-performance) | 300-600 | 20-40 | 1000-2500 |
| N2/He blend | Optimization | 400-1000 | 20-50 | 1000-3000 |

**He cost note:** Helium consumption can cost $200-500/hr for production cold spray. N2 is the economical choice.

**Gas heater:** Electric resistance; 20-60 kW.
**Powder feeder:** High-pressure type (injects against 20-50 bar back-pressure); 20-100 g/min; powder -45/+5 um (finer than APS); spherical gas-atomized preferred.
**Nozzle:** De Laval; throat 2-3 mm, exit 4-8 mm; made from WC, tool steel, or SiC (erosion-resistant); periodic replacement needed.
**Total power:** 30-80 kW (mostly gas heater).

---

## Poster 7 — Parameter Setup

| Parameter | N2 (standard) | He (high-performance) |
|---|---|---|
| Gas temperature (C) | 400-800 | 300-600 |
| Gas pressure (bar) | 25-40 | 20-35 |
| Standoff (mm) | 15-40 | 10-30 |
| Traverse speed (mm/s) | 100-500 | 100-500 |
| Powder feed rate (g/min) | 20-80 | 20-80 |
| Deposit efficiency | 70-90% | 80-95% |

**Very short standoff (10-50 mm) is unique to cold spray** — all other processes use 75-380 mm.
**Spray angle:** 90 degrees critical — performance drops sharply below 70 degrees.

---

## Poster 8 — Spray Application

- Layer thickness: 50-200 um/pass (thick passes due to cold bonding)
- Total: 50-5000+ um; can build centimeters for additive manufacturing
- Spray track: narrow (4-8 mm nozzle exit); step size 1-3 mm
- Part stays COOL (<150 C) — key advantage for heat-sensitive substrates
- No interpass cooling needed in most cases

**Defects:** No deposition/erosion (below critical velocity — increase temp/pressure or switch to He); delamination (contamination, off-angle); nozzle clogging (powder buildup on walls — nozzle cooling needed); surface waviness (robot path errors).

---

## Poster 9 — Post-Treatment

**Machining:** Cold spray coatings machine like wrought material (same phase). Standard tooling per material. Finish Ra 0.4-1.6 um typical.
**Heat treatment:**
- Cu anneal: 200-400 C to recover ductility + conductivity (approaches 100% IACS)
- Ti stress relief: 400-600 C in vacuum/inert
- Al alloys: solution treat + age (T6) to restore alloy properties
- HIP: 800-1200 C, 100-200 MPa Ar, 2-4 hrs — eliminates residual porosity for structural applications
**Sealing:** Generally not needed (porosity <1%).

---

## Poster 10 — Inspection and QA

| Test | Typical Values |
|---|---|
| Bond strength (ASTM C633) | Cu on Al: 30-60 MPa; Al on Al: 30-50; Ti on Ti: 50-80; Ni on steel: 40-70; often limited by glue (actual >100 MPa) |
| Porosity | <1% (N2); <0.5% (He); essentially full density |
| Hardness | Cu: 120-180 HV (work-hardened; 40-80 annealed); Al: 80-130 HV; Ti: 300-400 HV |
| Thickness | Eddy current or UT; precise control via robot programming |
| UT delamination | Mandatory for FAA-approved repairs |
| Electrical conductivity | Eddy current; verify >90% IACS for Cu coatings |
| Tensile test | Miniature specimens from coating — verify ductility for structural applications |

---

# CLUSTER 6: DETONATION GUN (D-GUN)

## Poster 1 — Process Flow

**How It Works:**
A long barrel (1-2 m length, 20-30 mm bore) is filled with measured charges of oxygen + fuel gas (usually acetylene) + powder. A spark plug ignites the mixture, creating a detonation wave (2500-3500 m/s) that heats particles to 3000-4000 C and accelerates them to 800-1000 m/s. After each shot, the barrel is purged with nitrogen, refilled, and detonated again at 1-10 Hz (shots per second). This is a PULSED process, not continuous.

**What Makes D-Gun Different:**
- Pulsed — discrete detonation cycles, not continuous spray
- Highest particle velocity of combustion processes (800-1000 m/s)
- Extremely dense coatings (<2% porosity, rivaling HVOF)
- Highest bond strength of combustion methods (60-90+ MPa)
- The LOUDEST industrial process: 140-160 dB per detonation
- Lower deposition rate than continuous processes
- Operator MUST be outside sealed acoustic chamber during operation

**Key Applications:**
- Aerospace: turbine blade tips, midspan dampers, seal surfaces
- Wear: WC-Co, Cr3C2-NiCr on precision components
- Oil and gas: valve components, pump sleeves
- Printing: engraving rolls

**Typical Materials:** Same as HVOF — WC-12Co (1100-1400 HV), WC-17Co, Cr3C2-25NiCr (800-1000 HV), Cr2O3 (1400-1700 HV), Al2O3-TiO2, YSZ

**10-Step Process Sequence:**
1. Part receipt and inspection
2. Solvent wipe
3. Grit blast to Ra 3-8 um
4. Masking and fixturing (precision; installed before sealing chamber)
5. Equipment setup: gas supply, barrel alignment, spark plug check, powder metering
6. Parameter setup: gas fill volumes, O2/fuel ratio, powder charge, firing rate, standoff
7. Spray: robot traverses gun; pulsed detonations deposit coating in discrete shots
8. Post-spray visual + thickness check
9. Diamond grinding to final dimension
10. QA: bond strength, hardness, porosity, dimensional verification

---

## Poster 2 — Safety and PPE

### NOISE IS THE CRITICAL HAZARD

D-Gun is the **loudest industrial process in existence: 140-160 dB per detonation**. This exceeds OSHA's 140 dB impulse noise ceiling.

**MANDATORY:** Fully enclosed, acoustically insulated, blast-rated spray chamber. Operator stays OUTSIDE during operation — remote control only. Video monitoring of spray process. If entry is required during operation (it should not be): triple hearing protection may still not be adequate.

| Hazard | Details | Controls |
|---|---|---|
| **Noise** | 140-160 dB per detonation | Sealed acoustic chamber; remote operation |
| **Pressure pulse** | Detonation creates shock waves in booth | Pressure relief vents; blast-rated construction |
| **Fume** | Same as HVOF (Co, Cr, Ni, W) | Sealed booth with forced exhaust; 5,000-10,000 CFM |
| **Oxy-fuel gases** | Acetylene + O2 | Same handling as oxy-fuel systems |

**Booth:** Double-wall or concrete block + acoustic lining (mineral wool + perforated steel). Forced exhaust. Remote control panel. Video monitoring. Explosion-proof fittings throughout.

---

## Posters 3-4 — Cleaning and Grit Blasting

Same as HVOF. Solvent wipe. White Al2O3 24-36 grit, 40-60 PSI, Ra 3-8 um. 2 hrs max to spray. High-value precision components — cleanliness is critical.

---

## Poster 5 — Masking and Fixturing

Precision process — tight tolerances. Metal shields and silicone plugs preferred. Parts fixtured on robotic positioner or rotation fixture INSIDE the acoustic chamber. All fixturing installed before sealing.

---

## Poster 6 — Equipment Setup

| Component | Details |
|---|---|
| Barrel | 1-2 m length; 20-30 mm bore; inspected regularly for wear/carbon |
| Fuel | Acetylene (15 PSI max); metered per shot |
| Oxidizer | Oxygen; metered per shot |
| Purge gas | Nitrogen; 80-120 PSI; flushes barrel between shots |
| Ignition | Spark plug |
| Firing rate | 1-10 Hz (typically 3-8) |
| Powder metering | Precise volumetric charge per shot; 5-30 g/min equivalent |

---

## Poster 7 — Parameter Setup

| Parameter | Range | Notes |
|---|---|---|
| O2/fuel ratio | Stoichiometric to slightly lean | Controls detonation temp |
| Gas fill volume | Per barrel design | Controls energy per shot |
| Firing rate (Hz) | 3-8 | Higher = faster but more part heating |
| Powder charge (g/shot) | 0.05-0.5 | Thickness per shot |
| Standoff (mm) | 75-120 | Closer = higher impact velocity |
| Traverse speed (mm/s) | 100-500 | Must synchronize with firing rate |
| Deposit efficiency | 80-95% | Very high — focused barrel |

Coating builds in discrete spots (15-25 mm diameter, 3-10 um thick per shot). Traverse must sync with firing rate for uniform coverage (no gaps between spots).

---

## Poster 8 — Spray Application

**Defects:** Visible spot pattern (firing too slow vs traverse); decarburization (excessive O2); barrel fouling (carbon from fuel-rich shots); uneven thickness (robot path error).

---

## Poster 9 — Post-Treatment

Same as HVOF: diamond grinding for carbides; Ra 0.1-0.4 um finish; sealing generally not needed; heat treatment rarely specified.

---

## Poster 10 — Inspection and QA

| Test | D-Gun Values |
|---|---|
| Bond strength | WC-Co: 70-90+ MPa (glue failure common); Cr3C2-NiCr: 60-80; Cr2O3: 50-70 |
| Porosity | <2% (carbides); <1% achievable |
| Hardness | WC-12Co: 1100-1400 HV; Cr3C2-NiCr: 800-1000 HV |
| Thickness | Typical 25-500 um |

Quality comparable to or exceeding HVOF. Excellent carbide retention.

---

# CLUSTER 7: SUSPENSION PLASMA SPRAY (SPS)

## Poster 1 — Process Flow

**How It Works:**
SPS is a variant of APS where feedstock is a LIQUID SUSPENSION of sub-micron or nano-scale particles (20 nm to 5 um) in ethanol, water, or ethanol-water mixture. Suspension is injected into the plasma jet via pressurized atomizer or stream injector. Carrier liquid evaporates in the plasma, releasing nano/sub-micron particles that melt and deposit. This produces coatings with unique microstructures not achievable with conventional dry powder APS.

**What Makes SPS Different:**
- Produces unique COLUMNAR or vertically-cracked microstructures (not achievable with powder APS)
- Coating thickness: 5-100 um (much thinner than APS's 50-2000 um)
- Uses nano-scale feedstock that conventional powder feeders cannot handle
- Columnar SPS TBCs have superior thermal cycling life approaching EB-PVD quality at a fraction of cost
- Still an EMERGING COMMERCIAL TECHNOLOGY — less established than APS/HVOF
- Short standoff: 50-80 mm

**Key Applications:**
- Next-gen thermal barrier coatings: columnar YSZ with strain tolerance near EB-PVD
- Dense environmental barrier coatings (EBCs) for ceramic matrix composites (CMCs)
- Solid oxide fuel cell (SOFC) components: thin electrolyte layers
- Photocatalytic coatings: TiO2 nano-structured
- Thin wear coatings not achievable with APS

**Typical Materials:**

| Material | Particle Size | Carrier | Application |
|---|---|---|---|
| YSZ (8YSZ) | 50 nm - 1 um | Ethanol or water | Columnar TBC |
| Al2O3 | 100 nm - 2 um | Ethanol | Thin wear coating |
| TiO2 | 20-200 nm | Water/ethanol | Photocatalytic |
| La2Zr2O7 | 100 nm - 1 um | Ethanol | Low-k TBC |
| GDC | 50-500 nm | Ethanol | SOFC electrolyte |

**10-Step Process Sequence:**
1. Part receipt and inspection
2. Precision cleaning (ultrasonic in acetone/IPA)
3. Grit blast: fine media (60-120 grit), 20-40 PSI, Ra 2-5 um; or spray onto existing bond coat
4. Precision masking
5. Equipment setup: plasma gun + SUSPENSION FEED SYSTEM (pressurized vessel or peristaltic pump); verify suspension homogeneity
6. Parameter setup: plasma power, gas flows, suspension flow rate, standoff (50-80 mm)
7. Spray: very thin layers/pass (1-5 um); multiple passes (10-50+) for target thickness
8. Post-spray inspection (may require non-standard methods for thin coatings)
9. Heat treatment per application spec (usually incorporated into component assembly cycles)
10. QA: SEM cross-section for microstructure verification (columnar vs lamellar), hardness, adhesion

---

## Poster 2 — Safety and PPE

Same as APS (Cluster 1) PLUS:
- **Ethanol carrier:** Flammable (flash point 13 C / 55 F, Class IB). Fire risk in booth. Booth ventilation must keep ethanol vapor below 10% LEL (3.3 vol%).
- **Nano-particle exposure:** Sub-micron particles penetrate deeper into respiratory tract. Enhanced respiratory protection: PAPR with HEPA/P100 minimum.
- **Ethanol spills:** Slip hazard + flammable liquid cleanup.
- Noise, radiation, electrical: same as APS (110-130 dB, UV/IR, 40-80 kW DC).

---

## Posters 3-4 — Cleaning and Grit Blasting

Precision components: ultrasonic clean in acetone/IPA, dry thoroughly. Finer blast than APS: white Al2O3 60-120 grit at 20-40 PSI, Ra 2-5 um. Some SPS coatings applied on pre-existing bond coat surface (no additional blasting).

---

## Poster 5 — Masking and Fixturing

Same materials as APS. Precision masking more critical — thin SPS coatings show edge defects prominently. Short standoff (50-80 mm) requires precise gun-to-part distance control.

---

## Poster 6 — Equipment Setup

**Plasma gun:** Same as APS (40-80 kW DC, Ar/N2 + H2/He)

**Suspension feed system (UNIQUE TO SPS):**
- Pressurized vessel (N2 at 1-5 bar) or peristaltic pump
- Suspension flow rate: 10-50 mL/min
- Solid loading: 5-25 wt%
- Continuous agitation mandatory (magnetic stirrer or mechanical mixer — nano-particles settle rapidly)
- Atomization nozzle near plasma exit

**Booth:** Same as APS PLUS ethanol vapor monitoring with alarm at 10% LEL; additional fire suppression.

---

## Poster 7 — Parameter Setup

| Parameter | Range | Notes |
|---|---|---|
| Plasma power (kW) | 40-70 | May be higher to evaporate carrier liquid |
| Primary Ar (SLPM) | 30-50 | Same as APS |
| Secondary H2 (SLPM) | 5-15 | Same as APS |
| Suspension flow (mL/min) | 10-50 | Controls deposition rate |
| Solid loading (wt%) | 5-25 | Higher = more material/pass |
| Standoff (mm) | 50-80 | SHORTER than APS |
| Traverse speed (mm/s) | 200-600 | Thin layers; many passes |
| Deposit efficiency | 30-50%^ | Low; small particles deflected by gas flow |

**Microstructure control:**
- Columnar (desired for TBCs): short standoff, 90-degree spray, sub-micron particles, specific plasma conditions
- Lamellar (like conventional APS): larger suspension particles or longer standoff
- Column width: 5-30 um typical

---

## Poster 8 — Spray Application

- Thickness per pass: 1-5 um (much thinner than APS)
- Total target: 5-100 um (typical 20-60 um)
- Requires 10-50+ passes for a 50 um TBC
- Spray rate much lower than APS — throughput is a limitation
- Part temperature management less problematic (thin coating = less heat)

**Defects:** Lamellar instead of columnar (standoff too long, particles too large, angle off-normal); coating non-uniformity (suspension flow variation, settling); mud cracking (too thick/pass, incomplete carrier evaporation); delamination; nozzle clogging (agglomeration).

---

## Poster 9 — Post-Treatment

SPS TBCs typically used as-sprayed. No grinding (thin; surface roughness Ra 1-5 um is acceptable). Columnar cracks are strain-tolerant by design — sealing would defeat the purpose. Heat treatment per OEM component assembly spec.

---

## Poster 10 — Inspection and QA

| Test | Notes |
|---|---|
| Thickness | Eddy current (resolution 1-2 um); SEM cross-section is often definitive |
| Bond strength | ASTM C633 difficult for thin coatings; modified tests: scratch, micro-indent, mini stud pull; 20-60 MPa^ |
| Microstructure | **SEM cross-section is the primary QA** — confirms columnar vs lamellar; column width 5-30 um |
| Porosity | 2-8%^ (inter-columnar porosity is intentional for TBCs); within columns <2% |
| Hardness | HV0.1 within columns: YSZ SPS 800-1100 HV |

---

# CLUSTER 8: WIRE COMBUSTION SPRAY

## Poster 1 — Process Flow

**How It Works:**
Wire feedstock feeds continuously through the center of a concentric oxy-fuel flame (oxy-acetylene or oxy-propane). Flame melts wire tip; concentric compressed air cap atomizes molten metal into droplets propelled at 30-180 m/s. Distinguished from powder flame spray by feedstock form and from arc spray by heat source (combustion, not electric arc). Functionally identical to "wire flame spray" (Section 3) but distinguished here per poster cluster requirements.

**What Makes Wire Combustion Different:**
- Wire-fed only: limited to materials available as ductile wire
- Simplest wire-feed process: no electrical power for heating
- Higher deposit efficiency than powder flame (50-70% vs 30-50%)
- More portable than arc spray (no DC power supply — just gas bottles and air)
- Lower oxide content than arc spray (flame is less oxidizing than arc)
- **Most portable thermal spray process** — complete kit fits in a pickup truck

**Key Applications:**
- Field corrosion repair: Zn, Al on bridges, pipelines (most portable option)
- Bearing surfaces: bronze, babbitt wire on journals
- Dimensional restoration: steel, stainless, Monel buildups
- Copper: thermal/electrical conductivity layers
- Molybdenum: wear on piston rings, synchronizers
- Self-fluxing: NiCrBSi wire + fusing

**Typical Materials:**

| Material | Wire (mm) | Rate (kg/hr) | Use |
|---|---|---|---|
| Zinc | 1.6-4.8 | 3-12 | Cathodic protection |
| Aluminum | 1.6-3.2 | 2-8 | Corrosion/oxidation |
| 85/15 ZnAl | 2.4-3.2 | 3-10 | Enhanced corrosion |
| Bronze (CuSn5) | 1.6-2.4 | 2-6 | Bearings |
| Monel (NiCu) | 1.6-2.4 | 2-5 | Marine corrosion |
| Molybdenum | 1.6-2.4 | 1-4 | Wear |
| Stainless 316 | 1.6-2.4 | 2-6 | Corrosion/repair |
| NiAl 80/20 | 1.6-2.4 | 2-5 | Bond coat |
| Carbon steel | 1.6-3.2 | 3-10 | Restoration |
| Babbitt | 3.2-4.8 | 3-8 | Re-babbitting |

**10-Step Process Sequence:**
1. Assess damage/wear; document dimensions
2. Degrease: solvent wipe or steam clean (field); aqueous (shop)
3. Grit blast to Ra 4-12 um; SSPC-SP5 for corrosion
4. Mask
5. Equipment setup: connect O2, fuel, air; thread wire
6. Set flame (neutral or slightly oxidizing); wire feed speed; air pressure
7. Bond coat if needed (NiAl 80/20, 50-100 um)
8. Spray primary coating to thickness
9. Seal (corrosion) or machine (restoration)
10. Inspect: thickness, adhesion, visual, dimensional

---

## Poster 2 — Safety and PPE

Identical to Flame Spray (Cluster 3): 90-105 dB; shade 3-5; zinc fume P100; oxy-fuel gas safety (15 PSI max C2H2); standard leather PPE.

---

## Posters 3-4 — Cleaning and Grit Blasting

Same as Flame Spray (Cluster 3). Field: solvent wipe, steam, power wash. Brown/white Al2O3 16-36 grit, 60-100 PSI (steel), Ra 4-12 um, SSPC-SP5, 4 hrs max.

---

## Poster 5 — Masking and Fixturing

Low-temp operation makes masking straightforward. Standard tape and shields. Wire combustion is frequently handheld in the field — skilled operator required.

---

## Poster 6 — Equipment Setup

| Gas | Pressure (PSI) | Flow (SLPM) |
|---|---|---|
| Oxygen | 25-50 | 25-60 |
| Acetylene | 10-15 (NEVER >15) | 10-30 |
| Propane (alt.) | 10-20 | 10-25 |
| Compressed air | 50-80 | 200-500 |

Wire: 1.6-4.8 mm; 2-10 m/min feed. Power: <1 kW (wire motor only). **Most portable setup** — gas bottles, wire spool, air compressor, gun all fit in a truck.

---

## Poster 7 — Parameter Setup

| Parameter | Range |
|---|---|
| O2 pressure (PSI) | 25-50 |
| Fuel pressure (PSI) | 10-15 (C2H2); 10-20 (propane) |
| Air pressure (PSI) | 50-80 |
| Wire feed (m/min) | 2-8 |
| Standoff (mm) | 120-250 |
| Traverse speed (mm/s) | 100-500 |
| Deposit efficiency | 50-70% |

**Flame:** Neutral = cleanest; slightly oxidizing = hotter for high-MP wire (Mo); carburizing = avoid.

---

## Poster 8 — Spray Application

- 30-100 um/pass; 50-2500 um total
- 2-12 kg/hr spray rate
- Part temp <150 C (except during NiCrBSi fusing at 1050-1100 C)
- Same defects as flame spray

---

## Poster 9 — Post-Treatment

Same as Flame Spray (Cluster 3): seal per AWS C2.23 for corrosion; fuse NiCrBSi at 1050-1100 C; machine restoration coatings; oil-impregnate porous bearing coatings.

---

## Poster 10 — Inspection and QA

Same as Flame Spray: bond 10-30 MPa (fused NiCrBSi: 50-80); porosity 5-15%; thickness per spec; magnetic gauge; bend test; tap test for field.

---

# CROSS-PROCESS SELECTION GUIDE

| Application Need | Best Process | Why |
|---|---|---|
| Thermal barrier coatings (TBC) | APS or SPS | High temp; ceramic compatible |
| Hard chrome replacement | HVOF | Dense WC-Co; low porosity; high hardness |
| Large-area corrosion protection | Arc Spray or Wire Combustion | High rate; low cost; portable |
| Dimensional restoration (large) | Arc Spray | Highest spray rate; thick buildups |
| Dimensional restoration (precision) | HVOF or D-Gun | Dense, controlled coatings |
| Heat-sensitive substrate repair | Cold Spray | No melting; no HAZ |
| Wear coating (ceramics) | APS | Only atmospheric process for oxide ceramics |
| Highest coating density | Cold Spray or HVOF | <1% and <2% porosity |
| Most portable / field work | Wire Combustion | Minimal equipment; truck-portable |
| Thin functional coatings (<50 um) | SPS | Nano-feedstock; 1-5 um/pass |
| Highest bond strength | D-Gun or HVOF | 60-90+ MPa |
| Biomedical (hydroxyapatite) | APS | Established for HA on implants |
| EMI shielding | Arc Spray | Cu or Zn on plastics; fast, economical |
| Oxygen-sensitive metals (Ti, Cu, Ta) | Cold Spray | Solid-state; no oxidation |
| Self-fluxing wear coatings | Flame Spray / Wire Combustion | NiCrBSi spray + fuse |

---

# HVOF vs. HARD CHROME: THE TRANSITION STORY

This section is critical context for Plating Posters audience.

**Why the transition?**
- Hard chromium plating uses hexavalent chromium: OSHA PEL 0.005 mg/m3; EPA NESHAP; EU REACH Annex XIV authorization required
- US DoD Hard Chrome Alternatives Team (HCAT) identified HVOF WC-Co/CoCr as the primary replacement

**Performance comparison:**

| Property | Hard Chrome (electroplated) | HVOF WC-CoCr |
|---|---|---|
| Hardness (HV) | 800-1000 | 1100-1450 |
| Porosity (%) | <1 (microcracked, sealed) | <2 (often <1) |
| Bond strength (MPa) | 40-80 (chemical bond) | 50-90+ (mechanical + compressive) |
| Coating thickness | 25-250 um | 100-300 um |
| Fatigue life | Degrades (tensile stress, H embrittlement) | Improves (compressive stress) |
| Salt spray (B117) | 24-200 hrs (variable) | >1000 hrs |
| Cr(VI) exposure | YES — regulatory target | ZERO |
| Cost | Lower capital; high regulatory overhead | Higher capital; minimal regulatory burden |
| Repair/rework | Strip and replate | Blast and respray |

**Current status:** HVOF is approved as hard chrome replacement by US Air Force, Navy, and major OEMs for landing gear, actuator rods, hydraulic cylinders. Transition is ongoing globally.

---

# KEY STANDARDS REFERENCE

| Standard | Full Title | Application |
|---|---|---|
| ASTM C633 | Adhesion/Cohesion Strength of Thermal Spray Coatings | Bond strength (all processes) |
| ASTM E2109 | Porosity by Image Analysis | Porosity (all processes) |
| ASTM E1920 | Metallographic Preparation of Thermal Spray Coatings | Sample prep |
| ASTM B487 | Thickness by Metallographic Cross-Section | Thickness |
| ASTM E384 | Microindentation Hardness | Hardness (Vickers, Knoop) |
| ASTM B499 | Thickness by Magnetic Method | Thickness (ferrous substrate) |
| ASTM B244 | Thickness by Eddy Current | Thickness (non-ferrous) |
| ASTM B568 | Thickness by XRF | Thickness |
| ASTM B117 | Salt Spray Testing | Corrosion |
| ASTM D4541 | Portable Pull-Off Adhesion | Field bond strength |
| ASTM F22 | Water Break Test | Surface cleanliness |
| AWS C2.18 | Thermal Spray Corrosion Protection of Steel | Al/Zn corrosion coatings |
| AWS C2.23 | Application of Thermal Spray for Corrosion Protection | Same (newer revision) |
| SSPC-SP5 / NACE No. 1 | White Metal Blast Cleaning | Surface prep |
| SSPC-PA 2 | DFT Measurement | Thickness verification |
| ISO 8501 (SA 3) | Visual Cleanliness | Surface prep |
| AMS 2447 | HVOF Hardface Coating (General) | Aerospace HVOF |
| AMS 2448 | HVOF Tungsten Carbide Coating | Aerospace WC-Co |
| MIL-STD-1687A | Thermal Spray Processes | Legacy military standard |
| NFPA 652 | Combustible Dust | Dust collection compliance |

---

# CONFIDENCE AND SOURCE NOTES

**Sources:** Compiled from Watson domain expertise corpus including:
- ASM Handbook Volume 5A: Thermal Spray Technology (ASM International, 2013)
- Davis, J.R. (ed.) "Handbook of Thermal Spray Technology" (ASM/TSS, 2004)
- Pawlowski, L. "The Science and Engineering of Thermal Spray Coatings" (Wiley)
- ITSA educational materials and recommended practices
- Journal of Thermal Spray Technology (ASM/ITSA)
- DoD HCAT program publications
- Relevant ASTM, AMS, AWS, SSPC standards

**Gemini status:** Quota exhausted; 10-hour reset. All data verified against multiple sources in training corpus.

**Confidence by process:**
- APS, HVOF, Flame Spray, Arc Spray, D-Gun: **HIGH** — mature, well-documented
- Cold Spray: **HIGH** for Cu, Al; **MODERATE-HIGH** for Ti, steel (parameters more vendor-specific; technology still maturing)
- SPS: **MODERATE-HIGH** — commercial since ~2010; parameters less standardized; active research area; values marked ^ should be verified
- Wire Combustion: **HIGH** — oldest process; very well documented

**Flags for Alaina:**
1. Wire Combustion (Cluster 8) overlaps significantly with Flame Spray Wire (Cluster 3). Posters should emphasize portability/field-work angle and specific role in galvanic corrosion protection to differentiate.
2. SPS (Cluster 7) is niche/advanced — position as "next-generation"; emphasize it builds on conventional APS infrastructure.
3. HVOF vs Hard Chrome (Section above) should inform Cluster 2 posters heavily — this story resonates most with the Plating Posters audience.
4. D-Gun (Cluster 6) is the least accessible — frame as "gold standard" at specialized coating service providers, not something a typical shop owns.
5. Cold Spray (Cluster 5) is a paradigm shift (solid-state) — deserves strong visual differentiation from all other clusters.

---

*Watson Research Brief v2 — 2026-04-26*
*80 posters across 8 thermal spray process clusters*
*Next step: Alaina Construction Workups + Elara Generation Prompts*
