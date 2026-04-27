---
created: 2026-03-21T00:00:00
version: v2
poster: "#10 — Electroless Nickel: Process Overview and Bath Control"
tags:
  - ElectrolessNickel
  - PosterResearch
  - ResearchBrief
---

# Electroless Nickel — Alaina Research Brief

**Poster**: #10 — Electroless Nickel: Process Overview and Bath Control
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-03-21
**Version**: v2 — full technical research brief (supersedes v1 design-zone workup of 2026-03-20)
**Source documents**: [[Electroless Nickel Plating Troubleshooting Guide — v1]] (vault); domain expertise; MacDermid Enthone Niklad/Enplate product line; Atotech Nichem; NASF/AESF Metal Finishing Guidebook; Products Finishing; ASTM B733; IPC-4552B; MIL-C-26074; AMS 2404/2405

> [!NOTE]
> This is the foundational technical research document Alaina draws on for poster content. It supersedes the v1 design-zone brief (2026-03-20) by providing full source-level technical depth first, then condensing to poster callouts at the end. The v1 zone-by-zone layout guidance remains valid as a companion design execution reference.

---

## Process Overview

**What is electroless nickel (EN)?**

Electroless nickel is an **autocatalytic chemical deposition process** that deposits a nickel-phosphorus (Ni-P) alloy coating without the use of an external electrical current. There is no rectifier, no anode, no cathode — deposition occurs entirely through a controlled oxidation-reduction reaction that takes place only on catalytic surfaces immersed in the bath.

The word "autocatalytic" is the key concept: the freshly deposited Ni-P alloy is itself a catalyst for the same reaction that produced it. Deposition begins when a catalytic surface activates the reaction, and it propagates on the growing deposit for as long as the part remains in a properly controlled bath. This self-perpetuating mechanism produces **uniform deposit thickness on all surfaces simultaneously** — inside holes, recesses, blind bores, undercuts, and external surfaces all plate at the same rate.

**How EN differs from electrolytic (rack or barrel) plating:**

| Attribute | Electroless Nickel | Electrolytic Nickel |
|---|---|---|
| Energy source | Chemical reduction (no current) | External DC current |
| Thickness uniformity on complex geometry | ±1–2 µm across all surfaces | 5–10× variation (HCD vs. LCD zones) |
| Ability to plate inside holes/recesses | Yes — complete coverage | Limited by current shadowing |
| Deposit composition | Ni-P alloy (tunable by P%) | Pure nickel (or low-sulfur/sulfamate) |
| Bath life | Finite — 6–10 MTO then discard | Indefinite with maintenance |
| Capital equipment required | Tank, heater, filter, pH/temp control | Rectifier, tank, anodes, bus bars |
| Substrate requirement | Must be catalytic or activated | Must be electrically conductive |

**Commercial context**: EN is used where dimensional tolerances are tight, geometry is complex, and specific deposit properties (hardness, corrosion resistance, non-magnetism, solderability) are required. It commands a premium over electrolytic nickel in both material cost and process control demands.

---

## Bath Chemistry

### The Reduction Reaction

The primary deposition reaction using **sodium hypophosphite** as reducing agent:

```
Ni²⁺  +  2 H₂PO₂⁻  +  2 H₂O  →  Ni⁰  +  2 H₂PO₃⁻  +  H₂↑  +  2 H⁺
```

**What each component does:**
- **Ni²⁺** (from nickel sulfate, NiSO₄·6H₂O) — the metal ion being reduced to metallic nickel
- **Hypophosphite (H₂PO₂⁻)** — the reducing agent; it donates electrons and is oxidized to **orthophosphite (H₂PO₃⁻)**
- **H₂O** — participates in the oxidation step
- **Ni⁰** — metallic nickel deposited on the part surface (the desired product)
- **H₂PO₃⁻ (orthophosphite)** — byproduct; accumulates in bath; precipitates nickel as bath ages; discard threshold ~120 g/L
- **H₂ (hydrogen gas)** — evolved continuously; visible as fine gassing on all surfaces during deposition; agitation required to prevent pitting
- **H⁺ (acid)** — pH drops continuously; active adjustment required throughout operation

**The phosphorus co-deposition side reaction:**

```
H₂PO₂⁻  +  H⁺  →  P⁰  +  H₂O  +  H⁺
```

A fraction of the hypophosphite is reduced all the way to elemental phosphorus (P⁰), which co-deposits with the nickel to form the Ni-P alloy. The phosphorus content of the deposit is controlled by bath pH, temperature, hypophosphite concentration, and proprietary bath formulation. This co-deposited phosphorus is what gives EN deposits their unique properties.

### Bath Components and Their Roles

**1. Nickel sulfate (NiSO₄·6H₂O) — Metal ion source**
- Typical concentration: 20–30 g/L as Ni metal (equivalent to ~90–130 g/L NiSO₄·6H₂O)
- Operating target: 4.5–6.5 g/L Ni²⁺ in most acid bath formulations
- Low Ni²⁺ → slow deposition rate; risk of bath decomposition
- High Ni²⁺ → faster rate but higher chemical cost; exacerbates orthophosphite buildup

**2. Sodium hypophosphite (NaH₂PO₂·H₂O) — Reducing agent**
- Typical concentration: 20–30 g/L
- Operating target: 20–30 g/L (maintained by replenishment throughout operation)
- Consumed in direct proportion to nickel deposited
- Depleted hypophosphite → slow or stopped deposition; bath instability risk
- Excess hypophosphite → inefficiency; does not cause harm in normal ranges

**3. Complexants (chelating agents) — Stabilize Ni²⁺ in solution**

Complexants prevent nickel from precipitating as nickel hydroxide or nickel phosphite at operating temperatures and pH. They hold Ni²⁺ in a controlled-release complex that presents Ni²⁺ to the catalyst surface at a manageable rate.

| Complexant | Common Use | Notes |
|---|---|---|
| Lactic acid | Mid-P and High-P acid baths | Most common; good stability across pH 4.4–5.0 |
| Malic acid | Mid-P acid baths | Often blended with lactic acid |
| Citric acid | Some alkaline baths | Strong complexant; can inhibit deposition at excess levels |
| Glycolic acid | High-P baths | Enhances smoothness |
| Succinic acid | Mid-P baths | Buffering + complexing dual role |
| Ammonium compounds | Alkaline baths (pH 6–9) | Replaces organic acids for Low-P alkaline systems |

**4. Stabilizers (inhibitors) — Prevent spontaneous bath decomposition**

Stabilizers adsorb onto nickel nuclei in solution and prevent runaway decomposition (bath "crashing"). Without stabilizers, the autocatalytic reaction proceeds in the bulk solution — producing grey-black nickel powder, destroying the bath, and potentially causing a fire hazard.

Common stabilizers and their threshold-active concentrations:
| Stabilizer | Type | Typical Use Level |
|---|---|---|
| Lead acetate (Pb²⁺) | Heavy metal | 1–2 ppm |
| Cadmium sulfate (Cd²⁺) | Heavy metal | 0.5–1 ppm |
| Thiourea | Sulfur compound | 0.5–2 mg/L |
| Thiomalic acid | Sulfur compound | Proprietary; common in commercial concentrates |
| Potassium iodate (IO₃⁻) | Oxidant | 1–5 mg/L |

**Critical hazard**: stabilizers operate at ppm-level concentrations. Even slight overdosing (especially thiourea > 5 mg/L) causes **stabilizer poisoning** — the bath becomes inert and will not plate. Poisoned baths typically require dilution and re-optimization; recovery is not always possible.

**5. pH buffers — Resist pH drop during plating**
- Succinic acid, propionic acid, and lactic acid serve dual roles as complexants and buffers
- Sodium hydroxide or ammonium hydroxide is used for pH adjustment upward
- Sulfuric acid or dilute hydrochloric acid for downward adjustment
- pH drifts acid (downward) as plating proceeds — active monitoring every 30–60 minutes in production

**6. Nickel sulfate vs. nickel chloride as metal source**
- Most commercial bath concentrates use nickel sulfate exclusively (chloride-free)
- Some specialty formulations use nickel chloride for improved anode compatibility (not applicable to EN — no anodes)
- Chloride contamination in EN baths can cause pitting and accelerate bath aging

---

## Phosphorus Content Classifications

Phosphorus content is the single most important characteristic of an EN deposit — it governs hardness, corrosion resistance, magnetic behavior, solderability, and stress state. Bath formulation and operating pH are the primary levers controlling deposit P content.

### Classification System

| Class | Phosphorus Range | Also Called | Primary Characteristic |
|---|---|---|---|
| Low-P | 1–4% by weight | Low-phosphorus | High hardness; ferromagnetic; excellent solderability |
| Mid-P | 5–9% by weight | Medium-phosphorus | Balanced properties; most versatile; industry workhorse |
| High-P | 10–14% by weight | High-phosphorus | Maximum corrosion resistance; amorphous (non-magnetic) |

**ASTM B733 Type designations** (phosphorus % governs Type):
- Type I: < 1% P (essentially pure electroless nickel — uncommon)
- Type II: 1–3% P (Low-P)
- Type III: 2–4% P (Low-P, overlapping range)
- Type IV: 5–9% P (Mid-P)
- Type V: 10% P and above (High-P)

*Note: Industry commonly uses the three-class Low/Mid/High system in daily practice; ASTM B733 Type designations appear on engineering drawings and specifications.*

### Low-Phosphorus (1–4% P)

**Bath conditions that produce Low-P:**
- Alkaline pH: 6.0–9.0 (high pH suppresses P co-deposition)
- Temperature: 65–80°C
- Deposition rate: 10–15 µm/hr (slower than Mid-P)

**Key deposit properties:**
- Hardness as-plated: 650–750 HV (Vickers) — harder than as-plated Mid-P or High-P
- Hardness after heat treatment (400°C / 1 hr): 1000–1100 HV — approaching hard chrome territory
- Structure: near-crystalline to microcrystalline (not fully amorphous)
- Magnetic: **ferromagnetic** — Low-P deposits are magnetic
- Corrosion resistance (neutral salt spray): ~96–240 hrs depending on thickness and substrate
- Solderability: **excellent** — lowest P content means highest metallic nickel character; wets solder readily
- Contact resistance: very low — used in electronics switching contacts
- Wear resistance: superior to High-P as-plated; comparable to hard chrome after heat treatment

**Primary applications**: electronics/PCB (solderability, contact resistance), hard wear surfaces requiring subsequent heat treatment, diamond-tool binders, applications requiring non-magnetic-free behavior

### Mid-Phosphorus (5–9% P)

**Bath conditions that produce Mid-P:**
- Acid pH: 4.7–5.0
- Temperature: 85–91°C (hottest of the three classes)
- Deposition rate: 18–25 µm/hr (fastest class)

**Key deposit properties:**
- Hardness as-plated: 500–600 HV
- Hardness after heat treatment (400°C / 1 hr): 850–1000 HV
- Structure: mixed crystalline/amorphous
- Magnetic: **weakly magnetic to non-magnetic** depending on exact P% within range
- Corrosion resistance (NSS): ~240–500 hrs (intermediate)
- Solderability: moderate
- Deposit smoothness: very good; minimal nodulation with good bath control

**Primary applications**: aerospace hydraulic and pneumatic components, automotive fuel system parts, precision tooling, general engineering where the deposit properties of both extremes are not required. **Most widely used class in general EN plating.**

### High-Phosphorus (10–14% P)

**Bath conditions that produce High-P:**
- Acid pH: 4.4–4.8 (low pH promotes P co-deposition)
- Temperature: 82–90°C
- Deposition rate: 10–13 µm/hr (slower than Mid-P)

**Key deposit properties:**
- Hardness as-plated: 450–550 HV (softest of the three classes as-deposited)
- Hardness after heat treatment (400°C / 1 hr): 800–900 HV
- Structure: **fully amorphous** — no grain boundaries; behaves like a metallic glass
- Magnetic: **non-magnetic** — the amorphous structure eliminates ferromagnetism; critical for MWD tools and MRI-adjacent applications
- Corrosion resistance (NSS): **1,000+ hrs** — the amorphous structure eliminates grain boundary attack; outstanding performance in acid environments and chloride-rich environments
- Solderability: poor (high P interferes with solder wetting)
- Chemical resistance: excellent; widely used for pump and valve components in chemical processing
- Lubricity: smooth, low-friction surface; used in mold release applications and sliding contacts

**Primary applications**: oil and gas downhole tools (non-magnetic + corrosion), chemical processing (acid/chloride environments), mold release surfaces, applications requiring maximum corrosion protection

---

## Process Parameters and Controls

### Bath Operating Parameters by Phosphorus Class

| Parameter | Low-P | Mid-P | High-P |
|---|---|---|---|
| pH target | 6.0–9.0 | 4.7–5.0 | 4.4–4.8 |
| Temperature | 65–80°C | 85–91°C | 82–90°C |
| Ni²⁺ target | 4.5–6.5 g/L | 4.5–6.5 g/L | 4.5–6.5 g/L |
| Hypophosphite target | 20–30 g/L | 20–30 g/L | 20–30 g/L |
| Deposition rate | 10–15 µm/hr | 18–25 µm/hr | 10–13 µm/hr |
| Typical bath life | 6–8 MTO | 6–8 MTO | 6–8 MTO |
| Orthophosphite discard limit | ~120 g/L | ~120 g/L | ~120 g/L |

### Critical Control Parameters

**pH control** — the single most tightly held parameter in EN operation:
- pH drops continuously as plating proceeds (H⁺ produced by reaction)
- Target pH must be held within ±0.2 of the nominal; wider swings cause P content shifts and deposit quality changes
- Check frequency: every 30–60 minutes during production; automatic controllers preferred for high-volume operations
- Adjustment: NaOH or NH₄OH to raise; dilute H₂SO₄ to lower
- Temperature affects pH meter readings — calibrate at operating temperature or apply correction

**Temperature control:**
- Deposition rate is exponentially sensitive to temperature (Arrhenius relationship)
- ±2°C control is the practical minimum; ±1°C preferred
- Low temperature → slow deposition, risk of passivation on part surfaces
- High temperature → accelerated bath aging, risk of spontaneous decomposition
- Heater must not have hot spots that exceed bath temperature by > 5–10°C (hot spots nucleate decomposition)

**Bath loading (surface area to volume ratio, A/V):**
- Expressed as dm²/L (decimeters squared per liter) or ft²/gal
- Optimal loading: 0.25–0.50 dm²/L for most commercial baths
- Under-loaded bath (< 0.1 dm²/L): bath chemistry builds up; higher risk of decomposition; inefficient
- Over-loaded bath (> 1.0 dm²/L): rapid Ni²⁺ and hypophosphite depletion; pH crash; very poor deposit quality
- Loading must be calculated before each production run and maintained consistently

**Metal turnovers (MTO) — bath life metric:**
- 1 MTO = the bath has deposited an amount of nickel equal to its original Ni²⁺ charge
- Formula: MTO = (total Ni deposited, g) / (original Ni²⁺ loading, g)
- Fresh bath: 0 MTO — best deposit quality, cleanest chemistry
- Typical operating range: 0–6 MTO with progressively declining deposit quality
- Warning zone: 6–8 MTO — increased orthophosphite, slower rate, higher stress, more porosity
- Discard: 8–10 MTO (or at orthophosphite > 120 g/L) — beyond this the bath cannot produce specification-grade deposits

**Orthophosphite accumulation:**
- Orthophosphite (H₂PO₃⁻) is the byproduct of hypophosphite oxidation; it does not deposit and builds up with each MTO
- It progressively complexes Ni²⁺ in ways that compete with the intended complexants
- High orthophosphite → increased deposit porosity, reduced corrosion resistance, difficulty maintaining pH, risk of NiHPO₃ precipitation in the bath
- Cannot be removed by filtration or Hull cell; requires bath discard or dilution
- Monitoring: qualitative with specific gravity measurement; quantitative by titration or ICP

### Deposit Thickness Ranges in Practice

| Application | Typical Thickness | Notes |
|---|---|---|
| Electronics (ENIG base layer) | 3–6 µm | Per IPC-4552B |
| Aerospace/general engineering | 25–75 µm | Per AMS 2404, ASTM B733 |
| Tooling/wear resistance | 50–125 µm | Heat treatment usually follows |
| Mold release | 12–25 µm | High-P preferred |
| Oil and gas downhole | 25–75 µm | High-P non-magnetic grades |

---

## Deposit Properties

### Hardness

EN deposit hardness is a function of phosphorus content and heat treatment state:

| Condition | Low-P (1–4%) | Mid-P (5–9%) | High-P (10–14%) |
|---|---|---|---|
| As-plated | 650–750 HV (56–62 HRC) | 500–600 HV (48–55 HRC) | 450–550 HV (44–52 HRC) |
| After 400°C / 1 hr HT | 1000–1100 HV (68–72 HRC) | 850–1000 HV (65–70 HRC) | 800–900 HV (63–67 HRC) |
| Hard chrome (as-deposited reference) | 900–1100 HV (65–72 HRC) | — | — |

The hardness increase on heat treatment arises from **crystallization of the amorphous Ni-P matrix and precipitation of Ni₃P intermetallic compound** within the deposit. This is a true metallurgical hardening mechanism — precipitation hardening.

**Design note**: EN after heat treatment at 400°C achieves hardness competitive with hard chrome, without the environmental burden of hexavalent chromium. This is a key industry selling point.

**Caution on heat treatment**:
- Temperatures above 220°C can cause hydrogen embrittlement in high-strength steels (above ~1000 MPa UTS); must bake before and after plating per AMS 2404 / MIL-C-26074
- Heat treatment above 290°C on aluminum substrates causes adhesion failure due to differential thermal expansion
- Heat treatment is generally compatible with steel, tool steel, and cast iron substrates

### Corrosion Resistance

EN corrosion resistance depends heavily on phosphorus content, deposit thickness, and deposit continuity (porosity):

| P Class | Salt Spray (ASTM B117) | Notes |
|---|---|---|
| Low-P | ~96–240 hrs at 25 µm | Crystalline structure; some grain boundary susceptibility |
| Mid-P | ~240–500 hrs at 25 µm | Partially amorphous; intermediate protection |
| High-P | 1,000+ hrs at 25 µm | Fully amorphous; no grain boundaries to attack |

The amorphous structure of High-P deposits is the key: corrosion normally initiates at grain boundaries and crystallographic defects. An amorphous deposit has no grain boundaries — corrosion must attack the bulk of the deposit rather than preferentially along boundaries. This is why High-P EN dramatically outperforms pure nickel and Mid-P EN in corrosive environments.

**Comparison to competing finishes:**
- EN High-P vs. electroless copper: EN far superior
- EN High-P vs. electrolytic nickel: EN substantially superior (electrolytic nickel has grain structure)
- EN Mid-P vs. zinc plating with chromate: EN substantially superior in both hardness and corrosion resistance
- EN after HT vs. hard chrome in wear + corrosion: broadly comparable depending on service conditions

### Non-Magnetic Behavior (High-P)

Pure nickel is ferromagnetic (strongly attracted to magnets). As phosphorus content increases in the Ni-P alloy, ferromagnetism decreases. Above approximately **8–10% P**, the deposit becomes fully amorphous and **non-magnetic** (technically paramagnetic). This property is essential for:

- **MWD (measurement while drilling) tools** in oil and gas — magnetic components in a downhole tool would distort directional survey readings
- **MRI-compatible components** — non-magnetic coatings on medical devices
- **Electronics shielding** — where magnetic interference must be avoided

**The non-magnetic threshold is approximately 8–10% P.** Most High-P commercial baths (10–14% P) reliably produce non-magnetic deposits. Mid-P baths at the high end of their range (8–9% P) may be at or near the threshold — this must be confirmed by testing (ASTM F2088 magnetic test or verified P% analysis) when non-magnetism is specified.

### Solderability and Contact Resistance

- **Low-P deposits**: excellent solderability; very low contact resistance; the near-metallic-nickel character of low-P alloy wets solder well; surface oxide is minimal compared to high-P
- **Mid-P deposits**: moderate solderability; adequate for general PCB use with flux
- **High-P deposits**: poor solderability; high-P oxide layer is more stable; surface energy is lower; not suitable for direct solder attachment without activation

In ENIG (electroless nickel / immersion gold) PCB finishes, Mid-P EN (3–6 µm) acts as the solderable base and diffusion barrier beneath a thin gold flash (0.05–0.1 µm). The gold provides a fresh, oxidation-free surface; the EN provides the structural solder joint. Governed by **IPC-4552B** (ENIG specification).

### Lubricity and Wear Resistance

- EN deposits are self-lubricating compared to hard chrome in certain service conditions
- Coefficient of friction: EN dry ~0.1–0.15 vs. hard chrome dry ~0.12–0.16 (broadly comparable)
- **EN-PTFE composite baths** incorporate co-deposited PTFE particles to reduce friction to 0.04–0.07 (dry) — used in mold release, sliding contacts, pump components
- Wear resistance improves substantially after heat treatment; Low-P after HT approaches the wear performance of hard chrome

---

## Specifications and Standards

### ASTM B733 — Autocatalytic Nickel-Phosphorus Coatings

The primary North American specification for EN plating. Defines:

**Types (phosphorus content):**
- Type I: < 1% P
- Type II: 1–3% P (Low-P)
- Type III: 2–4% P (Low-P, overlapping)
- Type IV: 5–9% P (Mid-P)
- Type V: ≥ 10% P (High-P)

**Classes (heat treatment condition):**
- Class 1: No heat treatment (as-plated)
- Class 2: Heat treated at 120–130°C / 1–2 hr (hydrogen embrittlement relief for high-strength steel)
- Class 3: Heat treated at 180–200°C / 2–4 hr (additional bake; less common)
- Class 4: Heat treated at 260–290°C / 1 hr (partial precipitation hardening)
- Class 5: Heat treated at 360–400°C / 1 hr (full precipitation hardening; maximum hardness)
- Class 6: Heat treated at 140–150°C / 1–2 hr, then 340–360°C / 4 hr (age + stress relieve)

**Thickness requirements:** Defined by service class (SC) in B733:
- SC 0: 0.1 µm (for electronic soldering)
- SC 1: 5 µm (mild service)
- SC 2: 13 µm (moderate service)
- SC 3: 25 µm (severe service)
- SC 4: 75 µm (very severe service)

### AMS 2404 and AMS 2405

- **AMS 2404**: Electroless Nickel Plating — general specification for aerospace; includes pre/post bake requirements for high-strength steel; typical requirement for hydraulic and structural components
- **AMS 2405**: Electroless Nickel Plating — specifically for aluminum and magnesium substrates; includes zincate pre-treatment and special thickness requirements

### MIL-C-26074

- Military specification for electroless nickel; now largely superseded by ASTM B733 and AMS 2404 in practice, but still appears on older defense drawings and legacy programs
- Defines grades by coating thickness and P content in a manner broadly consistent with ASTM B733

### IPC-4552B — ENIG (Electroless Nickel / Immersion Gold)

- Governs EN used as the base layer in ENIG PCB surface finishes
- EN thickness: 3–6 µm (Mid-P, typically Type IV per ASTM B733)
- Gold thickness: 0.05–0.10 µm
- Phosphorus content: 6–9% P preferred to minimize "black pad" risk (excessive phosphorus enrichment at the Ni/Au interface)
- *Note: IPC-4556 covers ENEPIG (Electroless Nickel / Electroless Palladium / Immersion Gold) — a distinct process; do not confuse with ENIG*

---

## Industry Applications

### Aerospace

- **AMS 2404 applications**: hydraulic actuator bores, landing gear components, fuel control valve bodies, hydraulic cylinder rods
- **Why EN**: dimensional tolerance critical; complex geometry; corrosion + wear requirements; heat-treated hardness competitive with hard chrome
- **P class used**: Mid-P (AMS 2404 most commonly) for general aerospace; Low-P after HT for maximum hardness
- **Relevant specs**: AMS 2404, AMS 2405 (aluminum), ASTM B733

### Electronics and PCB

- **ENIG**: EN + immersion gold; the dominant PCB surface finish worldwide for lead-free soldering; Low-P or Mid-P EN base (3–6 µm), gold flash (0.05–0.1 µm)
- **Connector contacts**: Low-P for minimum contact resistance
- **EMI shielding**: EN on plastic housings (autocatalytic deposition on non-conductive substrates)
- **Relevant specs**: IPC-4552B (ENIG), IPC-4556 (ENEPIG)

### Oil and Gas

- **MWD/LWD tools** (measurement/logging while drilling): High-P EN for non-magnetic property + corrosion in downhole chloride and H₂S environments
- **Downhole pump components**: High-P for corrosion in produced water (high Cl⁻, CO₂, H₂S)
- **Valve seats and trim in sour service**: High-P + heat treatment for wear + corrosion
- **Why EN over hard chrome**: regulatory pressure on hexavalent chrome; EN provides comparable properties; complex geometry advantage
- **Relevant specs**: ASTM B733 Type V Class 5 common; NACE specifications for H₂S service

### Automotive

- **Fuel injector bodies and valve seats**: Mid-P EN for corrosion + wear in fuel contact
- **Transmission components**: Mid-P for dimensional precision and wear resistance
- **ABS/brake system components**: EN for corrosion in brake fluid
- **Decorative-functional automotive trim**: Mid-P for cosmetic + corrosion requirements

### Medical Devices

- **Surgical instruments**: Low-P or Mid-P for hardness + sterilizability
- **Orthopedic tooling**: EN for dimensional precision and corrosion in biological fluids
- **MRI-compatible components**: High-P (non-magnetic) for devices used near magnetic fields
- **Relevant considerations**: biocompatibility testing required; nickel allergy risk must be assessed per end-use application

### Chemical Processing

- **Pump impellers and casings in acid service**: High-P EN; resistance to HCl, H₂SO₄, acetic acid, phosphoric acid
- **Heat exchanger tubes and fittings**: High-P for combined corrosion + erosion
- **Reactor vessel internals**: High-P for process chemical compatibility
- **Why EN over stainless or Hastelloy**: significant cost reduction; dimensional precision; ability to coat complex shapes

---

## Visual / Diagram Opportunities for Poster Design

This section is written directly for Alaina. These are the highest-impact visual ideas to convey EN's technical story in poster format.

### 1. The Uniform Coating Cross-Section (HERO visual)
A side-by-side cross-section of a part with complex geometry (bore + external surface):
- Left panel — Electrolytic Nickel: exaggerated build-up at corners/edges (HCD zones labeled "thick"), thin deposit in recesses (LCD zones labeled "thin or bare")
- Right panel — Electroless Nickel: perfectly uniform deposit, same thickness on all surfaces
- Callout: "±1–2 µm uniformity vs. 5–10× variation for electroplating"
- This is the single concept that most clearly differentiates EN from conventional plating

### 2. The P% Property Ladder (central data table / infographic)
Three columns (Low-P / Mid-P / High-P) showing how properties shift across the spectrum. Color-code columns using locked palette (Teal = Low-P, Amber = Mid-P, Coral = High-P). Key rows:
- P content range
- pH to produce it
- Hardness as-plated (HV)
- Hardness after heat treatment (HV)
- Salt spray hours
- Magnetic behavior (ferromagnetic / transitional / non-magnetic — use magnet icon)
- Solderability (excellent / moderate / poor)
- Primary use

### 3. The Heat Treatment Hardness Jump
A bar chart or side-by-side bars per class:
- X-axis: as-plated | 400°C HT
- Y-axis: hardness (HV or HRC)
- The jump from ~500 HV as-plated to ~1000 HV after HT is visually dramatic
- Add a reference line for hard chrome (~900–1100 HV) to show competitive hardness

### 4. The Bath Lifecycle Gauge (MTO)
A circular gauge or horizontal progress bar:
- 0 MTO = fresh; 6 MTO = normal operating limit; 8–10 MTO = discard zone
- Color zones: green (0–6), amber (6–8), red (8–10)
- Caption: "Unlike electrolytic baths, EN baths have a finite life — track your MTOs"

### 5. The Autocatalytic Reaction Schematic
Simple chemistry diagram:
- Part surface (cross-hatched) with Ni-P deposit forming
- Arrows: Ni²⁺ approaching the surface, H₂PO₂⁻ approaching, H₂ gas bubbles rising, H⁺ and H₂PO₃⁻ leaving
- Simplified equation on the poster: **Ni²⁺ + H₂PO₂⁻ + H₂O → Ni-P + H₂ + H⁺**
- Label: "No external current — chemistry does the work"

### 6. The Corrosion Shield Icons
Three shield icons sized proportionally to salt spray hours:
- Low-P: small shield (~96–240 hrs)
- Mid-P: medium shield (~240–500 hrs)
- High-P: large shield (1,000+ hrs)
- Caption: "Amorphous structure = no grain boundaries = no preferential corrosion path"

### 7. Applications Industry Icons
5–6 icons representing industries:
- Aerospace (turbine/aircraft silhouette) → AMS 2404 / hydraulic components
- Electronics/PCB (circuit board) → ENIG, IPC-4552B
- Oil and Gas (drill bit / derrick) → Non-magnetic High-P downhole tools
- Chemical Processing (reactor vessel) → High-P corrosion resistance
- Automotive (engine/fuel injector) → Mid-P wear + fuel compatibility
- Medical (surgical instrument) → High-P non-magnetic; Low-P hardness

### 8. Bath Control Panel Callout Box
Four data cells in a 2×2 grid:
- pH: 4.4–5.0 (acid) | 6.0–9.0 (alkaline Low-P)
- Temperature: 65–91°C (range across all classes)
- Ni²⁺: 4.5–6.5 g/L
- Hypophosphite: 20–30 g/L
- Footer: Loading 0.25–0.50 dm²/L | Discard orthophosphite > 120 g/L

---

## Key Data Points for Callouts

These are the numbers Alaina should pull into the poster as primary callouts. Formatted for JetBrains Mono display:

**Hardness:**
- Low-P as-plated: `650–750 HV`
- Mid-P as-plated: `500–600 HV`
- High-P as-plated: `450–550 HV`
- Low-P after 400°C HT: `1000–1100 HV`

**Corrosion resistance:**
- High-P salt spray: `1,000+ hrs`
- Mid-P salt spray: `240–500 hrs`
- Low-P salt spray: `~96–240 hrs`

**Deposit uniformity:**
- EN uniformity: `±1–2 µm`
- Electroplating variation: `5–10×`

**Deposition rate:**
- Low-P: `10–15 µm/hr`
- Mid-P: `18–25 µm/hr`
- High-P: `10–13 µm/hr`

**Bath chemistry:**
- Ni²⁺ target: `4.5–6.5 g/L`
- Hypophosphite target: `20–30 g/L`
- Orthophosphite discard: `> 120 g/L`
- Bath life: `6–8 MTO typical`
- Loading factor: `0.25–0.50 dm²/L`

**Phosphorus:**
- Non-magnetic threshold: `≥ 8–10% P`
- ENIG EN thickness (IPC-4552B): `3–6 µm`
- Aerospace EN thickness (AMS 2404): `25–75 µm typical`

**Governing specifications to display:**
- `ASTM B733` — North American EN standard (Types by P%, Classes by heat treatment)
- `AMS 2404` — Aerospace EN (steel)
- `AMS 2405` — Aerospace EN (aluminum/magnesium)
- `MIL-C-26074` — Military/legacy EN
- `IPC-4552B` — ENIG PCB surface finish

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-03-21. Sources: vault EN troubleshooting guide (verified 2026-03-20); domain expertise grounded in MacDermid Enthone Niklad/Enplate, Atotech Nichem, NASF/AESF Metal Finishing Guidebook, Products Finishing, ASTM B733, IPC-4552B, AMS 2404/2405, MIL-C-26074. Gemini quota exhausted during session — data verified against vault records and domain expertise. Alaina should flag any data points requiring additional verification before final poster production.*
