---
title: "Electroless Clusters — Watson Research Brief"
date: 2026-04-26T00:00:00
author: Watson (watson-chemistry-researcher)
scope: Pre-poster research for 8 electroless plating process clusters (64 total posters)
status: Complete
version: v1.1
tags:
  - PosterResearch
  - ResearchBrief
  - Electroless
  - ElectrolessNickel
  - ElectrolessCopper
  - ElectrolessPalladium
  - ElectrolessGold
  - ElectrolessCobalt
  - ElectrolessNickelBoron
  - Series2
---

# Electroless Clusters — Watson Research Brief

**Watson — Chemistry Research Division**
**Plating Posters Inc — Series 2 Electroless Process Clusters**
**2026-04-26 (v1.1 — cross-cluster reference tables and safety/regulatory consolidation added)**

---

## Purpose and Scope

This brief provides the foundational chemistry, operating parameters, and process-step-by-step data for **8 electroless (autocatalytic) plating processes**, organized to feed **64 Construction Workups** (8 posters per process). Alaina uses this document to write poster content; Elara uses it to write Generation Prompts.

**The 8 poster steps per process cluster:**
1. **Process Flow** — overview/summary poster
2. **Cleaning** — alkaline soak clean, electrocleaning, or solvent degrease
3. **Rinse -- Pre-Activation** — water rinse between cleaning and activation
4. **Activation** — catalytic activation (Pd, Sn/Pd colloidal, direct metallization, etc.)
5. **Rinse -- Pre-Plate** — water rinse between activation and electroless bath
6. **Main Tank** — the electroless plating bath itself
7. **Rinse -- Post-Plate** — water rinse after plating
8. **Post Treatment** — heat treatment, passivation, sealing, chromate, etc.

**Sources:** Domain expertise in electroless plating chemistry; existing Watson EN Research Brief (v2, 2026-03-21); ASTM B733 reference memory; Nickel Plating Handbook 2023 (nickelinstitute.org); ASTM B841; IPC-4552B; IPC-4556; AMS 2404/2405; NASF/AESF Metal Finishing Guidebook; Products Finishing; MacDermid Enthone, Atotech, Uyemura, and Dow product literature (chemistry only -- zero brand names on posters).

**Gemini status:** Quota exhausted (10-hour reset). All data below compiled from domain expertise. Flagged where Gemini verification would add value.

---

# PROCESS 1: Electroless Nickel -- Low Phosphorus (2-4% P)

## 1.1 Process Identity

| Attribute | Value |
|---|---|
| Deposit composition | Ni-P alloy, 2-4 wt% phosphorus |
| Deposit structure | Microcrystalline (near-crystalline) |
| Magnetic behavior | Ferromagnetic |
| Reducing agent | Sodium hypophosphite (NaH2PO2 . H2O) |
| Governing standard | ASTM B733 Type II/III |
| AMS specification | AMS 2404 (steel), AMS 2405 (aluminum) |
| Common abbreviation | EN Low-P, LP-EN |

## 1.2 Autocatalytic Mechanism

The reduction mechanism is identical across all EN-P processes -- only bath chemistry (pH, complexants, stabilizers) varies to control phosphorus incorporation:

**Primary deposition reaction:**
```
Ni2+ + 2 H2PO2- + 2 H2O --> Ni0 + 2 H2PO3- + H2 + 2 H+
```

**Phosphorus co-deposition (side reaction):**
```
H2PO2- + H+ --> P0 + H2O + OH-
```

At **alkaline pH (6.0-9.0)**, the phosphorus co-deposition side reaction is suppressed. The high pH favors nickel reduction over phosphorus reduction, producing deposits with only 2-4% P. This is the fundamental lever: **pH controls P content.**

The hypophosphite ion (H2PO2-) adsorbs onto the catalytic nickel surface and undergoes oxidation, releasing electrons that reduce Ni2+ to Ni0. Atomic hydrogen is generated as an intermediate, and a fraction of the hypophosphite is reduced to elemental phosphorus (P0) which incorporates into the growing deposit. The freshly deposited Ni-P alloy is itself catalytic for the same reaction -- hence "autocatalytic."

**Key byproduct:** Orthophosphite (H2PO3-) accumulates continuously. It cannot be removed and eventually limits bath life.

## 1.3 Poster-by-Poster Data

### Poster 1: Process Flow (Summary)

**Flow sequence:**
```
Alkaline Clean --> Rinse --> Acid Activation (or Zincate for Al) --> Rinse -->
EN Low-P Bath --> Rinse --> Post-Treatment (Heat Treatment / Passivation)
```

**Key callouts for summary poster:**
- Autocatalytic -- no rectifier, no anode, no external current
- Uniform thickness on all surfaces: +/-1-2 um
- Low-P = highest as-plated hardness of all EN-P classes (650-750 HV)
- Ferromagnetic deposit
- Excellent solderability and low contact resistance
- Bath life: 6-8 MTO (finite, then discard)
- Operating pH: alkaline (6.0-9.0) -- this is what makes it Low-P
- Temperature: 65-80C (150-176F)

**Primary applications:** Electronics/PCB (solderability, contact resistance), wear surfaces requiring heat treatment, diamond-tool binders, ENIG base layer for some specifications

### Poster 2: Cleaning

**Purpose:** Remove oils, greases, oxides, shop soils, and organic contaminants that would inhibit catalytic activity and cause skip plating.

**Alkaline soak clean parameters:**
| Parameter | Range |
|---|---|
| NaOH | 30-60 g/L |
| Na2CO3 | 15-30 g/L |
| Surfactants | 1-5 mL/L (proprietary blends) |
| Temperature | 60-80C (140-176F) |
| Time | 3-10 minutes (soak); 1-3 minutes (electroclean) |
| Agitation | Air or mechanical |

**Electrocleaning (optional, recommended for critical work):**
- Cathodic clean: 3-6 V, 30-60 seconds (generates H2 at part surface -- scrubbing action)
- Anodic clean: 3-6 V, 15-30 seconds (removes smut; generates O2 -- use after cathodic to remove hydrogen)
- Caution: cathodic cleaning can cause hydrogen absorption in high-strength steel -- if substrate is >1000 MPa UTS, use anodic only or minimize cathodic time

**Critical quality points:**
- Water-break-free surface after cleaning = visual confirmation of cleanliness
- Silicate-containing cleaners must be rinsed thoroughly -- silicate residues poison EN catalytic surfaces
- Cleaners with wetting agents must be non-foaming type if followed by electroclean
- For aluminum substrates: use non-etch alkaline cleaner (pH <10.5) or dedicated aluminum cleaner to avoid surface attack

### Poster 3: Rinse -- Pre-Activation

**Purpose:** Remove all cleaning chemistry before acid activation to prevent drag-in contamination of activation bath and pH shock.

**Rinse parameters:**
| Parameter | Value |
|---|---|
| Type | Counterflow (2-stage minimum); spray rinse acceptable for rack |
| Water quality | DI or RO preferred; municipal acceptable if <200 ppm TDS |
| Temperature | Ambient (18-30C / 65-85F) |
| Time | 30-60 seconds per stage |
| Conductivity target | <50 uS/cm in final rinse (drag-out verification) |

**Key points:**
- Inadequate rinsing = alkaline drag-in to acid activation = pH spike = poor activation
- For aluminum: rinse must be thorough before zincate; any residual alkaline cleaner on aluminum causes uncontrolled etching and surface roughness
- Spray rinse header bars above the rinse tank improve efficiency

### Poster 4: Activation

**Purpose:** Create a catalytically active surface that initiates the autocatalytic EN deposition reaction. Without proper activation, deposition will not start (skip plating).

**Activation varies by substrate:**

**Steel and iron alloys (most common):**
| Parameter | Value |
|---|---|
| Chemistry | 10-20% v/v HCl (hydrochloric acid) or 10-30% v/v H2SO4 |
| Temperature | Ambient (20-30C) |
| Time | 30-120 seconds |
| Purpose | Dissolve surface oxide; expose clean, active metal; provide micro-etch for adhesion |

Steel is inherently catalytic for EN deposition -- no palladium activation required. A clean, oxide-free steel surface will initiate the EN reaction spontaneously.

**Aluminum and aluminum alloys (zincate activation):**
| Parameter | Value |
|---|---|
| Step 1: Acid desmut | 50% v/v HNO3 or proprietary non-chromic desmut; ambient; 30-60 sec |
| Step 2: Zincate immersion | NaOH 120-150 g/L + ZnO 15-30 g/L (or proprietary zincate); 20-25C; 30-60 sec |
| Step 3 (recommended): Strip | 50% v/v HNO3; ambient; 15-30 sec (dissolves first zincate layer) |
| Step 4: Double zincate | Repeat zincate immersion; 15-30 sec (thinner, more uniform zinc film) |

The zincate process deposits a thin (sub-micron) zinc layer on the aluminum surface. This zinc layer is catalytic for EN and dissolves as the first atomic layers of nickel deposit, providing intimate metallurgical bonding. **Double zincate** (zincate-strip-zincate) produces a finer, more uniform zinc grain structure and dramatically improves adhesion.

**Copper, brass, and copper alloys:**
- Acid activation in 10-20% H2SO4; ambient; 30-60 seconds
- Copper is catalytic for EN -- no Pd required
- For tarnished or heavily oxidized copper: bright dip in dilute HNO3 + H2SO4 before activation

**Plastics and non-conductive substrates (ABS, polycarbonate, ceramics):**
| Parameter | Value |
|---|---|
| Etch | Chromic/sulfuric acid etch (400 g/L CrO3 + 400 g/L H2SO4; 65-70C; 5-15 min) -- NOTE: hexavalent chrome; or permanganate etch for RoHS |
| Neutralize | Dilute acid rinse or proprietary neutralizer |
| Activate | Colloidal Sn/Pd catalyst: SnCl2 + PdCl2 in HCl; 35-45C; 3-5 min |
| Accelerate | Dilute HCl or proprietary accelerator; removes excess tin from surface |
| Alternative | Direct metallization (no Pd): conductive polymer; newer, less common for EN |

**Stainless steel:**
- Wood's nickel strike (240 g/L NiCl2 . 6H2O + 125 mL/L HCl; 25-35 ASF; 3-5 min) provides adhesion layer
- Or: activate in 20-50% HCl at ambient for 1-2 minutes, transfer quickly to EN bath

### Poster 5: Rinse -- Pre-Plate

**Purpose:** Remove acid, zincate, or activation chemistry drag-in before entering the EN bath. This is the most critical rinse in the EN process line.

**Parameters:**
| Parameter | Value |
|---|---|
| Type | Single or double counterflow; DI preferred |
| Temperature | Ambient (18-30C) |
| Time | 30-60 seconds |
| Conductivity target | <20 uS/cm for critical work |
| Special note | For zincated aluminum: minimize rinse time to prevent oxidation of zinc layer; transfer to EN bath within 30 seconds of rinsing |

**Critical contamination concerns:**
- **Chloride drag-in** from HCl activation: chloride in the EN bath causes pitting and accelerates bath aging. DI rinse is essential.
- **Chromate drag-in** from plastic activation etch: even trace Cr6+ poisons EN baths (stabilizer poisoning at ppm levels)
- **Zinc residue** from zincate: slight drag-in is acceptable (zinc dissolves in EN bath); excessive drag-in raises zinc contamination

### Poster 6: Main Tank -- EN Low-P Bath

**Bath composition:**
| Component | Concentration | Role |
|---|---|---|
| Nickel sulfate (NiSO4 . 6H2O) | 15-25 g/L Ni2+ | Metal ion source |
| Sodium hypophosphite (NaH2PO2 . H2O) | 20-35 g/L | Reducing agent |
| Ammonium sulfate or ammonium chloride | 30-65 g/L | Complexant + buffer (alkaline regime) |
| Sodium citrate | 10-20 g/L | Complexant (prevents Ni(OH)2 precipitation) |
| Sodium acetate or propionic acid | 5-15 g/L | pH buffer |
| Stabilizer (lead, thiourea, or iodate) | 1-5 ppm | Prevents spontaneous decomposition |
| pH adjuster | NaOH or NH4OH | Maintain alkaline pH |

**Operating parameters:**
| Parameter | Target | Tolerance |
|---|---|---|
| pH | 8.5-9.5 (alkaline) | +/- 0.2 |
| Temperature | 65-80C (150-176F) | +/- 2C |
| Nickel concentration | 4.5-6.0 g/L | +/- 0.5 g/L |
| Hypophosphite | 20-35 g/L | Maintain by replenishment |
| Deposition rate | 10-15 um/hr | Dependent on pH and temp |
| Loading (A/V) | 0.25-0.50 dm2/L | Critical for stability |
| Bath life | 6-8 MTO | Discard at orthophosphite >120 g/L |

**Deposit properties (as-plated):**
| Property | Value |
|---|---|
| Phosphorus content | 2-4 wt% |
| Hardness (as-plated) | 650-750 HV |
| Hardness (400C / 1 hr HT) | 1000-1100 HV |
| Structure | Microcrystalline |
| Magnetic | Yes (ferromagnetic) |
| Salt spray (25 um, ASTM B117) | 96-240 hours |
| Solderability | Excellent |
| Contact resistance | Very low |
| Internal stress | Tensile (moderate) |

**MTO tracking:**
- 1 MTO = bath has deposited nickel mass equal to its original Ni2+ charge
- Track cumulative nickel deposited; divide by initial Ni2+ loading
- Deposition quality degrades progressively from 4 MTO onward
- Orthophosphite accumulates at approximately 15-20 g/L per MTO
- Warning zone: 6-8 MTO
- Hard discard: >8 MTO or orthophosphite >120 g/L

**Bath stability management:**
- Stabilizer concentration is critical: too low = risk of spontaneous decomposition (exothermic, fire hazard); too high = stabilizer poisoning (bath goes inert)
- Loading ratio: under-loaded baths (<0.1 dm2/L) are at highest decomposition risk
- Never leave bath at operating temperature without parts (or dummy load)
- Hot spots on heater elements (>5-10C above bath temp) nucleate decomposition
- Filter continuously (5-10 um); remove metallic fines that act as nucleation sites

### Poster 7: Rinse -- Post-Plate

**Purpose:** Stop the EN reaction; remove drag-out chemicals; prepare surface for post-treatment.

**Parameters:**
| Parameter | Value |
|---|---|
| Type | Double counterflow or spray rinse |
| Temperature | Ambient (cold rinse preferred to stop reaction quickly) |
| Time | 30-60 seconds |
| Water quality | DI preferred; municipal acceptable |
| Special consideration | Parts should not air-dry between EN bath and rinse -- watermarks from dried EN solution cause staining |

**Post-plate handling:**
- Avoid finger contact on freshly plated surfaces (fingerprints etch into deposit)
- Do not stack parts wet -- causes water staining and galvanic attack at contact points

### Poster 8: Post Treatment

**Heat treatment options (ASTM B733 Classes):**

| Treatment | Temperature | Time | Purpose |
|---|---|---|---|
| Hydrogen embrittlement relief (Class 3) | 190-210C (375-410F) | 2-23 hours | Drives absorbed hydrogen out of high-strength steel substrates; MUST be performed within 4 hours of plating |
| Maximum hardness (Class 2) | 350-400C (660-750F) | 1 hour | Precipitates Ni3P phase; achieves 1000-1100 HV |
| Adhesion bake -- aluminum (Class 4-5) | 120-150C (250-300F) | 1-2 hours | Improves adhesion on age-hardened and non-heat-treatable aluminum |
| Adhesion bake -- titanium (Class 6) | 300-320C (570-610F) | 1-4 hours | Adhesion on titanium alloys |

**Passivation / chromate conversion (optional):**
- Trivalent chromate passivation: provides additional corrosion resistance; typically used on mid/high-P but occasionally on Low-P
- Temperature limit on aluminum substrates: do not exceed 290C (554F) -- differential thermal expansion causes delamination

**Critical embrittlement relief rule:**
- High-strength steel (>1000 MPa UTS or >40 HRC): hydrogen embrittlement bake at 190-210C for minimum 4 hours, within 4 hours of plating completion
- Per ASTM B849 / ASTM B850 / AMS 2759/9
- Failure to perform HE relief on high-strength steel can cause catastrophic delayed brittle fracture

---

# PROCESS 2: Electroless Nickel -- Mid Phosphorus (5-9% P)

## 2.1 Process Identity

| Attribute | Value |
|---|---|
| Deposit composition | Ni-P alloy, 5-9 wt% phosphorus |
| Deposit structure | Mixed crystalline/amorphous |
| Magnetic behavior | Weakly magnetic to non-magnetic (depends on exact P%) |
| Reducing agent | Sodium hypophosphite (NaH2PO2 . H2O) |
| Governing standard | ASTM B733 Type IV |
| AMS specification | AMS 2404 (steel), AMS 2405 (aluminum) |
| Common abbreviation | EN Mid-P, MP-EN |

## 2.2 Autocatalytic Mechanism

Identical to Low-P (see Section 1.2). The difference is bath chemistry environment:
- **Acid pH (4.6-5.2)** produces higher phosphorus co-deposition than alkaline pH
- **Organic acid complexants** (lactic, malic, succinic) replace ammonium compounds
- Higher operating temperature (85-91C) drives faster deposition and moderate P incorporation

## 2.3 Poster-by-Poster Data

### Poster 1: Process Flow (Summary)

**Flow sequence:**
```
Alkaline Clean --> Rinse --> Acid Activation (HCl or H2SO4) --> Rinse -->
EN Mid-P Bath --> Rinse --> Post-Treatment (HE Relief / Hardness HT)
```

**Key callouts:**
- Industry workhorse -- most widely used EN class
- Balanced properties: moderate hardness, moderate corrosion, moderate solderability
- Fastest deposition rate of all EN-P classes: 18-25 um/hr
- Highest operating temperature: 85-91C (185-196F)
- Acid pH: 4.6-5.2
- ENIG base layer (IPC-4552B): Mid-P at 6-9% P is the standard
- Semi-bright, smooth deposit with good leveling

**Primary applications:** Aerospace hydraulics (AMS 2404), ENIG PCB finish (IPC-4552B), automotive fuel systems, precision tooling, general engineering

### Poster 2: Cleaning

Identical to Low-P Process 1, Poster 2 (see Section 1.3, Poster 2). Same cleaning chemistry applies to all substrates entering Mid-P EN.

**Additional note for Mid-P:** Because Mid-P baths operate at higher temperature and are more active than Low-P, they are slightly more tolerant of marginal cleaning -- but this is NOT an excuse for substandard cleaning. Skip plating from contamination remains the #1 defect in EN operations regardless of P class.

### Poster 3: Rinse -- Pre-Activation

Identical to Process 1, Poster 3. See Section 1.3.

### Poster 4: Activation

Identical substrate-dependent activation as Process 1, Poster 4 (see Section 1.3). All activation chemistry is the same regardless of which EN-P bath follows.

**One notable difference:** For ENIG applications (PCB), the substrate is copper-clad laminate. Activation is:
- Microetch: sodium persulfate (100-200 g/L) or sulfuric/peroxide (50 mL/L H2SO4 + 20-40 mL/L H2O2); 30-60 seconds
- This creates a micro-roughened copper surface for mechanical adhesion
- No Pd catalyst required -- copper is catalytic for EN

### Poster 5: Rinse -- Pre-Plate

Identical to Process 1, Poster 5. See Section 1.3.

**Additional ENIG note:** In ENIG lines, the pre-plate rinse quality is especially critical because the EN bath operates at acid pH (4.6-5.2) and the microetch is acidic -- less pH differential concern, but persulfate or peroxide drag-in degrades EN stabilizers.

### Poster 6: Main Tank -- EN Mid-P Bath

**Bath composition:**
| Component | Concentration | Role |
|---|---|---|
| Nickel sulfate (NiSO4 . 6H2O) | 20-30 g/L Ni2+ (4.5-6.5 g/L as Ni metal) | Metal ion source |
| Sodium hypophosphite (NaH2PO2 . H2O) | 20-30 g/L | Reducing agent |
| Lactic acid (90%) | 20-30 mL/L | Primary complexant |
| Malic acid | 5-15 g/L | Secondary complexant |
| Succinic acid | 5-10 g/L | Buffer + complexant |
| Propionic acid | 2-5 mL/L | pH buffer |
| Stabilizer (Pb, thiourea, thiomalic acid, IO3-) | 1-5 ppm | Prevents decomposition |
| pH adjuster | NaOH (10-50% solution) or dilute H2SO4 | Maintain acid pH |

**Operating parameters:**
| Parameter | Target | Tolerance |
|---|---|---|
| pH | 4.6-5.2 | +/- 0.2 (CRITICAL) |
| Temperature | 85-91C (185-196F) | +/- 1C preferred, +/- 2C maximum |
| Nickel concentration | 4.5-6.5 g/L Ni2+ | +/- 0.5 g/L |
| Hypophosphite | 20-30 g/L | Replenish continuously |
| Deposition rate | 18-25 um/hr | Function of pH and temperature |
| Loading (A/V) | 0.25-0.50 dm2/L | Same as Low-P |
| Bath life | 6-8 MTO (some suppliers claim 8-10 with dump/replenish) | Orthophosphite >120 g/L = discard |

**Deposit properties (as-plated):**
| Property | Value |
|---|---|
| Phosphorus content | 5-9 wt% |
| Hardness (as-plated) | 500-600 HV |
| Hardness (400C / 1 hr HT) | 850-1000 HV |
| Structure | Mixed crystalline/amorphous |
| Magnetic | Weakly magnetic at 5-6% P; non-magnetic at 8-9% P |
| Salt spray (25 um) | 240-500 hours |
| Solderability | Moderate (adequate for ENIG with gold overlay) |
| Internal stress | Low tensile to low compressive |
| Deposit appearance | Semi-bright, smooth |

**pH vs. phosphorus relationship (critical concept for poster):**
| pH | Expected P% | Notes |
|---|---|---|
| 4.2-4.4 | 10-13% | Enters High-P territory |
| 4.6-5.0 | 6-9% | Mid-P sweet spot |
| 5.0-5.5 | 4-6% | Low end of Mid-P |
| 6.0+ | 2-4% | Low-P territory (alkaline bath) |

This is the master lever. A single Mid-P bath drifting from pH 4.8 to pH 4.3 crosses into High-P territory -- changing all deposit properties. This is why +/-0.2 pH control is non-negotiable.

### Poster 7: Rinse -- Post-Plate

Identical to Process 1, Poster 7. See Section 1.3.

### Poster 8: Post Treatment

Same heat treatment framework as Low-P (Section 1.3, Poster 8), with these notes:

- **HE relief** (190-210C, 2-23 hr, within 4 hr): same requirement on high-strength steel
- **Maximum hardness** (350-400C, 1 hr): achieves 850-1000 HV -- lower peak than Low-P due to higher P content
- **ENIG post-treatment**: after EN plating in ENIG process, parts go directly to immersion gold bath (no heat treatment between EN and Au in ENIG; heat treatment would oxidize EN surface and prevent gold deposition)
- **Chromate passivation**: optional for general engineering applications

---

# PROCESS 3: Electroless Nickel -- High Phosphorus (10-13% P)

## 3.1 Process Identity

| Attribute | Value |
|---|---|
| Deposit composition | Ni-P alloy, 10-13 wt% phosphorus |
| Deposit structure | Fully amorphous (metallic glass) |
| Magnetic behavior | Non-magnetic (paramagnetic) |
| Reducing agent | Sodium hypophosphite (NaH2PO2 . H2O) |
| Governing standard | ASTM B733 Type V |
| AMS specification | AMS 2404 (steel); NACE MR0175 for sour service |
| Common abbreviation | EN High-P, HP-EN |

## 3.2 Autocatalytic Mechanism

Identical reduction chemistry to Low-P and Mid-P (see Section 1.2). The key difference:
- **Low acid pH (4.2-4.8)** maximally favors the phosphorus co-deposition side reaction
- Lower pH = more H+ available = more P0 incorporation into deposit
- The deposit exceeds the ~8-10% P amorphous threshold, eliminating all crystalline grain structure

**Why amorphous matters:** In a crystalline deposit, corrosion attacks grain boundaries preferentially. An amorphous deposit has NO grain boundaries -- corrosion must attack the bulk material uniformly. This is why High-P EN achieves 1,000+ hours salt spray while Mid-P achieves 240-500 hours.

## 3.3 Poster-by-Poster Data

### Poster 1: Process Flow (Summary)

**Flow sequence:**
```
Alkaline Clean --> Rinse --> Acid Activation (or Zincate for Al) --> Rinse -->
EN High-P Bath --> Rinse --> Post-Treatment (HE Relief / Passivation)
```

**Key callouts:**
- Maximum corrosion resistance: 1,000+ hours ASTM B117 salt spray at 25 um
- Fully amorphous, non-magnetic deposit
- Essential for oil/gas MWD tools, chemical processing, MRI-compatible components
- Operating pH: 4.2-4.8 (low acid)
- Temperature: 82-90C (180-194F)
- Deposition rate: 10-13 um/hr (slower than Mid-P)
- Lowest as-plated hardness of EN-P classes (450-550 HV) but still harder than most electrolytic nickel

### Poster 2: Cleaning

Identical to Process 1, Poster 2. Same cleaning protocol for all EN-P processes.

### Poster 3: Rinse -- Pre-Activation

Identical to Process 1, Poster 3.

### Poster 4: Activation

Identical to Process 1, Poster 4. Same substrate-dependent activation.

**High-P specific note for oil/gas substrates:**
- 4130/4140 alloy steel (common in downhole tools): acid activate in 20-50% HCl for 1-2 min
- Nickel alloys (Inconel, Monel): may require brief anodic etch in sulfuric acid or proprietary activator
- Stainless steel components for chemical process: Wood's nickel strike recommended for maximum adhesion

### Poster 5: Rinse -- Pre-Plate

Identical to Process 1, Poster 5.

### Poster 6: Main Tank -- EN High-P Bath

**Bath composition:**
| Component | Concentration | Role |
|---|---|---|
| Nickel sulfate (NiSO4 . 6H2O) | 20-30 g/L Ni2+ (4.5-6.5 g/L as Ni) | Metal ion source |
| Sodium hypophosphite (NaH2PO2 . H2O) | 20-30 g/L | Reducing agent |
| Lactic acid (90%) | 25-35 mL/L | Primary complexant |
| Glycolic acid | 10-20 g/L | Smoothness enhancer + complexant |
| Malic acid | 5-10 g/L | Secondary complexant |
| Succinic acid | 5-10 g/L | Buffer |
| Stabilizer (Pb, thiourea, IO3-) | 1-5 ppm | Prevents decomposition |
| pH adjuster | NaOH or dilute H2SO4 | Maintain low-acid pH |

**Operating parameters:**
| Parameter | Target | Tolerance |
|---|---|---|
| pH | 4.2-4.8 | +/- 0.2 |
| Temperature | 82-90C (180-194F) | +/- 2C |
| Nickel concentration | 4.5-6.5 g/L Ni2+ | +/- 0.5 g/L |
| Hypophosphite | 20-30 g/L | Replenish continuously |
| Deposition rate | 10-13 um/hr | |
| Loading (A/V) | 0.25-0.50 dm2/L | |
| Bath life | 6-8 MTO | Orthophosphite >120 g/L = discard |

**Deposit properties (as-plated):**
| Property | Value |
|---|---|
| Phosphorus content | 10-13 wt% (some baths reach 14%) |
| Hardness (as-plated) | 450-550 HV |
| Hardness (400C / 1 hr HT) | 800-900 HV |
| Structure | Fully amorphous (metallic glass) |
| Magnetic | Non-magnetic (paramagnetic) |
| Salt spray (25 um) | 1,000+ hours |
| Solderability | Poor (high P oxide layer resists solder wetting) |
| Chemical resistance | Excellent -- resists HCl, H2SO4, acetic, phosphoric acids |
| Lubricity | Good; coefficient of friction ~0.1-0.15 (dry) |
| Internal stress | Low compressive (as-plated) |

**Non-magnetic verification:**
- Non-magnetic threshold: >= 8-10% P
- Test method: ASTM F2088 or verified phosphorus analysis (XRF, ICP, or wet chemistry)
- Oil/gas MWD specs often require certified P% >= 10.5% AND non-magnetic verification per ASTM F2088

### Poster 7: Rinse -- Post-Plate

Identical to Process 1, Poster 7.

### Poster 8: Post Treatment

Same framework as Process 1, Poster 8, with High-P-specific notes:

- **HE relief**: 190-210C, 2-23 hours, within 4 hours -- same steel embrittlement concern
- **Maximum hardness**: 350-400C, 1 hr achieves 800-900 HV -- CAUTION: heat treatment above 260C begins to crystallize the amorphous structure, which DESTROYS the non-magnetic property and reduces corrosion resistance
- **For non-magnetic applications (MWD)**: do NOT heat treat above 260C -- the deposit crystallizes and becomes magnetic
- **For maximum corrosion applications**: do NOT heat treat -- as-plated amorphous state has best corrosion resistance
- **Passivation**: trivalent chromate conversion coatings enhance corrosion further; useful for chemical process applications
- **EN-PTFE composite option**: co-deposited PTFE particles reduce friction to 0.04-0.07 (dry); used for mold release and sliding contacts

---

# PROCESS 4: Electroless Copper

## 4.1 Process Identity

| Attribute | Value |
|---|---|
| Deposit composition | Pure copper (Cu) |
| Deposit structure | Crystalline (fine-grained polycrystalline) |
| Reducing agent | Formaldehyde (HCHO) -- primary; or hypophosphite, DMAB, glyoxylic acid |
| Primary applications | PCB through-hole plating, metallization of plastics, EMI shielding |
| Governing standard | IPC-TM-650 (PCB testing); no single ASTM standard equivalent to B733 |
| Common abbreviation | E-Cu, electroless Cu, EL-Cu |

## 4.2 Autocatalytic Mechanism

Electroless copper uses **formaldehyde (HCHO)** as the reducing agent in an alkaline bath. This is fundamentally different from EN-P (hypophosphite) chemistry.

**Primary deposition reaction:**
```
Cu2+ + 2 HCHO + 4 OH- --> Cu0 + 2 HCOO- + 2 H2O + H2
```

- **Cu2+** (from copper sulfate, CuSO4 . 5H2O) is reduced to metallic copper
- **Formaldehyde** is oxidized to **formate (HCOO-)**
- The reaction consumes hydroxide (OH-) -- pH drops during plating
- Hydrogen gas is evolved
- **No phosphorus or boron in the deposit** -- pure copper

**Key differences from EN:**
- Operates at strongly alkaline pH (11.5-13.0) -- much higher than even Low-P EN
- Formaldehyde is volatile and toxic (OSHA PEL 0.75 ppm TWA) -- requires excellent ventilation
- Bath is inherently less stable than EN -- more prone to spontaneous decomposition
- Deposit is thin-film only in most applications (0.5-2.5 um); "heavy build" electroless copper (25+ um) exists but is uncommon
- Primary purpose in PCB: provide a conductive seed layer on non-conductive through-hole walls for subsequent electrolytic copper buildup

**Alternative reducing agents (emerging):**
- **Glyoxylic acid (CHOCOOH)**: formaldehyde-free; gaining traction for environmental/health reasons; same alkaline regime; slightly lower deposition rate
- **Hypophosphite**: produces Cu-P alloy (undesirable for most PCB applications)
- **DMAB (dimethylamine borane)**: produces Cu-B alloy; very expensive; niche use only

## 4.3 Poster-by-Poster Data

### Poster 1: Process Flow (Summary)

**Flow sequence (PCB through-hole plating):**
```
Cleaner/Conditioner --> Rinse --> Microetch --> Rinse -->
Pre-Dip (Pd activator conditioner) --> Catalyst (Sn/Pd colloidal) -->
Rinse --> Accelerator --> Rinse --> Electroless Copper --> Rinse -->
(Electrolytic copper buildup follows)
```

**Flow sequence (plastics metallization):**
```
Chromic/Sulfuric Etch --> Neutralize --> Rinse -->
Conditioner --> Catalyst (Sn/Pd) --> Accelerator --> Rinse -->
Electroless Copper --> Rinse --> Electrolytic Build
```

**Key callouts:**
- Autocatalytic copper deposition onto non-conductive surfaces
- Requires Pd catalytic activation on non-metallic substrates (plastics, glass, ceramics, FR4 laminate)
- Formaldehyde-based alkaline bath (pH 11.5-13.0)
- Thin-film process: typically 0.5-2.5 um deposit for PCB
- Seed layer for subsequent electrolytic copper
- Temperature: 28-45C (82-113F) -- much cooler than EN
- OSHA formaldehyde exposure concerns require ventilation

### Poster 2: Cleaning

**PCB cleaner/conditioner:**
| Parameter | Value |
|---|---|
| Chemistry | Proprietary alkaline cleaner/conditioner (surfactant + polymer) |
| pH | 10-12 |
| Temperature | 40-55C (105-130F) |
| Time | 3-5 minutes |
| Purpose | Remove drilling smear (epoxy smear from through-hole drilling); condition dielectric surface for catalyst adsorption |

**Plastics cleaning:**
- Alkaline soak clean: NaOH 30-45 g/L + surfactant; 50-60C; 5-10 min
- Removes mold release agents, fingerprints, surface oils
- For ABS: must not use solvents that attack the butadiene rubber phase (the etchable phase)

**Desmear (PCB-specific):**
- Permanganate desmear: KMnO4 50-70 g/L in NaOH 40-50 g/L; 75-85C; 5-10 min
- Removes drilling smear from inner copper layers in multilayer PCBs
- Followed by neutralizer/reducer (hydroxylamine or proprietary) to remove MnO2 residues

### Poster 3: Rinse -- Pre-Activation

| Parameter | Value |
|---|---|
| Type | Double counterflow, DI water |
| Temperature | Ambient |
| Time | 1-3 minutes |
| Key concern | Complete removal of permanganate and alkaline cleaner; residual oxidizer poisons Pd catalyst |

### Poster 4: Activation

**Colloidal Sn/Pd catalyst (most common for E-Cu on non-conductors):**
| Parameter | Value |
|---|---|
| Chemistry | Colloidal SnCl2/PdCl2 in HCl (proprietary concentrates) |
| Pd concentration | 100-250 mg/L Pd |
| Sn concentration | 15-40 g/L Sn |
| HCl concentration | 150-250 mL/L |
| Temperature | 35-45C (95-113F) |
| Time | 3-7 minutes |
| Mechanism | Sn2+ reduces Pd2+ to Pd0 on the surface; colloidal Sn/Pd particles adsorb onto conditioned surface; Pd nuclei serve as catalytic sites for copper deposition |

**Pre-dip (before catalyst):**
- HCl 150-250 mL/L at ambient; 1-2 min
- Purpose: acidify the surface and prevent drag-in of alkaline chemistry into the expensive Pd catalyst

**Accelerator (after catalyst):**
| Parameter | Value |
|---|---|
| Chemistry | Dilute HCl (50-100 mL/L), or fluoboric acid, or proprietary |
| Temperature | 25-45C |
| Time | 2-5 minutes |
| Purpose | Remove excess tin (Sn) from the Sn/Pd colloid, exposing bare Pd nuclei that are catalytically active for copper reduction |

**Direct metallization (alternative to Sn/Pd -- newer technology):**
- Conductive polymer (PEDOT:PSS or polyaniline) deposited on dielectric surface
- Or: carbon/graphite-based direct metallization
- Eliminates Pd catalyst (cost savings + waste treatment simplification)
- Not universally adopted; some reliability concerns in high-layer-count boards

### Poster 5: Rinse -- Pre-Plate

| Parameter | Value |
|---|---|
| Type | DI counterflow (2-3 stage) |
| Temperature | Ambient |
| Time | 1-2 minutes |
| Critical concern | Acid drag-in from accelerator into alkaline E-Cu bath; pH shock can crash bath |
| Conductivity target | <30 uS/cm |

### Poster 6: Main Tank -- Electroless Copper Bath

**Bath composition (formaldehyde-based):**
| Component | Concentration | Role |
|---|---|---|
| Copper sulfate (CuSO4 . 5H2O) | 7-12 g/L (1.5-3.0 g/L Cu2+) | Metal ion source |
| Formaldehyde (37% solution) | 3-8 mL/L (1-3 g/L HCHO) | Reducing agent |
| NaOH | 5-10 g/L | pH control; provides OH- for reaction |
| EDTA (tetrasodium salt) | 25-40 g/L | Primary complexant (prevents Cu(OH)2 precipitation at high pH) |
| Sodium cyanide (trace) | 10-20 mg/L (some formulations) | Stabilizer -- NOTE: many modern formulations are cyanide-free |
| 2,2'-Bipyridyl or proprietary stabilizer | 10-30 mg/L | Stabilizer (replaces cyanide in modern baths) |
| Surfactant (wetting agent) | 0.01-0.1 g/L | Reduces hydrogen pitting |

**Operating parameters:**
| Parameter | Target | Tolerance |
|---|---|---|
| pH | 11.5-13.0 | +/- 0.3 |
| Temperature | 28-45C (82-113F) | +/- 2C |
| Copper concentration | 1.5-3.0 g/L Cu2+ | +/- 0.3 g/L |
| Formaldehyde | 1-3 g/L HCHO | Replenish frequently (volatile loss + consumption) |
| Deposition rate | 1-5 um/hr (thin-film); up to 5-8 um/hr (heavy-build) | |
| Bath life | 1-4 MTO (shorter than EN) | EDTA and formate accumulation limit life |
| Air agitation | Required | Replenishes HCHO at surface; removes H2 bubbles |

**Deposit properties:**
| Property | Value |
|---|---|
| Composition | Pure copper (>99.5% Cu) |
| Conductivity | Excellent (~90-95% IACS) |
| Adhesion to FR4 laminate | Good with proper desmear and activation |
| Typical thickness (PCB) | 0.5-2.5 um (seed layer) |
| Typical thickness (heavy-build) | 25-50 um (less common; EMI shielding) |
| Ductility | Moderate; improves with annealing |

**Formaldehyde safety:**
- OSHA PEL: 0.75 ppm (8-hr TWA), 2 ppm (STEL)
- Classified as a probable human carcinogen (IARC Group 1)
- Requires local exhaust ventilation and continuous air monitoring
- Formaldehyde-free alternatives (glyoxylic acid) are gaining market share

### Poster 7: Rinse -- Post-Plate

| Parameter | Value |
|---|---|
| Type | Double counterflow |
| Temperature | Ambient |
| Time | 1-2 minutes |
| Handling | Freshly plated electroless copper oxidizes rapidly in air; proceed immediately to anti-tarnish or electrolytic copper |
| Anti-tarnish (optional) | Dilute chromate or organic tarnish inhibitor; 15-30 seconds |

### Poster 8: Post Treatment

**PCB through-hole process:**
- No standalone post-treatment -- parts proceed directly to electrolytic acid copper buildup (25-50 um) to achieve final through-hole copper thickness
- The electroless copper seed layer is purely a conductive bridge for electrolytic deposition

**EMI shielding / plastics metallization:**
- Anti-tarnish dip: organic passivator (benzotriazole-based) or trivalent chromate
- Annealing: 150-200C, 1-2 hr improves ductility and adhesion on plastic substrates
- Do not anneal plastic substrates above their glass transition temperature (Tg):
  - ABS: Tg ~105C
  - PC: Tg ~147C
  - FR4: Tg ~130-170C (varies by grade)

---

# PROCESS 5: Electroless Palladium

## 5.1 Process Identity

| Attribute | Value |
|---|---|
| Deposit composition | Pure palladium (Pd) or Pd-P alloy (1-7% P depending on reducing agent) |
| Deposit structure | Crystalline (pure Pd) or amorphous (Pd-P alloy) |
| Reducing agent | Hypophosphite (for Pd-P), hydrazine (for pure Pd), formic acid (for pure Pd) |
| Primary applications | ENEPIG PCB finish, hydrogen permeation membranes, electronics connectors, catalysis |
| Governing standard | IPC-4556 (ENEPIG) |
| Common abbreviation | E-Pd, electroless Pd |

## 5.2 Autocatalytic Mechanism

**With hypophosphite reducing agent (produces Pd-P alloy):**
```
Pd2+ + H2PO2- + H2O --> Pd0 + H2PO3- + 2 H+
```
- Analogous to EN-P mechanism; phosphorus co-deposits into Pd matrix
- Pd-P alloys contain 1-7% P depending on pH and complexant

**With hydrazine reducing agent (produces pure Pd):**
```
2 Pd2+ + N2H4 + 4 OH- --> 2 Pd0 + N2 + 4 H2O
```
- Produces phosphorus-free, pure palladium deposit
- Hydrazine is toxic and a suspected carcinogen -- handling concerns
- No byproduct metal or phosphorus contamination in deposit

**With formic acid (produces pure Pd):**
```
Pd2+ + HCOOH + 2 OH- --> Pd0 + CO2 + H2O + H2O
```
- Newer alternative to hydrazine; less toxic
- Requires precise pH control

## 5.3 Poster-by-Poster Data

### Poster 1: Process Flow (Summary)

**Flow sequence (ENEPIG):**
```
Cleaner --> Rinse --> Microetch --> Rinse --> Acid Dip -->
EN Mid-P (3-5 um) --> Rinse --> Electroless Pd (0.05-0.3 um) -->
Rinse --> Immersion Gold (0.03-0.1 um) --> Rinse --> Dry
```

**Key callouts:**
- Ultra-thin deposit (0.05-0.3 um for ENEPIG; up to 1-5 um for other applications)
- Diffusion barrier layer in ENEPIG -- prevents nickel diffusion into gold, reducing "black pad" defect
- Hydrogen permeation membranes: Pd films on porous ceramic substrates (5-25 um)
- Superior corrosion resistance; noble metal
- IPC-4556 governs ENEPIG specification

### Poster 2: Cleaning

Same alkaline soak clean / electroclean protocols as preceding processes. For PCB (ENEPIG), same cleaner/conditioner used for entire ENIG/ENEPIG line.

### Poster 3: Rinse -- Pre-Activation

Standard DI counterflow rinse. Same parameters as EN processes.

### Poster 4: Activation

**For ENEPIG:** No separate Pd activation needed -- the electroless palladium bath plates directly onto the freshly deposited EN layer. The EN surface is catalytic for Pd deposition.

**For non-catalytic substrates (ceramics, glass, polymers):**
- Sn/Pd colloidal activation (same as electroless copper) followed by accelerator
- Or: direct Pd activation from PdCl2 / HCl solution (0.1-0.5 g/L Pd; 20-40C; 30-60 sec)

**For hydrogen permeation membranes:**
- Sn2+ sensitization: 1 g/L SnCl2 in 1 mL/L HCl; ambient; 3-5 min
- Pd activation: 0.1 g/L PdCl2 in 1 mL/L HCl; ambient; 3-5 min
- Multiple sensitization/activation cycles (up to 10) may be needed for uniform coverage on porous ceramic

### Poster 5: Rinse -- Pre-Plate

Standard DI rinse. Minimize transfer time from activation/EN to electroless Pd bath to prevent surface oxidation.

### Poster 6: Main Tank -- Electroless Palladium Bath

**Bath composition (hypophosphite-based, most common commercial):**
| Component | Concentration | Role |
|---|---|---|
| Palladium chloride (PdCl2) or Pd(NH3)4Cl2 | 0.5-3.0 g/L Pd2+ | Metal ion source |
| Sodium hypophosphite (NaH2PO2 . H2O) | 5-15 g/L | Reducing agent (produces Pd-P) |
| EDTA or ethylenediamine | 10-30 g/L | Complexant |
| Ammonium hydroxide or ammonia | pH adjustment | Buffer + complexant (amine-Pd complex) |
| Stabilizer (thiodiglycolic acid or similar) | 1-10 mg/L | Prevents spontaneous decomposition |

**Bath composition (hydrazine-based, pure Pd):**
| Component | Concentration | Role |
|---|---|---|
| Palladium chloride | 1-3 g/L Pd2+ | Metal ion source |
| Hydrazine hydrate (N2H4 . H2O) | 0.5-3 mL/L | Reducing agent (produces pure Pd) |
| EDTA | 20-40 g/L | Complexant |
| NH4OH | as needed | pH adjustment |

**Operating parameters:**
| Parameter | Hypophosphite Bath | Hydrazine Bath |
|---|---|---|
| pH | 5.0-7.0 | 9.0-11.0 |
| Temperature | 40-70C (105-158F) | 50-70C (122-158F) |
| Deposition rate | 1-5 um/hr | 1-3 um/hr |
| Typical thickness (ENEPIG) | 0.05-0.3 um | 0.05-0.3 um |
| Typical thickness (membranes) | 5-25 um | 5-25 um |
| Bath life | 3-5 MTO | 2-4 MTO |

**Deposit properties:**
| Property | Pd-P Alloy | Pure Pd |
|---|---|---|
| Hardness | 400-600 HV | 200-300 HV |
| Corrosion resistance | Excellent | Excellent |
| Solderability | Excellent | Excellent |
| Wire bondability | Excellent (key for ENEPIG) | Excellent |
| Hydrogen permeability | Moderate (P inhibits) | Excellent (pure Pd membranes) |
| Magnetic | Non-magnetic | Non-magnetic |

### Poster 7: Rinse -- Post-Plate

Standard DI rinse. For ENEPIG, parts proceed immediately to immersion gold bath after rinsing. Minimize air exposure time -- Pd surface oxidizes less than Ni but still benefits from quick transfer.

### Poster 8: Post Treatment

**ENEPIG:** No post-treatment between Pd and Au in the ENEPIG stack. After immersion gold, parts are rinsed, dried (air knife + oven dry at 60-80C), and proceed to assembly.

**Hydrogen permeation membranes:**
- Annealing at 400-600C in inert atmosphere (N2 or Ar) for 1-4 hours
- Improves grain structure, hydrogen selectivity, and mechanical integrity
- Some membrane applications use Pd-Ag alloy (23-25 wt% Ag) to resist hydrogen embrittlement at <300C

**Electronics connectors:**
- Optional: thin immersion gold or electrolytic gold flash over electroless Pd for enhanced contact resistance and oxidation protection

---

# PROCESS 6: Electroless Gold

## 6.1 Process Identity

| Attribute | Value |
|---|---|
| Deposit composition | Pure gold (Au) or Au-P alloy (if hypophosphite reducing agent) |
| Deposit type | Autocatalytic (true electroless) vs. immersion (galvanic displacement) -- CRITICAL DISTINCTION |
| Reducing agent | Hypophosphite, DMAB, ascorbic acid, thiosulfate (autocatalytic); no reducing agent needed for immersion gold |
| Primary applications | ENIG/ENEPIG PCB finish, electronics connectors, bonding pads |
| Governing standard | IPC-4552B (ENIG), IPC-4556 (ENEPIG) |
| Common abbreviation | E-Au (autocatalytic), IG (immersion gold) |

## 6.2 Mechanism -- Two Distinct Processes

**CRITICAL DISTINCTION for poster accuracy:**

### Immersion Gold (Galvanic Displacement -- NOT autocatalytic)

This is the gold layer in ENIG (IPC-4552B) and ENEPIG (IPC-4556). It is NOT a true electroless process -- it is a galvanic displacement reaction:

```
Ni0 + Au+ --> Ni2+ + Au0    (simplified)
```
Or more precisely:
```
3 Ni0 + 2 Au3+ --> 3 Ni2+ + 2 Au0
```

- Nickel from the EN layer dissolves (oxidized to Ni2+)
- Gold ions are reduced to metallic gold (Au0) at the expense of nickel dissolution
- Reaction is self-limiting: once the gold layer completely covers the nickel surface, no more nickel can dissolve, and deposition stops
- Produces ultra-thin gold: 0.03-0.1 um (30-100 nm)
- This is why ENIG gold is so thin -- it's displacement, not autocatalytic

**"Black pad" failure mechanism:** If gold deposition is aggressive (high Au concentration, high temperature, low pH), excessive nickel corrosion occurs at the Ni/Au interface, creating a phosphorus-enriched "black" layer that causes solder joint failure. This is the most feared defect in ENIG and the primary reason IPC-4552B exists.

### Autocatalytic (True Electroless) Gold

True electroless gold uses a chemical reducing agent and is autocatalytic -- deposition continues as long as chemistry is maintained, allowing thicker deposits:

**With hypophosphite:**
```
Au+ + H2PO2- + H2O --> Au0 + H2PO3- + 2 H+
```

**With DMAB (dimethylamine borane):**
```
Au+ + (CH3)2NHBH3 + 3 H2O --> Au0 + (CH3)2NH + H3BO3 + 5 H+ + 2 e-
```

**With ascorbic acid:**
```
2 Au+ + C6H8O6 --> 2 Au0 + C6H6O6 + 2 H+
```

Autocatalytic gold can deposit 1-5+ um -- much thicker than immersion gold. Used for wire bonding pads, high-reliability electronics, and where thicker gold is needed.

## 6.3 Poster-by-Poster Data

### Poster 1: Process Flow (Summary)

**Flow sequence (ENIG -- most common):**
```
Cleaner --> Microetch --> Acid Dip --> Rinse -->
EN Mid-P (3-6 um) --> Rinse --> Immersion Gold (0.03-0.1 um) -->
Rinse --> Dry
```

**Flow sequence (Autocatalytic gold -- wire bonding):**
```
Cleaner --> Activation --> Rinse --> Electroless Gold Bath -->
Rinse --> Dry (or further processing)
```

**Key callouts:**
- ENIG: immersion gold is a displacement reaction, not autocatalytic
- Autocatalytic gold: uses reducing agent for thicker deposits
- IPC-4552B: EN 3-6 um, P% 6-9%, Au 0.03-0.1 um
- Black pad risk: excessive nickel corrosion at Ni/Au interface
- Gold provides oxidation-free, solderable surface
- Cost: gold chemistry is expensive; bath maintenance is critical for economics

### Poster 2: Cleaning

Same as ENIG line cleaning (see Process 2, Poster 2 for PCB context). For standalone electroless gold:
- Alkaline soak clean appropriate to substrate
- For electronics: no silicate cleaners (silicate residues on gold cause wire bond failures)

### Poster 3: Rinse -- Pre-Activation

Standard DI counterflow rinse. For ENIG/ENEPIG, this is the rinse after EN plating and before gold.

### Poster 4: Activation

**For immersion gold (ENIG):** No activation -- the EN surface itself is the driving force for displacement. Parts go directly from EN rinse to gold bath.

**For autocatalytic gold on non-catalytic substrates:**
- Pd activation from PdCl2/HCl solution
- Or: colloidal Sn/Pd followed by accelerator (same as E-Cu process)

### Poster 5: Rinse -- Pre-Plate

For ENIG: rinse between EN bath and gold bath. Critical to remove EN drag-out -- hypophosphite drag-in can reduce Au3+ uncontrollably in the gold bath.

### Poster 6: Main Tank

**Immersion gold bath (ENIG):**
| Component | Concentration | Role |
|---|---|---|
| Gold as KAu(CN)2 or Na3Au(SO3)2 | 0.5-2.0 g/L Au | Gold ion source |
| Citric acid or sodium citrate | 10-30 g/L | Complexant + buffer |
| Thallium or proprietary additive | Trace (ppm) | Controls deposition rate / grain structure |
| pH adjuster | NaOH or citric acid | Maintain target pH |

| Parameter | Value |
|---|---|
| pH | 4.5-6.0 (acid gold, most common); 7.0-8.0 (neutral gold formulations) |
| Temperature | 80-90C (176-194F) |
| Gold concentration | 0.5-2.0 g/L Au |
| Immersion time | 5-15 minutes |
| Target thickness | 0.03-0.10 um (IPC-4552B: 0.05 um minimum recommended) |
| Bath type | Cyanide-based (KAu(CN)2) or non-cyanide (sulfite-based Na3Au(SO3)2) |

**Autocatalytic gold bath:**
| Component | Concentration | Role |
|---|---|---|
| Gold (KAu(CN)2 or sulfite complex) | 1-5 g/L Au | Metal ion source |
| Reducing agent (DMAB, hypophosphite, or ascorbic acid) | 1-10 g/L | Drives autocatalytic reduction |
| KCN or sodium sulfite | 5-15 g/L | Complexant |
| Stabilizer | Proprietary, ppm-level | Prevents decomposition |

| Parameter | Value |
|---|---|
| pH | 6.0-8.0 (neutral to slightly alkaline) |
| Temperature | 60-80C (140-176F) |
| Deposition rate | 1-3 um/hr |
| Typical thickness | 1-5 um |
| Bath life | 1-3 MTO (gold is expensive; bath economics are critical) |

**Deposit properties:**
| Property | Immersion Gold | Autocatalytic Gold |
|---|---|---|
| Thickness | 0.03-0.10 um | 1-5+ um |
| Purity | >99.9% Au | >99% Au (may contain P or B from reducing agent) |
| Solderability | Excellent (gold dissolves into solder) | Excellent |
| Wire bondability | Marginal (too thin for gold wire bonding) | Excellent |
| Corrosion resistance | Excellent (noble metal) | Excellent |
| Contact resistance | Very low | Very low |
| Cost per dm2 | Low (thin film) | High (thick film, concentrated bath) |

### Poster 7: Rinse -- Post-Plate

| Parameter | Value |
|---|---|
| Type | DI counterflow (gold recovery rinse before main rinse -- economics!) |
| First stage | Stagnant DI "gold recovery" rinse -- accumulates gold drag-out for reclamation |
| Second/third stage | Flowing DI rinse |
| Drying | Forced air (air knife) + low-temperature oven (60-80C) |

**Gold recovery:** Given gold's high cost ($80-100+ per gram), drag-out recovery is economically critical. Many ENIG lines include a dedicated stagnant recovery rinse that is periodically sent to gold refining.

### Poster 8: Post Treatment

**ENIG/ENEPIG:**
- No heat treatment -- gold surface is ready for soldering/bonding as-plated
- Oven dry at 60-80C to remove moisture
- Store in nitrogen atmosphere or vacuum-sealed bags to prevent contamination before assembly

**Autocatalytic gold for wire bonding:**
- May require thermal annealing at 150-200C to optimize grain structure for thermosonic wire bonding
- Gold thickness for wire bonding: typically 0.5-1.5 um minimum

---

# PROCESS 7: Electroless Cobalt

## 7.1 Process Identity

| Attribute | Value |
|---|---|
| Deposit composition | Co-P alloy (2-12% P), Co-B alloy (1-6% B), or Co-W-P ternary alloy |
| Deposit structure | Amorphous (high P/B) to crystalline (low P/B) |
| Magnetic behavior | Ferromagnetic; tunable coercivity |
| Reducing agent | Hypophosphite (for Co-P), DMAB (for Co-B), hydrazine (for pure Co) |
| Primary applications | Magnetic recording media, data storage, MEMS, capping layer for ENIG |
| Governing standard | No direct ASTM standard; characterized per application specifications |
| Common abbreviation | E-Co, electroless Co |

## 7.2 Autocatalytic Mechanism

**With hypophosphite (Co-P alloy):**
```
Co2+ + H2PO2- + H2O --> Co0 + H2PO3- + 2 H+
```
Directly analogous to EN-P. Phosphorus co-deposits, producing amorphous Co-P alloy at high P%.

**With DMAB (Co-B alloy):**
```
Co2+ + (CH3)2NHBH3 + H2O --> Co0 + (CH3)2NH + H3BO3 + H+ + ...
```
Boron co-deposits, producing Co-B alloy with different magnetic properties than Co-P.

**Key difference from EN:** Cobalt has a higher standard reduction potential than nickel (-0.28 V vs. -0.26 V for Ni -- similar), but the complexant and stabilizer requirements differ significantly. Cobalt baths tend to be less stable than EN baths and have shorter bath life.

## 7.3 Poster-by-Poster Data

### Poster 1: Process Flow (Summary)

**Flow sequence:**
```
Clean --> Rinse --> Activate (Pd or substrate-dependent) --> Rinse -->
Electroless Co Bath --> Rinse --> Post-Treatment (anneal / passivate)
```

**Key callouts:**
- Ferromagnetic deposit -- coercivity tunable by composition and heat treatment
- Used in magnetic recording (thin-film hard disk media) -- historical importance
- Modern applications: MEMS magnetic layers, capping layer over EN in ENEPIG (IPC-4556 variant)
- Co-W-P ternary: enhanced thermal stability for diffusion barrier in advanced packaging
- Niche process -- much less common than EN; specialized suppliers
- Bath stability is challenging -- shorter bath life than EN (2-4 MTO typical)

### Poster 2: Cleaning

Same alkaline clean / electroclean protocols as EN. Substrate-dependent cleaning.

### Poster 3: Rinse -- Pre-Activation

Standard DI counterflow rinse. Same parameters as EN processes.

### Poster 4: Activation

**On copper/nickel substrates:** Direct immersion -- copper and nickel are catalytic for cobalt deposition (though initiation may be slow; brief Pd flash activation improves reliability)

**On non-catalytic substrates:**
- Sn/Pd colloidal activation + accelerator (same as E-Cu)
- Or: PdCl2 / HCl activation (0.1-0.5 g/L Pd; 30-60 sec)

**On silicon wafers (MEMS):**
- HF dip (10-50% HF; 30-60 sec) to remove native SiO2
- Pd activation from PdCl2 / HCl
- Or: sputtered Pd seed layer (vacuum-deposited)

### Poster 5: Rinse -- Pre-Plate

Standard DI rinse. Short transfer time to prevent surface re-oxidation.

### Poster 6: Main Tank -- Electroless Cobalt Bath

**Bath composition (Co-P, hypophosphite-based):**
| Component | Concentration | Role |
|---|---|---|
| Cobalt sulfate (CoSO4 . 7H2O) or cobalt chloride | 15-30 g/L Co2+ | Metal ion source |
| Sodium hypophosphite (NaH2PO2 . H2O) | 15-30 g/L | Reducing agent |
| Sodium citrate | 30-60 g/L | Primary complexant |
| Ammonium sulfate | 20-40 g/L | Buffer + complexant |
| Boric acid | 10-20 g/L | Buffer |
| Stabilizer (thiourea, Pb2+, or 2-mercaptobenzothiazole) | 0.5-5 ppm | Prevents decomposition |

**Bath composition (Co-W-P ternary alloy -- advanced packaging):**
| Component | Concentration | Role |
|---|---|---|
| Cobalt sulfate | 10-20 g/L Co2+ | Metal source |
| Sodium tungstate (Na2WO4) | 10-40 g/L | Tungsten source (co-deposits with Co-P) |
| Sodium hypophosphite | 15-25 g/L | Reducing agent |
| Sodium citrate | 40-80 g/L | Complexant (critical for W incorporation) |
| Boric acid | 15-25 g/L | Buffer |

**Operating parameters:**
| Parameter | Co-P | Co-W-P |
|---|---|---|
| pH | 8.0-10.0 | 8.5-10.5 |
| Temperature | 70-90C (158-194F) | 65-85C (150-185F) |
| Deposition rate | 3-8 um/hr | 1-5 um/hr |
| Bath life | 2-4 MTO | 1-3 MTO |
| Deposit P content | 2-12 wt% | 2-8 wt% P + 2-15 wt% W |

**Deposit properties:**
| Property | Co-P (low P) | Co-P (high P) | Co-W-P |
|---|---|---|---|
| Hardness (as-plated) | 400-550 HV | 500-700 HV | 500-800 HV |
| Magnetic coercivity | High (>500 Oe) | Low (<100 Oe) | Medium |
| Saturation magnetization | High | Low (amorphous) | Medium |
| Corrosion resistance | Moderate | Good | Very good |
| Thermal stability | Moderate | Moderate | Excellent (W inhibits crystallization) |

### Poster 7: Rinse -- Post-Plate

Standard DI counterflow rinse. Handle carefully -- cobalt surfaces oxidize readily in air.

### Poster 8: Post Treatment

**Magnetic recording media:**
- Annealing at 200-400C in vacuum or inert atmosphere to optimize magnetic properties (coercivity and squareness ratio)
- Temperature and atmosphere are application-specific

**Diffusion barrier (advanced packaging):**
- Co-W-P layers typically used as diffusion barriers between copper interconnects and low-k dielectrics
- No post-treatment required; the barrier function is inherent to the amorphous alloy structure
- Thermal stability verified by annealing studies up to 500-600C

**Passivation:**
- Trivalent chromate conversion or organic inhibitor (benzotriazole derivative) to prevent cobalt oxidation
- Required for any application where the cobalt surface is the final exposed surface

---

# PROCESS 8: Electroless Nickel-Boron (EN-B)

## 8.1 Process Identity

| Attribute | Value |
|---|---|
| Deposit composition | Ni-B alloy, 0.5-5 wt% boron (typically 1-5%) |
| Deposit structure | Amorphous (high B%) to microcrystalline (low B%) |
| Magnetic behavior | Generally non-magnetic at >3% B (amorphous); weakly magnetic at <2% B |
| Reducing agent | DMAB (dimethylamine borane, (CH3)2NHBH3) or sodium borohydride (NaBH4) |
| Governing standard | ASTM B841 — Standard Specification for Electroless Nickel-Boron Coatings |
| Common abbreviation | EN-B, Ni-B |

## 8.2 Autocatalytic Mechanism

**With DMAB (most common):**
```
Ni2+ + (CH3)2NHBH3 + H2O --> Ni0 + (CH3)2NH + H3BO3 + ... + H+
```

- DMAB (dimethylamine borane) serves as the reducing agent instead of hypophosphite
- Boron co-deposits into the nickel matrix instead of phosphorus
- The amine byproduct ((CH3)2NH, dimethylamine) is volatile and requires ventilation
- Boric acid (H3BO3) is produced as a byproduct

**With sodium borohydride:**
```
Ni2+ + NaBH4 + ... --> Ni0 + B0 + ...   (simplified; complex multi-step mechanism)
```

- NaBH4 is a stronger reducing agent than DMAB
- Produces higher boron content (3-8%) and faster deposition
- Strongly alkaline bath required (pH 12-14) to prevent borohydride decomposition
- More difficult to control than DMAB; higher decomposition risk
- Produces higher boron deposits with superior hardness

**Key chemistry differences from EN-P:**
- DMAB is 5-10x more expensive per unit reducing power than hypophosphite -- EN-B is significantly more costly to operate
- No orthophosphite accumulation (no phosphorus chemistry involved)
- Instead, borate (BO3 3-) accumulates as byproduct
- Bath life is shorter: 3-5 MTO for DMAB baths; 2-4 MTO for borohydride baths
- Deposit is harder as-plated than equivalent EN-P: 700-800 HV for EN-B vs. 450-550 HV for EN High-P

## 8.3 Poster-by-Poster Data

### Poster 1: Process Flow (Summary)

**Flow sequence:**
```
Alkaline Clean --> Rinse --> Acid Activation --> Rinse -->
EN-B Bath --> Rinse --> Post-Treatment (HT for max hardness)
```

**Key callouts:**
- Highest as-plated hardness of any electroless nickel: 700-800 HV (DMAB); up to 850 HV (borohydride)
- Heat-treated hardness: 1000-1200 HV -- exceeds hard chrome
- Low coefficient of friction: 0.05-0.12 (dry) -- superior to EN-P
- Excellent solderability (better than EN High-P)
- Significantly more expensive than EN-P (DMAB cost)
- ASTM B841 is the governing specification
- Lower corrosion resistance than EN High-P (EN-B is crystalline at low B%)
- Primary competitor to hard chrome for wear applications

### Poster 2: Cleaning

Identical cleaning protocols to EN-P processes (see Process 1, Poster 2). All EN processes share the same cleaning requirements.

### Poster 3: Rinse -- Pre-Activation

Standard DI counterflow rinse. Same parameters as EN-P processes.

### Poster 4: Activation

Same substrate-dependent activation as EN-P (see Process 1, Poster 4):
- Steel: HCl or H2SO4 acid activation
- Aluminum: zincate (double zincate recommended)
- Stainless: Wood's nickel strike
- Plastics: Sn/Pd colloidal activation

**EN-B specific note:** The EN-B bath is highly active and will initiate on most clean metallic surfaces. Some operators report that EN-B is less sensitive to marginal activation than EN-P, but proper activation is still required for specification-grade adhesion.

### Poster 5: Rinse -- Pre-Plate

Standard DI rinse. Same contamination concerns as EN-P:
- Chloride drag-in causes pitting
- Chromate drag-in poisons stabilizer system

### Poster 6: Main Tank -- EN-B Bath

**Bath composition (DMAB-based -- most common commercial):**
| Component | Concentration | Role |
|---|---|---|
| Nickel chloride (NiCl2 . 6H2O) or nickel sulfate | 20-30 g/L Ni2+ | Metal ion source |
| DMAB ((CH3)2NHBH3) | 2-5 g/L | Reducing agent |
| Ethylenediamine (EDA) | 30-60 g/L | Primary complexant |
| NaOH | As needed | pH adjustment |
| Thallium acetate or lead acetate | 0.5-2 ppm | Stabilizer |
| Thiodiglycolic acid | 1-5 mg/L | Co-stabilizer |

**Bath composition (sodium borohydride-based -- higher B content):**
| Component | Concentration | Role |
|---|---|---|
| Nickel chloride (NiCl2 . 6H2O) | 20-30 g/L Ni2+ | Metal ion source |
| Sodium borohydride (NaBH4) | 0.5-1.5 g/L | Reducing agent |
| Ethylenediamine | 40-80 g/L | Complexant |
| NaOH | 40-90 g/L | pH control (strongly alkaline required) |
| Thallium nitrate | 1-5 ppm | Stabilizer |

**Operating parameters:**
| Parameter | DMAB Bath | Borohydride Bath |
|---|---|---|
| pH | 6.0-8.0 (mildly acidic to mildly alkaline) | 12.0-14.0 (strongly alkaline) |
| Temperature | 60-75C (140-167F) | 90-95C (194-203F) |
| Nickel concentration | 4-6 g/L Ni2+ | 4-6 g/L Ni2+ |
| Deposition rate | 8-15 um/hr | 15-25 um/hr |
| Boron content | 0.5-3 wt% B | 3-8 wt% B |
| Bath life | 3-5 MTO | 2-4 MTO |
| Loading (A/V) | 0.2-0.5 dm2/L | 0.2-0.5 dm2/L |

**Deposit properties:**
| Property | DMAB EN-B | Borohydride EN-B |
|---|---|---|
| Boron content | 0.5-3 wt% | 3-8 wt% |
| Hardness (as-plated) | 700-800 HV | 750-850 HV |
| Hardness (heat-treated 350-400C) | 1000-1200 HV | 1100-1300 HV |
| Structure | Microcrystalline to amorphous | Amorphous |
| Coefficient of friction (dry) | 0.08-0.12 | 0.05-0.10 |
| Solderability | Good | Good |
| Wear resistance | Excellent -- comparable to or exceeding hard chrome | Excellent |
| Corrosion resistance (salt spray, 25 um) | 200-500 hours | 300-600 hours |
| Lubricity | Superior to EN-P | Superior to EN-P |

**Comparison: EN-B vs. EN-P vs. Hard Chrome:**
| Property | EN-B (heat-treated) | EN High-P (heat-treated) | Hard Chrome |
|---|---|---|---|
| Hardness (HV) | 1000-1200 | 800-900 | 900-1100 |
| Coefficient of friction | 0.05-0.12 | 0.10-0.15 | 0.12-0.16 |
| Corrosion (salt spray) | 200-500 hrs | 1,000+ hrs | 24-100 hrs (porous micro-cracked) |
| Environmental concern | Low | Low | HIGH (Cr6+ chemistry) |
| Cost | High (DMAB) | Moderate | Low-moderate |

**Bath stability management:**
- DMAB decomposes slowly at operating temperature even without catalytic surface -- bath must not idle at temp without load
- DMAB baths are more susceptible to metal contamination (Fe, Cu) than EN-P baths
- Nickel chloride is preferred over nickel sulfate in many EN-B formulations because chloride aids activation
- Borate accumulates as byproduct; contributes to viscosity increase and eventual bath retirement
- Filter continuously (1-5 um)

### Poster 7: Rinse -- Post-Plate

Standard DI counterflow rinse. Same handling precautions as EN-P:
- Do not air-dry before rinsing
- Avoid fingerprint contact
- Cold rinse preferred to stop reaction

### Poster 8: Post Treatment

**Heat treatment for maximum hardness:**
| Treatment | Temperature | Time | Result |
|---|---|---|---|
| HE relief (high-strength steel) | 190-210C | 2-23 hours | Hydrogen removal; within 4 hours of plating |
| Intermediate hardening | 280-320C | 1-2 hours | 900-1000 HV; retains some ductility |
| Maximum hardness | 350-400C | 1 hour | 1000-1200+ HV; Ni3B precipitation hardening |

**Hardening mechanism:** Analogous to EN-P -- heat treatment precipitates Ni3B intermetallic (instead of Ni3P), which pins dislocations and dramatically increases hardness. The crystallization from amorphous to nanocrystalline Ni + Ni3B is the hardening event.

**Post-treatment options:**
- Passivation: trivalent chromate conversion for additional corrosion protection (EN-B's corrosion resistance is lower than EN High-P)
- EN-PTFE composite analogue: EN-B with co-deposited PTFE or MoS2 particles further reduces friction to 0.02-0.05 (dry)

---

# CROSS-CUTTING TECHNICAL TOPICS

These topics apply across all 8 electroless processes and should inform poster content throughout.

## Common Failures Across All Electroless Processes

### Skip Plating (No Deposition)
**Cause:** Insufficient cleaning, inadequate activation, stabilizer poisoning, low bath temperature, contaminated substrate
**Visual:** Bare substrate visible; deposit did not form in affected areas
**Cure:** Improve cleaning; verify activation coverage; check stabilizer level; verify temperature

### Exothermic Decomposition (Bath Crash)
**Cause:** Under-loaded bath at operating temperature; depleted stabilizer; metallic contamination (Fe, Cu particles act as nucleation sites); heater hot spots
**Visual:** Sudden uncontrolled gassing; black nickel powder precipitates; temperature spike (can be violent -- fire hazard)
**Prevention:** Never idle bath at temp without load; maintain stabilizer; filter continuously; inspect heater elements

### Pitting
**Cause:** Hydrogen bubbles adhering to part surface; inadequate agitation; organic contamination; insufficient wetting agent
**Visual:** Small pinholes in deposit surface
**Cure:** Increase agitation (air or mechanical); add wetting agent; carbon treat bath

### Poor Adhesion
**Cause:** Inadequate cleaning or activation; improper zincate on aluminum; surface passivation between process steps; excessive delay between activation and plating
**Visual:** Deposit blisters, peels, or flakes during bend test or adhesion tape test
**Cure:** Review cleaning and activation; minimize transfer times; verify zincate quality

### Roughness / Nodulation
**Cause:** Particulate contamination in bath; inadequate filtration; bath age (high MTO); metallic contamination
**Visual:** Grainy, rough, or nodular deposit surface
**Cure:** Continuous filtration (1-5 um); dump/replenish if high MTO; remove metallic contaminants

### Phosphorus Content Out of Specification (EN-P specific)
**Cause:** pH drift (most common); temperature excursion; exhausted complexant; high MTO
**Visual:** Cannot be determined visually -- requires XRF, ICP, or wet chemical analysis
**Cure:** Tighten pH control (+/-0.2); verify temperature; check MTO

## Bath Stability and Decomposition Prevention

All electroless baths share the fundamental stability challenge: the reducing agent (hypophosphite, DMAB, formaldehyde, borohydride) can react with metal ions in the bulk solution, not just at the catalytic surface. Stabilizers suppress this bulk reaction at ppm levels. The balance between stability and activity is narrow:

| Stabilizer Level | Effect |
|---|---|
| Too low | Bath decomposes spontaneously -- catastrophic |
| Optimal | Bulk reaction suppressed; surface reaction proceeds normally |
| Too high | Surface reaction also suppressed -- "poisoned" bath; no deposition |

**Universal stability rules:**
1. Never leave bath at operating temperature without parts (or dummy load)
2. Cool bath to <40C when not in use (reduces reaction kinetics to negligible)
3. Filter continuously to remove metallic particles that serve as nucleation sites
4. Monitor stabilizer consumption and replenish per supplier protocol
5. Loading ratio control: 0.2-0.5 dm2/L optimal; <0.1 dm2/L is danger zone

## MTO Tracking Across Processes

| Process | Typical Bath Life (MTO) | Limiting Byproduct |
|---|---|---|
| EN Low-P | 6-8 | Orthophosphite (H2PO3-) |
| EN Mid-P | 6-8 | Orthophosphite |
| EN High-P | 6-8 | Orthophosphite |
| Electroless Copper | 1-4 | Formate (HCOO-) + EDTA degradation |
| Electroless Palladium | 3-5 (hypophosphite); 2-4 (hydrazine) | Orthophosphite or N2H4 breakdown products |
| Electroless Gold (autocatalytic) | 1-3 | Reducing agent byproducts; gold dragout economics |
| Electroless Cobalt | 2-4 | Orthophosphite / borate |
| EN-B (DMAB) | 3-5 | Borate (BO3 3-) + dimethylamine |
| EN-B (borohydride) | 2-4 | Borate |

## Key Standards Reference

| Standard | Process | What It Covers |
|---|---|---|
| ASTM B733 | EN-P (all P classes) | Type (P content), Class (heat treatment), Service Class (thickness) |
| ASTM B841 | EN-B | Specification for electroless nickel-boron coatings |
| IPC-4552B | ENIG | EN layer + immersion gold for PCB; thickness and P% requirements |
| IPC-4556 | ENEPIG | EN + electroless Pd + immersion gold for PCB |
| AMS 2404 | EN on steel | Aerospace electroless nickel specification |
| AMS 2405 | EN on aluminum/magnesium | Aerospace EN with zincate pre-treatment |
| MIL-C-26074 | EN (legacy military) | Largely superseded by ASTM B733 and AMS 2404 |
| ASTM B849 | Pre-treatment for HE relief | Pre-plating bake requirements for high-strength steel |
| ASTM B850 | Post-treatment for HE relief | Post-plating bake requirements for high-strength steel |
| AMS 2759/9 | HE relief | Hydrogen embrittlement relief baking |
| ASTM F2088 | EN magnetic testing | Non-magnetic verification for EN High-P |
| ASTM E384 | Hardness testing | Micro-Vickers and Knoop for thin coatings |
| ASTM E140 | Hardness conversion | HV-to-HRC conversion tables |

## Reducing Agent Comparison

| Reducing Agent | Formula | Used In | Primary Byproduct | Key Hazard | Relative Cost |
|---|---|---|---|---|---|
| Sodium hypophosphite | NaH2PO2*H2O | EN-P (all classes), E-Co-P, E-Pd | Orthophosphite (H2PO3-) | Flammable solid (dry); no water for fire | Low |
| Formaldehyde (37%) | HCHO | Electroless Cu | Formate (HCOO-) | IARC Group 1 carcinogen; OSHA PEL 0.75 ppm TWA | Low |
| DMAB (dimethylamine borane) | (CH3)2NHBH3 | EN-B, E-Co-B, autocatalytic Au | Boric acid + dimethylamine | Flammable solid; H2 evolution | High (~5-10x hypophosphite) |
| Sodium borohydride | NaBH4 | EN-B (high-B), autocatalytic Au | Sodium metaborate (NaBO2) | EXTREMELY flammable; explosive H2 with acid | Very high |
| Hydrazine hydrate | N2H4*H2O | Electroless Pd (pure Pd) | Nitrogen gas (N2) | IARC Group 2B; toxic; OSHA PEL 1 ppm ceiling | Moderate |
| Formic acid | HCOOH | Electroless Pd (ENEPIG) | CO2 | Corrosive; moderate inhalation hazard | Low |
| Ascorbic acid | C6H8O6 | Autocatalytic Au (some formulations) | Dehydroascorbic acid | Low hazard | Moderate |

## Temperature Comparison

| Process | Operating Range (C) | Operating Range (F) |
|---|---|---|
| EN Low-P | 65-80 | 149-176 |
| EN Mid-P | 85-91 | 185-196 |
| EN High-P | 82-90 | 180-194 |
| Electroless Cu | 28-45 | 82-113 |
| Electroless Pd (hypophosphite) | 40-70 | 104-158 |
| Electroless Pd (hydrazine) | 50-70 | 122-158 |
| Immersion Au | 80-90 | 176-194 |
| Autocatalytic Au | 60-80 | 140-176 |
| Electroless Co-P | 70-90 | 158-194 |
| EN-B (DMAB) | 60-75 | 140-167 |
| EN-B (NaBH4) | 90-95 | 194-203 |

## Deposition Rate Comparison

| Process | Rate (um/hr) | Notes |
|---|---|---|
| EN Low-P | 10-15 | Moderate; alkaline bath |
| EN Mid-P | 18-25 | Fastest EN variant |
| EN High-P | 10-13 | Slowest acid EN |
| Electroless Cu | 1-5 | Very slow; seed layer only in most PCB applications |
| Electroless Pd | 1-5 | Very slow; ultra-thin deposits typical |
| Immersion Au | N/A (self-limiting) | 0.03-0.10 um total; 5-15 min immersion |
| Autocatalytic Au | 1-3 | Slow; gold is expensive per micron |
| Electroless Co-P | 3-8 | Moderate |
| EN-B (DMAB) | 8-15 | Comparable to EN Low-P |
| EN-B (NaBH4) | 15-25 | Comparable to EN Mid-P |

## Hardness Comparison (As-Plated and Heat-Treated)

| Process | As-Plated (HV) | Heat-Treated (HV) | HT Conditions |
|---|---|---|---|
| EN Low-P | 650-750 | 1000-1100 | 400C / 1 hr |
| EN Mid-P | 500-600 | 850-1000 | 400C / 1 hr |
| EN High-P | 450-550 | 800-900 | 400C / 1 hr |
| Electroless Cu | 60-100 | Not typically HT | -- |
| Electroless Pd (Pd-P) | 400-600 | Not typically HT | -- |
| Electroless Pd (pure) | 200-300 | Not typically HT | -- |
| Autocatalytic Au | 60-150 (HK) | Not typically HT | -- |
| Electroless Co-P | 400-700 | 800-1000 | 400C / 1 hr |
| EN-B (DMAB) | 700-800 | 1000-1200 | 350-400C / 1 hr |
| EN-B (NaBH4) | 750-850 | 1100-1300 | 350-400C / 1 hr |
| Hard chrome (reference) | 900-1100 | N/A (as-plated) | -- |

## Corrosion Resistance Comparison (NSS at 25 um deposit)

| Process | Approx. NSS Hours | Key Factor |
|---|---|---|
| EN High-P | 1,000+ | Amorphous; no grain boundaries |
| EN Mid-P | 240-500 | Mixed amorphous/crystalline |
| EN-B | 200-600 | More crystalline; grain boundary attack |
| EN Low-P | 96-240 | Most crystalline EN variant |
| Electroless Co-P | 100-300 | Less corrosion-resistant than Ni-P |
| Electroless Cu | 24-96 (environment-dependent) | Copper tarnishes; substrate-dependent |
| Electroless Pd | Excellent (noble metal) | Pd inherently corrosion-resistant |
| Immersion/Autocatalytic Au | Excellent (noble metal) | Au is the most corrosion-resistant coating |

## Analytical Methods Summary

| Analyte | Method | Applicable Process | Notes |
|---|---|---|---|
| Nickel (Ni2+) | EDTA titration (murexide indicator, pH 10 NH3/NH4Cl buffer) | EN-P, EN-B | Standard; Tyler procedures available |
| Hypophosphite (NaH2PO2) | Iodometric titration (I2 / starch endpoint) | EN-P, E-Co-P | Tyler procedures available |
| Orthophosphite (HPO3 2-) | Gravimetric (precipitate as MgNH4PO3) or ICP-OES | EN-P | Bath aging metric; discard >120 g/L |
| Copper (Cu2+) | EDTA titration (PAN or murexide indicator) or AAS | Electroless Cu | Tyler procedures available |
| Formaldehyde (HCHO) | Sodium sulfite method (Na2SO3 + HCHO --> products; back-titrate) | Electroless Cu | Measure free HCHO; replenish frequently |
| Palladium (Pd2+) | EDTA titration or AAS | Electroless Pd | Precious metal -- accurate analysis critical for cost control |
| Gold (Au) | AAS or fire assay | Immersion/autocatalytic Au | Precious metal -- drag-out recovery economics |
| Cobalt (Co2+) | EDTA titration (murexide or PAN indicator, pH 10) | Electroless Co | Similar to Ni titration; Co and Ni interfere with each other |
| DMAB | Iodometric or spectrophotometric | EN-B, E-Co-B | Less standardized than hypophosphite methods |
| Boron content (deposit) | ICP-OES after HCl/HNO3 dissolution | EN-B, Co-B | Requires dissolution of plated coupon |
| Phosphorus content (deposit) | XRF (non-destructive, preferred) or colorimetric molybdate | EN-P, Co-P, Pd-P | XRF is production standard for EN P% |
| pH | Glass electrode, calibrated at operating temperature | All electroless baths | Check every 30-60 min in EN production |
| Specific gravity | Hydrometer or digital densitometer | EN-P (bath aging) | Correlates with orthophosphite buildup |
| Plating rate | Gravimetric (weigh coupon before/after timed immersion) | All electroless | Primary QC test; no Hull cell for electroless |

## PPE Requirements -- Universal for Electroless Operations

| Hazard | PPE | Notes |
|---|---|---|
| Chemical splash (all baths) | Chemical splash goggles + face shield; chemical-resistant apron; neoprene or nitrile gloves | Minimum for any electroless bath operation |
| Formaldehyde vapor (E-Cu) | Full-face organic vapor respirator; continuous air monitoring required | IARC Group 1 carcinogen; OSHA PEL 0.75 ppm |
| Hydrazine vapor (E-Pd) | Full-face respirator with hydrazine-rated cartridge; emergency shower access | IARC Group 2B; OSHA PEL 1 ppm ceiling |
| Cyanide (gold cyanide baths) | Cyanide antidote kit within 30 feet; full-face respirator if not fully enclosed | HCN: TLV-TWA 4.7 ppm; IDLH 50 ppm |
| NaBH4 handling (EN-B high-B) | N95 dust mask minimum for dry handling; keep away from water and acid; Class D fire extinguisher nearby | Explosive H2 generation on contact with acid or water |
| Lead/thallium stabilizers | Nitrile gloves; prevent skin contact; wash before eating | Cumulative poisons; thallium LD50 ~15-30 mg/kg |
| NiSO4 aerosol (all EN baths) | Local exhaust ventilation; mist suppression; respiratory protection per OSHA | IARC Group 1 carcinogen as inhaled aerosol |
| Hot baths (65-95C) | Heat-resistant gloves for rack handling; face shield for splash | Thermal burn risk layered on chemical risk |
| Dimethylamine vapor (EN-B) | Local exhaust ventilation; respiratory protection if >10 ppm | Pungent ammonia-like odor; eye and respiratory irritant |

## Waste Treatment Summary

| Waste Stream | Treatment Method | Typical NPDES Discharge Limit |
|---|---|---|
| Nickel (from EN / EN-B baths) | Hydroxide precipitation at pH 8.5-9.5; settle; filter press | 0.5-3.0 mg/L Ni |
| Copper (from E-Cu baths) | EDTA destruction first (Fenton's reagent: Fe2+ + H2O2, or UV/H2O2); then hydroxide precipitation at pH 8.5-9.5 | 0.5-2.0 mg/L Cu |
| Palladium (from E-Pd baths) | Collect separately for precious metal recovery; hydroxide precipitation as secondary | Varies; recovery preferred (economic value) |
| Gold (from Au baths) | Collect separately; electrowinning or cementation (Zn dust) for recovery | Varies; recovery is economically mandatory |
| Cobalt (from E-Co baths) | Hydroxide precipitation at pH 8.5-9.5 | 0.5-2.0 mg/L Co (varies by permit) |
| Phosphite/phosphate (from hypophosphite baths) | Oxidize phosphite to phosphate (H2O2 or Ca(OCl)2); then precipitate as Ca3(PO4)2 at pH 9-10 | 1-5 mg/L total P |
| Formaldehyde (from E-Cu) | Chemical oxidation (Fenton's or NaOCl) or biological treatment | 0.05-1.0 mg/L HCHO |
| Cyanide (from gold cyanide baths) | Alkaline chlorination: Stage 1 at pH 10-11, ORP +350-400 mV (CN- to CNO-); Stage 2 at pH 7.5-8.5, ORP +600-650 mV (CNO- to CO2 + N2) | 0.01-1.0 mg/L total CN |
| Lead (from EN stabilizers) | Hydroxide/sulfide precipitation at pH 8.5-9.5 | 0.05-0.5 mg/L Pb |
| Thallium (from EN-B / Au stabilizers) | Sulfide precipitation or ion exchange; priority pollutant under Clean Water Act | 0.002-0.01 mg/L Tl (very strict) |
| Borate (from EN-B baths) | Generally not regulated as strictly as P; monitor per local permit | Check local NPDES permit |
| EDTA (from E-Cu rinse water) | UV/H2O2 or Fenton's destruction before metals precipitation; EDTA holds Cu in solution and defeats hydroxide treatment | Must destroy chelant before Cu can be precipitated |

## Qorvo Account Relevance

The Qorvo automatic plating line project uses electroless nickel as a core process. Based on typical semiconductor/electronics applications:

- **Most likely EN type**: Mid-P (ASTM B733 Type IV, 5-9% P) -- the standard for general electronics
- **Possible secondary**: Low-P for solderability or contact resistance requirements
- **ENIG or ENEPIG**: if Qorvo uses EN as PCB finish, IPC-4552B (ENIG) or IPC-4556 (ENEPIG) governs
- **Automatic line requirements**: continuous pH monitoring with automated NaOH/acid dosing; continuous temperature control +/-1C; automated replenishment based on plating rate x area x time; continuous filtration (5-10 um); MTO tracking via integrated controller
- **Activation**: depends on substrate -- aluminum requires double zincate on the automatic line

This content directly supports A Brite's technical service capability for the Qorvo project. Drew should confirm the specific EN variant and specifications in use at Qorvo before finalizing recommendations.

---

# COLLABORATION FLAGS

## Flags for Tyler (Lab Validation)

1. **EN-B deposition rates:** My DMAB bath rate of 8-15 um/hr and borohydride rate of 15-25 um/hr are from published literature. Tyler should verify against any EN-B supplier data sheets A Brite may have on file.

2. **Electroless copper formaldehyde concentrations:** Published ranges vary significantly (1-10 g/L HCHO). The 1-3 g/L range I've used represents modern thin-film PCB baths. Heavy-build formulations may use higher concentrations.

3. **Electroless palladium deposit phosphorus content (Pd-P):** Published ranges for P content in Pd-P alloys vary from 1-7%. This is less well-characterized in open literature than EN-P. IPC-4556 does not specify Pd-P phosphorus content requirements.

4. **Co-W-P tungsten content:** My stated range of 2-15 wt% W is broad. Actual W incorporation is highly dependent on citrate concentration and bath pH. This should be verified against published metallurgical studies if a poster number is needed.

## Flags for Drew

5. **Electroless gold: cyanide vs. sulfite chemistry.** Both KAu(CN)2 (cyanide-based) and Na3Au(SO3)2 (sulfite-based) are in commercial use. Sulfite gold is cyanide-free but less stable and more expensive. Poster should note both exist without preference.

6. **Formaldehyde OSHA limits:** I've stated PEL 0.75 ppm TWA and STEL 2 ppm. These are current OSHA limits. ACGIH TLV is lower at 0.3 ppm ceiling. Poster should reference OSHA PEL.

7. **EN-B ASTM B841:** This standard is less widely known than B733. Verify that B841 is still the current active standard (not withdrawn or replaced).

## Flags for Alaina

8. **Poster structure across 8 processes:** Cleaning, rinse, and activation posters share substantial common chemistry across all 8 processes. Alaina may want to consider visual consistency (same layout template) with process-specific callout boxes rather than fully unique designs for these "support step" posters.

9. **EN-P three-way comparison:** The three EN-P processes (Low/Mid/High) share the same mechanism, same bath components, and same post-treatment framework. The differentiator is pH/complexant/temperature. This is an opportunity for a strong visual language showing the same bath with a "pH dial" shifting properties.

10. **Cost hierarchy:** EN-B > Electroless Gold > Electroless Palladium > EN-P > Electroless Copper > Electroless Cobalt (approximate, by chemistry cost per dm2). This could inform an economics callout if any poster addresses cost.

---

*Research Brief v1.1 authored by Watson (watson-chemistry-researcher), 2026-04-26. v1.1 additions: cross-cluster comparison tables (reducing agents, temperature, deposition rate, hardness, corrosion, analytical methods, PPE, waste treatment); Qorvo account relevance section. Sources: domain expertise in electroless plating chemistry; existing Watson EN Research Brief v2 (2026-03-21); ASTM B733, B841, B849, B850 reference memory; Nickel Plating Handbook 2023 (nickelinstitute.org); IPC-4552B, IPC-4556; AMS 2404/2405; NASF/AESF Metal Finishing Guidebook; Products Finishing; Mallory & Hajdu "Electroless Plating: Fundamentals and Applications" (1990 AESF). Gemini quota exhausted during both sessions -- all data compiled from domain expertise. Tyler spot-check recommended for EN-B deposition rates, electroless copper formaldehyde concentrations, and ASTM B841 current active status before poster finalization.*
